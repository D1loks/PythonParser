from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Team
from django.urls import reverse_lazy


class TeamListView(ListView):
    model = Team
    template_name = 'team_list.html'
    context_object_name = 'teams'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Team.objects.filter(name__icontains=query)
        return Team.objects.all()


class TeamDetailView(DetailView):
    model = Team
    template_name = 'teams/team_detail.html'


class TeamUpdateView(UpdateView):
    model = Team
    template_name = 'teams/team_form.html'
    fields = ['name', 'year', 'wins', 'losses', 'win_percent']
    success_url = reverse_lazy('team-list')


class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'teams/team_confirm_delete.html'
    success_url = reverse_lazy('team-list')