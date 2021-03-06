#-*- coding: utf-8 -*-
from functools import reduce

import django_filters
from django.core.exceptions import ImproperlyConfigured
from django.db.models import Q
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render,redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.template import context
from django.template.loader import render_to_string
from django.template.response import TemplateResponse
from haystack.query import SearchQuerySet
from django_filters import FilterSet
from naxodu import settings
from django.core.paginator import Paginator
from callboard.models import Category, Goods, SubCategory, AttributeMap, AttributeValue, Attribute, Type
from callboard.forms import AdverForm, GoodsImageGallery, ProductFilterForm
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from .forms import GoodsSearchForm
from .forms import AddAttrForm, EditAdvertForm, EditAttrForm, AddAttrFilterForm

import simplejson as json



from django.contrib import  auth

# Create your views here.


def advdetail(request,pk):

    args = {}
    # args['username'] = request.user.username
    # args['uw'] = uw
    good = get_object_or_404(Goods,pk=pk)

    if (good.is_active or request.user==good.user):

        test = request.session.get('has_viewd_%s' % pk,False)
        # добавляем один просмотр за сессию... автору просмотр не засчитывается
        if (request.session.get('has_viewd_%s' % pk)!=True and request.user != good.user):
                request.session['has_viewd_%s' % pk] = True
                # good = Goods.objects.get(pk=pk)

                good.views = good.views+1
                good.save()
                args['adv'] = good
                # attribute= good.attributemap_set.all().order_by('attribute_name_id__ordering')
                args['fotolist'] = good.goodsimagegallery_set.all().select_related('good')
                # args['attribute'] = attribute
                args['user_products'] = Goods.objects.filter(user=good.user).order_by('-order_date').exclude(id=good.pk)[:8]
                args['request'] = request
                args['request'] = request
                if good.attributes:
                    args['attribute'] = get_attribute_value(good.attributes)


                try:
                    releted_products = good.subcategory.attributes.get(attribute_name_id__key_words=True)
                    if releted_products:
                        val = releted_products.value()

                        args['releted_products'] = Goods.objects.filter(attributemap__attribute_value__vallue=val).order_by('?').exclude(id=good.pk)[:5]
                except:

                    args['releted_products'] = Goods.objects.filter(subcategory=good.subcategory).order_by('?').exclude(id=good.pk)[:5]

                return  render(request,'advdetail.html', args)


        # attribute= good.attributemap_set.all().order_by('attribute_name_id__ordering')
        args['adv'] = good
        args['fotolist'] = good.goodsimagegallery_set.all().select_related('good')
        if good.attributes:
            args['attribute'] = get_attribute_value(good.attributes)
        # args['attribute'] = attribute
        args['request'] = request
        args['user_products'] = Goods.objects.filter(user=good.user).order_by('-order_date').exclude(id=good.pk)[:8]

        try:
            releted_products = good.subcategory.attributes.get(attribute_name_id__key_words=True)
            if releted_products:
                val = releted_products.value()

                args['releted_products'] = Goods.objects.filter(attributemap__attribute_value__vallue=val).order_by('?').exclude(id=good.pk)[:5]
        except:

            args['releted_products'] = Goods.objects.filter(subcategory=good.subcategory).order_by('?').exclude(id=good.pk)[:5]

        return  render(request,'advdetail.html', args)

    return redirect('/')




