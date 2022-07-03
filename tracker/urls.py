from django.urls import path
from django.http import HttpResponse
from django.views.generic import CreateView, ListView, UpdateView, DetailView
from . import views


urlpatterns = [
    path('',views.home),
    path('main/register',views.register_page, name ='register'),
    path('main/login',views.login_page, name ='login'),
    path('main/dashboard/',views.home, name='dashboard'),
    path('main/stats',views.stats, name='stats'),
    path('training/training_dashboard',views.training_dashboard, name='training_dashboard'),
    path('training/create_session',views.TrainingCreateView.as_view(), name='create_session'),
    path('training/update_session/<int:pk>',views.TrainingUpdateView.as_view(), name='update_session'),
    path('training/delete_session/<int:pk>',views.TrainingDeleteView.as_view(), name='delete_session'),
    path('training/training_list', views.TrainingListView.as_view(), name='training_list'),
    path('player/player_dashboard',views.player_dashboard, name='player_dashboard'),
    path('player/create_player',views.PlayerCreateView.as_view(), name='create_player'),
    path('player/update_player/<int:pk>',views.PlayerUpdateView.as_view(), name='update_player'),
    path('player/training_list/<int:pk>',views.training_list, name='training_list'),
    path('player/delete_player/<int:pk>',views.PlayerDeleteView.as_view(), name='delete_player'),
    path('player/squad_attendance',views.squad_attendance, name='squad_attendance'),
    path('player/squad_stats', views.SquadStats.as_view(), name='squad_stats'),
    path('player/game_list/<int:pk>',views.game_list, name='game_list'),
    path('match/match_dashboard', views.match_dashboard, name='match_dashboard'),
    path('match/create_squad/<int:pk>',views.create_squad, name='create_squad'),
    path('match/add_player_to_match/<int:pk>',views.add_player_to_match, name='add_player_to_match'),
    path('training/create_match',views.MatchCreateView.as_view(), name='create_match'),
    path('match/update_match/<int:pk>',views.MatchUpdateView.as_view(), name='update_match'),
    path('match/delete_match/<int:pk>',views.MatchDeleteView.as_view(), name='delete_match'),
    path('match/match_list', views.MatchListView.as_view(), name='match_list'),
    path('main/create_club',views.ClubCreateView.as_view(), name='create_club'),
    path('match/team_sheet/<int:pk>',views.team_sheet, name='team_sheet'),     
    ]
