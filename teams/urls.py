from django.urls import path
from .views import TeamListView, TeamDetailView, TeamUpdateView, TeamDeleteView

urlpatterns = [
    path('', TeamListView().get, name='team-list'),
    path('team/<int:pk>/', TeamDetailView().get, name='team-detail'),
    path('team/<int:pk>/update/', TeamUpdateView().get, name='team-update'),
    path('team/<int:pk>/delete/', TeamDeleteView().get, name='team-delete'),
]
