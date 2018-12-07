from django.shortcuts import render
from django.views.generic import ListView

from django.http import HttpResponseRedirect
from .forms import NewProjectForm
from .models import Project
# Create your views here.

class NewView(ListView):
    model = Project
    template_name = 'projects/partials/new.html' 



def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NewProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            p = Project(**form.cleaned_data)
            p.save()
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NewProjectForm()

    return render(request, 'projects/partials/create.html', {'form': form})