from django.shortcuts import render, redirect, get_object_or_404
from . models import Category
from . models import FoodItem
from django.contrib import messages
from . forms import FoodUpload
# from django.http import HttpResponse
# Create your views here.

# def index(request):
#     return HttpResponse('Hello Resturant Page')

def index(request):
    categories = Category.objects.all()
    
    context = {
        'categories' : categories
    }
    
    return render (request, 'index.html', context)

def fooditem(request, pk):
    fooditem = FoodItem.objects.none()
    category = None
    
    if pk:
        category = get_object_or_404(Category, pk=pk)
        fooditem = FoodItem.objects.filter(category=category)
        
    context = {
        'fooditem' : fooditem,
        'category' : category,
    }
    
    return render (request, 'food.html', context)

def _get_cart(session):
    return session.setdefault('cart', {})


def add_to_cart(request, fooditem_id):
    cart = _get_cart(request.session)
    item = get_object_or_404(FoodItem, id=fooditem_id)
    cart[str(item.id)] = cart.get(str(item.id), 0) + 1
    request.session.modified = True
    messages.success(request, f'Added {item.name} to cart.')
    return redirect('fooditem', pk=item.category.id)

def remove_cart(request, fooditem_id):
    cart = _get_cart(request.session)
    item_id_str = str(fooditem_id)
    if item_id_str in cart:
        del cart[item_id_str]
        request.session.modified = True
        messages.success(request, 'Item removed from cart.')
    return redirect('view_cart')

def view_cart(request):
    cart = _get_cart(request.session)
    food_items = []
    total_price = 0

    for item_id, quantity in cart.items():
        item = get_object_or_404(FoodItem, id=int(item_id))
        item.total_price = item.price * quantity
        item.quantity = quantity
        food_items.append(item)
        total_price += item.total_price
        

    context = {
        'food_items': food_items,
        'total_price': total_price,
    }

    return render(request, 'cart.html', context)

def checkout(request):
    cart = _get_cart(request.session)
    if not cart:
        messages.error(request, 'Your cart is empty.')
    return redirect('create_order')
    
    # clear the cart after checkout
    # request.session['cart'] = {}
    # request.session.modified = True
    # messages.success(request, 'Checkout successful! Thank you for your order.')
    # return redirect('index')
    
def upload_food(request):
    form = FoodUpload()
    if request.method == 'POST':
        form = FoodUpload(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.save()
            messages.success(request, 'Food Uploaded Successfully')
            return redirect('index')
        else:
            messages.error(request, 'Error Uploading Food')
    return render (request, 'upload.html', {'form':form})