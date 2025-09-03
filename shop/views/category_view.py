from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseNotFound, HttpResponseServerError
from shop.services import category_service
from decorators.auth_decorators import login_admin_required



# Category List View
class CategoryListView(View):
    def get(self, request):
        try:
            categories = category_service.get_all_categories()
            return render(request, 'category/category_list.html', {'categories': categories})
        except Exception as e:
            print(f"Error displaying categories: {e}")
            return HttpResponseServerError("Something went wrong.")


# Category Detail View
class CategoryDetailView(View):
    def get(self, request, category_id):
        category = category_service.get_category_by_id(category_id)
        if category:
            return render(request, 'category/category_detail.html', {'category': category})
        return HttpResponseNotFound("Category not found.")


# Category Create View
class CategoryCreateView(View):
    @login_admin_required
    def get(self, request):
        return render(request, 'category/category_create.html')

    @login_admin_required
    def post(self, request):
        data = {
            'name': request.POST.get('name'),
            'description': request.POST.get('description'),
            'slug': request.POST.get('slug'),
            'image': request.FILES.get('image')
        }
        category = category_service.create_category(data)
        if category:
            messages.success(request, "Category created successfully.")
            return redirect('category_list')
        messages.error(request, "Failed to create category.")
        return render(request, 'category/category_create.html', {'data': data})


# Category Update View
class CategoryUpdateView(View):
    @login_admin_required
    def get(self, request, category_id):
        category = category_service.get_category_by_id(category_id)
        if category:
            return render(request, 'category/category_update.html', {'category': category})
        return HttpResponseNotFound("Category not found.")

    @login_admin_required
    def post(self, request, category_id):
        data = {
            'name': request.POST.get('name'),
            'description': request.POST.get('description'),
            'slug': request.POST.get('slug'),
            'image': request.FILES.get('image')
        }
        category = category_service.update_category(category_id, data)
        if category:
            messages.success(request, "Category updated successfully.")
            return redirect('category_list')
        messages.error(request, "Failed to update category.")
        return render(request, 'category/category_update.html', {'category': data, 'error': True})


# Category Delete View
class CategoryDeleteView(View):
    @login_admin_required
    def get(self, request, category_id):
        category = category_service.get_category_by_id(category_id)
        if category:
            return render(request, 'category/category_delete.html', {'category': category})
        return HttpResponseNotFound("Category not found.")

    @login_admin_required
    def post(self, request, category_id):
        try:
            success = category_service.delete_category(category_id)
            if success:
                messages.success(request, "Category deleted.")
            else:
                messages.error(request, "Failed to delete category.")
        except Exception as e:
            messages.error(request, "Unexpected error occurred while deleting category.")
            print(e)
        return redirect('category_list')