@login_required
def editadvert(request,adv_id):

    obj = get_object_or_404(Goods,pk=adv_id)

    if request.user == obj.user:


        if request.method == "POST":
            eaf = EditAdvertForm(request.POST,instance=obj)
            # att_map = AttributeMap.objects.filter(product_name=obj).order_by('attribute_name__ordering')
            eattf = EditAttrForm(request.POST,obj=obj)
            if eaf.is_valid():

                     attr_dic = {}
                     for attr in obj.subcategory.attributes.all().order_by('ordering'):
                        if request.POST.get(attr.name):
                            attr_desc={}
                            attr_desc['verbos_name'] = attr.verbos_name
                            if attr.attr_type =='choice':
                                attr_desc['value'] = str(attr.attributevalue_set.get(pk=request.POST.get(attr.name)).pk)
                                attr_desc['value_name'] = attr.attributevalue_set.get(pk=request.POST.get(attr.name)).vallue
                            else:
                                attr_desc['value'] = request.POST.get(attr.name)
                                attr_desc['value_name'] = request.POST.get(attr.name)

                            attr_desc['ordering'] = attr.ordering
                            attr_desc['filtering'] = attr.filtering
                            attr_dic[attr.name] = attr_desc


            eaf.instance.attributes = attr_dic
            eaf.save()
            return redirect('/')

                # att_map = AttributeMap.objects.filter(product_name=obj).order_by('attribute_name__ordering')
                # for attr in att_map:
                #         a = request.POST.get(attr.attribute_name.name)
                #     # if request.POST.get(attr.attribute_name.name):
                #         a_val = request.POST.get(attr.attribute_name.name)
                #         if attr.attribute_name.type =='choice':
                #             if a:
                #                 a_val_obj = AttributeValue.objects.get(pk=a_val)
                #             else:
                #                 a_val_obj = None
                #             AttributeMap.objects.update_or_create(product_name = eaf.instance, attribute_name=attr.attribute_name,
                #
                #                                                  defaults={'attribute_value': a_val_obj})
                #         else:
                #
                #             AttributeMap.objects.update_or_create(product_name = eaf.instance, attribute_name=attr.attribute_name,
                #
                #                                                   defaults={'attribute_value_manual': a_val})





        else:
            eaf = EditAdvertForm(instance=obj)
            # att_map = AttributeMap.objects.filter(product_name=obj).order_by('attribute_name__ordering')
            eattf = EditAttrForm(obj=obj)
            # print(eattf)
            args={}

            args['object'] = obj
            args['EditAdvertForm'] = eaf
            args['EditAttrForm'] = eattf

            return  render(request,'editadvert.html',args)

    else:

        return HttpResponseRedirect('/')

def all(items):
    import operator
    return reduce(operator.and_, [bool(item) for item in items])


@login_required
def createadv(request):


    url = request.POST.get('next','/')

    form = AdverForm(request.POST or None, request.FILES or None)
    if request.method =='POST':

     if form.is_valid():
         form.instance.user = request.user

         attr_dic = {}

         for attr in form.cleaned_data['subcategory'].attributes.all().order_by('ordering'):
            if request.POST.get(attr.name):
                attr_desc={}
                attr_desc['verbos_name'] = attr.verbos_name

                if attr.attr_type =='choice':
                    attr_desc['value'] = str(attr.attributevalue_set.get(pk=request.POST.get(attr.name)).pk)
                    attr_desc['value_name'] = attr.attributevalue_set.get(pk=request.POST.get(attr.name)).vallue

                else:
                    attr_desc['value'] = request.POST.get(attr.name)
                    attr_desc['value_name'] = request.POST.get(attr.name)

                attr_desc['ordering'] = attr.ordering
                attr_desc['filtering'] = attr.filtering
                attr_dic[attr.name] = attr_desc

                #
                # if attr.type =='choice':
                #     val = AttributeValue.objects.get(pk=request.POST.get(attr.name))
                #     AttributeMap.objects.create(product_name = form.instance, attribute_name=attr, attribute_value=val)
                # else:
                #     val = request.POST.get(attr.name)
                #     AttributeMap.objects.create(product_name = form.instance, attribute_name=attr, attribute_value_manual=val)

         form.instance.attributes = attr_dic
         form.save()
         return redirect(url,{'username':request.user.username})

    args = {}
    args['form'] = form
    args['next'] = url
    return  render(request,'createadv.html', args)

def notes(request):
    form = GoodsSearchForm(request.GET)
    test = request.GET.get('q')
    notes = form.search().models(Goods).filter(content=test).order_by('-text')

    return render_to_response('notes.html', {'notes': notes})


