from django import forms

class ContactForm(forms.Form):
	from_email = forms.EmailField(max_length=100, required=True)
	email=forms.EmailField()
	message=forms.CharField(widget=forms.Textarea, required=True)