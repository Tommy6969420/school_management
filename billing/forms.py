from django import forms
from.models import Billing, ClassBills,Months


class BillingForm(forms.ModelForm):
     # months = forms.MultipleChoiceField(choices=)
     class Meta:
         model=Billing
         fields="__all__"
class ClassBillsForm(forms.ModelForm):
     class Meta:
          model=ClassBills
          fields="__all__"

