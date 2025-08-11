from shop.models import Category
from django.core.exceptions import ObjectDoesNotExist

def get_all_categories():
    try:
        return Category.objects.all().order_by('name')
    except Exception as e:
        print(f"Error fetching categories: {e}")
        return []

def get_category_by_id(category_id):
    try:
        return Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        print(f"Category with ID {category_id} not found.")
        return None
    except Exception as e:
        print(f"Error retrieving category: {e}")
        return None

def create_category(data):
    try:
        category = Category.objects.create(
            name=data.get('name'),
            description=data.get('description', ''),
            image=data.get('image'),
            slug=data.get('slug')
        )
        return category
    except Exception as e:
        print(f"Error creating category: {e}")
        return None

def update_category(category_id, data):
    try:
        category = Category.objects.get(id=category_id)
        category.name = data.get('name', category.name)
        category.description = data.get('description', category.description)
        category.slug = data.get('slug', category.slug)
        category.image = data.get('image', category.image)
        category.save()
        return category
    except ObjectDoesNotExist:
        print(f"Category with ID {category_id} not found.")
        return None
    except Exception as e:
        print(f"Error updating category: {e}")
        return None

def delete_category(category_id):
    try:
        category = Category.objects.get(id=category_id)
        category.delete()
        return True
    except ObjectDoesNotExist:
        print(f"Category with ID {category_id} not found.")
        return False
    except Exception as e:
        print(f"Error deleting category: {e}")
        return False