from django.contrib import admin

from moviesapp.models import Movies

class MoviesAdmin(admin.ModelAdmin):
    '''
        Admin View for Movie
    '''
    list_display = ('name','hero','heroine','director','producer','music','release')
    
admin.site.register(Movies, MoviesAdmin)
# Register your models here.
