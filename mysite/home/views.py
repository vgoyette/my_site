from django.shortcuts import render
from django.http import HttpResponse, request
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from home.models import Project
from .forms import ContactForm

# Create your views here.
def home(request):
	return render(request, 'index.html')

def projects(request):
	return render(request, 'projects.html')
	
def about(request):
	return render(request, 'about.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			email_subject = f'New contact {form.cleaned_data["email"]}: {form.cleaned_data["subject"]}'
			email_message = form.cleaned_data['message']
			send_mail(email_subject, email_message, settings.CONTACT_EMAIL, settings.ADMIN_EMAIL)
			return render(request, 'contact_success.html')
	
	form = ContactForm()
	context = {'form' : form}
	return render(request, 'contact.html', context)

def safar_details(request):
	return render(request, 'projects_details/safar_details.html')

def irishcribs_details(request):
	return render(request, 'projects_details/irishcribs_details.html')

def thiswebsite_details(request):
	return render(request, 'projects_details/thiswebsite_details.html')