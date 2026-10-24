from django.views.generic import TemplateView


class OrderListView(TemplateView):
    """Каркас списка заказов. Без данных: настоящий список — на этапе Э6."""

    template_name = "orders/order_list.html"
