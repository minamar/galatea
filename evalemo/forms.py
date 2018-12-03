from django import forms
from django.utils.safestring import mark_safe


class ParticipantForm(forms.Form):
    subject = forms.IntegerField(label='Participant\'s number')
    sex = forms.IntegerField(label='Sex')
    age = forms.IntegerField(label='Age')


class SliderForm(forms.Form):
    pleasure = forms.FloatField(label='Pleasure', widget=forms.NumberInput(
        attrs={'type': 'range', 'name': 'AS_pleasure', 'id': 'AS-arousal', 'value': '.5', 'min': '0', 'max': '1',
               'step': '0.01'}))
    arousal = forms.FloatField(label='Arousal', widget=forms.NumberInput(
        attrs={'type': 'range', 'name': 'AS_arousal', 'id': 'AS-arousal', 'value': '.5', 'min': '0', 'max': '1',
               'step': '0.01'}))


class DifficultyForm(forms.Form):
    # likert_A = forms.ChoiceField(label='Level of Arousal: ', widget=forms.RadioSelect, choices=(('1','Very easy'), ('2','Somewhat easy'), ('3','Moderately'),('4','Somewhat hard'),('5','Very hard')))
    # likert_V = forms.ChoiceField(label='Level of Pleasure: ', widget=forms.RadioSelect, choices=(('1','Very easy'), ('2','Somewhat easy'), ('3','Moderately'),('4','Somewhat hard'),('5','Very hard')))
    likert_A = forms.ChoiceField(label='Level of Arousal: ', widget=forms.RadioSelect, choices=(
    ('1', 'Not confident at all'), ('2', 'Slightly confident'), ('3', 'Somewhat confident'), ('4', 'Confident'),
    ('5', 'Very confident')))
    likert_V = forms.ChoiceField(label='Level of Pleasure: ', widget=forms.RadioSelect, choices=(
    ('1', 'Not confident at all'), ('2', 'Slightly confident'), ('3', 'Somewhat confident'), ('4', 'Confident'),
    ('5', 'Very confident')))


# class PanasForm(forms.Form):
# 	p1 = forms.ChoiceField(label='Interested: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p2 = forms.ChoiceField(label='Distressed: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p3 = forms.ChoiceField(label='Excited: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p4 = forms.ChoiceField(label='Upset: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p5 = forms.ChoiceField(label='Strong: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p6 = forms.ChoiceField(label='Guilty: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p7 = forms.ChoiceField(label='Scared: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p8 = forms.ChoiceField(label='Hostile: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p9 = forms.ChoiceField(label='Enthusiastic: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p10 = forms.ChoiceField(label='Proud: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p11 = forms.ChoiceField(label='Irritable: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p12 = forms.ChoiceField(label='Alert: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p13 = forms.ChoiceField(label='Ashamed: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p14 = forms.ChoiceField(label='Inspired: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p15 = forms.ChoiceField(label='Nervous: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p16 = forms.ChoiceField(label='Determined: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p17 = forms.ChoiceField(label='Attentive: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p18 = forms.ChoiceField(label='Jittery: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p19 = forms.ChoiceField(label='Active: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))
# 	p20 = forms.ChoiceField(label='Afraid: ',initial='1', widget=forms.RadioSelect, choices=(('1','Very slightly or not at all'), ('2','A little'), ('3','Moderately'),('4','Quite a bit'),('5','Extremely')))

class PanasForm(forms.Form):
    p1 = forms.ChoiceField(label='Interested: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p2 = forms.ChoiceField(label='Distressed: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p3 = forms.ChoiceField(label='Excited: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p4 = forms.ChoiceField(label='Upset: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p5 = forms.ChoiceField(label='Strong: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p6 = forms.ChoiceField(label='Guilty: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p7 = forms.ChoiceField(label='Scared: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p8 = forms.ChoiceField(label='Hostile: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p9 = forms.ChoiceField(label='Enthusiastic: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p10 = forms.ChoiceField(label='Proud: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p11 = forms.ChoiceField(label='Irritable: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p12 = forms.ChoiceField(label='Alert: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p13 = forms.ChoiceField(label='Ashamed: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p14 = forms.ChoiceField(label='Inspired: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p15 = forms.ChoiceField(label='Nervous: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p16 = forms.ChoiceField(label='Determined: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p17 = forms.ChoiceField(label='Attentive: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p18 = forms.ChoiceField(label='Jittery: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p19 = forms.ChoiceField(label='Active: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
    p20 = forms.ChoiceField(label='Afraid: ', widget=forms.RadioSelect, choices=(
    ('1', 'Very slightly or not at all'), ('2', 'A little'), ('3', 'Moderately'), ('4', 'Quite a bit'),
    ('5', 'Extremely')))
