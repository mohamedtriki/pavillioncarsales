from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings
from cars import views
from .views import get_json_car_data, get_json_model_data
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



urlpatterns = [
    path('',views.vehicles),
    path('<slug>', views.vehicle_detail),
    path('cars-json/', get_json_car_data, name='cars-json'),
    path('models-json/<str:car>/', get_json_model_data, name='models-json'),
]
urlpatterns+= staticfiles_urlpatterns()          
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)