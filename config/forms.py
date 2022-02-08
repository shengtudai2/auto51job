from django import forms

class userConfig(forms.Form):
    noti = (
        (True, "是"),
        (False, "否"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}), disabled=True, required=False)
    openId = forms.CharField(label="openId", max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    token = forms.CharField(label="token", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    notify = forms.ChoiceField(label="qq通知", choices=noti)
    qq = forms.CharField(label="qq号", max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))



