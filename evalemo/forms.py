# -*- coding: utf-8 -*-
from django import forms
from backports.functools_lru_cache import lru_cache


class ParticipantForm(forms.Form):
    subject = forms.IntegerField(label='Participant\'s number')
    sex = forms.ChoiceField(label='Sex', choices=(('F', 'F'), ('M', 'M'), ('O', 'O')))
    age = forms.IntegerField(label='Age')
    anim_experience = forms.IntegerField(label='Animation experience', min_value=0, max_value=10)


class SliderForm(forms.Form):
    pleasure = forms.FloatField(label='Displeased - Pleased', widget=forms.NumberInput(
        attrs={'type': 'range', 'name': 'AS_pleasure', 'id': 'AS-arousal', 'min': '0', 'max': '1',
               'step': '0.01'}))
    arousal = forms.FloatField(label='Inactive - Active', widget=forms.NumberInput(
        attrs={'type': 'range', 'name': 'AS_arousal', 'id': 'AS-arousal', 'min': '0', 'max': '1',
               'step': '0.01'}))
    dominance = forms.FloatField(label='Submissive - Dominant', widget=forms.NumberInput(
        attrs={'type': 'range', 'name': 'AS_arousal', 'id': 'AS-arousal', 'min': '0', 'max': '1',
               'step': '0.01'}))


PRI_EMO_CHOICES= [
    ('Anger', 'Anger'),
    ('Disgust', 'Disgust'),
    ('Fear', 'Fear'),
    ('Happiness', 'Happiness'),
    ('Sadness', 'Sadness'),
    ('Surprise', 'Surprise'),
    ]


SEC_EMO_CHOICES = [
    (' ', ' '),
    ('Affection', 'Affection'),
    ('Lust', 'Lust'),
    ('Longing', 'Longing'),
    ('Cheerfulness', 'Cheerfulness'),
    ('Zest', 'Zest'),
    ('Contentment', 'Contentment'),
    ('Pride', 'Pride'),
    ('Optimism', 'Optimism'),
    ('Enthrallment', 'Enthrallment'),
    ('Relief', 'Relief'),
    ('Surprise', 'Surprise'),
    ('Irritation', 'Irritation'),
    ('Exasperation', 'Exasperation'),
    ('Rage', 'Rage'),
    ('Disgust', 'Disgust'),
    ('Envy', 'Envy'),
    ('Torment', 'Torment'),
    ('Suffering', 'Suffering'),
    ('Sadness', 'Sadness'),
    ('Disappointment', 'Disappointment'),
    ('Shame', 'Shame'),
    ('Neglect', 'Neglect'),
    ('Sympathy', 'Sympathy'),
    ('Horror', 'Horror'),
    ('Nervousness', 'Nervousness'),
]

from django.db.models.fields import BLANK_CHOICE_DASH

# TODO: Keep the following 2 classes that contain initial='1' for the debbugging. For a real experiment comment them out and uncomment the Experiment Copy
# Debugging Copy with initial values
class WasEmotionForm(forms.Form):

    attention = forms.ChoiceField(label="The robot's behavior draws my attention.", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Strongly disagree'), ('2', 'Disagree'), ('3', 'Neither agree nor disagree'), ('4', 'Agree'),
        ('5', 'Strongly agree')))
    likert_was_emotion = forms.ChoiceField(label="The robot's expression was emotional.", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Strongly disagree'), ('2', 'Disagree'), ('3', 'Neither agree nor disagree'), ('4', 'Agree'),
        ('5', 'Strongly agree')))
    # pri_emo = forms.CharField(label='', widget=forms.Select(choices=BLANK_CHOICE_DASH + PRI_EMO_CHOICES))


# Debugging Copy with initial values
class SurveyForm(forms.Form):

    anth_1 = forms.ChoiceField(label="anthropomorphism", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Fake'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Natural')))
    anth_2 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Machinelike'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Humanlike')))
    anth_3 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Unconscious'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Conscious')))
    anth_4 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Artificial'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Lifelike')))
    anth_5 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Moving rigidly'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Moving elegantly')))
    animacy_1 = forms.ChoiceField(label="animacy", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Dead'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Alive')))
    animacy_2 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Stagnant'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Lively')))
    animacy_3 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Mechanical'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Organic')))
    animacy_4 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Artificial'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Lifelike')))
    animacy_5 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Inert'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Interactive')))
    animacy_6 = forms.ChoiceField(label=" ", initial='1', widget=forms.RadioSelect, choices=(
        ('1', 'Apathetic'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Responsive')))


# TODO: Uncomment for the real experiment, and comment out for debugging
# # Experiment Copy without initial values
# class WasEmotionForm(forms.Form):
#
#     attention = forms.ChoiceField(label="The robot's behavior draws my attention.", widget=forms.RadioSelect, choices=(
#         ('1', 'Strongly disagree'), ('2', 'Disagree'), ('3', 'Neither agree nor disagree'), ('4', 'Agree'),
#         ('5', 'Strongly agree')))
#     likert_was_emotion = forms.ChoiceField(label="The robot's expression was emotional.", widget=forms.RadioSelect, choices=(
#         ('1', 'Strongly disagree'), ('2', 'Disagree'), ('3', 'Neither agree nor disagree'), ('4', 'Agree'),
#         ('5', 'Strongly agree')))
#     pri_emo = forms.CharField(label='', widget=forms.Select(choices=BLANK_CHOICE_DASH + PRI_EMO_CHOICES))
#
#
# # Experiment Copy without initial values
# class SurveyForm(forms.Form):
#
#     anth_1 = forms.ChoiceField(label="anthropomorphism", widget=forms.RadioSelect, choices=(
#         ('1', 'Fake'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Natural')))
#     anth_2 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Machinelike'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Humanlike')))
#     anth_3 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Unconscious'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Conscious')))
#     anth_4 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Artificial'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Lifelike')))
#     anth_5 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Moving rigidly'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Moving elegantly')))
#     animacy_1 = forms.ChoiceField(label="animacy", widget=forms.RadioSelect, choices=(
#         ('1', 'Dead'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Alive')))
#     animacy_2 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Stagnant'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Lively')))
#     animacy_3 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Mechanical'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Organic')))
#     animacy_4 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Artificial'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Lifelike')))
#     animacy_5 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Inert'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Interactive')))
#     animacy_6 = forms.ChoiceField(label=" ", widget=forms.RadioSelect, choices=(
#         ('1', 'Apathetic'), ('2', ''), ('3', ''), ('4', ''), ('5', 'Responsive')))

