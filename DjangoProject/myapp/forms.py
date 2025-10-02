from django import forms 
from django.contrib.auth.forms import UserCreationForm 
class CustomUserCreationForm(UserCreationForm): 
 class Meta(UserCreationForm.Meta): 
    model = UserCreationForm.Meta.model # Use the default User model 
    fields = UserCreationForm.Meta.fields + ('email',) # Add email to fields