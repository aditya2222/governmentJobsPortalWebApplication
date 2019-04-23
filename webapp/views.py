from django.shortcuts import render
from django.views import generic
from .models import JobsModel

# Create your views here.


class JobsListView(generic.ListView):
	template_name = 'jobs_list.html'
	models = JobsModel
	queryset = JobsModel.objects.all()


class JobsDetailView(generic.DetailView):
	model = JobsModel
	template_name = 'jobs_details.html'