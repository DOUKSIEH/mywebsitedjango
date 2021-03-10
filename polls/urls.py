from django.urls import path

from . import views

app_name = 'polls'

##Permet d'utilisation des vues génériques 
urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


# urlpatterns = [
#     # ex: /polls/
#     path('', views.IndexView.as_view(), name='index'),
#     # ex: /polls/5/
#     path('<int:pk>/', views.Detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:pk>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),

# ]