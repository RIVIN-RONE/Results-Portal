from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from result import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('result.urls')),
    path('success/<str:rollnumber>/', views.success, name='success'),
]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
