from django.forms import ModelForm
from .models import Pharmacy

class PharmacyForm(ModelForm):
    class Meta:
        model = Pharmacy
        fields = ('mask','hand_sanitizer')
