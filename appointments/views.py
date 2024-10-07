from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime, timedelta, time
from .models import Doctor, Appointment, PastAppointment
from .forms import AppointmentForm

@login_required
def detail(request, id):
    appointment = Appointment.objects.get(pk=id)
    return render(request, "appointments/detail.html", {"appointment": appointment})

@login_required
def past_appointments(request):
    appointments = PastAppointment.objects.all()
    return render(request, "appointments/past_appointments.html", {"appointments": appointments})

@login_required
def get_doctors(request):
    specialty= request.GET.get('specialty')
    if specialty:
        doctors = Doctor.objects.filter(specialty=specialty).values('id', 'name')
        return JsonResponse(list(doctors), safe=False)
    return JsonResponse([], safe=False)

@login_required
def get_available_times(request):
    date_str = request.GET.get('date')
    if date_str:
        date = datetime.strptime(date_str, '%Y-%m-%d').date()

        appointments = Appointment.objects.filter(date=date)
        start_time = datetime.combine(date, time(8, 0))
        end_time = datetime.combine(date, time(17, 0))
        time_slots = []

        while start_time < end_time:
            if not appointments.filter(start_time=start_time.time()).exists():
                time_slots.append(start_time.time())
            start_time += timedelta(minutes=30)

        return JsonResponse(time_slots, safe=False)

@login_required
def new(request):
    tomorrow = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)  
            appointment.user = request.user
            appointment.save()
            return redirect("success")

    else: 
        form = AppointmentForm()
    return render(request, "appointments/new.html", {"form": form, 'tomorrow': tomorrow})

@login_required
def success(request):
    return render(request, "appointments/success.html")

@login_required
def edit(request, id):
    tomorrow = (datetime.now().date() + timedelta(days=1)).strftime('%Y-%m-%d')
    appointment = Appointment.objects.get(pk=id)
    if request.method == "POST":
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect("detail", id)
        else:
            print(form.errors)
    else:
        form = AppointmentForm(instance=appointment)
    return render(request, "appointments/edit.html", {"form": form, "appointment": appointment, "tomorrow":tomorrow})

@login_required
def cancel(request, id):
    appointment = Appointment.objects.get(pk=id)
    if request.method == "POST":
        appointment.delete()
        return redirect("home")
    else:
        return render(request, "appointments/cancel.html", {"appointment": appointment})