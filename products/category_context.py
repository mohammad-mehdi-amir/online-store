from .models import Category

def category1(request):
    return {'Category':Category.objects.select_related('discount').prefetch_related('products').all()}