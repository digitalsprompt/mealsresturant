def cart_item_count(request):
    cart = request.session.get('cart', {})
    count = 0

    for qty in cart.values():
        try:
            count += int(qty)
        except (TypeError, ValueError):
            continue

    return {'cart_item_count': count}
