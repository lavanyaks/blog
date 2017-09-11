from django import forms

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].widget.attrs['placeholder'] = "Your name"
        self.fields['contact_email'].widget.attrs['placeholder'] = "Your email"
        self.fields['content'].widget.attrs['placeholder'] = "What would you like to say?"
