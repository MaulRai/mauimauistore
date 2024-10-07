from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "rating", "stock", "desc", "image"]
        
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'border border-gray-300 rounded-lg p-2 w-full mb-1' 
            })
            
    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_desc(self):
        desc = self.cleaned_data["desc"]
        return strip_tags(desc)