from products.models import Product, Property, Wishlist

# class Wishlist:
#     def __init__(self, request):
#         self.request = request

#         self.session = request.session

#         wishlist = self.session.get('wishlist')

#         if not wishlist:
#             wishlist = self.session['wishlist'] = list()
#         self.wishlist=wishlist
#         def save(self):
#             self.session.modified = True

#     def add(self,product,customer):
#         try:
#             product_obj=product
#             customer_obj=customer
#             Wishlist.objects.get_or_create(
#                 product=product_obj,
#                 customer=customer_obj
#             )
#             self.wishlist.append(Wishlist.objects.get_or_create(
#                 product=product_obj,
#                 customer=customer_obj
#             ))
#             self.save
#         except Exception as e:
#             print(e,'----------------------')


#     def remove(self,**kwargs):
#         try:
#             product_obj=kwargs['product']
#             customer_obj=kwargs['customer']


#             self.wishlist.append(
#                 Wishlist.objects.delete(
#                 product=product_obj,
#                 customer=customer_obj
#             )
#             )
#             self.save
#         except Exception as e:
#             print(e,'----------------------')


class Cart:

    def __init__(self, request):
        self.request = request

        self.session = request.session

        cart = self.session.get('cart')
        # cart = self.session.get('wishlist')

        if not cart:
            cart = self.session['cart'] = dict()


        self.cart = cart

    def save(self):
        self.session.modified = True

    def add(self, product, add_or_replace, **kwargs):
        color = kwargs['color']
        size = kwargs['size']
        quantity = kwargs['quantites']
        s=size
        product_id = str(product.id)
        label = str(product_id)+str(color)+str(size)
        # p_obj = Product.objects.get(id=product_id)
        property_obj=Property.objects.get(product=product_id, color=color, size=s)
        if property_obj.number >= 1 and property_obj.number >=quantity:
            if (label in self.cart and size == self.cart[label]['size'] and color == self.cart[label]['color']):
                if add_or_replace == 'on':
                    self.cart[label]['quantity'] = quantity
                else:
                    self.cart[label]['quantity'] += quantity

            else:
                self.cart[label] = {'product': product_id, 'quantity': quantity, 'color': str(
                    color), 'size': str(size)}
            self.save()
        else:
            raise Property.DoesNotExist

    def remove(self, product_id, color, size):
        label = str(product_id)+str(color)+str(size)
        if label in self.cart:
            del self.cart[label]

        self.save()

    def __iter__(self):
        product_ids = []
        cart = self.cart.copy()
        # products = []
        # for item in product_ids:
        #     products.append(Product.objects.select_related('category','sicount').get(id=item))

        for item in cart.keys():
            pro = Product.objects.select_related('category','discount').prefetch_related('propertes').get(id=int(cart[item]['product']))
            if pro.discount:
                product_price = int(
                    float(pro.price)-float(pro.price)*pro.discount.discount)
            else:
                product_price = pro.price
                
            cart[item]['total_price'] = (cart[item]['quantity'])*product_price
            cart[item]['product_object'] = pro
            yield cart[item]

    def __len__(self):
        return len(self.cart.keys())

    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        # product_ids = self.cart.keys()
        product_ids = []
        for item in self.cart.values():
            product_ids.append(item['product'])

        products = []
        for item in product_ids:
            products.append(Product.objects.get(id=item))

        # return sum(item['quantity']*item['product_object'].price for item in self.cart.values())
        s = 0
        for item in self.cart.values():
            product_obj= Product.objects.select_related('category','discount').get(id=int(item['product']))
            prdouct_price = float(product_obj.price)
            if product_obj.discount:
                totla_item_price = int(
                    (prdouct_price-prdouct_price * product_obj.discount.discount)*item['quantity'])
            else:
                totla_item_price = prdouct_price*item['quantity']

            s += totla_item_price
        return s
