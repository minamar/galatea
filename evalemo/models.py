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
    numPlay = models.IntegerField()
    startAnimTime = models.FloatField()
    endAnimTime = models.FloatField()
    order = models.CharField(max_length=5)
    diff_a = models.IntegerField()
    diff_v = models.IntegerField()

    def __str__(self):
        return '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t' % (
        self.trial, self.subject, self.idAnim, self.nameAnim, self.valence, self.arousal, self.numPlay,
        self.startAnimTime, self.endAnimTime, self.order, self.diff_a, self.diff_v)


class JudgeForm(ModelForm):
    class Meta:
        model = Judge
        fields = ['trial', 'subject', 'idAnim', 'nameAnim', 'valence', 'arousal', 'numPlay', 'startAnimTime',
                  'endAnimTime', 'order', 'diff_a', 'diff_v']


@python_2_unicode_compatible
class Demographic(models.Model):
    subject = models.IntegerField()
    age = models.IntegerField()
    sex = models.IntegerField()
    paf = models.IntegerField()
    naf = models.IntegerField()

    def __str__(self):
        return '%s\t%s\t%s\t%s\t%s\t' % (self.subject, self.age, self.sex, self.paf, self.naf)


class DemographicForm(ModelForm):
    class Meta:
        model = Demographic
        fields = ['subject', 'sex', 'age', 'paf', 'naf']


def get_absolute_url(self):
    """
    Returns the url to access a particular instance of the model.
    """
    return reverse('model-detail-view', args=[str(self.id)])

