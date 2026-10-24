from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Главная страница. Только каркас: данные появятся на этапе Э6."""

    template_name = "core/home.html"
