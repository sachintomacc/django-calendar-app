from django.contrib import admin
from django.urls import path

from core.views import home,CalendarView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
     path('calendar/', CalendarView.as_view(), name='calendar'), # here
]
