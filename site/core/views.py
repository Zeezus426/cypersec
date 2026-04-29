from django.shortcuts import render
from .forms import ContactForm

def home(request):
    return render(request, 'core/home.html')

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'core/contact_success.html', {
                'form': ContactForm(),
                'success': True
            })
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})
