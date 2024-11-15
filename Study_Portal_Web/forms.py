from django import forms
from .models import Homework, Notes, Todo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NotesForms(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter title",
                    "required": "required",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "Enter description",
                    "required": "required",
                }
            ),
        }


class HomeworkForm(forms.ModelForm):
    class Meta:
        model = Homework
        widgets = {
            "due": forms.DateTimeInput(attrs={"type": "datetime-local"}),
        }
        fields = ["subject", "title", "description", "due", "is_finished"]


class DashboardForm(forms.Form):
    text = forms.CharField(max_length=100, label="Enter Your Search : ")


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "is_finished"]


class ConversionForm(forms.Form):
    CHOICES = [("length", "Length"), ("mass", "Mass")]
    measurement = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)


class ConversionLengthForm(forms.Form):
    CHOICES = [("yard", "Yard"), ("foot", "Foot")]
    input = forms.CharField(
        required=False,
        label=False,
        widget=forms.TextInput(
            attrs={"type": "number", "placeholder": "Enter the Number: "}
        ),
    )
    measure1 = forms.CharField(label="", widget=forms.Select(choices=CHOICES))
    measure2 = forms.CharField(label="", widget=forms.Select(choices=CHOICES))


class ConversionMassForm(forms.Form):
    CHOICES = [("pound", "Pound"), ("kilogram", "Kilogram")]
    input = forms.CharField(
        required=False,
        label=False,
        widget=forms.TextInput(
            attrs={"type": "number", "placeholder": "Enter the Number: "}
        ),
    )
    measure1 = forms.CharField(label="", widget=forms.Select(choices=CHOICES))
    measure2 = forms.CharField(label="", widget=forms.Select(choices=CHOICES))


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]
