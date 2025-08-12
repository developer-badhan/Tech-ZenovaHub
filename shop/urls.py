from django.urls import path
from . import views

urlpatterns = [

    # Home Route
    path('', views.HomeView.as_view(), name='home'),

    # Product Routes
    path('tech-zenovahub/products/', views.ProductListView.as_view(), name='product_list'),
    path('tech-zenovahub/products/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('tech-zenovahub/products/<int:product_id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('tech-zenovahub/products/<int:product_id>/edit/', views.ProductUpdateView.as_view(), name='product_update'),
    path('tech-zenovahub/products/<int:product_id>/delete/', views.ProductDeleteView.as_view(), name='product_delete'),

    # Product Category Routes
    path('tech-zenovahub/categories/', views.CategoryListView.as_view(), name='category_list'),
    path('tech-zenovahub/categories/create/', views.CategoryCreateView.as_view(), name='category_create'),
    path('tech-zenovahub/categories/<int:category_id>/', views.CategoryDetailView.as_view(), name='category_detail'),
    path('tech-zenovahub/categories/<int:category_id>/edit/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('tech-zenovahub/categories/<int:category_id>/delete/', views.CategoryDeleteView.as_view(), name='category_delete'),

    # Product Order Routes
    path('tech-zenovahub/orders/', views.OrderListView.as_view(), name='order_list'),
    path('tech-zenovahub/orders/create/', views.OrderCreateView.as_view(), name='order_create'),
    path('tech-zenovahub/orders/<int:order_id>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('tech-zenovahub/orders/<int:order_id>/delete/', views.OrderDeleteView.as_view(), name='order_delete'),

    # Product Order Item Routes
    path('tech-zenovahub/orders/<int:order_id>/items/', views.OrderItemListView.as_view(), name='order_item_list'),
    path('tech-zenovahub/orders/<int:order_id>/items/create/', views.OrderItemCreateView.as_view(), name='order_item_create'),
    path('tech-zenovahub/orders/items/<int:item_id>/edit/', views.OrderItemUpdateView.as_view(), name='order_item_update'),
    path('tech-zenovahub/orders/items/<int:item_id>/delete/', views.OrderItemDeleteView.as_view(), name='order_item_delete'),

    # Cart Routes
    path('tech-zenovahub/cart/', views.CartDetailView.as_view(), name='cart_detail'),
    path('tech-zenovahub/cart/add/', views.CartAddItemView.as_view(), name='cart_add'),
    path('tech-zenovahub/cart/update/', views.CartUpdateItemView.as_view(), name='cart_update'),
    path('tech-zenovahub/cart/remove/', views.CartRemoveItemView.as_view(), name='cart_remove'),
    path('tech-zenovahub/cart/clear/', views.CartClearView.as_view(), name='cart_clear'),

    # Product Review Routes
    path('tech-zenovahub/products/<int:product_id>/reviews/', views.ProductReviewListView.as_view(), name='review_list'),
    path('tech-zenovahub/products/<int:product_id>/reviews/create/', views.ProductReviewCreateView.as_view(), name='review_create'),
    path('tech-zenovahub/products/<int:product_id>/reviews/update/', views.ProductReviewUpdateView.as_view(), name='review_update'),
    path('tech-zenovahub/products/<int:product_id>/reviews/delete/', views.ProductReviewDeleteView.as_view(), name='review_delete'),

    # Cart Wishlist Routes
    path('tech-zenovahub/wishlist/', views.WishlistListView.as_view(), name='wishlist'),
    path('tech-zenovahub/wishlist/add/<int:product_id>/', views.WishlistAddView.as_view(), name='wishlist_add'),
    path('tech-zenovahub/wishlist/remove/<int:product_id>/', views.WishlistRemoveView.as_view(), name='wishlist_remove'),

    # Product Coupon Routes
    path('tech-zenovahub/coupons/', views.CouponListView.as_view(), name='coupon_list'),
    path('tech-zenovahub/coupons/apply/', views.CouponApplyView.as_view(), name='coupon_apply'),
    path('tech-zenovahub/coupons/remove/', views.CouponRemoveView.as_view(), name='coupon_remove'),

    # Product Shipment Routes
    path('tech-zenovahub/shipments/<int:order_id>/', views.ShipmentDetailView.as_view(), name='shipment_detail'),
    path('tech-zenovahub/shipments/<int:order_id>/create/', views.ShipmentCreateView.as_view(), name='shipment_create'),
    path('tech-zenovahub/shipments/<int:order_id>/update-tracking/', views.ShipmentUpdateTrackingView.as_view(), name='shipment_update_tracking'),
    path('tech-zenovahub/shipments/<int:order_id>/mark-shipped/', views.ShipmentMarkShippedView.as_view(), name='shipment_mark_shipped'),
    path('tech-zenovahub/shipments/<int:order_id>/mark-delivered/', views.ShipmentMarkDeliveredView.as_view(), name='shipment_mark_delivered'),


]








