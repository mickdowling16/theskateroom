from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None

    if 'product_size' in request.POST:
        size = request.POST['product_size']

    bag = request.session.get('bag', {})

    sale_successful = False

    if size:
        if item_id in list(bag.keys()):
            if size in bag[item_id]['items_by_size'].keys():
                if product.stock >= quantity:
                    bag[item_id]['items_by_size'][size] += quantity
                    sale_successful = True
                else:
                    messages.error(request, f'Not enough stock available for {product.name}.')
            else:
                if product.stock >= quantity:
                    bag[item_id]['items_by_size'][size] = quantity
                    sale_successful = True
                else:
                    messages.error(request, f'Not enough stock available for {product.name}.')
        else:
            if product.stock >= quantity:
                bag[item_id] = {'items_by_size': {size: quantity}}
                sale_successful = True
            else:
                messages.error(request, f'Not enough stock available for {product.name}.')
    else:
        if item_id in list(bag.keys()):
            if product.stock >= quantity:
                bag[item_id] += quantity
                sale_successful = True
            else:
                messages.error(request, f'Not enough stock available for {product.name}.')
        else:
            if product.stock >= quantity:
                bag[item_id] = quantity
                sale_successful = True
            else:
                messages.error(request, f'Not enough stock available for {product.name}.')

    # Update stock only if the sale is successful
    if sale_successful:
        product.stock -= quantity
        product.save()
        messages.success(request, f'Successfully added {quantity} {product.name} to your bag.')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if quantity > 0:
            # Check if adjusting the quantity exceeds the available stock
            if product.stock + bag[item_id]['items_by_size'][size] >= quantity:
                product.stock += bag[item_id]['items_by_size'][size] - quantity
                bag[item_id]['items_by_size'][size] = quantity
                product.save()
                messages.success(
                    request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
            else:
                messages.error(
                    request, f'Not enough stock available for {product.name}. Reduce quantity and try again.')
        else:
            product.stock += bag[item_id]['items_by_size'][size]
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            product.save()
            messages.success(
                request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            # Check if adjusting the quantity exceeds the available stock
            if product.stock + bag[item_id] >= quantity:
                product.stock += bag[item_id] - quantity
                bag[item_id] = quantity
                product.save()
                messages.success(
                    request, f'Updated {product.name} quantity to {bag[item_id]}')
            else:
                messages.error(
                    request, f'Not enough stock available for {product.name}. Reduce quantity and try again')
        else:
            product.stock += bag[item_id]
            bag.pop(item_id)
            product.save()
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            product.stock += bag[item_id]['items_by_size'][size]
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            product.save()
            messages.success(
                request, f'Removed size {size.upper()} {product.name} from your bag')
        else:
            product.stock += bag[item_id]
            bag.pop(item_id)
            product.save()
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
