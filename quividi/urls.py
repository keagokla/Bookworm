from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('bookworm/', include("bookworm.urls")),
    path('accounts/', include("accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', RedirectView.as_view(pattern_name='books', permanent=True)),
    path('admin/', admin.site.urls),
]