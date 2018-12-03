# If you want run it from the shell
#python manage.py shell

from evalemo.models import Judge
import pandas as pd
from collections import OrderedDict

ratings = []

# Append judge entries in a dictionary
for judgei in Judge.objects.values():
	ratings.append(judgei)

# ratings look like that:
# [{'arousal': 0.5,
#  'endAnimTime': 1.0440828800201416,
#  'group': 1,
#  u'id': 19,
#  'idAnim': 42,
#  'nameAnim': u'Amused_1',
#  'numPlay': 1,
#  'order': u'A',
#  'startAnimTime': 7.640270948410034,
#  'subject': 1,
#  'trial': 1,
#  'valence': 0.5}]


# Save judge entries (python dictionary) to pandas dataframe
df = pd.DataFrame(ratings)

# Save pandas df to pickle
df.to_pickle('/home/mina/Dropbox/APRIL-MINA/django/galatea/Data/ratingsP20.pkl')

# Read from pickle
P16= pd.read_pickle('/home/mina/Dropbox/APRIL-MINA/django/galatea/Data/ratingsP20.pkl')

# Save in csv
P16.to_csv('/home/mina/Dropbox/APRIL-MINA/django/galatea/Data/ratingsP20.csv', sep='\t', encoding='utf-8')



# nOW FOR THE DEMOGRAPHICS
from evalemo.models import Demographic
import pandas as pd
from collections import OrderedDict

demographics = []

# Append judge entries in a dictionary
for demoi in Demographic.objects.values():
	demographics.append(demoi)


# Save judge entries (python dictionary) to pandas dataframe
df = pd.DataFrame(demographics)

# Save pandas df to pickle
df.to_pickle('/home/mina/Dropbox/APRIL-MINA/django/galatea/Data/demographicsP20.pkl')

# Read from pickle
D16= pd.read_pickle('/home/mina/Dropbox/APRIL-MINA/django/galatea/Data/demographicsP20.pkl')

# Save in csv
D16.to_csv('/home/mina/Dropbox/APRIL-MINA/django/galatea/Data/demographicsP20.csv', sep='\t', encoding='utf-8')


