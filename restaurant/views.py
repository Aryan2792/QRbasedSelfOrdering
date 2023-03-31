from django.shortcuts import *
from django.http import *
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import *
import random as rn
from maildemo import sendEmail, sendMsg


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


def menu(request):
    categories = Category.objects.all()
    dishes = Dishes.objects.all()
    return render(request, 'menu.html', {'categories': categories, 'dishes': dishes})


def cart(request):
    if 'user' in request.session:
        return render(request, 'cart.html')
    else:
        return redirect('index')

def userlogout(request):
    if 'user' in request.session:
        request.session['user'] = ''
        del request.session['user']
        return redirect('index')
    else:
        return redirect('index')

def order(request):
    if 'user' in request.session:
        order = Order.objects.filter(visitor_id=request.session['user']['id'])
        return render(request, 'orders.html',{'orders':order})
    else:
        return redirect('index')

def orderdetails(request, id=0):
    if 'user' in request.session:
        order = OrderDetail.objects.filter(order_id=id)
        return render(request, 'orderdetails.html',{'orders':order})
    else:
        return redirect('index')


@method_decorator(csrf_exempt, name="dispatch")
class loginUser(View):
    def post(self, request):
        email = request.POST['email']
        phone = request.POST['phone']
        print(email, phone)
        otp = rn.randint(1000, 9999)
        user = Visitors.objects.filter(email=email, mobile=phone)
        message = f'Here is your One Time Password(OTP) {otp}'
        if len(user) == 0:
            new_user = Visitors(email=email, mobile=phone, otp=otp)
            new_user.save()
            sendEmail(to=email, subject='One Time Password', message=message)
            sendMsg(phone,message)
            return HttpResponse('New')
        else:
            user.update(otp=otp)
            sendEmail(to=email, subject='One Time Password', message=message)
            sendMsg(phone,message)
            return HttpResponse('Old')


@method_decorator(csrf_exempt, name='dispatch')
class checkUser(View):
    def post(self, request):
        if 'name' in request.POST:
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            otp = request.POST['otp']
            user = Visitors.objects.filter(email=email, mobile=phone)
            if str(user[0].otp) == otp:
                user.update(otp=None, name=name)
                request.session['user'] = {
                    'email': email,
                    'mobile': phone,
                    'name': name
                }
                return HttpResponse('success')
            else:
                return HttpResponse('Invalid OTP, Please try again...')
        else:
            email = request.POST['email']
            phone = request.POST['phone']
            otp = request.POST['otp']
            user = Visitors.objects.filter(email=email, mobile=phone)
            if str(user[0].otp) == otp:
                user.update(otp=None)
                request.session['user'] = {
                    'id': user[0].pk,
                    'email': email,
                    'mobile': phone,
                    'name': user[0].name
                }
                return HttpResponse('success')
            else:
                return HttpResponse('Invalid OTP, Please try again...')


@method_decorator(csrf_exempt, name='dispatch')
class addToCart(View):
    def post(self, request, **kwargs):
        pid = kwargs['id']
        if 'user' in request.session:
            dish = Dishes.objects.get(pk=pid)
            cart = Cart.objects.filter(dish=dish, visitor_id=request.session['user']['id'])
            if len(cart) == 0:
                quantity = 1
                cart = Cart(item=dish.name, photo=dish.photo, quantity=1, total=quantity * dish.price, price=dish.price,
                            dish=dish, visitor_id=request.session['user']['id'])
                cart.save()
                return JsonResponse({'status': True, 'message': 'Added to Cart'}, safe=False)
            else:
                return JsonResponse({'status': False, 'message': 'Already in your cart .....'})
        else:
            return JsonResponse({'status': False, 'message': 'Please Login First.....'})


def getCartQuantity(request):
    if 'user' in request.session:
        return JsonResponse(
            {'status': True, 'cartQuantity': len(Cart.objects.filter(visitor_id=request.session['user']['id']))},
            safe=False)
    else:
        return JsonResponse(
            {'status': True, 'cartQuantity': 0},
            safe=False)

@csrf_exempt
def getCartDetails(request):
    cart = Cart.objects.filter(visitor_id=request.session['user']['id'])
    grandtotal = 0
    for i in cart:
        grandtotal += i.total
    return JsonResponse({'cart': list(cart.values()), 'gtotal': grandtotal}, safe=False)

def removeCart(request, id):
    cart = Cart.objects.get(pk=id)
    cart.delete()
    # cart.save()
    return HttpResponse('success')

def changeQuantity(request, id, q):
    cart = Cart.objects.get(pk=id)
    cart.quantity = q
    cart.total = cart.quantity * cart.price
    cart.save()
    return HttpResponse('success')

@method_decorator(csrf_exempt, name='dispatch')
class confirmOrder(View):
    def post(self, request):
        userId = request.session['user']['id']
        cart = Cart.objects.filter(visitor_id=userId)
        total = 0
        for i in cart:
            total += i.total
        order = Order(visitor_id=userId, total=total)
        order.save()
        for i in cart:
            od = OrderDetail(order=order, dish_id=i.dish_id, price=i.price,
                             total=i.total, quantity=i.quantity)
            od.save()
            i.delete()
        sendMsg(request.session['user']['mobile'], f'Your Order has been placed. Your Order Amount is {total} with order id. {order.pk}')
        return JsonResponse({'status':True, 'orderid':order.pk})

def thankspage(request, id):
    return render(request, 'thankspage.html', {'orderid':id})