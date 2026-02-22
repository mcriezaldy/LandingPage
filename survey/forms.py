from django import forms
from .models import Survey

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name',
                  'email',
                  'age',
                  'satisfaction',
                  'feedback',
                  'agree_law',
                  'agree_parent',
                  'agree_ethics',]

    def clean(self):
        cleaned_data = super().clean()

        if not cleaned_data.get("agree_law"):
            self.add_error("agree_law", "Anda harus menyetujui peraturan.")

        if not cleaned_data.get("agree_parent"):
            self.add_error("agree_parent", "Anda harus menyetujui ketentuan usia.")

        if not cleaned_data.get("agree_ethics"):
            self.add_error("agree_ethics", "Anda harus menyetujui etika penggunaan.")

        return cleaned_data