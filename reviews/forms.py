from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """ 
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'product': 'Select Product',
            'review': 'Write your review here',
         }

        self.fields['product'].widget.attrs['autofocus'] = True

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'