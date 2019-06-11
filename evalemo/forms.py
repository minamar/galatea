from django import forms
from dal import autocomplete

class ParticipantForm(forms.Form):
    subject = forms.IntegerField(label='Participant\'s number')
    sex = forms.ChoiceField(label='Sex', choices=(('F', 'F'), ('M', 'M'), ('O', 'O')))
    age = forms.IntegerField(label='Age')
    anim_experience = forms.IntegerField(label='Animation experience', min_value=0, max_value=10)


class SliderForm(forms.Form):
    pleasure = forms.FloatField(label='Displeasure-Pleasure', widget=forms.NumberInput(
        attrs={'type': 'range', 'name': 'AS_pleasure', 'id': 'AS-arousal', 'value': '.5', 'min': '0', 'max': '1',
               'step': '0.01'}))
    arousal = forms.FloatField(label='Nonarousal-Arousal', widget=forms.NumberInput(
        attrs={'type': 'range', 'name': 'AS_arousal', 'id': 'AS-arousal', 'value': '.5', 'min': '0', 'max': '1',
               'step': '0.01'}))
    dominance = forms.FloatField(label='Submissiveness-Dominance', widget=forms.NumberInput(
        attrs={'type': 'range', 'name': 'AS_arousal', 'id': 'AS-arousal', 'value': '.5', 'min': '0', 'max': '1',
               'step': '0.01'}))


class WasEmotionForm(forms.Form):
    attention = forms.ChoiceField(label="The robot's behavior draws my attention.", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Strongly disagree'), ('2', 'Disagree'), ('3', 'Neither agree nor disagree'), ('4', 'Agree'),
        ('5', 'Strongly agree')))
    likert_was_emotion = forms.ChoiceField(label="The robot's expression was emotional.", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Strongly disagree'), ('2', 'Disagree'), ('3', 'Neither agree nor disagree'), ('4', 'Agree'),
        ('5', 'Strongly agree')))
    # cat_emotion = forms.CharField(
    #     label="",
    #     required=False,
    #     max_length=200,
    #     widget=forms.TextInput(attrs={'size': '80', 'autocomplete': 'off', 'required': False}))

    # cat_emotion = forms.CharField(
    #     label="",
    #     required=False,
    #     max_length=200,
    #     widget=forms.TextInput(attrs={'size': '80', 'autocomplete': 'off', 'required': False}))


# class SurveyForm(forms.Form):
#     bel_1 = forms.ChoiceField(label="The robot's behavior draws my attention.", widget=forms.RadioSelect, choices=(
#         ('1', 'Strongly disagree'), ('2', 'Disagree'), ('3', 'Neither agree nor disagree'), ('4', 'Agree'),
#         ('5', 'Strongly agree')))
#     anth_1 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Fake'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', 'Natural')))
#     anth_2 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Machine like'), ('2', '2'), ('3', '2'), ('4', '4'), ('5', 'Humanlike')))
#     anth_3 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Unconscious'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', 'Conscious')))
#     anth_4 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Artificial'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', 'Lifelike')))
#     anth_5 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Moving rigidly'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', 'Moving elegantly')))

# Copy with initial values for debugging
class SurveyForm(forms.Form):

    anth_1 = forms.ChoiceField(label="Fake", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Fake'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Natural')))
    anth_2 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Machinelike'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Humanlike')))
    anth_3 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Unconscious'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Conscious')))
    anth_4 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Artificial'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Lifelike')))
    anth_5 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Moving rigidly'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Moving elegantly')))
    animacy_1 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Dead'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Alive')))
    animacy_2 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Stagnant'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Alive')))
    animacy_3 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Mechanical'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Organic')))
    animacy_4 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Artificial'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Lifelike')))
    animacy_5 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Inert'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Interactive')))
    animacy_6 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Apathetic'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Responsive')))