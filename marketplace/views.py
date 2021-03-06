from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, get_object_or_404
from django.views.generic import ListView

from marketplace.models import Order
from callboard.models import Goods, Category
from django.db.models import Q
from django.template import RequestContext



# Create your views here.

class UserProductListView(ListView):

    model = Goods
    queryset = Goods.objects.only_active().select_related('user').order_by('-order_date')

    def get_context_data(self,*args, **kwargs):

        context = super(UserProductListView,self).get_context_data(*args,**kwargs)


        # cat_list = Category.objects. подумать как выбрать список категорий по которым есть объявы у автора.



        context['query'] = self.request.GET.get('q')



        context['user_shop'] = get_object_or_404(User, username = self.kwargs['user_name'] )



        return context

    def get_queryset(self,*args,**kwargs):


        print(self.kwargs.get('user_name', None))




        if self.kwargs.get('user_name', None) != None:

            qs = super(UserProductListView,self).get_queryset(*args,**kwargs).\
                    filter(user__username=self.kwargs['user_name'])
        else:
             qs = super(UserProductListView,self).get_queryset(*args,**kwargs)

        return qs



@login_required
def pruduct_list(request):

        sort = request.GET.get('sort')
        args={}

        if sort is not None:

            args['market']  = Goods.objects.filter(user=request.user).order_by(str(sort))
        else:
            args['market'] = Goods.objects.filter(user=request.user).order_by('-order_date')


        return render(request,'marketplace.html', args)




def order_list(request, user_name):
    if request.user.username == user_name:
        sort = request.GET.get('sort')
        args={}
        if sort is not None:

            args['my_orders'] = my_orders = Order.objects.filter(Q(buyer__username=user_name)).order_by(str(sort))
            args['orders_to_me'] = orders_to_me = Order.objects.filter(Q(seller__username=user_name) & ~Q(order_status = 'Draft')).order_by(str(sort))
            args['market'] = market = Goods.objects.filter(user__username=user_name).order_by(str(sort))
        else:
            args['my_orders'] = my_orders = Order.objects.filter(Q(buyer__username=user_name))
            args['orders_to_me'] = orders_to_me = Order.objects.filter(Q(seller__username=user_name) & ~Q(order_status = 'Draft'))
            args['market'] = market = Goods.objects.filter(user__username=user_name)

        args['username'] = user_name
        args['request'] = request
        # args['uw'] = getuw(user_name)

        return render_to_response('marketplace.html', args)
    else:
        return HttpResponseRedirect('/')



@login_required
def change_product_status(reques, product_id):
    product = get_object_or_404(Goods, pk = product_id)
    if reques.user == product.user:
        if product.is_active == True:
            product.is_active=False
            product.save()

        else:
            product.is_active= True
            product.save()

    return  HttpResponse('Статус измененн')

@login_required
def delete_product(reques, product_id):
    product = get_object_or_404(Goods, pk = product_id)
    if reques.user == product.user:
        product.delete()


    return  HttpResponse('Объявление удалено')