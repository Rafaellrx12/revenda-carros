from django import forms
from cars.models import Car



class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = "__all__"

    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error("factory_year","O ano de fabricação deve ser acima de 1974")
        return factory_year