def autocomplete(request):
    sqs = SearchQuerySet().models(Goods).autocomplete(auto_name=request.GET.get('q', ''))

    suggestions = [result.auto_name for result in sqs]
    content_type = [result.content_type for result in sqs]
    #Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    jdata = json.dumps({
        'results': suggestions, 'content_type':content_type
    })
    return HttpResponse(jdata, content_type='application/json')

def category(request,category):
    return HttpResponse(category)

def subcategory(request,subcategory):
    return HttpResponse(subcategory)





class ProductFilter(FilterSet):
    category = django_filters.CharFilter(name='category__id',distinct=True)
    subcategory = django_filters.CharFilter(name='subcategory__id',distinct=True)
    name = django_filters.CharFilter(name='name', lookup_type='icontains',distinct=True)
    min_price = django_filters.NumberFilter(name='price', lookup_type='gte',distinct=True)
    max_price = django_filters.NumberFilter(name='price', lookup_type='lte',distinct=True)
    MarkaMoto = django_filters.CharFilter(name='attributes',lookup_type='MarkaMoto__value__contains',distinct=True)
    ModelMoto = django_filters.CharFilter(name='attributes',lookup_type='ModelMoto__value__contains',distinct=True)
    CreatYear = django_filters.CharFilter(name='attributes',lookup_type='CreatYear__value__contains',distinct=True)

    class Meta:
        model = Goods
        fields = [
            'min_price',
            'max_price',
            'category',
            'subcategory',
            'name',
            'description',
            'MarkaMoto',
            'ModelMoto',
            'CreatYear'

        ]


def product_list(request):
    qs = Goods.objects.all().order_by('-order_date')
    sort = request.GET.get("sort")

    if sort:

        if sort == 'price':
            qs = sorted(Goods.objects.all(), key=lambda a: a.ua_price[0])
        else:
            qs = Goods.objects.all().order_by(sort)

    filter = ProductFilter(request.GET, queryset=qs)
    return render(request,'callboard/goods_list.html',{"object_list":filter})

class FilterMixin(object):
    filter_class = None

    search_ordering_param = "sort"

    def get_queryset(self,*args,**kwargs):
        try:
            qs = super(FilterMixin, self).get_queryset(*args,**kwargs)
            return qs
        except:
            raise ImproperlyConfigured("You must have a queryset to use the FilterMixin")


    def get_context_data(self, *args, **kwargs):
        context = super(FilterMixin,self).get_context_data(*args,**kwargs)
        qs = self.get_queryset()
        sort = self.request.GET.get(self.search_ordering_param)

        if sort:

            # if sort == 'price':
            #     qs = sorted(qs, key=lambda a: a.ua_price[0])
            # else:
            #     qs = qs.order_by(sort)


            qs = qs.order_by(sort)

        filter_class = self.filter_class

        if filter_class:
            f = filter_class(self.request.GET, queryset = qs)
            context["object_list"] = f
        return  context

