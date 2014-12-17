from django import forms
from order.models import Order

# TODO: Load from DB.
PACKAGES_CHOICES = (('1', 'Package 1'),
                    ('2', 'Package 2'),
                    ('3', 'Package 3'))

class OrderForm1(forms.Form):
    package = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=PACKAGES_CHOICES)

class OrderForm2(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['photo','message']

class OrderForm3(forms.Form):
    payment = forms.CharField()