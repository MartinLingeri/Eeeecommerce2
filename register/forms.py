from django import forms
from django.contrib.auth.forms import UserCreationForm

from models.models import CustomUser, Countries, State


class RegisterForm(UserCreationForm):
    nombre = forms.CharField(max_length=45)
    COUNTRIES = []
    for p in Countries.objects.all():
        COUNTRIES.append((p.idcountries, p.name))
    country = forms.IntegerField(widget=forms.Select(choices=COUNTRIES))

    state = forms.IntegerField(widget=forms.Select(choices=[]))

    class Meta:
        model = CustomUser
        fields = ("nombre", "country", "state", "password1", "password2")

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)

        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
