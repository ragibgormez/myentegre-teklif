from django.http import Http404
from django.views.generic import TemplateView


class TasarimSeciciView(TemplateView):
    template_name = "core/tasarim-secici.html"


class V1KurumsalView(TemplateView):
    template_name = "core/v1-minimal.html"


class V2ModernView(TemplateView):
    template_name = "core/v2-modern.html"


class V3JourneyView(TemplateView):
    template_name = "core/v3-journey.html"


# Versiyon ve sayfa whitelist — guvenli template loading
ALLOWED_VERSIONS = {"v1", "v2", "v3"}
ALLOWED_KURUMSAL_PAGES = {
    "hikayemiz",
    "yonetim-kadromuz",
    "felsefemiz",
    "insan-kaynaklari",
    "kurumsal-kimlik",
    "franchise",
}


class KurumsalView(TemplateView):
    """Her demo (v1, v2, v3) icin 6 kurumsal alt sayfa."""

    def get_template_names(self):
        version = self.kwargs.get("version")
        page = self.kwargs.get("page")
        if version not in ALLOWED_VERSIONS or page not in ALLOWED_KURUMSAL_PAGES:
            raise Http404("Sayfa bulunamadi")
        return [f"core/{version}/kurumsal/{page}.html"]
