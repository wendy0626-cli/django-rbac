from django.urls import path, re_path
from . import views

urlpatterns = [
    path('users/', views.users),
    path('users/new/', views.users_new),
    re_path(r'^users/edit/(?P<id>\d+)/$', views.users_edit),
    re_path(r'^users/delete/(?P<id>\d+)$/', views.users_delete),

    path('roles/', views.roles),
    path('roles/new/', views.roles_new),
    re_path(r'^roles/edit/(?P<id>\d+)/$', views.roles_edit),
    re_path(r'^roles/delete/(?P<id>\d+)$/', views.roles_delete),

    path('permissions/', views.permissions),
    path('permissions/new/', views.permissions_new),
    re_path(r'^permissions/edit/(?P<id>\d+)/$', views.permissions_edit),
    re_path(r'^permissions/delete/(?P<id>\d+)/$', views.permissions_delete),

    path('menus/', views.menus),
    path('menus/new/', views.menus_new),
    re_path(r'^menus/edit/(?P<id>\d+)/$', views.menus_edit),
    re_path(r'^menus/delete/(?P<id>\d+)/$', views.menus_delete),

    path('', views.index)
]
