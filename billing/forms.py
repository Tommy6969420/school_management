from django.forms import ModelForm
from.models import Billing, ClassBills
class BillingForm(ModelForm):
     class Meta:
         model=Billing
         fields="__all__"
class ClassBillsForm(ModelForm):
     class Meta:
          model=ClassBills
          fields="__all__"

