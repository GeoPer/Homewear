from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.template import loader

from .models import Category, Product

def index(request):
    latest_category_list = Category.objects.all()
    print(latest_category_list)
    template = loader.get_template('homewear/index.html')
    context = {
        'latest_category_list': latest_category_list,
    }
    return HttpResponse(template.render(context, request))

def detail_cat(request, category_id):
    category_list = Category.objects.all()
    template = loader.get_template('homewear/detail.html')
    context = {
        'category_list': category_list,
    }
    return HttpResponse(template.render(context, request))

def detail_prod(request, product_id):
    return HttpResponse("You're looking at product %s." % product_id)

def results(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'homewear/results.html', {'category': category})\

def vote(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    try:
        selected_product = category.product_set.get(pk=request.POST['product'])
    except (KeyError, Product.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'homewear/detail.html', {
            'category': category,
            'error_message': "You didn't select a product.",
        })
    else:
        selected_product.quantity += 1
        selected_product.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('homewear:results', args=(category.id,)))