from django.shortcuts import render
from random import randint  #追加
from django.shortcuts import render, redirect  # redirect を追加
from .models import MyApp
from django.views.generic import TemplateView, ListView
from .models import Person
from django.contrib.auth.decorators import login_required
from .models import MyMail
from .forms import MyMailForm
from django.contrib import messages
# from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse


# myapp/views.py　　



def loggedin_view(request):
    # ログイン後に表示したいコンテンツをコンテキストに追加する
    context = {
        'message': 'ログインしました。ようこそ！',
        # 他のコンテンツを追加
    }
    return render(request, 'loggedin_template.html', context)

# from .models import YourModel

@login_required
def person_list(request):
    data = Person.objects.all()
    return render(request, 'person_list.html', {'data': data})
#
class IndexView(TemplateView):
    template_name = "index.html"

class AboutView(TemplateView):
    template_name = "about.html"  
class PersonListView(ListView):
    model = Person        

def myappDetailView(request, pk):  # pk パラメータを引数として受け取る
    template_name = "myapp/myapp-detail.html"
    
    # ここで pk を使ってデータベースからオブジェクトを取得する
    try:
        myapp = MyApp.objects.get(pk=pk)
    except MyApp.DoesNotExist:
        # オブジェクトが存在しない場合のエラーハンドリングを行うか、適切に処理を行ってください
        myapp = None
    
    ctx = {
        "number": pk,  # pk を number としてテンプレートに渡す
        "object": myapp,
    }
    return render(request, template_name, ctx)

# def myappCreateView(request):
#     template_name = "myapp/myapp-form.html"

#     if request.method == "POST":
#         # POST リクエストが送信された場合の処理
#         title = request.POST.get("title")
#         content = request.POST.get("content")
        
#         # データベースにデータを保存するか、必要な処理を行います
#         obj = MyApp(title=title, content=content)
#         obj.save()
#         # データを保存した後、リダイレクトする例
#         # この場合、リダイレクト先のURLを適切に指定してください
#         return redirect("myapp_form")

#     # GET リクエストの場合はフォームを表示
#     return render(request, template_name)
 ###以下に更新 

def myappCreateView(request):    
    template_name = "myapp/mymail-form.html"

    if request.method == "POST":
        # POST リクエストが送信された場合の処理
        form = MyMailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mymail_form")

    # GET リクエストの場合はフォームを表示
    else:
        form = MyMailForm()

    context = {
        'form': form,
    }

    return render(request, template_name, context)
###

def mymailCreateView(request):
    template_name = "myapp/mymail-form.html"

    if request.method == "POST":
        # POST リクエストが送信された場合の処理
        form = MyMailForm(request.POST)
        if form.is_valid():
            form.save()
            # 成功メッセージを設定
            messages.success(request, 'Form submitted successfully!')
            return redirect("mymail_form")
    else:
        form = MyMailForm()

    context = {
        'form': form,
    }

    return render(request, template_name, context)
##以上に書き換え



####
def myappListView(request):
    template_name = "myapp/myapp_list.html" 
    ctx = {}
    qs = MyApp.objects.all()
    ctx["object_list"] = qs     

    return render(request, template_name, ctx)
    # return render(request, "myapp/update_myapp-list.html", ctx)

##
def myappUpdateListView(request):
    template_name = "myapp/update_myapp-list.html"  # 新しいテンプレートのパスを指定
    ctx = {}
    # ビューに必要なコンテキストを設定
    qs = MyApp.objects.all()
    ctx["object_list"] = qs
    return render(request, template_name, ctx)


# myapp/views.py
def my_view(request):
    # ビューで使用するデータを含む辞書を作成
    context = {
        'key1': 'value1',
        'key2': 'value2',
        # 他のデータを追加
    }

    # テンプレートをレンダリングする際に context を渡す
    return render(request, 'myapp_list.html', context)

# def myappUpdateView(request, pk):
#     # ここで更新の処理を実装
#     # pk パラメータを使って特定のオブジェクトを取得し、更新処理を行う
#     # 更新が完了したら適切なリダイレクト先にリダイレクトするなどの処理を行う
#     # 以下は更新処理が完了した後の例
#     obj = MyApp.objects.get(pk=pk)  # YourModel を実際のモデル MyAppに置き換えてください
#     obj.some_field = 'new_value'  # ここで更新処理を行う
#     obj.save()  # 保存を忘れずに

#     # 更新後のデータをコンテキストに追加
#     context = {
#         'updated_object': obj,
#     }

