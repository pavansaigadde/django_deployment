import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstproject.settings')

import django
django.setup()

##Fake population script

import random
from first_app.models import Topic,Webpage,Accessrecord

##import faker module
from faker import Faker 

fakegen = Faker()

# Create a list of topics
topics = ['Politics','Technology','Business','Sports','Entertainment']

#Create a function to add these topics to Topic model

def add_topic():
	#Get only one element
	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t


def populate(N=5):

	for entry in range(N):

		# Get topic for the entry
		top=add_topic()
		# Create fake data for that entry
		fake_name=fakegen.company()
		fake_url=fakegen.url()
		fake_date=fakegen.date()

		# create new webentry
		Webpg = Webpage.objects.get_or_create(topic=top,name=fake_name,url=fake_url)[0]
		# create new access records
		acc_rec=Accessrecord.objects.get_or_create(name=Webpg,date=fake_date)[0]

if __name__ == '__main__':
	print('populating data....')
	populate(20)
	print('population completed!!')