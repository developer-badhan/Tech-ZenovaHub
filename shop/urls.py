from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [

    # Home Route
    path('', views.HomeView.as_view(), name='home'),

    # Product Routes
    path('tech-zenovahub.com/products/', views.ProductListView.as_view(), name='product_list'),
    path('tech-zenovahub.com/products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('tech-zenovahub.com/products/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('tech-zenovahub.com/products/<int:product_id>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
    path('tech-zenovahub.com/products/<int:product_id>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),
    path('teach-zenovahub.com/products/list',views.ProductLListAdminView.as_view(),name= 'product_list_admin'),

    # Product Category Routes
    path('tech-zenovahub.com/categories/', views.CategoryListView.as_view(), name='category_list'),
    path('tech-zenovahub.com/categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('tech-zenovahub.com/categories/<int:category_id>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('tech-zenovahub.com/categories/<int:category_id>/edit/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('tech-zenovahub.com/categories/<int:category_id>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Product Order Routes
    path('tech-zenovahub.com/orders/', views.OrderListView.as_view(), name='order_list'),
    path('tech-zenovahub.com/orders/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('tech-zenovahub.com/orders/<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('tech-zenovahub.com/orders/<int:order_id>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),

    # Product Order Item Routes
    path('tech-zenovahub.com/orders/<int:order_id>/items/', views.OrderItemListView.as_view(), name='order_item_list'),
    path('tech-zenovahub.com/orders/<int:order_id>/items/create/', views.OrderItemCreateView.as_view(), name='order_item_create'),
    path('tech-zenovahub.com/orders/items/<int:item_id>/edit/', views.OrderItemUpdateView.as_view(), name='order_item_update'),
    path('tech-zenovahub.com/orders/items/<int:item_id>/delete/', views.OrderItemDeleteView.as_view(), name='order_item_delete'),

    # Cart Routes
    path('tech-zenovahub.com/cart/', views.CartDetailView.as_view(), name='cart_detail'),
    path('tech-zenovahub.com/cart/add/', views.CartAddItemView.as_view(), name='cart_add'),
    path('tech-zenovahub.com/cart/update/', views.CartUpdateItemView.as_view(), name='cart_update'),
    path('tech-zenovahub.com/cart/remove/', views.CartRemoveItemView.as_view(), name='cart_remove'),
    path('tech-zenovahub.com/cart/clear/', views.CartClearView.as_view(), name='cart_clear'),

    # Product Review Routes
    path('tech-zenovahub.com/products/<int:product_id>/reviews/', views.ProductReviewListView.as_view(), name='review_list'),
    path('tech-zenovahub.com/products/<int:product_id>/reviews/create/', views.ProductReviewCreateView.as_view(), name='review_create'),
    path('tech-zenovahub.com/products/<int:product_id>/reviews/update/', views.ProductReviewUpdateView.as_view(), name='review_update'),
    path('tech-zenovahub.com/products/<int:product_id>/reviews/delete/', views.ProductReviewDeleteView.as_view(), name='review_delete'),

    # Cart Wishlist Routes
    path('tech-zenovahub.com/wishlist/', views.WishlistListView.as_view(), name='wishlist'),
    path('tech-zenovahub.com/wishlist/add/<int:product_id>/', views.WishlistAddView.as_view(), name='wishlist_add'),
    path('tech-zenovahub.com/wishlist/remove/<int:product_id>/', views.WishlistRemoveView.as_view(), name='wishlist_remove'),
    path('tech-zenovahub.com/wishlist/to/cart/<int:product_id>/', views.WishToCartView.as_view(), name='wishlist_cart'),


    # Product Coupon Routes
    path('tech-zenovahub.com/coupons/', views.CouponListView.as_view(), name='coupon_list'),
    path('tech-zenovahub.com/coupons/create/', views.CouponCreateView.as_view(), name='coupon_create'),
    path('tech-zenovahub.com/coupons/<int:coupon_id>/update/', views.CouponUpdateView.as_view(), name='coupon_update'),
    path('tech-zenovahub.com/coupons/<int:coupon_id>/delete/', views.CouponDeleteView.as_view(), name='coupon_delete'),
    path('tech-zenovahub.com/coupons/<int:coupon_id>/apply/', views.CouponApplyView.as_view(), name='coupon_apply'),

    # Product Shipment Routes
    path('tech-zenovahub.com/shipments/<int:order_id>/', views.ShipmentDetailView.as_view(), name='shipment_detail'),
    path('tech-zenovahub.com/shipments/<int:order_id>/create/', views.ShipmentCreateView.as_view(), name='shipment_create'),
    path('tech-zenovahub.com/shipments/<int:order_id>/update-tracking/', views.ShipmentUpdateTrackingView.as_view(),  name='shipment_update_tracking'),
    path('tech-zenovahub.com/shipments/<int:order_id>/mark-shipped/', views.ShipmentMarkShippedView.as_view(), name='shipment_mark_shipped'),
    path('tech-zenovahub.com/shipments/<int:order_id>/mark-delivered/', views.ShipmentMarkDeliveredView.as_view(), name='shipment_mark_delivered'),

    # Product Search Routes
    path('tech-zenovahub.com/products/search/', views.ProductSearchView.as_view(), name='product_search'),

    # Assign Coupon to User
    path('tech-zenovahub.com/coupons/<int:coupon_id>/assign/', views.AssignCouponToUserView.as_view(), name='assign_coupon_to_user'),

    # Customer Routes for Coupon Management
    path('customer/my-coupons/', views.CustomerCouponListView.as_view(), name='customer_coupon_list'),

    # Policy Terms
    path('terms-of-use/', TemplateView.as_view(template_name="policies/terms_of_use.html"), name="terms_of_use"),
    path('privacy-policy/', TemplateView.as_view(template_name="policies/privacy_policy.html"), name="privacy_policy"),
    path('payment-policy/', TemplateView.as_view(template_name="policies/payment_policy.html"), name="payment_policy"),
    path('warranty-service/', TemplateView.as_view(template_name="policies/warranty_service.html"), name="warranty_service"),


]






