from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('studet/<int:pk>', views.student_detail),
    path('studet/', views.student_list)
]
