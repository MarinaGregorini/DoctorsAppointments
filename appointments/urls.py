from django.urls import path
from appointments import views

urlpatterns = [
    path('detail/<int:id>', views.detail, name="detail"),
    path('past_appointments', views.past_appointments, name="past_appointments"),
    path('new', views.new, name="new"),
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('get_available_times/', views.get_available_times, name='get_available_times'),
    path('success/', views.success, name='success'),
    path('edit/<int:id>', views.edit, name="edit"),
    path('cancel/<int:id>', views.cancel, name="cancel")
]