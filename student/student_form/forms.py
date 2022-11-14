from django import forms
from django.core.exceptions import ValidationError
from student_form.models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = "__all__"
        # fields = ["name", "content"]
        # exclude = ["name"]

    def clean(self):
        """
        Raise `ValidationError` if user didn't provide both name and email.
        """
        cleaned_data = super().clean() # Making sure default cleaning is being done.
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")
        age =  cleaned_data.get("age")

        

        if not name :
            raise ValidationError("Please provide valid name .")

        if not email:
            raise ValidationError("Please provide  email.")
        
        if age <18:

             raise ValidationError("Age must be greater than 18.")

        return cleaned_data

