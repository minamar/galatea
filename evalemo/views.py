# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from evalemo.forms import ParticipantForm, SliderForm, DifficultyForm, PanasForm
from evalemo.models import Judge, Demographic
from django.core.management import call_command
from StringIO import StringIO
from django.http import HttpResponseRedirect
import random
from django.http import JsonResponse
import qi
import argparse
import sys
from scripts import runAnim
import time
import numpy
from scripts.animDict import trials_order, trials_order_tr


# Display the table Judges
def display(request):
    query_results = Judges.objects.all()


def evaluation(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        time_submit = time.time()
        # create a form instance and populate it with data from the request:
        form = SliderForm(request.POST)

        if form.is_valid():
            valence = form.cleaned_data['pleasure']
            arousal = form.cleaned_data['arousal']
            request.session['valence'] = valence
            request.session['arousal'] = arousal
            startAnimTime = time_submit - request.session['time_startAnim']
            endAnimTime = time_submit - request.session['time_stopAnim']
            request.session['startAnimTime'] = startAnimTime
            request.session['endAnimTime'] = endAnimTime

            return HttpResponseRedirect('/difficulty/')

    # if a GET (or any other method) we'll create a blank form
    else:

        form = SliderForm()

    # Replay count: How many times th participant replays the animation
    request.session['replay_count'] = 0
    # Trial count: Which trial are we on
    request.session['trial_count'] += 1
    print("\n=============================	Trial count: " + str(request.session['trial_count']) + "\n")
    # Store the trial count and the subject to use it in the evaluation view
    # Randomize the order of the sliders
    if (random.random() < 0.5):
        form.order_fields(['arousal', 'pleasure'])
        request.session['order'] = 'A'
    else:
        form.order_fields(['pleasure', 'arousal'])
        request.session['order'] = 'V'
    numPlay = request.session['replay_count']
    trial_count = request.session['trial_count']
    subject = request.session['subject']
    request.session['current_anim'] = trials_order[subject][trial_count - 1]  # anim_order[trial_count-1]
    return render(request, 'AS.html',
                  {'form': form, 'flag': 1, 'state': 1})  # (state == 1) ? "/ajaxplay" : "/ajaxplayTR"


def difficulty(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DifficultyForm(request.POST)
        if form.is_valid():
            diff_a = form.cleaned_data['likert_A']
            diff_v = form.cleaned_data['likert_V']
            subject = request.session['subject']
            valence = request.session['valence']
            arousal = request.session['arousal']
            numPlay = request.session['replay_count']
            idAnim = request.session['current_anim']
            nameAnim = request.session['nameAnim']
            order = request.session['order']
            trial = request.session['trial_count']
            startAnimTime = request.session['startAnimTime']
            endAnimTime = request.session['endAnimTime']
            # creating an judge object containing all the data
            judge_obj = Judge(trial=trial, valence=valence, arousal=arousal, subject=subject, numPlay=numPlay,
                              idAnim=idAnim, nameAnim=nameAnim, order=order, startAnimTime=startAnimTime,
                              endAnimTime=endAnimTime, diff_a=diff_a, diff_v=diff_v)
            # saving all the data in the current object into the database
            judge_obj.save()
            if (request.session['nItems'] == request.session['trial_count']):
                for sesskey in request.session.keys():
                    del request.session[sesskey]
                return HttpResponseRedirect('/goodbye/')
            else:
                return HttpResponseRedirect('/evaluation/')
    else:

        form = DifficultyForm()

    trial_count = request.session['trial_count']
    subject = request.session['subject']
    # Store the index for the next animation display
    if request.session['nItems'] < request.session['trial_count']:
        return HttpResponseRedirect('/goodbye/')

    return render(request, 'difficulty.html', {'form': form})  # initial template for homepage, 'flag':1, 'state':1


def ajaxplay(request):
    attempt = 0
    while True:
        # Starting time of the animation
        time_startAnim = time.time()
        # Connect to the robot
        session = qi.Session()
        try:
            session.connect("tcp://pepper.local:9559")
            # Run the animation and get the name of it
            nameAnim = runAnim.main(session, request.session['current_anim'])
            time_stopAnim = time.time()
            break
        except RuntimeError:
            time.sleep(5)
            attempt += 1
            print("***********************	Cannot connect to Naoqi. Attempt: " + str(attempt))
            continue

    # # Run the animation and get the name of it
    # nameAnim = runAnim.main(session, request.session['current_anim'])
    # Stooping time of the animation
    # time_stopAnim =time.time()
    # Replay button is clicked
    request.session['replay_count'] += 1
    numPlay = request.session['replay_count']
    # Only the first time animation is played, save the start/stop time
    if request.session['replay_count'] == 1:
        request.session['nameAnim'] = nameAnim
        request.session['time_startAnim'] = time_startAnim
        request.session['time_stopAnim'] = time_stopAnim

    print("=============================	(Replay count from ajax: " + str(request.session['replay_count']) + ") \n")
    return HttpResponse({'replay_count': numPlay})


def get_participant(request):
    # request.session.flush()
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            request.session['subject'] = subject
            request.session['age'] = age
            request.session['sex'] = sex

            request.session['nItems'] = len(trials_order[subject])
            return HttpResponseRedirect('/panas/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ParticipantForm()

    # # DUMMY VALUES WHEN ROBOT IS MISSING: REMOVE AFTER DEBUGGING
    # request.session['nameAnim'] = 'dummy'
    # request.session['time_startAnim'] = time.time()
    # request.session['time_stopAnim'] = time.time()
    # # DUMM VALUES END
    request.session['replay_count'] = 0
    request.session['trial_count'] = 0
    request.session['trial_count_tr'] = 0
    print("\n=============================	Session id at get_participant is: " + str(request.session.session_key))
    print("\n=============================	Trial count get_participant is: " + str(
        request.session['trial_count']) + "\n")
    return render(request, 'index.html', {'form': form})  # initial template for homepage


def get_panas(request):
    if request.method == 'POST':
        form = PanasForm(request.POST)
        if form.is_valid():
            pos_affect = int(form.cleaned_data['p1']) + int(form.cleaned_data['p3']) + int(
                form.cleaned_data['p5']) + int(form.cleaned_data['p9']) + int(form.cleaned_data['p10']) + int(
                form.cleaned_data['p12']) + int(form.cleaned_data['p14']) + int(form.cleaned_data['p16']) + int(
                form.cleaned_data['p17']) + int(form.cleaned_data['p19'])
            neg_affect = int(form.cleaned_data['p2']) + int(form.cleaned_data['p4']) + int(
                form.cleaned_data['p6']) + int(form.cleaned_data['p7']) + int(form.cleaned_data['p8']) + int(
                form.cleaned_data['p11']) + int(form.cleaned_data['p13']) + int(form.cleaned_data['p15']) + int(
                form.cleaned_data['p18']) + int(form.cleaned_data['p20'])
            print("\n=============================	Positive affect is : " + str(pos_affect))
            print("\n=============================	Negative affect is : " + str(neg_affect) + "\n")
            # request.session['pos_affect'] = pos_affect
            # request.session['neg_affect'] = neg_affect
            subject = request.session['subject']
            age = request.session['age']
            sex = request.session['sex']
            # Save demographic data in the database
            demographic_obj = Demographic(subject=subject, age=age, sex=sex, paf=pos_affect, naf=neg_affect)
            # saving all the data in the current object into the database
            demographic_obj.save()
            return HttpResponseRedirect('/instructionsTR/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = PanasForm()

    return render(request, 'panas.html', {'form': form})  # initial template for homepage


# Create your views here.
class HomePageView(TemplateView):
    template_name = "index.html"


class InstructionsAPageView(TemplateView):
    template_name = "instructionsA.html"


class InstructionsTRPageView(TemplateView):
    template_name = "instructionsTR.html"


class GoodbyePageView(TemplateView):
    template_name = "goodbye.html"


#### TRAINING SESSION VIEWS ###########
def tr_evaluation(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SliderForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/difficultyTR/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SliderForm()
    # Randomize the order of the sliders
    if (random.random() < 0.5):
        form.order_fields(['arousal', 'pleasure'])
        request.session['order'] = 'A'
    else:
        form.order_fields(['pleasure', 'arousal'])
        request.session['order'] = 'V'
    request.session['trial_count_tr'] += 1
    print("\n=============================	Trial_count_tr = " + str(request.session['trial_count_tr']) + "\n")
    request.session['current_anim_tr'] = trials_order_tr[request.session['trial_count_tr'] - 1]
    return render(request, 'AS.html',
                  {'form': form, 'flag': 1, 'state': 0})  # (state == 1) ? "/ajaxplay" : "/ajaxplayTR"


def tr_difficulty(request):
    if request.method == 'POST':
        form = DifficultyForm(request.POST)
        if form.is_valid():

            if len(trials_order_tr) == (request.session['trial_count_tr']):
                return HttpResponseRedirect('/instructionsA/')
            else:
                return HttpResponseRedirect('/evaluationTR/')
    else:
        form = DifficultyForm()
    return render(request, 'difficulty.html', {'form': form})


def tr_ajaxplay(request):
    attempt = 0
    while True:
        # Starting time of the animation
        time_startAnim = time.time()
        # Connect to the robot
        session = qi.Session()
        try:
            session.connect("tcp://pepper.local:9559")
            # Run the animation and get the name of it
            nameAnim = runAnim.main(session, request.session['current_anim_tr'])
            break
        except RuntimeError:
            attempt += 1
            print("***********************	Cannot connect to Naoqi. Attempt: " + str(attempt))
            continue

    return HttpResponse()
