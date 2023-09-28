from django.db import models

class MyApp(models.Model):
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f"{self.title} - {self.content}"  
    # 表題の表示　 この場合titleとcontentが表示される

    # def __str__(self): #add code
    #     return self.content
# class MyApp(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.CharField(max_length=1000)
#     number = models.IntegerField()  # number フィールドを追加

#     timestamp = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title





class Person(models.Model):
    class Meta:
        db_table = 'person'

    name = models.CharField(verbose_name='名前', max_length=255)
    age = models.IntegerField(verbose_name='年齢')
    email = models.EmailField(verbose_name='メール', default='')
    phone = models.CharField(verbose_name='電話', max_length=20, default='')
    address = models.CharField(verbose_name='住所', max_length=255, default='')

    def __str__(self):
        ret = str(self.name) + '(' + str(self.age) + '才)'
        return ret



class MyMail(models.Model):  # MyMail という名前のモデルを作成する
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sender = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

# from django.db import models

# class Person(models.Model):      # 人物モデル
#     class Meta:
#         db_table = 'person'

#     name = models.CharField(verbose_name='名前', max_length=255)
#     age = models.IntegerField(verbose_name='年齢')

#     def __str__(self):
#         ret = str(self.name) + '(' + str(self.age) + '才)'
#         return ret
    

# データベースのテーブルに該当する、modelの中身を定義します。
# ここでは極力シンプルな「人物」モデルを作成しました。
    # def __str__(self):
    #     return "付けたい名前"

# Create your models here.
# from django.db import models

# class MyModel(models.Model):
#     field1 = models.CharField(max_length=100)
#     field2 = models.IntegerField()

#     def __str__(self):
#         return self.field1  # ここでオブジェクトがどのように表示されるかを定義
