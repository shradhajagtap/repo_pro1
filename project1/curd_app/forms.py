from django import forms
from .models import SchoolTeacher


class SchoolTeacherForm(forms.ModelForm):
    class Meta:
        model = SchoolTeacher
        fields = "__all__"

        widgets = {
            "teacher_school_name": forms.TextInput(attrs={"class": "form-control"}),
            "teacher_name": forms.TextInput(attrs={"class": "form-control"}),
            "school_location": forms.TextInput(attrs={"class": "form-control"}),
            "teaching_experience": forms.NumberInput(),
            "teacher_age": forms.NumberInput(),
            "teacher_address": forms.Textarea()
        }
