from django.contrib import admin
from .models import MyApp, Person, MyMail  #追記




# admin.site.register(MyApp) #追記 Adminページへ再度アクセスして,新しくMyAppが追加確認





class MyAppAdmin(admin.ModelAdmin):  #add 
    list_display = ('title', 'timestamp')  # 'title'と'timestamp'を表示

admin.site.register(MyApp, MyAppAdmin)
admin.site.register(Person)
admin.site.register(MyMail)

# Register your models here.
