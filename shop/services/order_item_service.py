from shop.models import OrderItem, Order, Product
from django.core.exceptions import ObjectDoesNotExist

def get_items_by_order(order_id):
    try:
        return OrderItem.objects.filter(order__id=order_id)
    except Exception as e:
        print(f"Error fetching order items for order {order_id}: {e}")
        return []

def get_item_by_id(item_id):
    try:
        return OrderItem.objects.get(id=item_id)
    except ObjectDoesNotExist:
        print(f"Order item with ID {item_id} not found.")
        return None
    except Exception as e:
        print(f"Error retrieving order item: {e}")
        return None

def create_order_item(order, product_id, quantity, price=None):
    try:
        product = Product.objects.get(id=product_id)
        return OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=price or product.price
        )
    except Product.DoesNotExist:
        print(f"Product with ID {product_id} not found.")
        return None
    except Exception as e:
        print(f"Error creating order item: {e}")
        return None

def update_order_item(item_id, quantity=None, price=None):
    try:
        item = OrderItem.objects.get(id=item_id)
        if quantity is not None:
            item.quantity = quantity
        if price is not None:
            item.price = price
        item.save()
        return item
    except ObjectDoesNotExist:
        print(f"Order item with ID {item_id} not found.")
        return None
    except Exception as e:
        print(f"Error updating order item: {e}")
        return None

def delete_order_item(item_id):
    try:
        item = OrderItem.objects.get(id=item_id)
        item.delete()
        return True
    except ObjectDoesNotExist:
        print(f"Order item with ID {item_id} not found.")
        return False
    except Exception as e:
        print(f"Error deleting order item: {e}")
        return False