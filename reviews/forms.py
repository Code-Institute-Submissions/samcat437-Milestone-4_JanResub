from django import forms
from .models import Reviews


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Reviews
        fields = ('review',)

    def __init__(self, *args, **kwargs):
        """ 
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