class ProductListView(FilterMixin,ListView):
    model = Goods
    queryset = Goods.objects.only_active().select_related('user').order_by('-order_date')




    filter_class = ProductFilter

    def get_context_data(self,*args, **kwargs):
        username = auth.get_user(self.request).username
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        context['username'] = username
        context['cat_list'] = Category.objects.all()
        context['callboard'] = True

        if self.kwargs.get('category', None) != None:
         # context['subcat_list'] = SubCategory.objects.filter(category__slug=self.kwargs['category'])
         context['category'] = Category.objects.get(slug=self.kwargs['category'])


        if self.kwargs.get('subcategory', None) != None:
         # context['subcat_list'] = SubCategory.objects.filter(category__slug=self.kwargs['category'])
             subcategory = SubCategory.objects.get(slug=self.kwargs['subcategory'])

             print(self.kwargs)
             print(self.args)






             attr_form = AddAttrFilterForm(data=self.request.GET or None, sub_category=subcategory)
             context['attr_form'] = attr_form

             context['subcategory'] = subcategory



        context['subcat_list'] = SubCategory.objects.all()
        context['query'] = self.request.GET.get('q')
        context["filter_form"] = ProductFilterForm(data=self.request.GET or None)
        return context


    def get_queryset(self,*args,**kwargs):



        print(self.kwargs.get('category', None))
        print(self.kwargs.get('subcategory', None))





        if self.kwargs.get('category', None) != None:

            if self.kwargs.get('subcategory', None)!= None:
                qs = super(ProductListView,self).get_queryset(*args,**kwargs).\
                    filter(Q(category__slug=self.kwargs['category'])\
                           & Q(subcategory__slug=self.kwargs['subcategory']))
            else:
                qs = super(ProductListView,self).get_queryset(*args,**kwargs).filter(category__slug=self.kwargs['category'])
        else:
            qs = super(ProductListView,self).get_queryset(*args,**kwargs)


        # qs = super(ProductListView,self).get_queryset(*args,**kwargs)

        query = self.request.GET.get('q')

        if query:
            qs = SearchQuerySet().models(Goods).filter(text=query)
        return  qs

        # if query:
        #     qs = self.model.objects.filter(
        #         Q(name__icontains=query) |
        #         Q(description__in=query)
        #     )
        #     try:
        #         qs2 = self.model.objects.filter(
        #             Q(price=query)
        #         )
        #         qs = (qs|qs2).distinct()
        #     except:
        #         pass
        # return qs


def get_subcategory(request, category_id):
    category = Category.objects.get(pk=category_id)
    subcategories = category.subcategory_set.all()
    subcategories_dict = {}
    for subcategory in subcategories:
    # if your subcategory has field name
        subcategories_dict[subcategory.id] = subcategory.name

                                             # +' ['+str(subcategory.count_products())+']'

    return HttpResponse(json.dumps(subcategories_dict), content_type="application/json")



def get_subcategory_list(request, category_id):
    template = 'subcategory_list.html'

    sub_list = SubCategory.objects.filter(category_id=category_id)
    args = {}
    args['sub_list'] = sub_list

    # html = render_to_string('subcategory_list.html', args)
    # print(sub_list)
    # print(html)

    # return HttpResponse(html)

    return TemplateResponse(request,template,args)



def get_attribute_form(request,subcategory_id,type_id):


    try:
        subcategory = SubCategory.objects.get(pk=subcategory_id)
    except:
        subcategory=None

    try:
        type = Type.objects.get(pk=type_id)
    except:
        type=None

    if subcategory.attributes.count() > 0 and subcategory.type.count()==0:
        form = AddAttrForm(sub_category=subcategory,type_id=type)

        args ={}
        args['form'] = form
        # print(form)
        if form:
            return TemplateResponse(request,'attr_form.html',args)
        else:
            return  HttpResponse('pass')

    if type and type.attributes.count() >0:
        form = AddAttrForm(sub_category=subcategory,type_id=type)

        args ={}
        args['form'] = form
        # print(form)
        if form:
            return TemplateResponse(request,'attr_form.html',args)
        else:
            return  HttpResponse('pass')

    return  HttpResponse('pass')


def my_send_mail():
    print('sent')
    send_mail('Ленусику', 'Любимому жулику.', 'loveyou@avtocry.com', ['o.korablev@gmail.com'])


# def callboard (request):
#     sort = request.GET.get('sort')
#     args = {}
#     if sort:
#         args['sort'] = sort
#
#     return render_to_response('callboard/goods_list.html', args, context_instance=RequestContext(request))

def get_attribute_value(attr_list):


    global_list=[]
    sorted_d = sorted(attr_list.items(), key=lambda v: v[1]['ordering'])
    for s in sorted_d:
        list=[]
        list.append(s[1]['verbos_name'])
        list.append(s[1]['value_name'])
        global_list.append(list)

    return global_list