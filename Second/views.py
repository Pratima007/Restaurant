from django.shortcuts import render, redirect, get_object_or_404
from hotel.models import Second, Order
from hotel.forms import SecondForm
from django.contrib import messages

def home_view(request):
    return render(request, 'home.html') 

def home(request):
    scd_obj = Second.objects.all()
    context = {'hotels': scd_obj}
    return render(request, 'home.html', context)

def menu(request):
    scd_obj = Second.objects.all()
    context = {'hotels': scd_obj}
    return render(request, 'menu.html', context)

def create(request):
    if request.method == 'POST':
        form = SecondForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item created successfully!')
            return redirect('menu')
        else:
            messages.error(request, 'There was an error with your submission.')
    else:
        form = SecondForm()

    return render(request, 'create.html', {'form': form})

def edit(request, pk):
    hotel = get_object_or_404(Second, id=pk)
    if request.method == "POST":
        hotel.name = request.POST.get('name')
        hotel.price = request.POST.get('price')
        hotel.save()
        messages.success(request, 'Hotel item updated successfully!')
        return redirect('menu')
    context = {'hotel': hotel}
    return render(request, 'edit.html', context)

def delete(request, pk):
    hotel = get_object_or_404(Second, id=pk)
    hotel.delete()
    messages.success(request, 'Hotel item deleted successfully!')
    return redirect('menu')

def order_food(request, pk):
    hotel = get_object_or_404(Second, pk=pk)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        total_price = hotel.price * quantity
        Order.objects.create(hotel=hotel, quantity=quantity, total_price=total_price)
        messages.success(request, f'Your order for {quantity} {hotel.name}(s) totaling Rs{total_price:.2f} is successful!')
        return redirect('menu')
    else:
        messages.error(request, 'Invalid request method.')
        return redirect('menu')

def order_list(request):
    orders = Order.objects.all().order_by('-ordered_at')
    return render(request, 'order_list.html', {'orders': orders})
