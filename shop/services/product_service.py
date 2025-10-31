from shop.models import Product
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from shop.models import Category
from user.models import User
from shop.utils import slug_util


# Fetch all Products
def get_all_products(active_only=True):
    try:
        if active_only:
            products = Product.objects.filter(is_active=True).order_by('-created_at')
        else:
            products = Product.objects.all().order_by('-created_at')

        print(f"[get_all_products] Retrieved {products.count()} products")
        return products

    except Exception as e:
        print(f"[get_all_products] Error: {e}")
        return []


# Fetch Products By ID
def get_product_by_id(product_id):
    try:
        product = Product.objects.get(id=product_id)
        print(f"[get_product_by_id] Found product {product.id} - {product.name}")
        return product
    except ObjectDoesNotExist:
        print(f"[get_product_by_id] Product with ID {product_id} not found.")
        return None
    except Exception as e:
        print(f"[get_product_by_id] Error retrieving product {product_id}: {e}")
        return None



# Create a new Product
def create_product(data, request, files=None):
    try:
        category_id = data.get('category')
        category = Category.objects.get(id=category_id)
        user_id = request.session.get('user_id')
        if not user_id:
            raise ValueError("No user_id in session. Ensure login sets session values.")
        created_by = User.objects.get(id=user_id)
        provided_sku = data.get('sku')
        name = data.get('name')
        sku = slug_util.generate_unique_skg(Product, name, provided_sku)
        product = Product.objects.create(
            category=category,
            name=name,
            description=data.get('description'),
            price=data.get('price'),
            stock=data.get('stock'),
            image=files.get('image') if files else None,
            sku=sku,
            tags=data.get('tags', ''),
            created_by=created_by
        )
        return product
    except Category.DoesNotExist:
        print(f"Category with ID {category_id} not found.")
        return None
    except User.DoesNotExist:
        print(f"User with ID {user_id} not found in DB.")
        return None
    except Exception as e:
        print(f"Error creating product: {e}")
        return None



# Update the existing Product
def update_product(product_id, data, request, files=None):
    try:
        product = Product.objects.get(id=product_id)
        product.name = data.get('name', product.name)
        product.description = data.get('description', product.description)
        product.price = data.get('price', product.price)
        product.stock = data.get('stock', product.stock)
        product.tags = data.get('tags', product.tags)
        product.is_active = bool(data.get('is_active', product.is_active))
        new_sku_input = data.get('sku')
        new_name_input = data.get('name')
        if new_sku_input or (new_name_input and new_name_input != product.name):
            product.sku = slug_util.generate_unique_skg(Product, new_name_input or product.name, new_sku_input)
        if 'category' in data:
            try:
                product.category = Category.objects.get(id=data.get('category'))
            except Category.DoesNotExist:
                print(f"Category with ID {data.get('category')} not found. Keeping existing category.")
        if files and files.get('image'):
            product.image = files.get('image')
        user_id = request.session.get('user_id')
        if user_id:
            try:
                product.updated_by = User.objects.get(id=user_id)
            except User.DoesNotExist:
                print(f"User with ID {user_id} not found. Skipping updated_by.")
        product.save()
        return product
    except Product.DoesNotExist:
        print(f"Product with ID {product_id} not found.")
        return None
    except Exception as e:
        print(f"Error updating product: {e}")
        return None


# Delete an existing Product
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


# Search for Products
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




