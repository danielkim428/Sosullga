from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("series/<int:series_id>", views.series, name='series'),
    path("login", views.login_view, name='login'),
    path("logout", views.logout_view, name='logout'),
    path("pageSetting", views.pageSetting, name='pageSetting'),
    path("setting", views.setting, name='setting'),
    path("account", views.account, name='account'),
    path("request", views.request, name='request'),
    path("register", views.register, name='register'),
    path("read/<int:read_id>/<int:read_page>", views.read, name='read'),
    path("read/<int:read_id>/next", views.next, name="next"),
    path("read/<int:read_id>/bookmark", views.bookmark, name="bookmark"),
]
