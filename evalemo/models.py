# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Judge(models.Model):
    trial = models.IntegerField()
    subject = models.IntegerField()
    idAnim = models.IntegerField()
    nameAnim = models.CharField(max_length=300)
    valence = models.FloatField()
    arousal = models.FloatField()
    dominance = models.FloatField()
    attention = models.IntegerField()
    was_emotion = models.IntegerField()
    cat_emotion = models.CharField(max_length=300)
    reaction_time = models.FloatField()

    def __str__(self):
        return '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t' % (
            self.trial, self.subject, self.idAnim, self.nameAnim, self.valence, self.arousal, self.dominance,
            self.attention, self.was_emotion, self.cat_emotion, self.reaction_time)


class JudgeForm(ModelForm):
    class Meta:
        model = Judge
        fields = ['trial', 'subject', 'idAnim', 'nameAnim', 'valence', 'arousal', 'dominance', 'attention', 'was_emotion',
                  'cat_emotion', 'reaction_time']


@python_2_unicode_compatible
class Survey(models.Model):
    subject = models.IntegerField()
    condition = models.CharField(max_length=5)
    anth_1 = models.IntegerField()
    anth_2 = models.IntegerField()
    anth_3 = models.IntegerField()
    anth_4 = models.IntegerField()
    anth_5 = models.IntegerField()
    animacy_1 = models.IntegerField()
    animacy_2 = models.IntegerField()
    animacy_3 = models.IntegerField()
    animacy_4 = models.IntegerField()
    animacy_5 = models.IntegerField()
    animacy_6 = models.IntegerField()

    def __str__(self):
        return '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t' % (
            self.subject, self.condition, self.anth_1, self.anth_2, self.anth_3, self.anth_4, self.anth_5,
            self.animacy_1, self.animacy_2, self.animacy_3, self.animacy_4, self.animacy_5, self.animacy_6)


class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ['subject', 'condition', 'anth_1', 'anth_2', 'anth_3', 'anth_4', 'anth_5', 'animacy_1', 'animacy_2',
                  'animacy_3', 'animacy_4', 'animacy_5', 'animacy_6']


@python_2_unicode_compatible
class Demographic(models.Model):
    subject = models.IntegerField(unique=True)
    age = models.IntegerField()
    sex = models.CharField(max_length=1)
    anim_experience = models.IntegerField()

    def __str__(self):
        return '%s\t%s\t%s\t%s\t' % (self.subject, self.age, self.sex, self.anim_experience)


class DemographicForm(ModelForm):
    class Meta:
        model = Demographic
        fields = ['subject', 'sex', 'age', 'anim_experience']


