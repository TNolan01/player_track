from django.forms.widgets import NumberInput
from django import forms
from django.forms import fields, CheckboxInput
from django.urls import reverse_lazy
from django.forms import ModelForm, BaseInlineFormSet, inlineformset_factory, modelformset_factory
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Field, Layout, ButtonHolder, Fieldset
from bootstrap_datepicker_plus.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput, YearPickerInput


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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
       
    widgets = {
        'session_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'session_name': forms.Textarea(attrs={'class': 'form-control'})
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
             'match_date': DatePickerInput()
        }
        
        
        
class Team_SelectionForm(forms.ModelForm):
    class Meta:
        model = Team_Selection
        fields = ['match', 'player', 'jersey_number', 'game_status', 'goals', 'points', 'notes']
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'player',
                'jersey_number',
                'game_status',
                'goals',
                'points',
                'notes'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )

