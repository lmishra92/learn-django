from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .forms import RestaurantCreateForm, RestaurantLocationForm, ShoppingForm
from .models import RestaurantLocation
from postcode.forms import PostCodeForm

# Create your views here.

# function based view
def restaurant_createview(request):
    form = PostCodeForm(request.POST or None)
    post_code = None
    if form.is_valid():
        postcode = request.POST.get("postcode")
        post_code = postcode

    if form.errors:
        print(form.errors)

    template_name = "restaurants/form.html"
    context = {"form": form, "postcode":post_code}


    return render(request, template_name, context)
# class based views

class RestaurantListView(ListView):

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        print(slug)
        if slug:
            queryset = RestaurantLocation.objects.filter(
                Q(category__icontains=slug) |
                Q(category__iexact=slug)
            )
        else:
            queryset = RestaurantLocation.objects.all()
        return queryset


class RestaurantDetailView(DetailView):
    queryset = RestaurantLocation.objects.all()

class RestaurantCreateView(CreateView):

    form_class = RestaurantLocationForm
    template_name = "restaurants/form.html"
    success_url = '/restaurants/'