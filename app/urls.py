from django.conf.urls.static import static
from django.urls import path

from PetPost import settings
from app import views

urlpatterns = [
    path("", views.main_page, name="main"),
    path("order/", views.order, name="order"),
    path("international-transportation/", views.international_transportation, name="international_transportation"),
    path("services/", views.legal_services, name="legal_services"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
