from django.shortcuts import render
from .models import Post
from django.views.generic import View
from django.http import HttpResponse
from .forms import ContactForm

#our views.
def index(request):
	return render(request, 'index.html', {})
def events(request):
	return render(request, 'events.html', {})
def contact(request):
	return render(request, 'contact.html', {})
def post1(request):
	return render(request, 'post1.html', {})
def post2(request):
	return render(request, 'post2.html', {})
def post3(request):
	return render(request, 'post3.html', {})

def emailView(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			from_email=form.cleaned_data['from_email']
			message=form.cleaned_data['message']
			try:
				send_mail(message,from_email, ['bakshaksemmwa@gmail.com'])
			except BadHeaderError:
				return HttpResponse('invalid header found.')
			return redirect('success')
	return render(request, "contact.html",{'form':form})

def successView(request):
	return HttpResponse("Sent! Thank you for your message.")