#     return render(request, 'myapp/update_template.html', context)
###
def myappUpdateView(request, pk):
    # パラメータ pk を使って特定のモデルオブジェクトを取得
    obj = MyApp.objects.get(pk=pk)
    
    # モデルオブジェクトのフィールドを変更
    obj.some_field = 'new_value'
    
    # モデルオブジェクトを保存
    obj.save()
    
    # 更新後のデータをコンテキストに追加
    context = {
        'updated_object': obj,
    }

    return render(request, 'myapp/update_myapp-list.html', context)

###
def myappDeleteView(request, pk):
    # ここで削除の処理を実装
    # pk パラメータを使って特定のオブジェクトを取得し、削除処理を行う
    # 削除が完了したら適切なリダイレクト先にリダイレクトするなどの処理を行う
    # 以下は削除処理が完了した後の例
    obj = MyApp.objects.get(pk=pk)  # YourModel を実際のモデルMyAppに置き換えてください
    obj.delete()  # ここで削除処理を行う

    # 削除後のメッセージをコンテキストに追加
    context = {
        'message': '削除が完了しました。',
    }

    return render(request, 'myapp/delete_template.html', context)
# views.py

## views.py

# def mymail_list(request):
#     # デバッグのためにsearchパラメータの値を取得して表示
#     search_param = request.GET.get('search', '')
#     print("searchパラメータの値:", search_param)

#     search_form = MyMailForm(request.GET)
#     objects = MyMail.objects.all()

#     if search_form.is_valid() and search_form.cleaned_data['search']:
#         search_term = search_form.cleaned_data['search']
#         objects = objects.filter(subject__icontains=search_term)

#     context = {'object_list': objects, 'search_form': search_form}
#     return render(request, 'myapp/mymail_list.html', context)

# def send_email(request):
#     if request.method == 'POST':
#         # POST リクエストを処理
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')
#         sender = request.POST.get('sender')

#         # 実際にメールを送信
#         send_mail(
#             subject,
#             message,
#             sender,
#             ['recipient@example.com'],  # 送信先のメールアドレスを指定
#             fail_silently=False,
#         )

#         # メール送信後、リダイレクトまたは他の処理を行う
#         return HttpResponseRedirect(reverse('mymail_list'))  # リダイレクト先のURLを指定

#     return render(request, 'myapp/mymail_form.html')



# ...

# def mymail_list(request):
#     # デバッグのために search パラメータの値を取得して表示
#     search_param = request.GET.get('search', '')
#     print("search パラメータの値:", search_param)

#     search_form = MyMailForm(request.GET)
#     objects = MyMail.objects.all()

#     if search_form.is_valid() and search_form.cleaned_data['search']:
#         search_term = search_form.cleaned_data['search']
#         objects = objects.filter(subject__icontains=search_term)

#     context = {'object_list': objects, 'search_form': search_form}
#     return render(request, 'myapp/mymail_list.html', context)

# def myappCreateView(request):    
#     template_name = "myapp/mymail-form.html"

#     if request.method == "POST":
#         # POST リクエストが送信された場合の処理
#         form = MyMailForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("mymail_form")

#     # GET リクエストの場合はフォームを表示
#     else:
#         form = MyMailForm()

#     context = {
#         'form': form,
#     }

    #return render(request, template_name, context)


# ユーザーが値を入力できない状態はhttp://127.0.0.1:8000/mymail/list/ここはそれを希望します。がhttp://127.0.0.1:8000/myapp/form/ここでは表示して欲しいのです
# 理解しました。特定のURLでフォームの各フィールドを表示し、他のURLでは非表示にしたい場合、Djangoのビュー関数内でフォームをカスタマイズする方法があります。以下のように、ビューごとにフォームのウィジェットを設定できます。
# myapp/views.py ファイル内で、次のようにフォームのウィジェットを設定。
# ...

def mymail_list(request):
    # デバッグのために search パラメータの値を取得して表示
    search_param = request.GET.get('search', '')
    print("search パラメータの値:", search_param)

    search_form = MyMailForm(request.GET)
    objects = MyMail.objects.all()

    if search_form.is_valid() and search_form.cleaned_data['search']:
        search_term = search_form.cleaned_data['search']
        objects = objects.filter(subject__icontains=search_term)

    context = {'object_list': objects, 'search_form': search_form}
    return render(request, 'myapp/mymail_list.html', context)

def myappCreateView(request):    
    template_name = "myapp/mymail-form.html"

    if request.method == "POST":
        # POST リクエストが送信された場合の処理
        form = MyMailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("mymail_form")

    # GET リクエストの場合はフォームを表示
    else:
        form = MyMailForm()

    context = {
        'form': form,
    }

    return render(request, template_name, context)
