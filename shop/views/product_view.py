from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import  HttpResponseNotFound, HttpResponseServerError
# from decorators.auth_decorators import admin_required
from shop.services import product_service
from shop.models import Category

# class ProductListView(View):
#     def get(self, request):
#         try:
#             products = product_service.get_all_products()
#             return render(request, 'shop/product_list.html', {'products': products})
#         except Exception as e:
#             print(f"Error displaying product list: {e}")
#             return HttpResponseServerError("Something went wrong.")

# class ProductDetailView(View):
#     def get(self, request, product_id):
#         product = product_service.get_product_by_id(product_id)
#         if product:
#             return render(request, 'shop/product_detail.html', {'product': product})
#         return HttpResponseNotFound("Product not found.")

# class ProductCreateView(View):
#     def get(self, request):
#         categories = Category.objects.all()
#         return render(request, 'product/product_create.html', {'categories': categories})

#     def post(self, request):
#         data = {
#             'category': request.POST.get('category'),
#             'name': request.POST.get('name'),
#             'description': request.POST.get('description'),
#             'price': request.POST.get('price'),
#             'stock': request.POST.get('stock'),
#             'image': request.FILES.get('image'),
#             'sku': request.POST.get('sku'),
#             'tags': request.POST.get('tags')
#         }
#         product = product_service.create_product(data, request.user)
#         if product:
#             messages.success(request, "Product created successfully.")
#             return redirect('shop:product_list')
#         messages.error(request, "Failed to create product.")
#         return redirect('shop:product_create')

# class ProductUpdateView(View):
#     def get(self, request, product_id):
#         product = product_service.get_product_by_id(product_id)
#         categories = Category.objects.all()
#         if product:
#             return render(request, 'shop/product_update.html', {
#                 'product': product,
#                 'categories': categories
#             })
#         return HttpResponseNotFound("Product not found.")

#     def post(self, request, product_id):
#         data = {
#             'category': request.POST.get('category'),
#             'name': request.POST.get('name'),
#             'description': request.POST.get('description'),
#             'price': request.POST.get('price'),
#             'stock': request.POST.get('stock'),
#             'image': request.FILES.get('image'),
#             'sku': request.POST.get('sku'),
#             'tags': request.POST.get('tags'),
#             'is_active': request.POST.get('is_active') == 'on'
#         }
#         product = product_service.update_product(product_id, data)
#         if product:
#             messages.success(request, "Product updated successfully.")
#             return redirect('shop:product_detail', product_id=product.id)
#         messages.error(request, "Failed to update product.")
#         return redirect('shop:product_update', product_id=product_id)

# class ProductDeleteView(View):
#     def post(self, request, product_id):
#         success = product_service.delete_product(product_id)
#         if success:
#             messages.success(request, "Product deleted.")
#         else:
#             messages.error(request, "Failed to delete product.")
#         return redirect('shop:product_list')


class ProductListView(View):
    def get(self, request):
        products = []
        try:
            products = product_service.get_all_products()
            print(f"[ProductListView] Loaded {len(products)} products")
        except Exception as e:
            print(f"[ProductListView] Error: {e}")
            messages.error(request, "Failed to load products.")
        
        return render(request, 'product/product_list.html', {'products': products})


class ProductDetailView(View):
    def get(self, request, product_id):
        product = product_service.get_product_by_id(product_id)
        if product:
            return render(request, 'product/product_detail.html', {'product': product})
        return HttpResponseNotFound("Product not found.")


class ProductCreateView(View):
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'product/product_create.html', {'categories': categories})

    def post(self, request):
        try:
            data = request.POST.copy()
            files = request.FILES
            product = product_service.create_product(data, request.user, files=files)
            if product:
                messages.success(request, "Product created successfully.")
                return redirect('product_list')
        except Exception as e:
            print(f"[ProductCreateView] Error: {e}")
        
        messages.error(request, "Failed to create product.")
        return redirect('product_create')


class ProductUpdateView(View):
    def get(self, request, product_id):
        product = product_service.get_product_by_id(product_id)
        categories = Category.objects.all()
        if product:
            return render(request, 'product/product_update.html', {
                'product': product,
                'categories': categories
            })
        return HttpResponseNotFound("Product not found.")

    def post(self, request, product_id):
        try:
            data = request.POST.copy()
            files = request.FILES
            product = product_service.update_product(product_id, data, files=files)
            if product:
                messages.success(request, "Product updated successfully.")
                return redirect('product_detail', product_id=product.id)
        except Exception as e:
            print(f"[ProductUpdateView] Error: {e}")
        
        messages.error(request, "Failed to update product.")
        return redirect('product_update', product_id=product_id)



class ProductDeleteView(View):
    def post(self, request, product_id):
        try:
            success = product_service.delete_product(product_id)
            if success:
                messages.success(request, "Product deleted.")
            else:
                messages.error(request, "Product not found or could not be deleted.")
        except Exception as e:
            print(f"[ProductDeleteView] Error: {e}")
            messages.error(request, "An unexpected error occurred.")
        return redirect('product_list')

'''
class ProductSearchView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        try:
            results = product_service.search_products(query)
            return render(request, 'product/product_search.html', {
                'query': query,
                'results': results
            })
        except Exception as e:
            print(f"[ProductSearchView] Error: {e}")
            messages.error(request, "Search failed.")
            return render(request, 'product/product_search.html', {'query': query, 'results': []})

path('tech-zenovahub.com/products/search/', views.ProductSearchView.as_view(), name='product_search'),

{% extends 'main.html' %}
{% block title %}Search Results{% endblock %}

{% block content %}
<h3>Search Results for "{{ query }}"</h3>

{% if results %}
    <ul class="list-group">
        {% for product in results %}
            <li class="list-group-item">
                <a href="{% url 'product_detail' product.id %}">{{ product.name }}</a>
            </li>
        {% endfor %}
    </ul>
{% else %}
    <p>No products found matching your search.</p>
{% endif %}
{% endblock %}


'''
