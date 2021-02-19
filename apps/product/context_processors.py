from apps.product.models import Category

# register the below method under settings.py > TEMPLATES > 'OPTIONS' > 'context_processors' 

def menu_categories(request):
    return {'menu_categories': Category.objects.all()}