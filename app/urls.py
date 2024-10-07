from django.contrib import admin
from django.urls import path, include
from website.views import home, user_dashboard, update_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('appointments/', include('appointments.urls')),
    path('auth/', include('django.contrib.auth.urls'))
]
