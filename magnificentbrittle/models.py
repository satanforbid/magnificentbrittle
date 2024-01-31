from django.db import models

class Patients(models.Model):
    id = models.BigAutoField(primary_key=True)
    # Full name of the patient
    name = models.CharField(max_length=50)
    # Email address of the patient
    email = models.EmailField(max_length=50, blank=True)
    # Phone number of the patient
    phone = models.CharField(max_length=50, blank=True)
    # Physical address of the patient
    address = models.CharField(max_length=255)
    # Associated healthcare or mental health professional
    professional = models.CharField(max_length=50, blank=True)
    # Date and time of the patient's appointment
    appointment = models.DateTimeField()
    # Birthdate of the patient
    date_of_birth = models.DateField(blank=True, null=True)

    # Gender identity of the patient
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer Not To Say')
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)

    # Detailed medical history of the patient
    medical_history = models.TextField(blank=True)
    # Health insurance provider for the patient
    insurance_provider = models.CharField(max_length=50, blank=True)
    # Insurance policy number of the patient
    insurance_policy_number = models.CharField(max_length=20, blank=True)
    # Full name of the patient's emergency contact
    emergency_contact_name = models.CharField(max_length=50, blank=True)
    # Phone number of the patient's emergency contact
    emergency_contact_phone = models.CharField(max_length=15, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not hasattr(self, 'records'):
            Records.objects.create(patient=self)

    def delete(self, *args, **kwargs):
        records_instance = Records.objects.filter(patient=self).first()
        if records_instance:
            records_instance.delete()

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name

# Quick Recap:
# The Patients model captures personal and medical information for individuals,
# including details like name, contact information, gender, medical history,
# and emergency contact information.

class Records(models.Model):
    # Foreign key linking to the Patients model
    patient = models.OneToOneField(Patients, on_delete=models.CASCADE, primary_key=True, related_name='records')
    # Specific mental health diagnosis or diagnoses
    diagnosis = models.CharField(max_length=100, blank=True)
    # Details about the patient's current treatment plan
    treatment_plan = models.TextField(blank=True)
    # Information about the patient's current therapist or counselor
    therapist_info = models.CharField(max_length=255, blank=True)
    # Details about the patient's history of psychiatric medications
    medication_history = models.TextField(blank=True)
    # Information about the patient's specific symptoms and potential triggers
    symptoms_and_triggers = models.TextField(blank=True)
    # Information about the patient's support system
    support_system = models.TextField(blank=True)
    # Patient's personal goals and aspirations for their mental health
    goals_and_aspirations = models.TextField(blank=True)
    # Strategies or activities the patient uses to cope with stress or manage their mental health
    coping_mechanisms = models.TextField(blank=True)
    # Information about the patient's overall quality of life
    quality_of_life_indicators = models.TextField(blank=True)
    # Patient's feedback on treatment approaches and personal preferences
    feedback_and_preferences = models.TextField(blank=True)

    # Additional attributes if needed
    additional_attribute1 = models.CharField(max_length=50, blank=True)
    additional_attribute2 = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"Record for {self.patient.name}"

# Quick Recap:
# The Records model establishes a relationship with the Patients model using a foreign key.
# It captures mental health-specific attributes for individual patients, including diagnosis,
# treatment plan, therapist information, and various other aspects.

class Consultation(models.Model):
    # Reference to the patient for whom the consultation is scheduled
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    # Date and time of consultation
    appointment_datetime = models.DateTimeField()
    # Associated healthcare or mental health professional for the consultations
    professional = models.CharField(max_length=50, blank=True)
    # Purpose or type of the consultation (e.g., consultation, follow-up)
    purpose = models.CharField(max_length=50, blank=True)
    # Additional notes or details about the consultation
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Consultation for {self.patient.name} with {self.professional.name}"

# Quick Recap:
# The Consultation model represents scheduled appointments in the system.
# It includes a reference to the patient, date and time of the appointment,
# the associated healthcare or mental health professional, purpose or type of
# consultation, appointment, and additional notes or details.


class Person(models.Model):
    # Common attributes for Professionals and Assistants

    # Full name of the person
    name = models.CharField(max_length=50)
    # Email address of the person
    email = models.EmailField(max_length=50, blank=True)
    # Phone number of the person
    phone = models.CharField(max_length=15, blank=True)
    # Physical address of the person
    address = models.CharField(max_length=255)
    # Educational background of the person
    education = models.TextField(blank=True)
    # Languages spoken by the person
    languages_spoken = models.CharField(max_length=50, blank=True)
    # Number of years of professional experience
    experience = models.PositiveIntegerField(blank=True, null=True, help_text="Years of experience")
    # Additional information about the person
    additional_info = models.TextField(blank=True)

    class Meta:
        abstract = True

# Quick Recap:
# The abstract Person model contains common attributes shared by Professionals and Assistants.

class Professionals(Person):
    # Detailed information about mental health professionals

    # General professional title or category
    profession = models.CharField(max_length=50, blank=True)
    # Specific area of expertise or specialization
    specialty = models.CharField(max_length=50, blank=True)
    # License number associated with the professional
    license_number = models.CharField(max_length=20, blank=True)
    # Approach or methodology used in psychotherapy
    psychotherapy_approach = models.CharField(max_length=50, blank=True)
    # Different therapeutic techniques or modalities used by the professional
    therapeutic_modalities = models.TextField(blank=True)
    # Specific populations the professional specializes in or has experience with
    populations_served = models.TextField(blank=True)

    def __str__(self):
        return self.name

# Quick Recap:
# The Professionals model extends the Person model, adding attributes specific to mental health professionals.

class Assistant(Person):
    # Attributes specific to Assistants

    # Position or job title of the Assistant
    position = models.CharField(max_length=50, blank=True)
    # Department where the Assistant works
    department = models.CharField(max_length=50, blank=True)
    # Date when the Assistant joined
    date_of_joining = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

# Quick Recap:
# The Assistant model extends the Person model, adding attributes specific to Assistants.

