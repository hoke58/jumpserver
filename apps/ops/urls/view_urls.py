# ~*~ coding: utf-8 ~*~
from __future__ import unicode_literals
from django.urls import path
from django.views.generic import TemplateView


from .. import views

__all__ = ["urlpatterns"]

app_name = "ops"

urlpatterns = [
    # Resource Task url
    path('task/', views.TaskListView.as_view(), name='task-list'),
    path('task/<uuid:pk>/', views.TaskDetailView.as_view(), name='task-detail'),
    path('task/<uuid:pk>/adhoc/', views.TaskAdhocView.as_view(), name='task-adhoc'),
    path('task/<uuid:pk>/history/', views.TaskHistoryView.as_view(), name='task-history'),
    path('adhoc/<uuid:pk>/', views.AdHocDetailView.as_view(), name='adhoc-detail'),
    path('adhoc/<uuid:pk>/history/', views.AdHocHistoryView.as_view(), name='adhoc-history'),
    path('adhoc/history/<uuid:pk>/', views.AdHocHistoryDetailView.as_view(), name='adhoc-history-detail'),
    path('celery/task/<uuid:pk>/log/', views.CeleryTaskLogView.as_view(), name='celery-task-log'),
    # 进程管理
    path('process/', views.ProcessContrlView.as_view(), name='process'),

    path('command-execution/', views.CommandExecutionListView.as_view(), name='command-execution-list'),
    path('command-execution/start/', views.CommandExecutionStartView.as_view(), name='command-execution-start'),
]
