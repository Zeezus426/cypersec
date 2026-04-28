from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ContactForm
# Create your views here.
def home(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # Saves directly to the database
            return redirect('success_url')  # Replace with your success URL name
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})