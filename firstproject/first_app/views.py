from django.shortcuts import render
from django.http import HttpResponse
# import models
from first_app.models import Topic,Webpage,Accessrecord
# Create your views here.

def index(request):
	#This will get objects with attributes name and date
	access_list = Accessrecord.objects.order_by('date')
	date_dict={'access_records':access_list}

	webpage_list=Webpage.objects.order_by('topic')
	print(webpage_list)
	webpage_dict={'my_page':webpage_list}
	for x,y in webpage_dict.items():
		print(x,y)
	#first_webpage=Webpage.objects[0]
	#print(first_webpage)

	return render(request,'first_app/index.html',context=date_dict)
	#return HttpResponse('Hello World')
