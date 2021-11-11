from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),

    # ex: /players/id/5/
    path('id/<int:player_id>/', views.detail, name='detail'),

    # ex: /polls/5/
    path('<int:player_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:player_id>/results/', views.results, name='results'),
    
    # ex: /polls/5/vote/
    path('<int:player_id>/vote/', views.vote, name='vote'),
]
