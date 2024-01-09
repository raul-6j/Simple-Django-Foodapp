from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Items
from django.template import loader
from .forms import itemForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.

# Function_base_index

def index(request):
    item_list = Items.objects.all()
    # template = loader.get_template('food/index.html')
    # context = {
    #     'item_list':item_list,
    # }
    # # return HttpResponse(template.render(context,request))
    return render(request,'food/index.html',{'item_list':item_list})

# Class_based_index

class indexClassView(ListView):
    model = Items;
    template_name = 'food/index.html';
    context_object_name = 'item_list';


# Function_base_detail

def detail(request,item_id):

    item = Items.objects.get(pk=item_id)
    context = {
        'item':item,
    }
    return render(request,'food/detail.html',context)

# Class_based_detail

class foodDetail(DetailView):
    model = Items;
    template_name = 'food/detail.html';



def create_item(request):

    form = itemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form':form})

# this is class based view for create view

class createItem(CreateView):
    model = Items;
    fields = ['item_name','item_desc','item_price','item_image']

    def form_valid(self,form):
        form.instance.user_name = self.request.user

        return super().form_valid(form)
    template_name = 'food/item-form.html'

def update_item(request,item_id):

    item = Items.objects.get(id=item_id)
    form = itemForm(request.POST or None,instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    return render(request,'food/item-form.html',{'form':form,'item':item})

def delete_item(request,item_id):

    item = Items.objects.get(id=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    return render(request,'food/item_delete.html',{'item':item})

