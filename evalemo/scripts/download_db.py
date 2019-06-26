# To download the database and save the 3 models in csv dataframes, run a terminal from galatea_vae where manage.py is.
# The run the following:
# $ ./manage.py shell
# >>> execfile('evalemo/scripts/download_db.py')

from evalemo.models import Judge, Demographic, Survey
import pandas as pd


# TODO: Change the 3 destinations [and csv names if needed] accordingly in your computer
dest_judge = '/home/mina/Dropbox/APRIL-MINA/django/galatea_vae/Data/ratings.csv'
dest_democraphic = '/home/mina/Dropbox/APRIL-MINA/django/galatea_vae/Data/demographics.csv'
dest_survey = '/home/mina/Dropbox/APRIL-MINA/django/galatea_vae/Data/surveys.csv'


# For the ratings (DB: Judges)
ratings = []

# Append Judge entries in a dictionary
for judgei in Judge.objects.values():
	ratings.append(judgei)

# Save to pandas dataframe
df = pd.DataFrame(ratings)
df = df.drop('id', 1)
# Save in csv
df.to_csv(dest_judge, sep=',', encoding='utf-8')

# For demographics (DB: Demographics)
demographics = []

for demoi in Demographic.objects.values():
	demographics.append(demoi)

# Save to pandas dataframe
df = pd.DataFrame(demographics)
df = df.drop('id', 1)
# Save in csv
df.to_csv(dest_democraphic, sep=',', encoding='utf-8')


# For Godspeed questionnaire (DB: Surveys)
surveys = []

for surveyi in Survey.objects.values():
	surveys.append(surveyi)

# Save to pandas dataframe
df = pd.DataFrame(surveys)
df = df.drop('id', 1)
# Save in csv
df.to_csv(dest_survey, sep=',', encoding='utf-8')