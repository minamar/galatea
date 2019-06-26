# To download the database
#python manage.py shell

from evalemo.models import Judge
import pandas as pd
from collections import OrderedDict

# Change the destination and csv name in your computer
dest = '/home/mina/Dropbox/APRIL-MINA/django/galatea_vae/Data/ratings_grpilot.csv'

ratings = []

# Append judge entries in a dictionary
for judgei in Judge.objects.values():
	ratings.append(judgei)

# Save judge entries (python dictionary) to pandas dataframe
df = pd.DataFrame(ratings)

# Save in csv
df.to_csv(dest, sep='\t', encoding='utf-8')



# For Demografics
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


