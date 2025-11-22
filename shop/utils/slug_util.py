from django.utils.text import slugify
import random
import string


# Auto generate slug 
def generate_unique_slug(model, name, provided_slug=None):
    base_slug = slugify(provided_slug or name)
    slug = base_slug
    counter = 1

    # Ensure uniqueness
    while model.objects.filter(slug=slug).exists():
        random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=4))
        slug = f"{base_slug}-{random_suffix}"
        counter += 1
        if counter > 20:
            raise ValueError("Unable to generate a unique slug after 20 attempts.")

    return slug


# Auto generate skg
def generate_unique_skg(model, name, provided_sku=None):
    base_sku = slugify(provided_sku or name).lower() 
    sku = base_sku
    counter = 1

    # Ensure uniqueness using the 'sku' field
    while model.objects.filter(sku=sku).exists():
        random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=4))
        sku = f"{base_sku}-{random_suffix}"
        counter += 1
        if counter > 20:
            raise ValueError("Unable to generate a unique SKU after 20 attempts.")

    return sku


