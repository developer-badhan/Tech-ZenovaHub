from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import  HttpResponseNotFound
from shop.services import product_service,review_service
from shop.models import Category
from decorators.auth_decorators import login_admin_required,signin_required,customer_required
from user.utils.auth_status import get_user_login_status



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
        if not product:
            return HttpResponseNotFound("Product not found.")
        reviews = review_service.get_product_reviews(product_id)
        is_logged_in, active_user, user_role = get_user_login_status(request)
        user_review = None
        if is_logged_in and active_user:
            user_review = reviews.filter(user=active_user).first()
        context = {
            "product": product,
            "reviews": reviews,
            "user_review": user_review,
            "is_logged_in": is_logged_in,
            "active_user": active_user,
            "user_role": user_role,
        }
        return render(request, "product/product_detail.html", context)



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
                return redirect('product_list_admin')
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
                return redirect('product_list_admin')
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
        return redirect('product_list_admin')


# Product List Admin View
class ProductLListAdminView(View):
    @login_admin_required
    def get(self, request):
        try:
            products = product_service.get_all_products(active_only=False)
            return render(request, 'product/product_listadmin.html', {'products': products})
        except Exception as e:
            print(f"[ProductLListAdminView] Error: {e}")
            messages.error(request, "Failed to load admin product list.")
            return redirect('admin_dashboard')


# Product Search View
class ProductSearchView(View):
    @signin_required
    @customer_required
    def get(self, request):
        query = request.GET.get('q', '').strip()
        filter_type = request.GET.get('filter', 'manual') 
        try:
            results = product_service.search_products(query)
            if filter_type == "cheap":
                results = results.order_by("price")  
            elif filter_type == "expensive":
                results = results.order_by("-price")
            return render(request, 'product/product_search.html', {
                'query': query,
                'results': results,
                'filter_type': filter_type
            })
        except Exception as e:
            print(f"[ProductSearchView] Error: {e}")
            messages.error(request, "Search failed. Please try again.")
            return render(request, 'product/product_search.html', {
                'query': query,
                'results': [],
                'filter_type': 'manual'
            })


