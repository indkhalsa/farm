from django import forms
from assist.models import Item, Good, ItemDetail, GoodDetail


class GoodDetailForm(forms.ModelForm):
    sold_by = forms.CharField(max_length=40, help_text="Please enter your name.")
    sel_date = forms.DateField(help_text="Date Sold")
    bitPkw = forms.IntegerField(help_text="Please enter the Bit rate pre Kw")
    weight = forms.IntegerField(help_text="Please enter the Total Weight in Kw")
    total = forms.IntegerField(help_text="Please enter the Total Ammount")

    class Meta:
	model = GoodDetail

	fields = ('sold_by', 'sel_date', 'bitPkw', 'weight', 'total')


class ItemDetailForm(forms.ModelForm):
    pur_by = forms.CharField(max_length=40, help_text="Please enter your Name.")
    pur_date = forms.DateField(help_text="Date Purchased")
    price = forms.IntegerField(help_text="Please enter the Price")

    class Meta:
	model = ItemDetail
	
	fields = ('pur_by', 'pur_date', 'price')

