from django.contrib import admin
from django.urls import include,path
from django.views.generic import RedirectView

urlpatterns = [
    path('port/', include('port.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/port/')),
]
