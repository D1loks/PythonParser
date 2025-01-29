from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from .models import Team
from django.urls import reverse_lazy
import mysql.connector
from dotenv import load_dotenv
import os


class DatabaseConnection:
    def __init__(self):
        load_dotenv()
        self.connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        self.cursor = self.connection.cursor(dictionary=True)


class TeamListView:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get(self, request):
        query = request.GET.get('q', '')
        
        if query:
            sql = """
                SELECT * FROM teams 
                WHERE name LIKE %s
            """
            self.db.cursor.execute(sql, (f'%{query}%',))
        else:
            self.db.cursor.execute("SELECT * FROM teams")
        
        teams = self.db.cursor.fetchall()
        return render(request, 'team_list.html', {'teams': teams})


class TeamDetailView:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get(self, request, pk):
        sql = "SELECT * FROM teams WHERE id = %s"
        self.db.cursor.execute(sql, (pk,))
        team = self.db.cursor.fetchone()
        return render(request, 'team_detail.html', {'team': team})


class TeamUpdateView:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get(self, request, pk):
        sql = "SELECT * FROM teams WHERE id = %s"
        self.db.cursor.execute(sql, (pk,))
        team = self.db.cursor.fetchone()
        return render(request, 'team_form.html', {'team': team})
    
    def post(self, request, pk):
        name = request.POST.get('name')
        year = request.POST.get('year')
        wins = request.POST.get('wins')
        losses = request.POST.get('losses')
        win_percent = request.POST.get('win_percent')
        
        sql = """
            UPDATE teams 
            SET name = %s, year = %s, wins = %s, losses = %s, win_percent = %s
            WHERE id = %s
        """
        self.db.cursor.execute(sql, (name, year, wins, losses, win_percent, pk))
        self.db.connection.commit()
        
        return redirect('team-list')


class TeamDeleteView:
    def __init__(self):
        self.db = DatabaseConnection()
    
    def get(self, request, pk):
        sql = "SELECT * FROM teams WHERE id = %s"
        self.db.cursor.execute(sql, (pk,))
        team = self.db.cursor.fetchone()
        return render(request, 'team_confirm_delete.html', {'team': team})
    
    def post(self, request, pk):
        sql = "DELETE FROM teams WHERE id = %s"
        self.db.cursor.execute(sql, (pk,))
        self.db.connection.commit()
        return redirect('team-list')