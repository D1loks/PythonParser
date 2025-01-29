from django.urls import path
from .views import TeamListView, TeamDetailView, TeamUpdateView, TeamDeleteView

urlpatterns = [
    path('', TeamListView.as_view(), name='team-list'),
    path('team/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('team/<int:pk>/update/', TeamUpdateView.as_view(), name='team-update'),
    path('team/<int:pk>/delete/', TeamDeleteView.as_view(), name='team-delete'),
]