from django.urls import path
from django.contrib import admin
from .views import myappListView, myappDetailView, myappCreateView, IndexView, AboutView, PersonListView, mymailCreateView, myappUpdateListView, mymail_list #, #send_email
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', IndexView.as_view()),  
    path('about/', AboutView.as_view()),
    path("myapp/", views.myappListView, name="myapp-list"),
    path("detail/<int:pk>/", myappDetailView, name="myapp-detail"),
    path('person_list/', login_required(views.PersonListView.as_view()), name='person_list'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('loggedin/', views.loggedin_view, name='loggedin_view'),
    path('myapp/form/', views.myappCreateView, name='myapp_form'),
    path('mymail/form/', views.mymailCreateView, name='mymail_form'),
    path('myapp/update/<int:pk>/', views.myappUpdateView, name='myapp-update'),
    path('mymail/list/', views.mymail_list, name='mymail_list'),
    # path('mymail/send/', views.send_email, name='send_email'),  # この行を修正
]




# from django.urls import path
# from django.contrib import admin
# # from .views import myappListView, myappDetailView, myappCreateView, IndexView, AboutView, PersonListView # 追加  #ポイント1
# from .views import myappListView, myappDetailView, myappCreateView, IndexView, AboutView, PersonListView, mymailCreateView, myappUpdateListView, mymail_list, send_email  #新しいビューを作成毎に
# from . import views
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.views import LogoutView
# from django.contrib.auth.decorators import login_required


# # urlpatterns = [
# #     path("", myappListView), #ポイント2
# #     path("detail/<int:number>/", myappDetailView), # 追加
# #     path('form/', views.myappCreateView, name='myapp_form'),
    
# # ]
# urlpatterns = [
#     path('', IndexView.as_view()),  
#     path('about/', AboutView.as_view()),
#     path("myapp/", views.myappListView, name="myapp-list"),
#     path("detail/<int:pk>/", myappDetailView, name="myapp-detail"),
#     path('person_list/', login_required(views.PersonListView.as_view()), name='person_list'),
#     path('login/', LoginView.as_view(), name='login'),
#     path('logout/', LogoutView.as_view(), name='logout'),
#     path('loggedin/', views.loggedin_view, name='loggedin_view'),
#     path('person_list/', views.person_list, name='person_list'),  # ダブりを削除
#     path('myapp/form/', views.myappCreateView, name='myapp_form'),
#     path('mymail/form/', views.mymailCreateView, name='mymail_form'),
#     path('myapp/update/<int:pk>/', views.myappUpdateView, name='myapp-update'),
#     path('mymail/list/', views.mymail_list, name='mymail_list'),
#     path('mymail/form/', views.send_email, name='send_email'),
#  ] 


#     # path('myapp_admin/', admin.site.urls),
#     # path('myapp/update/<int:pk>/', views.myappUpdateView, name='myapp-update'),
    


#     # path('myapp/delete/<int:pk>/', views.myappDeleteView, name='myapp-delete'),
#     # path('myapp/list/', views.myappListView, name='myapp-list'),  # URLパターンとビューを関連付ける
#     # path("myapp/detail/<int:pk>/", myappDetailView, name="myapp-detail")
  
#     # path("myapp/update-list/", views.myappUpdateListView, name="myapp-update-list"),



# # urls.py






# # urlpatterns = [いらない
# #   path('', IndexView.as_view()),  
# #   path('about/', AboutView.as_view()),
# #   path("myapp/", myappListView, name="myapp-list"),
# #   # path("detail/<int:number>/", myappDetailView, name="myapp-detail"),#書直13行に
# #   path("detail/<int:pk>/", myappDetailView, name="myapp-detail"),
# #   path('person_list/', views.PersonListView.as_view(), name='person_list'),
# #   path('login/', LoginView.as_view(), name='login'),
# #   path('logout/', LogoutView.as_view(), name='logout'),
# #   path('loggedin/', views.loggedin_view, name='loggedin_view'),
# #   path('person_list/', login_required(views.PersonListView.as_view()), name='person_list'),
# #   path('person_list/', views.person_list, name='person_list'),  
# # #   path('form/', views.myappCreateView, name='myapp_form'),
# #   path('myapp/form/', views.myappCreateView, name='myapp_form'),
# # ]





