from django.urls import path, include
from . import views


urlpatterns = [
       path('',views.home,name='home'),
       path('delete/<int:taskid>/', views.delete, name='delete'),
       path('update/<int:id>/',views.update,name='update'),
       path('homelistview/',views.Tasklistview.as_view(),name='homelistview'),
       path('detailview/<int:pk>/',views.TaskDetailview.as_view(),name='detailview'),
       path('updateview/<int:pk>/',views.TaskUpdateview.as_view(),name='updateview'),
       path('deleteview/<int:pk>/',views.Taskdeleteview.as_view(),name='deleteview'),


]