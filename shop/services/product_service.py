from shop.models import Product
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

def get_all_products(active_only=True):
    try:
        if active_only:
            return Product.objects.filter(is_active=True).order_by('-created_at')
        return Product.objects.all().order_by('-created_at')
    except Exception as e:
        print(f"Error fetching products: {e}")
        return []

def get_product_by_id(product_id):
    try:
        return Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        print(f"Product with ID {product_id} not found.")
        return None
    except Exception as e:
        print(f"Error retrieving product: {e}")
        return None

def create_product(data, user):
    try:
        product = Product.objects.create(
            category=data.get('category'),
            name=data.get('name'),
            description=data.get('description'),
            price=data.get('price'),
            stock=data.get('stock'),
            image=data.get('image'),
            sku=data.get('sku'),
            tags=data.get('tags', ''),
            created_by=user
        )
        return product
    except Exception as e:
        print(f"Error creating product: {e}")
        return None

def update_product(product_id, data):
    try:
        product = Product.objects.get(id=product_id)
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        product.image = data.get('image', product.image)
        product.sku = data.get('sku', product.sku)
        product.tags = data.get('tags', product.tags)
        product.category = data.get('category', product.category)
        product.is_active = data.get('is_active', product.is_active)
        product.save()
        return product
    except ObjectDoesNotExist:
        print(f"Product with ID {product_id} not found.")
        return None
    except Exception as e:
        print(f"Error updating product: {e}")
        return None

def delete_product(product_id):
    try:
        product = Product.objects.get(id=product_id)
        product.delete()
        return True
    except ObjectDoesNotExist:
        print(f"Product with ID {product_id} not found.")
        return False
    except Exception as e:
        print(f"Error deleting product: {e}")
        return False

def search_products(query):
    try:
        return Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(tags__icontains=query)
        ).filter(is_active=True)
    except Exception as e:
        print(f"Error searching products: {e}")
        return []