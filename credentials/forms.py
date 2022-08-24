from django.forms import ModelForm
from django import forms
from .models import District,Branch,Registration

class Addform(forms.ModelForm):
    Gender = [('male', 'male'), ('female', 'female')]
    gender=forms.ChoiceField(choices=Gender,widget=forms.RadioSelect())
    debitcard=forms.BooleanField(required = False)
    creditcard=forms.BooleanField(required = False)
    passbook=forms.BooleanField(required = False)
    mail_id=forms.EmailField()
    DOB=forms.DateField()
    class Meta:
        model= Registration
        fields=('name','DOB','gender','phonenumber','mail_id','address1','address2','address3','district','branch','account','debitcard','creditcard','passbook')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = Branch.objects.none()

        if 'district' in self.data:
            try:
                district_id = int(self.data.get('district'))
                self.fields['branch'].queryset = Branch.objects.filter(district_id=district_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['branch'].queryset = self.instance.district.branch_set.order_by('name')

