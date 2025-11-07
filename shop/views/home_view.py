from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib import messages
from shop.services.home_service import get_homepage_context


# Home View For Shop
class HomeView(TemplateView):
    template_name = "home_page.html"  

    def get(self, request, *args, **kwargs):
        context = get_homepage_context(request.user)
        if request.session.get("show_welcome", False):
            messages.success(request, f"Welcome back, {request.user.first_name} 👋")
            request.session["show_welcome"] = False
        return render(request, self.template_name, context)
