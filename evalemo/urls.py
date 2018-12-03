# evalemo/urls.py
from django.conf.urls import url
from evalemo import views

app_name = 'evalemo'

urlpatterns = [

    url(r'^$', views.get_participant, name='get_participant'),  # index and participant number form 

    url(r'^evaluation/$', views.evaluation, name='evaluation'),

    url(r'^ajaxplay/$', views.ajaxplay, name='ajaxplay'),

    url(r'^instructionsA/$', views.InstructionsAPageView.as_view()), 

    url(r'^goodbye/$', views.GoodbyePageView.as_view()), 

    url(r'^difficulty/$', views.difficulty, name='difficulty'), 

    url(r'^panas/$', views.get_panas, name='get_panas'),


# Training

    url(r'^instructionsTR/$', views.InstructionsTRPageView.as_view()),

    url(r'^evaluationTR/$', views.tr_evaluation, name='tr_evaluation'),

    url(r'^ajaxplayTR/$', views.tr_ajaxplay, name='tr_ajaxplay'),

    url(r'^difficultyTR/$', views.tr_difficulty, name='tr_difficulty'), 

]