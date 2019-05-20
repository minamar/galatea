# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from evalemo.forms import ParticipantForm, SliderForm, WasEmotionForm, SurveyForm
from evalemo.models import Judge, Demographic, Survey
from django.http import HttpResponseRedirect
from scripts import play_df_cond_gaussian_sampling
from scripts.animDict import trials_order_tr
from scripts.anim_utils import *

naoqi_session = None
motion_ses = None
posture_ses = None
leds_ses = None
nItems = 24
nItems_tr = 3
n_comparisons = 4

# Display the table Judges
def display(request):
    query_results = Judge.objects.all()


########## TASK 1 VIEW - COMPARISON ##################


def play_comp(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        time_submit = time.time()
        # create a form instance and populate it with data from the request:
        form = SurveyForm(request.POST)

        if form.is_valid():
            subject = request.session['subject']
            idAnim = request.session['current_anim']
            condition = idAnim
            anth_1 = int(form.cleaned_data['anth_1'])
            anth_2 = int(form.cleaned_data['anth_2'])
            anth_3 = int(form.cleaned_data['anth_3'])
            anth_4 = int(form.cleaned_data['anth_4'])
            anth_5 = int(form.cleaned_data['anth_5'])
            animacy_1 = int(form.cleaned_data['animacy_1'])
            animacy_2 = int(form.cleaned_data['animacy_2'])
            animacy_3 = int(form.cleaned_data['animacy_3'])
            animacy_4 = int(form.cleaned_data['animacy_4'])
            animacy_5 = int(form.cleaned_data['animacy_5'])
            animacy_6 = int(form.cleaned_data['animacy_6'])

            # Save demographic data in the database
            survey_obj = Survey(subject=subject, condition=condition, anth_1=anth_1, anth_2=anth_2, anth_3=anth_3,
                                anth_4=anth_4, anth_5=anth_5, animacy_1=animacy_1, animacy_2=animacy_2,
                                animacy_3=animacy_3, animacy_4=animacy_4, animacy_5=animacy_5, animacy_6=animacy_6)
            # saving all the data in the current object into the database
            survey_obj.save()
            if n_comparisons == request.session['comp_trial_count']:
                # for sesskey in request.session.keys():
                #     del request.session[sesskey]
                return HttpResponseRedirect('/instructionsTR/')
            else:
                return HttpResponseRedirect('/play_comp/')
        # if a GET (or any other method) we'll create a blank form
    else:

        form = SurveyForm()

    # Comparison trial count: Which trial are we on
    request.session['comp_trial_count'] += 1
    comp_trial_count = request.session['comp_trial_count']
    print("\n=============================	Comparison trial count: " + str(comp_trial_count) + "\n")

    # The id of current anim from the permutation of the listed anims (comp_trials_list)
    request.session['current_anim'] = request.session['comp_trials_list'][comp_trial_count - 1]  # anim_order[trial_count-1]
    print("\n=============================	Current anim: " + str(request.session['current_anim']) + "\n")
    print("\n=============================	Comp_trials_list: " + str(request.session['comp_trials_list']) + "\n")
    return render(request, 'play_comp.html',
                  {'form': form, 'flag': 1, 'state': 1})  # (state == 1) ? "/ajaxplay" : "/ajaxplayTR"


def ajaxplay_comp(request):

    while True:
        # Run the animation and get the name of it
        nameAnim = play_df_cond_gaussian_sampling.main(motion_ses, leds_ses, request.session['current_anim'])
        break

    # Replay button is clicked
    request.session['comp_replay_count'] += 1

    return HttpResponse()




########## TASK 2 VIEW - EVALUATION ##################

def evaluation(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        time_submit = time.time()
        # create a form instance and populate it with data from the request:
        form = SliderForm(request.POST)

        if form.is_valid():
            valence = form.cleaned_data['pleasure']
            arousal = form.cleaned_data['arousal']
            dominance = form.cleaned_data['dominance']
            request.session['valence'] = valence
            request.session['arousal'] = arousal
            request.session['dominance'] = dominance
            request.session['reaction_time'] = time_submit - request.session['time_stopAnim']

            return HttpResponseRedirect('/wasEmotion/')

    # if a GET (or any other method) we'll create a blank form
    else:

        form = SliderForm()

    # Replay count: How many times th participant replays the animation
    request.session['replay_count'] = 0
    # Trial count: Which trial are we on
    request.session['trial_count'] += 1
    print("\n=============================	Trial count: " + str(request.session['trial_count']) + "\n")
    # Store the trial count and the subject to use it in the evaluation view

    form.order_fields(['pleasure', 'arousal', 'dominance'])

    trial_count = request.session['trial_count']
    subject = request.session['subject']
    request.session['current_anim'] = request.session['trials_list'][trial_count - 1]  # anim_order[trial_count-1]
    return render(request, 'AS.html',
                  {'form': form, 'flag': 1, 'state': 1})  # (state == 1) ? "/ajaxplay" : "/ajaxplayTR"


def was_emotion(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = WasEmotionForm(request.POST)
        if form.is_valid():
            attention = form.cleaned_data['attention']
            was_emotion = form.cleaned_data['likert_was_emotion']
            cat_emotion = form.cleaned_data['cat_emotion']
            subject = request.session['subject']
            valence = request.session['valence']
            arousal = request.session['arousal']
            dominance = request.session['dominance']
            idAnim = request.session['current_anim']
            nameAnim = request.session['nameAnim']
            trial = request.session['trial_count']
            reaction_time = request.session['reaction_time']
            # creating a judge object containing all the data
            judge_obj = Judge(attention=attention, was_emotion=was_emotion, cat_emotion=cat_emotion, trial=trial, valence=valence, arousal=arousal, dominance=dominance, subject=subject,
                              idAnim=idAnim, nameAnim=nameAnim, reaction_time=reaction_time)
            # saving all the data in the current object into the database
            judge_obj.save()
            if nItems == request.session['trial_count']:
                for sesskey in request.session.keys():
                    del request.session[sesskey]
                return HttpResponseRedirect('/goodbye/')
            else:
                return HttpResponseRedirect('/evaluation/')
    else:

        form = WasEmotionForm()

    trial_count = request.session['trial_count']
    subject = request.session['subject']
    # Store the index for the next animation display
    if nItems < request.session['trial_count']:
        return HttpResponseRedirect('/goodbye/')

    return render(request, 'wasEmotion.html', {'form': form})  # initial template for homepage, 'flag':1, 'state':1


def ajaxplay(request):

    while True:
        # Run the animation and get the name of it
        nameAnim = play_df_cond_gaussian_sampling.main(motion_ses, leds_ses, request.session['current_anim'])
        time_stopAnim = time.time()
        break

    # Replay button is clicked
    request.session['replay_count'] += 1
    # numPlay = request.session['replay_count']
    # # Only the first time animation is played, save the stop time
    if request.session['replay_count'] == 1:
        request.session['nameAnim'] = nameAnim
        request.session['time_stopAnim'] = time_stopAnim

    return HttpResponse()

################ PARTICIPANT VIEW ################################
def get_participant(request):
    global naoqi_session
    global motion_ses
    global leds_ses

    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            age = form.cleaned_data['age']
            sex = form.cleaned_data['sex']
            anim_experience = form.cleaned_data['anim_experience']
            request.session['subject'] = subject
            request.session['age'] = age
            request.session['sex'] = sex
            request.session['trials_list'] = np.random.permutation(range(1, nItems + 1)).tolist()
            request.session['comp_trials_list'] = np.random.permutation([28, 29, 30, 31]).tolist()
            # Save demographic data in the database
            demographic_obj = Demographic(subject=subject, age=age, sex=sex, anim_experience=anim_experience)
            # saving all the data in the current object into the database
            demographic_obj.save()
            return HttpResponseRedirect('/play_comp/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ParticipantForm()

    # # DUMMY VALUES WHEN ROBOT IS MISSING: Comment out after debugging
    # request.session['nameAnim'] = 'dummy'
    # request.session['time_startAnim'] = time.time()
    # request.session['time_stopAnim'] = time.time()

    # Connect to robot (Change IP in anim_utils)
    naoqi_session = naoqi_connect()
    # Load naoqi modules
    motion_ses, aplayer_ses, posture_ses, leds_ses, alife_ses = load_modules(naoqi_session)
    # Resting state
    init_rest(leds_ses, alife_ses, posture_ses)

    request.session['replay_count'] = 0
    request.session['trial_count'] = 0          # Task 2 main
    request.session['comp_trial_count'] = 0     # Task 1
    request.session['trial_count_tr'] = 0       # Task 2 training
    print("\n=============================	Session id at get_participant is: " + str(request.session.session_key))
    print("\n=============================	Trial count get_participant is: " + str(
        request.session['trial_count']) + "\n")
    return render(request, 'index.html', {'form': form})  # initial template for homepage


############ HTML VIEWS #######################
class HomePageView(TemplateView):
    template_name = "index.html"


class InstructionsEvalPageView(TemplateView):
    template_name = "instructions_eval.html"


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
            return HttpResponseRedirect('/wasEmotionTR/')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = SliderForm()

    form.order_fields(['pleasure', 'arousal', 'dominance'])
    request.session['order'] = 'VAD'

    request.session['trial_count_tr'] += 1
    print("\n=============================	Trial_count_tr = " + str(request.session['trial_count_tr']) + "\n")
    request.session['current_anim_tr'] = trials_order_tr[request.session['trial_count_tr'] - 1]
    return render(request, 'AS.html',
                  {'form': form, 'flag': 1, 'state': 0})  # (state == 1) ? "/ajaxplay" : "/ajaxplayTR"


def tr_was_emotion(request):
    if request.method == 'POST':
        form = WasEmotionForm(request.POST)
        if form.is_valid():

            if len(trials_order_tr) == request.session['trial_count_tr']:
                return HttpResponseRedirect('/instructions_eval/')
            else:
                return HttpResponseRedirect('/evaluationTR/')
    else:
        form = WasEmotionForm()
    return render(request, 'wasEmotion.html', {'form': form})


def tr_ajaxplay(request):
    while True:
        if motion_ses is not None:
            play_df_cond_gaussian_sampling.main(motion_ses, leds_ses, request.session['current_anim_tr'])
            break
        else:
            print("Motion ses is none")

    return HttpResponse()
