from django.shortcuts import render
from django.views.generic import TemplateView


class TasarimSeciciView(TemplateView):
    template_name = "core/tasarim-secici.html"


class V1KurumsalView(TemplateView):
    template_name = "core/v1-kurumsal.html"


class V2ModernView(TemplateView):
    template_name = "core/v2-modern.html"


class V3JourneyView(TemplateView):
    template_name = "core/v3-journey.html"
