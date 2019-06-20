# evalemo/urls.py
from django.conf.urls import url
from evalemo import views


app_name = 'evalemo'

urlpatterns = [

    url(r'^$', views.get_participant, name='get_participant'),  # index and participant number form 

    url(r'^goodbye/$', views.GoodbyePageView.as_view()),



    # Task 2
    url(r'^evaluation/$', views.evaluation, name='evaluation'),

    url(r'^ajaxplay/$', views.ajaxplay, name='ajaxplay'),

    url(r'^instructions_eval/$', views.InstructionsEvalPageView.as_view()),

    url(r'^wasEmotion/$', views.was_emotion, name='was_emotion'),


    # Task 1
    url(r'^play_comp/$', views.play_comp, name='play_comp'),

    url(r'^ajaxplay_comp/$', views.ajaxplay_comp, name='ajaxplay_comp'),




# Training

    url(r'^instructionsTR/$', views.InstructionsTRPageView.as_view()),

    url(r'^evaluationTR/$', views.tr_evaluation, name='tr_evaluation'),

    url(r'^ajaxplayTR/$', views.tr_ajaxplay, name='tr_ajaxplay'),

    url(r'^wasEmotionTR/$', views.tr_was_emotion, name='tr_was_emotion'),

]