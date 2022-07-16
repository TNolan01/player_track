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
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *


# main related views
@unauthenticated_user
def register_page(request):
    form = CreateUserForm
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='visitor')
            user.groups.add(group)
            messages.info(request, 'Account created for ' + username)
            return redirect('login')
        else:
            print(form.errors)
    context = {'form': form}
    return render(request, 'main/register.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in')
            return redirect('dashboard')
        else:
            messages.info(request, 'Username and/or password are incorrect')
    context = {}
    return render(request, 'main/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'coaching', 'visitor'])
def home(request):
    all_players = Player.objects.all().count()
    all_sessions = Session.objects.all().count()
    all_matches = Match.objects.all().count()
    tomorrow = datetime.datetime.today()+datetime.timedelta()
    trainings = Session.objects.filter(session_date__gte=tomorrow)[:5]
    matches = Match.objects.filter(match_date__gte=tomorrow)[:5]
    club = Club.objects.filter()[0]
    context = {'all_players': all_players,
               'all_sessions': all_sessions,
               'all_matches': all_matches,
               'trainings': trainings,
               'matches': matches,
               'club': club
               }
    return render(request, 'main/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def stats(request):
    all_players = Player.objects.all().count()
    all_sessions = Session.objects.all().count()
    context = {'all_players': all_players,
               'all_sessions': all_sessions}
    return render(request, 'main/stats.html', context)


def no_access(request):
    return render(request, 'main/no_access.html')


# training related views
@login_required(login_url='login')
def training_dashboard(request):
    tomorrow = datetime.datetime.today()+datetime.timedelta()
    sessions = Session.objects.filter(session_date__gte=tomorrow)[:5]
    context = {'sessions': sessions}
    return render(request, 'training/training_dashboard.html', context)


class TrainingCreateView(SuccessMessageMixin, CreateView):
    model = Session
    form_class = SessionForm
    template_name = 'training/create_session.html'
    success_url = reverse_lazy('training_dashboard')
    success_message = "New training session created"


class TrainingUpdateView(SuccessMessageMixin, UpdateView):
    model = Session
    form_class = SessionForm
    template_name = 'training/update_session.html'
    success_url = reverse_lazy('training_dashboard')
    success_message = "Successfully updated training session"


class TrainingDeleteView(SuccessMessageMixin, DeleteView):
    model = Session
    template_name = 'training/delete_session.html'
    success_url = reverse_lazy('training_dashboard')
    success_message = "Training session deleted"
    
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(TrainingDeleteView, self).delete(request, *args, **kwargs)


class TrainingListView(ListView):
    model = Session
    template_name = 'training/training_list.html'
    success_url = reverse_lazy('training_dashboard')


# player related views
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def player_dashboard(request):
    all_players = Player.objects.all().count
    session_total = Player.objects.values('name').annotate(count_sessions=Count('session'))
    training = Session.objects.all()
    all_sessions = Session.objects.all().count()
    players = Player.objects.all().order_by('name')
    training_total = Session.objects.all().count()
    all_matches = Match.objects.all().count()
    context = {'training': training,
               'session_total': session_total,
               'all_sessions': all_sessions,
               'players': players,
               'training_total': training_total,
               'all_players': all_players,
               'all_matches': all_matches
               }

    return render(request, 'player/player_dashboard.html', context)


class PlayerCreateView(SuccessMessageMixin, CreateView):
    model = Player
    form_class = PlayerForm
    template_name = 'player/create_player.html'
    success_url = reverse_lazy('player_dashboard')
    success_message = "New player created successfully"


class PlayerUpdateView(SuccessMessageMixin, UpdateView):
    model = Player
    form_class = PlayerEditForm
    template_name = 'player/update_player.html'
    success_url = reverse_lazy('player_dashboard')
    success_message = "Player data updated successfully"


class PlayerDetailView(DetailView):
    queryset = Session.objects.all()
    template_name = 'player/training_list.html'
    success_url = reverse_lazy('player_dashboard')


class PlayerDeleteView(SuccessMessageMixin, DeleteView):
    model = Player
    template_name = 'player/delete_player.html'
    success_url = reverse_lazy('player_dashboard')
    success_message = "The player has been deleted successfully"
    
    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(PlayerDeleteView, self).delete(request, *args, **kwargs)


# This returns the training attendance history for each individual player, part of player section.
@login_required(login_url='login')
def training_list(request, pk):
    player = Player.objects.get(id=pk)
    session_total = Session.objects.all().count()
    training = Session.objects.all().filter(player=player)
    training_total = Session.objects.all().filter(player=player).count()
    if training_total == 0:
        attendance = 'No training attended. 0'
    else:
        attendance = int((training_total * 100) / session_total)
    context = {'training': training,
               'session_total': session_total,
               'training_total': training_total,
               'player': player,
               'attendance': attendance}
    return render(request, 'player/training_list.html', context)


# List all players, their attendance and the attendance percentage.
@login_required(login_url='login')
def squad_attendance(request):
    session_total = Player.objects.values('name').annotate(count_sessions=Count('session'))
    player = Player.objects.all()
    training = Session.objects.all()
    st = Session.objects.all().count()
    all_players = Player.objects.all().count
    training_total = Session.objects.all().filter(player=player).count()
    if training_total == 0:
        attendance = 'No training attended. 0'
    else:
        attendance = int((training_total * 100) / session_total)
    context = {'training': training,
               'session_total': session_total,
               'st': st,
               'all_players': all_players,
               'training_total': training_total,
               'attendance': attendance}
    return render(request, 'player/squad_attendance.html', context)


# This returns the game attendance history for each individual player, part of player section.
@login_required(login_url='login')
def game_list(request, pk):
    player = Player.objects.get(id=pk)
    total_games = Match.objects.all().count()
    games_played = Team_Selection.objects.all().filter(player=player).order_by('match')
    total_matches_played = Team_Selection.objects.all().filter(player=player).count()
    if total_matches_played == 0:
        played = 'No games played'
        played_percentage = 0
    else:
        played = total_matches_played
        played_percentage = int((played * 100) / total_games)
    context = {'total_games': total_games,
               'games_played': games_played,
               'total_matches_played': total_matches_played,
               'player': player,
               'played': played,
               'played_percentage': played_percentage}
    return render(request, 'player/game_list.html', context)


class SquadStats(ListView):
    model = Session
    template_name = 'player/squad_stats.html'
    success_url = reverse_lazy('player_dashboard')

    def get_queryset(self, *args, **kwargs):
        return Player.objects.order_by('name')

    def get_context_data(self, **kwargs):
        context = super(SquadStats, self).get_context_data(**kwargs)
        context['all_sessions'] = Session.objects.all().count()
        context['player'] = Player.objects.all()
        context['session_total'] = Player.objects.values('name').annotate(count_sessions=Count('session')).order_by('-count_sessions')
        context['all_players'] = all_players = Player.objects.all().count
        return context


# match related views
@login_required(login_url='login')
def match_dashboard(request):
    tomorrow = datetime.datetime.today()+datetime.timedelta()
    matches = Match.objects.filter(match_date__gte=tomorrow)[:5]
    context = {'matches': matches}
    return render(request, 'match/match_dashboard.html', context)


class MatchCreateView(SuccessMessageMixin, CreateView):
    model = Match
    form_class = MatchForm
    template_name = 'match/create_match.html'
    success_url = reverse_lazy('match_dashboard')
    success_message = "New match fixture was created successfully"


class MatchUpdateView(SuccessMessageMixin, UpdateView):
    model = Match
    form_class = MatchForm
    template_name = 'match/update_match.html'
    success_url = reverse_lazy('match_dashboard')
    success_message = "Match data has been updated successfully"


class MatchDeleteView(SuccessMessageMixin, DeleteView):
    model = Match
    template_name = 'match/delete_match.html'
    success_url = reverse_lazy('match_dashboard')
    success_message = "Match data has been deleted successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(MatchDeleteView, self).delete(request, *args, **kwargs)

class MatchListView(ListView):
    model = Match
    template_name = 'match/match_list.html'
    success_url = reverse_lazy('match_dashboard')


@login_required(login_url='login')
def create_squad(request, pk):
    MatchFormSet = inlineformset_factory(Match, Team_Selection, form=CreateSquad, fields=('player', 'jersey_number', 'game_status'), extra=22, max_num=25)
    match = Match.objects.get(id=pk)
    players = Player.objects.all()
    formset = MatchFormSet(instance=match)
    if request.method == 'POST':
        formset = MatchFormSet(request.POST, instance=match)
        if formset.is_valid():
            formset.save()
            return redirect('match_dashboard')
    context = {'formset': formset,
               'match': match,
               'players': players
               }
    return render(request, 'match/create_squad.html', context)


# Clubname
class ClubCreateView(UpdateView):
    model = Club
    form_class = ClubForm
    template_name = 'main/create_club.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        obj = Club.objects.filter()[0]
        return obj


# Team Sheet
@login_required(login_url='login')
def team_sheet(request, pk):
    match = Match.objects.get(id=pk)
    squad = Team_Selection.objects.all().filter(match=match).order_by('jersey_number')
    match_data = Team_Selection.objects.filter(match=match)[:1]
    context = {'match_data': match_data,
               'squad': squad
               }
    return render(request, 'match/team_sheet.html', context)


# Error Code Pages
def error_403(request, exception):
    return render(request, '403_csrf.html')


def error_404(request, exception):
    return render(request, '404.html')
