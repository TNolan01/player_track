from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.forms import inlineformset_factory, formset_factory, modelformset_factory
from .forms import *
from .models import *
from django.template import RequestContext 
from django.http import HttpResponse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic import DetailView
from django.db.models import Count
from extra_views import CreateWithInlinesView, UpdateWithInlinesView, InlineFormSetFactory



#main related views
def home(request):
    all_players = Player.objects.all().count()
    all_sessions = Session.objects.all().count()
    all_matches = Match.objects.all().count()
    trainings = Session.objects.all().order_by('session_date')[:5]
    matches = Match.objects.all().order_by('match_date')[:5]
    context = {'all_players': all_players,
               'all_sessions': all_sessions,
               'all_matches': all_matches,
               'trainings': trainings,
               'matches': matches}
    return render(request, 'main/dashboard.html', context)


def stats(request):
    all_players = Player.objects.all().count()
    all_sessions = Session.objects.all().count()
    context = {'all_players': all_players,
               'all_sessions': all_sessions}
    return render(request, 'main/stats.html', context)



#training related views
def training_dashboard(request):
    trainings = Session.objects.all().order_by('session_date')
    context = {'trainings': trainings}
    return render(request, 'training/training_dashboard.html', context)


class TrainingCreateView(CreateView):
    model = Session
    form_class = SessionForm
    template_name = 'training/create_session.html'
    success_url = reverse_lazy('training_dashboard')
    
    
class TrainingUpdateView(UpdateView):
    model = Session
    form_class = SessionForm
    template_name = 'training/update_session.html'
    success_url = reverse_lazy('training_dashboard')
    
    
class TrainingDeleteView(DeleteView):
    model = Session
    template_name = 'training/delete_session.html'
    success_url = reverse_lazy('training_dashboard')
    
        
#player related views
def player_dashboard(request):
    all_players = Player.objects.all().count
    session_total = Player.objects.values('name').annotate(count_sessions=Count('session'))
    training = Session.objects.all()
    all_sessions = Session.objects.all().count()
    players = Player.objects.all().order_by('name')
    training_total = Session.objects.all().count()
    context  = {'training': training,
                'session_total': session_total,
                'all_sessions': all_sessions,
                'players': players,
                'training_total': training_total,
                'all_players': all_players
                }
        
    return render(request, 'player/player_dashboard.html', context)


class PlayerCreateView(CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player/create_player.html'
    success_url = reverse_lazy('player_dashboard')
    
    
class PlayerUpdateView(UpdateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player/update_player.html'
    success_url = reverse_lazy('player_dashboard')
    
    
class PlayerDetailView(DetailView):
    queryset = Session.objects.all()
    template_name = 'player/training_list.html'
    success_url = reverse_lazy('player_dashboard')
    
    
class PlayerDeleteView(DeleteView):
    model = Player
    template_name = 'player/delete_player.html'
    success_url = reverse_lazy('player_dashboard')

# This returns the training attendance history for each individual player, part of player section.
def training_list(request, pk):
    player = Player.objects.get(id=pk)
    session_total = Session.objects.all().count()
    training = Session.objects.all().filter(player=player)
    training_total = Session.objects.all().filter(player=player).count()
    if training_total == 0:
        attendance = 'No training attended. 0'
    else:
        attendance = int((training_total * 100) / session_total)
    context  = {'training': training,
                'session_total': session_total,
                'training_total': training_total,
                'player': player,
                'attendance': attendance}
    return render(request,'player/training_list.html', context)


#List all players, their attendance and the attendance percentage.
def squad_attendance(request):
    session_total = Player.objects.values('name').annotate(count_sessions=Count('session'))
    training = Session.objects.all()
    st = Session.objects.all().count()
    players = Player.objects.all().count
    training_total = Session.objects.all().count()
    context  = {'training': training,
                'session_total': session_total,
                'st': st,
                'players': players,
                'training_total': training_total,
                }
    return render(request,'player/squad_attendance.html', context)


class SquadStats(ListView):
    model = Session
    template_name = 'player/squad_stats.html'
    success_url = reverse_lazy('player_dashboard')


    def get_queryset(self, *args, **kwargs):
        return Player.objects.order_by('name')
             
    
    def get_context_data(self, **kwargs):
        context = super(SquadStats, self).get_context_data(**kwargs)
        context ['st'] = Session.objects.all().count()
        context ['player'] = Player.objects.all()
        context ['session_total'] = Player.objects.values('name').annotate(count_sessions=Count('session'))
           
        return context
    
    
    def calc(self):
        st = Session.objects.all().count
        session_total = Player.objects.values('name').annotate(count_sessions=Count('session'))
        return self(calc=([session_total.count_sessions]*100)/st)


# match related views
def match_dashboard(request):
    matches = Match.objects.all().order_by('match_date')
    context = {'matches': matches}
    return render(request, 'match/match_dashboard.html', context)


class MatchCreateView(CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'match/create_match.html'
    success_url = reverse_lazy('match_dashboard')
    
    
class MatchUpdateView(UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'match/update_match.html'
    success_url = reverse_lazy('match_dashboard')
    
    
class MatchDeleteView(DeleteView):
    model = Match
    template_name = 'match/delete_match.html'
    success_url = reverse_lazy('match_dashboard')
  
    
def add_player_to_match(request, pk):
    GameFormSet = inlineformset_factory(Match, Team_Selection, form = Team_SelectionForm)
    match = Match.objects.get(id=pk)
    player = Player.objects.all()
    formset = GameFormSet(instance=match)
    if request.method == 'POST':
        formset = GameFormSet(request.POST, instance=match)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset':formset,
               'player':player,
               'match': match
            }
    return render(request, 'match/add_player_to_match.html', context)


# Test Views for Match functions



    