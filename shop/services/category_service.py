from shop.models import Category
from django.core.exceptions import ObjectDoesNotExist
from shop.utils import slug_util


# Fetch all Categories
def get_all_categories():
    try:
        return Category.objects.all().order_by('name')
    except Exception as e:
        print(f"Error fetching categories: {e}")
        return []


# Fetch a Category by ID
def get_category_by_id(category_id):
    try:
        return Category.objects.get(id=category_id)
    except ObjectDoesNotExist:
        print(f"Category with ID {category_id} not found.")
        return None
    except Exception as e:
        print(f"Error retrieving category: {e}")
        return None


# Create a new Category
def create_category(data):
    try:
        name = data.get('name')
        provided_slug = data.get('slug')
        slug = slug_util.generate_unique_slug(Category, name, provided_slug)
        category = Category.objects.create(
            name=name,
            description=data.get('description', ''),
            image=data.get('image'),
            slug=slug
        )
        return category
    except Exception as e:
        print(f"Error creating category: {e}")
        return None

# # Update an existing Category
def update_category(category_id, data):
    try:
        category = Category.objects.get(id=category_id)
        category.name = data.get('name', category.name)
        category.description = data.get('description', category.description)
        new_image = data.get('image')
        if new_image:
            category.image = new_image
        new_slug = data.get('slug')
        if new_slug:
            category.slug = slug_util.generate_unique_slug(Category, category.name, new_slug)
        elif category.slug != slug_util.generate_unique_slug(Category, category.name, category.slug):
            category.slug = slug_util.generate_unique_slug(Category, category.name)
        category.save()
        return category
    except ObjectDoesNotExist:
        print(f"Category with ID {category_id} not found.")
        return None
    except Exception as e:
        print(f"Error updating category: {e}")
        return None



# Delete an existing Category
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
    

# Create a new Category
def create_category(data):
    try:
        name = data.get('name')
        provided_slug = data.get('slug')

        slug = slug_util.generate_unique_slug(Category, name, provided_slug)

        category = Category.objects.create(
            name=name,
            description=data.get('description', ''),
            image=data.get('image'),
            slug=slug
        )
        return category
    except Exception as e:
        print(f"Error creating category: {e}")
        return None




