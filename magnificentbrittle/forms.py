from django.forms import ModelForm, DateTimeInput
from .models import Patients, Person, Professionals, Assistant, Records

class PatientForm(ModelForm):
    class Meta:
        model = Patients
        fields = '__all__'
        widgets = {
            'appointment': DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def clean_appointment(self):
        appointment = self.cleaned_data.get('appointment')
        return appointment

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

class ProfessionalForm(PersonForm):
    class Meta:
        model = Professionals
        fields = '__all__'

class AssistantForm(PersonForm):
    class Meta:
        model = Assistant
        fields = '__all__'

class RecordForm(ModelForm):
    class Meta:
        model = Records
        fields = '__all__'