from django.conf.urls import url
from EmployeeApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^department$', views.departmentAPI),
    url(r'^department/([0-9]+)$', views.departmentAPI),
    url(r'^employee$', views.employeeAPI),
    url(r'^employee/([0-9]+)$', views.employeeAPI),

    url(r'^Employee/SaveImageFile$', views.SaveImageFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
