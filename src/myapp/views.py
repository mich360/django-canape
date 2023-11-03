from django.shortcuts import render, redirect
from .models import MyApp, Person, MyMail
from .forms import MyMailForm
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.asgi import get_asgi_application

def loggedin_view(request):
    context = {
        'message': 'ログインしました。ようこそ！',
    }
    return render(request, 'loggedin_template.html', context)

@login_required
def person_list(request):
    data = Person.objects.all()
    return render(request, 'person_list.html', {'data': data})

class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"

class PersonListView(ListView):
    model = Person

def myappDetailView(request, pk):
    template_name = "myapp/myapp-detail.html"

    try:
        myapp = MyApp.objects.get(pk=pk)
    except MyApp.DoesNotExist:
        myapp = None

    ctx = {
        "number": pk,
        "object": myapp,
    }
    return render(request, template_name, ctx)

# ASGIアプリケーションのライフサイクルハンドラ
from . import my_custom_startup_handler, my_custom_shutdown_handler
from .my_custom_startup_handler import my_custom_startup_handler
from .my_custom_shutdown_handler import my_custom_shutdown_handler

django_asgi_app = get_asgi_application()

async def application(scope, receive, send):
    if scope['type'] == 'lifespan':
        if scope['asgi']['type'] == 'startup':
            await my_custom_startup_handler()
        elif scope['asgi']['type'] == 'shutdown':
            await my_custom_shutdown_handler()
    else:
        await django_asgi_app(scope, receive, send)

def myappCreateView(request):
    template_name = "myapp/mymail-form.html"

    if request.method == "POST":
        form = MyMailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mymail_form")
    else:
        form = MyMailForm()

    context = {
        'form': form,
    }

    return render(request, template_name, context)

def mymailCreateView(request):
    template_name = "myapp/mymail-form.html"

    if request.method == "POST":
        form = MyMailForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully!')
            return redirect("mymail_form")
    else:
        form = MyMailForm()

    context = {
        'form': form,
    }

    return render(request, template_name, context)

def myappListView(request):
    template_name = "myapp/myapp_list.html"
    ctx = {}
    qs = MyApp.objects.all()
    ctx["object_list"] = qs

    return render(request, template_name, ctx)

def myappUpdateListView(request):
    template_name = "myapp/update_myapp-list.html"
    ctx = {}
    qs = MyApp.objects.all()
    ctx["object_list"] = qs
    return render(request, template_name, ctx)

def my_view(request):
    context = {
        'key1': 'value1',
        'key2': 'value2',
    }

    return render(request, 'myapp_list.html', context)

def myappUpdateView(request, pk):
    obj = MyApp.objects.get(pk=pk)
    obj.some_field = 'new_value'
    obj.save()
    context = {
        'updated_object': obj,
    }

    return render(request, 'myapp/update_myapp-list.html', context)

def myappDeleteView(request, pk):
    obj = MyApp.objects.get(pk=pk)
    obj.delete()
    context = {
        'message': '削除が完了しました.',
    }
    return render(request, 'myapp/delete_template.html', context)

def mymail_list(request):
    search_param = request.GET.get('search', '')
    print("search パラメータの値:", search_param)

    search_form = MyMailForm(request.GET)
    objects = MyMail.objects.all()

    if search_form.is_valid() and search_form.cleaned_data['search']:
        search_term = search_form.cleaned_data['search']
        objects = objects.filter(subject__icontains=search_term)

    context = {'object_list': objects, 'search_form': search_form}
    return render(request, 'myapp/mymail_list.html', context)
######
