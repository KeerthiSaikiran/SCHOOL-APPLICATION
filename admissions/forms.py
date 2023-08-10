from django import forms

from admissions.models import Student


class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class VendorForm(forms.Form):
    vendor_name = forms.CharField()
    item = forms.CharField()
    number_of_items = forms.IntegerField()
    contact_details = forms.CharField()



