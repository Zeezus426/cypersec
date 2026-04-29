# forms.py
from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'business_name', 'email', 'phone', 'message', 'how_did_you_hear']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control'}),
            'business_name': forms.TextInput(attrs={'placeholder': 'Business Name (optional)', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '04XX XXX XXX', 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tell us about your situation or enquiry...', 'rows': 5, 'class': 'form-control'}),
            'how_did_you_hear': forms.TextInput(attrs={'placeholder': 'How did you hear about us?', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['business_name'].required = False
        self.fields['phone'].required = False
        self.fields['how_did_you_hear'].required = False
        self.fields['message'].label = 'Brief description of your situation or enquiry'
        self.fields['how_did_you_hear'].label = 'How did you hear about us?'