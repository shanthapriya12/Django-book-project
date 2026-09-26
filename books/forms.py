from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price','category', 'cover']

    def clean_price(self):
        price = self.cleaned_data['price']

        if price < 0:
            raise forms.ValidationError("Price cannot be negative.")

        return price