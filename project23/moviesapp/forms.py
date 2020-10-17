from django import forms
from moviesapp.models import Movies

class MoviesForm(forms.ModelForm):
	class Meta:
		model=Movies
		fields=('name','hero','heroine','director','producer','music','release')
 
    