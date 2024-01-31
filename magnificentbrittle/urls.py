from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="homePage"),
    path('about/', views.about_page, name="aboutPage"),
    path('services/', views.services_page, name="servicesPage"),
    path('emergency/', views.emergency_page, name="emergencyPage"),
    path('login/', views.loginPage, name="loginPage"),
    path('signup/', views.signup_page, name="signupPage"),
    path('dashboard/', views.dashboard_page, name="dashboardPage"),
    path('profile/<int:pk>/', views.profile_page, name="profilePage"),
    path('professionalprofile/<int:pk>/', views.professional_page, name="professionalPage"),
    path('assistantprofile/<int:pk>/', views.assistant_page, name="assistantPage"),
    path('records/<int:patient_id>/', views.records_page, name="recordsPage"),
    path('schedule/', views.schedule_page, name="schedulePage"),
    path('create_patient/', views.createPatientPage, name="createPatientPage"),
    path('update_patient/<int:pk>/', views.updatePatient, name="updatePatient"),
    path('delete_patient/<int:pk>/', views.deletePatient, name="deletePatient"),
    path('create_records/<int:patient_id>/', views.createRecords, name='createRecords'),
    path('update_records/<int:records_id>/', views.updateRecord, name="updateRecord"),
    path('create_professional/', views.createProfessionalPage, name="createProfessionalPage"),
    path('create_assistant/', views.createAssistantPage, name="createAssistantPage"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
