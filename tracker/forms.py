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





class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'
        
    date_of_birth = forms.DateField(widget=NumberInput(attrs={'type':'date'}))


class CustomMMCF(forms.ModelMultipleChoiceField):
    def label_from_instance(self, player):
        return "%s" % player.name
    
    
class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ['session_date','session_name','player']
    
    
        widgets = {
        'session_date': DatePickerInput(attrs=None, format ='%Y-%d-%m', options=None),
        'session_name': forms.Textarea(attrs={'class': 'form-control', 'rows':'4', 'cols':'50'})
        }
     
    player = CustomMMCF(
        queryset=Player.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    
class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['match_date','match_details','venue']
        widgets = {
            
            'match_date': DatePickerInput(attrs=None, format ='%Y-%d-%m', options=None)
        }
        
  
        
class SquadForm(forms.ModelForm):
    class Meta:
        model = Team_Selection
        fields = ['match', 'player', 'jersey_number', 'game_status']
        
        widgets = {
        'jersey_number': forms.Select(attrs={'class': 'form-control','required':False, 'placeholder':'Jersey'}),
        'game_status' : forms.Select(attrs={'class': 'form-control','required':False}), 
        }

        player = CustomMMCF(
        queryset=Player.objects.all(),
        widget=forms.Select(attrs={'class': 'form-select' })
        )


class CreateSquad(forms.ModelForm):
    class Meta:
        fields = ['match', 'player', 'jersey_number', 'game_status']

    def __init__(self, *args, **kwargs):
        super(CreateSquad, self).__init__(*args, **kwargs)
        self.fields['player'].widget.attrs['class'] = 'form-select'
