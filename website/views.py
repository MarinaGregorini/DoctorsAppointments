from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.utils import timezone
from appointments.models import Appointment, PastAppointment
from django.contrib import messages
from .forms import UserRegistrationForm, CustomUserChangeForm

def home(request):
    if request.user.is_authenticated:
        return redirect('user_dashboard')
    else:
        return render(request, "website/home.html")

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def user_dashboard(request):
    now = timezone.now()
    past_appointments = Appointment.objects.filter(date__lt=now.date())
    for appointment in past_appointments:

        PastAppointment.objects.create(
            date=appointment.date,
            start_time=appointment.start_time,
            doctor_name=str(appointment.doctor),
            user=appointment.user
        )
        appointment.delete()

    current_appointments = Appointment.objects.all()

    return render(request, "website/user_dashboard.html", {"appointments": current_appointments})

@login_required
def update_user(request):
    user = request.user
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_dashboard')

    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, 'registration/update_user.html', {'form': form})