# Generated by Django 4.2.6 on 2024-01-30 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assistant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('education', models.TextField(blank=True)),
                ('languages_spoken', models.CharField(blank=True, max_length=50)),
                ('experience', models.PositiveIntegerField(blank=True, help_text='Years of experience', null=True)),
                ('additional_info', models.TextField(blank=True)),
                ('position', models.CharField(blank=True, max_length=50)),
                ('department', models.CharField(blank=True, max_length=50)),
                ('date_of_joining', models.DateField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(max_length=255)),
                ('professional', models.CharField(blank=True, max_length=50)),
                ('appointment', models.DateTimeField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other'), ('P', 'Prefer Not To Say')], max_length=1)),
                ('medical_history', models.TextField(blank=True)),
                ('insurance_provider', models.CharField(blank=True, max_length=50)),
                ('insurance_policy_number', models.CharField(blank=True, max_length=20)),
                ('emergency_contact_name', models.CharField(blank=True, max_length=50)),
                ('emergency_contact_phone', models.CharField(blank=True, max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Professionals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('education', models.TextField(blank=True)),
                ('languages_spoken', models.CharField(blank=True, max_length=50)),
                ('experience', models.PositiveIntegerField(blank=True, help_text='Years of experience', null=True)),
                ('additional_info', models.TextField(blank=True)),
                ('profession', models.CharField(blank=True, max_length=50)),
                ('specialty', models.CharField(blank=True, max_length=50)),
                ('license_number', models.CharField(blank=True, max_length=20)),
                ('psychotherapy_approach', models.CharField(blank=True, max_length=50)),
                ('therapeutic_modalities', models.TextField(blank=True)),
                ('populations_served', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Records',
            fields=[
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='records', serialize=False, to='magnificentbrittle.patients')),
                ('diagnosis', models.CharField(blank=True, max_length=100)),
                ('treatment_plan', models.TextField(blank=True)),
                ('therapist_info', models.CharField(blank=True, max_length=255)),
                ('medication_history', models.TextField(blank=True)),
                ('symptoms_and_triggers', models.TextField(blank=True)),
                ('support_system', models.TextField(blank=True)),
                ('goals_and_aspirations', models.TextField(blank=True)),
                ('coping_mechanisms', models.TextField(blank=True)),
                ('quality_of_life_indicators', models.TextField(blank=True)),
                ('feedback_and_preferences', models.TextField(blank=True)),
                ('additional_attribute1', models.CharField(blank=True, max_length=50)),
                ('additional_attribute2', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_datetime', models.DateTimeField()),
                ('professional', models.CharField(blank=True, max_length=50)),
                ('purpose', models.CharField(blank=True, max_length=50)),
                ('notes', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='magnificentbrittle.patients')),
            ],
        ),
    ]
