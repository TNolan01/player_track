from django.forms.widgets import NumberInput
from django import forms
from django.forms import fields, CheckboxInput
from django.urls import reverse_lazy
from django.forms import ModelForm, BaseInlineFormSet, inlineformset_factory, modelformset_factory
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Field, Layout, ButtonHolder, Fieldset, Div, Row, Column
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput
from django.forms.models import formset_factory
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
       
    date_of_birth = forms.DateField(widget=NumberInput({'type':'date'}))
   
    def clean_name(self, *args, **kwargs):
        name = self.cleaned_data.get('name')
        for instance in Player.objects.all():
            if instance.name == name:
                raise forms.ValidationError('There is already a player named ' + name)
        return name


class PlayerEditForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
       
    date_of_birth = forms.DateField(widget=NumberInput({'type':'date'}))
   
    
class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, player):
        return "%s" % player.name
    
    
class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['session_date', 'session_name', 'player']
    
        widgets = {
            'session_date': DatePickerInput(attrs={'placeholder': 'YY-MM-DD'}, format='%Y-%m-%d', options=None),
            'session_name': forms.Textarea(attrs={'class': 'form-control', 'rows': '4', 'cols': '50'})
        }
     
    player = CustomMMCF(
        queryset=Player.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    
class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['match_date', 'match_details', 'venue']
        widgets = {
            
            'match_date': DatePickerInput(attrs={'placeholder': 'YY-MM-DD'}, format='%Y-%m-%d', options=None)
        }
    
    def clean_match_date(self, *args, **kwargs):
        match_date = self.cleaned_data.get('match_date')
        if match_date < datetime.date.today():
            raise ValidationError('A new match cannot be set for a date in the past')
        for instance in Match.objects.all():
            if instance.match_date == match_date:
                raise ValidationError('There is already a game on that date')
        return match_date

class SquadForm(forms.ModelForm):
    class Meta:
        model = Team_Selection
        fields = ['match', 'player', 'jersey_number', 'game_status']
        
        widgets = {
            'jersey_number': forms.Select(attrs={'class': 'form-control', 'required': False}),
            'game_status': forms.Select(attrs={'class': 'form-control', 'required': False}),
        }

        player = CustomMMCF(
            queryset=Player.objects.all(),
            widget=forms.Select(attrs={'class': 'form-select'})
        )


class CreateSquad(forms.ModelForm):
    class Meta:
        fields = ['match', 'player', 'jersey_number', 'game_status']

    def __init__(self, *args, **kwargs):
        super(CreateSquad, self).__init__(*args, **kwargs)
        self.fields['player'].widget.attrs['class'] = 'form-select'
                
    def clean_jersey_number(self, *args, **kwargs):
        jersey_number = self.cleaned_data.get('jersey_number')
        if jersey_number is None:
            raise forms.ValidationError('Please enter a jersey number')
        return jersey_number

    def clean_game_status(self, *args, **kwargs):
        game_status = self.cleaned_data.get('game_status')
        if len(game_status) < 2:
            raise forms.ValidationError('Please enter game status')
        return game_status


class ClubForm(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'
        
        widgets = {
            'club_name': forms.TextInput(attrs={'class': 'form-control'})
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        