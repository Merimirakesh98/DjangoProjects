from django.shortcuts import render
from moviesapp.forms import MoviesForm
from moviesapp.models import Movies

def home_page(request):
	return render(request=request, template_name='moviesapp/home.html')

def add_movie(request):
	movie_form=MoviesForm()
	my_dict={'movie_form':movie_form}
	if request.method=='POST':
		form_data=MoviesForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit=True)

	if request.method=="POST":
		form_data=MoviesForm(request.POST)
		if form_data.is_valid():
			print(f'Movie Name:{form_data.cleaned_data["name"]}')
			print(f'Hero Name:{form_data.cleaned_data["hero"]}')
			print(f'Heroine Name:{form_data.cleaned_data["heroine"]}')
			print(f'Director Name:{form_data.cleaned_data["director"]}')
			print(f'Producer Name:{form_data.cleaned_data["producer"]}')
			print(f'Music Director Name:{form_data.cleaned_data["music"]}')
			print(f'Release Date:{form_data.cleaned_data["release"]}')
		
	return render(request=request, template_name='moviesapp/add.html',context=my_dict)


def movie_list(request):
	movie_data=Movies.objects.all()
	my_dict={'movie_data':movie_data}
	return render(request=request,template_name='moviesapp/list.html',context=my_dict)

