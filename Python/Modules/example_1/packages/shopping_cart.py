def buy(*args, **kwargs):
    cart = []
    for item in args:
        cart.append(item)
    print("bought selected items")
    return cart