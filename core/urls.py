from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.TasarimSeciciView.as_view(), name="tasarim-secici"),
    path("v1/", views.V1KurumsalView.as_view(), name="v1-kurumsal"),
    path("v2/", views.V2ModernView.as_view(), name="v2-modern"),
    path("v3/", views.V3JourneyView.as_view(), name="v3-journey"),
    path(
        "<str:version>/kurumsal/<str:page>/",
        views.KurumsalView.as_view(),
        name="kurumsal",
    ),
]
