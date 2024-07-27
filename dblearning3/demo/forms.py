from django import forms
from .models import Author

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


# When you create an instance of AuthorForm, Django will automatically generate form 
# fields that correspond to the fields in the Author model. For example, if the Author 
# model has fields like name, email, and bio, then the generated form will have input 
# fields for name, email, and bio.
        