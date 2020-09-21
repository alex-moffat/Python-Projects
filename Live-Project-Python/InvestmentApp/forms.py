from datetime import datetime
from django.forms import ModelForm
from django.forms.widgets import *
from .models import Stock, Trade


# ========== STOCK
class StockForm(ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'
        widgets = {
            'symbol': TextInput(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'category': Select(attrs={'class': 'form-control'}),
            'link': TextInput(attrs={'placeholder': 'optional', 'class': 'form-control', 'type': 'url'}),
            'notes': TextInput(attrs={'placeholder': 'optional', 'class': 'form-control'})
        }


# ========== TRADE
class TradeForm(ModelForm):
    class Meta:
        model = Trade
        fields = '__all__'
        widgets = {
            'stock': Select(attrs={'class': 'form-control'}),
            'open': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'quantity': NumberInput(attrs={'class': 'form-control'}),
            'open_cost': NumberInput(attrs={'class': 'form-control'}),
            'close': DateInput(attrs={'placeholder': 'optional', 'class': 'form-control', 'type': 'date'}),
            'close_cost': NumberInput(attrs={'class': 'form-control'}),
            'paper': CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    # Logic for raising error if close_date < open_date
    def clean(self):
        cleaned_data = super().clean()
        open_date = cleaned_data.get('open')
        close_date = cleaned_data.get('close')
        close_cost = cleaned_data.get('close_cost')
        try:
            if close_date is not None:
                if close_date < open_date:
                    msg = 'Close date should be greater than open date.'
                    self._errors['close'] = self.error_class([msg])
                if close_cost is None:
                    msg = 'Must have a closing cost to close the trade.'
                    self._errors['close_cost'] = self.error_class([msg])
        except ValueError:
            print('Invalid Close date format')
