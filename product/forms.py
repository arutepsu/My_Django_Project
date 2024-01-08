from django import forms
from product.models import Category


class ProductForm(forms.Form):
    title = forms.CharField(
        max_length=50,
        min_length=3,
        label='Product title',
    )
    text = forms.CharField(
        widget=forms.Textarea,
        label='Product description',
        required=False,
    )
    image = forms.CharField(
        required=False,
        label="Product picture",
    )
    rate = forms.IntegerField(
        label="Rate",
        required=False,
    )


class CategoryForm(forms.Form):
    name = forms.CharField(
        max_length=50,
        min_length=3,
        label='Category name',
    )
    text = forms.CharField(
        required=False,
        label="Category description"
    )


class ReviewForm(forms.Form):
    text = forms.CharField(
        max_length=50,
        min_length=3,
        label='Product review',
    )
