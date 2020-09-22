
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mult/', include("mult.urls")),
    path('newyear/', include("newyear.urls")),
    path('tasks/', include("tasks.urls")),
    path('flights/', include("flights.urls")),
]
