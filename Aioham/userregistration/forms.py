from django.forms import ModelForm
from userregistration.models import Profile 

# Create the form class.
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "location", "birth_date", "img"]

