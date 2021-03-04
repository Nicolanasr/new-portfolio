from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.index, name='index'),
    path('project/<int:project_id>', views.project, name='project'),
    path('my-resume', views.resume, name='resume'),
    # path('success/', views.successView, name='success'),
]
