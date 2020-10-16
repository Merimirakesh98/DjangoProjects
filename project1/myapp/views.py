from django.shortcuts import render
from myapp.forms import LoginForm
from datetime import datetime

# Create your views her
def home_page(request):
	form=LoginForm()
	my_dict={'form':form}
	return render(request=request, template_name='myapp/homepage.html',context=my_dict)

def collect_page(request):
	name=request.GET['name']
	my_dict={'name':name}
	response=render(request=request, template_name='myapp/collect.html',context=my_dict)
	response.set_cookie('name',name)
	return response

def display(request):
	name=request.COOKIES['name']
	data=datetime.now()
	my_dict={'name':name,'data':data}
	return render(request=request, template_name='myapp/display.html',context=my_dict)
