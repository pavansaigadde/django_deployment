from django.shortcuts import render

#from myapp import forms
# Create your views here.

# Create a function for index HTML

def index(request):
	my_dict = {'add_text': 'This data is added using views.py'}
	return render(request,'myapp/index.html',context=my_dict)

