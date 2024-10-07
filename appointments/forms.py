from django import forms
from .models import Appointment, Doctor

class AppointmentForm(forms.ModelForm):
    specialty = forms.ChoiceField(
        choices=[],
        required=True,
        label="Select Specialty"
    )
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.none(), required=True)

    class Meta:
        model = Appointment
        fields = ['specialty', 'doctor', 'date', 'start_time']

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
    
        specialties = Doctor.objects.values_list('specialty', flat=True).distinct()
        self.fields['specialty'].choices = [(s, s) for s in specialties]

        self.fields['doctor'].queryset = Doctor.objects.none()

        if 'specialty' in self.data:
            specialty = self.data.get('specialty')
            if specialty:
                self.fields['doctor'].queryset = Doctor.objects.filter(specialty=specialty).order_by('name')
 
        elif self.instance and self.instance.pk:
            self.fields['doctor'].queryset = Doctor.objects.filter(specialty=self.instance.specialty).order_by('name')
            self.fields['specialty'].widget.attrs['readonly'] = True
            self.fields['doctor'].widget.attrs['readonly'] = True