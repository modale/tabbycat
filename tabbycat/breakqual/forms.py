from django import forms

from utils.forms import OptionalChoiceField

from .models import BreakingTeam

# ==============================================================================
# Break eligbility form
# ==============================================================================


class BreakEligibilityForm(forms.Form):
    """Sets which teams are eligible for the break."""

    def __init__(self, tournament, *args, **kwargs):
        super(BreakEligibilityForm, self).__init__(*args, **kwargs)
        self.tournament = tournament
        self._create_and_initialise_fields()

    @staticmethod
    def _fieldname_eligibility(team):
        return 'eligibility_%(team)d' % {'team': team.id}

    def _create_and_initialise_fields(self):
        """Dynamically generate fields, one ModelMultipleChoiceField for each
        Team."""
        for team in self.tournament.team_set.all():
            self.fields[self._fieldname_eligibility(team)] = forms.ModelMultipleChoiceField(
                queryset=self.tournament.breakcategory_set.all(), widget=forms.CheckboxSelectMultiple,
                required=False)
            self.initial[self._fieldname_eligibility(team)] = team.break_categories.all()

    def save(self):
        for team in self.tournament.team_set.all():
            team.break_categories = self.cleaned_data[self._fieldname_eligibility(team)]
            team.save()

    def team_iter(self):
        for team in self.tournament.team_set.all():
            yield team, self[self._fieldname_eligibility(team)]


# ==============================================================================
# Breaking teams form
# ==============================================================================

class BreakingTeamsForm(forms.Form):
    """Updates the remarks on breaking teams and regenerates the break."""

    def __init__(self, category, *args, **kwargs):
        super(BreakingTeamsForm, self).__init__(*args, **kwargs)
        self.category = category
        self._prefetch_breakingteams()
        self._create_and_initialise_fields()

    @staticmethod
    def _fieldname_remark(team):  # Team not BreakingTeam
        return 'remark_%(team)d' % {'team': team.id}

    def get_remark_field(self, team):  # Team not BreakingTeam
        return self[self._fieldname_remark(team)].as_widget(attrs={'class': 'form-control'})

    def _bt(self, team):
        return self._bts_by_team_id[team.id]

    def _prefetch_breakingteams(self):
        self._bts_by_team_id = {bt.team_id: bt for bt in self.category.breakingteam_set.all()}

    def _create_and_initialise_fields(self):
        """Dynamically generate fields, one Select for each BreakingTeam."""
        for team in self.category.breaking_teams.all():
            self.fields[self._fieldname_remark(team)] = OptionalChoiceField(choices=BreakingTeam.REMARK_CHOICES, required=False)
            try:
                self.initial[self._fieldname_remark(team)] = self._bt(team).remark
            except KeyError:
                self.initial[self._fieldname_remark(team)] = None

    def save(self):
        for team in self.category.breaking_teams.all():
            try:
                bt = self._bt(team)
            except KeyError:
                continue
            bt.remark = self.cleaned_data[self._fieldname_remark(team)]
            bt.save()
