from .cart import Cart,Wishlist

def cart(request):
    return {'cart':Cart(request)}