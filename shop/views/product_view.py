from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import  HttpResponseNotFound
from shop.services import product_service
from shop.models import Category
from decorators.auth_decorators import login_admin_required,signin_required,customer_required



# Product List View
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


# Product Detail View
class ProductDetailView(View):
    def get(self, request, product_id):
        product = product_service.get_product_by_id(product_id)
        if product:
            return render(request, 'product/product_detail.html', {'product': product})
        return HttpResponseNotFound("Product not found.")


# Product Create View
class ProductCreateView(View):
    @login_admin_required
    def get(self, request):
        categories = Category.objects.all()
        return render(request, 'product/product_create.html', {'categories': categories})

    @login_admin_required
    def post(self, request):
        try:
            data = request.POST.copy()
            files = request.FILES
            print("DEBUG session:", request.session.items())
            print("DEBUG request.user:", request.user)
            product = product_service.create_product(data, request, files=files)
            if product:
                messages.success(request, "Product created successfully.")
                return redirect('product_list')
        except Exception as e:
            print(f"[ProductCreateView] Error: {e}")
        
        messages.error(request, "Failed to create product.")
        return redirect('product_create')


# Product Update View
class ProductUpdateView(View):
    @login_admin_required
    def get(self, request, product_id):
        product = product_service.get_product_by_id(product_id)
        categories = Category.objects.all()
        if product:
            return render(request, 'product/product_update.html', {
                'product': product,
                'categories': categories
            })
        return HttpResponseNotFound("Product not found.")

    @login_admin_required
    def post(self, request, product_id):
        try:
            data = request.POST.copy()
            files = request.FILES
            product = product_service.update_product(product_id, data, request, files=files)
            if product:
                messages.success(request, "Product updated successfully.")
                return redirect('product_detail', product_id=product.id)
        except Exception as e:
            print(f"[ProductUpdateView] Error: {e}")
        
        messages.error(request, "Failed to update product.")
        return redirect('product_update', product_id=product_id)


# Product Delete View
class ProductDeleteView(View):
    @login_admin_required
    def get(self, request, product_id):
        product = product_service.get_product_by_id(product_id)
        if not product:
            return HttpResponseNotFound("Product not found.")
        return render(request, 'product/product_delete.html', {'product': product})

    @login_admin_required
    def post(self, request, product_id):
        try:
            success = product_service.delete_product(product_id)
            if success:
                messages.success(request, "Product deleted.")
            else:
                messages.error(request, "Product not found or could not be deleted.")
        except Exception as e:
            print(f"[ProductDeleteView] Error (POST): {e}")
            messages.error(request, "An unexpected error occurred.")
        return redirect('product_list')


# Product Search View
class ProductSearchView(View):
    @signin_required
    @customer_required
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



