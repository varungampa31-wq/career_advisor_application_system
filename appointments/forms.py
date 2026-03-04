from django import forms
from .models import Appointment, AvailabilitySlot
from django.contrib.auth.models import User


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['slot']  # only slot now

    def __init__(self, *args, **kwargs):
        student = kwargs.pop('student', None)
        super().__init__(*args, **kwargs)

        if student:
            # show only free slots of student's course advisor
            self.fields['slot'].queryset = AvailabilitySlot.objects.filter(
                advisor__profile__course=student.profile.course
            ).exclude(
                appointment__isnull=False
            )