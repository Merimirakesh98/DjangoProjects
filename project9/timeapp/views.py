from django.shortcuts import render
from datetime import datetime

# Create your views here.
def welcome_client(request):
	date=datetime.now()
	hour=int(datetime.now().hour)
	msg='Welcome to Study_Online Good'
	if hour>0 and hour<12:
		msg=msg+'Morning'
	elif hour>12 and hour <16:
		msg=msg+'Afternoon'
	elif hour>16 and hour <21:
		msg=msg+'Evening'
	else:
		msg=msg+'Night'
	my_dict={'date':date,'msg':msg}
	return render(request=request, template_name='timeapp/time.html',context=my_dict)
