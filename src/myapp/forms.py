
from django import forms
from .models import MyMail
from django import forms


class MyMailForm(forms.ModelForm):
    class Meta:
        model = MyMail
        fields = ['subject', 'message', 'sender']

    # 各フィールドのラベルを非表示にする
    subject = forms.CharField(label='', required=True)
    message = forms.CharField(label='', required=True, widget=forms.Textarea)
    sender = forms.EmailField(label='', required=True)



class MyMailForm(forms.ModelForm):
    # 新しい検索フィールドを追加
    search = forms.CharField(max_length=100, required=False, label='検索')

    class Meta:
        model = MyMail
        fields = ['subject', 'message', 'sender', 'search']

# # class MyMailForm(forms.ModelForm):
# #     # 既存のフィールド
# #     subject = forms.CharField(max_length=100)
# #     message = forms.CharField(widget=forms.Textarea)
# #     sender = forms.EmailField()

# #     # 新しい検索フィールドを追加
# #     search = forms.CharField(max_length=100, required=False, label='検索')

# #     class Meta:
# #         model = MyMail
# #         fields = ['subject', 'message', 'sender', 'search']



# # from django import forms
# # from .models import MyMail

# # class MyMailForm(forms.ModelForm):
# #     class Meta:
# #         model = MyMail
# #         fields = ['subject', 'message', 'sender']



###メイルフォームを隠す
# from django import forms
# from .models import MyMail

# class MyMailForm(forms.ModelForm):
#     # 新しい検索フィールドを追加
#     search = forms.CharField(max_length=100, required=False, label='検索')

#     class Meta:
#         model = MyMail
#         fields = ['subject', 'message', 'sender', 'search']

#     # フォームの各フィールドのウィジェットをカスタマイズ
#     subject = forms.CharField(
#         label='',
#         required=True,
#         widget=forms.TextInput(attrs={'style': 'display: none;'}),
#     )
#     message = forms.CharField(
#         label='',
#         required=True,
#         widget=forms.Textarea(attrs={'style': 'display: none;'}),
#     )
#     sender = forms.EmailField(
#         label='',
#         required=True,
#         widget=forms.EmailInput(attrs={'style': 'display: none;'}),
#     )

