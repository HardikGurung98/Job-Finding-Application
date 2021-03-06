from django import forms
from django.forms import ModelForm
from jobs.models import JobPost
from account.models import(JOB_CATEGORY_CHOICES, EDUCATION_CHOICES)
from jobs.models import (LOCATION_CHOOSE, WORKING_SHIFTS, Job_Level_Choices,
                        JOB_AVALIABLE_TIME, Gender)

from django.contrib.admin import widgets



class job_post_form(forms.ModelForm):
    JobTitle = forms.CharField(widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder': 'Graphic Designer, Web Developer'}
    ), max_length=500,  required=True)
    Location = forms.ChoiceField(choices=LOCATION_CHOOSE, required=True)
    NumberOfVacancies = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Number Of Vacancies'}
        ), min_value=0, required=False)

    SalaryStart = forms.FloatField(widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder': 'Salary start with in rs'}
    ), min_value=0, required=False)

    EndSalary = forms.FloatField(widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder': 'Salary end with in rs'}
    ), min_value=0, required=False)

    JobLevel = forms.ChoiceField(choices=Job_Level_Choices, required=False)
    AvaliableTime = forms.ChoiceField(choices=JOB_AVALIABLE_TIME, required=False)
    JobShift = forms.ChoiceField(choices=WORKING_SHIFTS, required=False)
    RequiredEducation = forms.ChoiceField(choices=EDUCATION_CHOICES, required=False)
    RequiredExperience = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'required experince for thus job'}
    ), min_value=0, required=False)
    JobCategory = forms.ChoiceField(choices=JOB_CATEGORY_CHOICES, required=True)
    Gender = forms.ChoiceField(choices=Gender, required=False)

    HiringBanner = forms.ImageField(required=False)

    JobExpiryDate = forms.DateTimeField( help_text= 'Note* format YY-MM-DD H:M:S', input_formats=['%Y-%m-%d %H:%M:%S']) 






    class Meta():
        model = JobPost
        fields = ['JobTitle','Location', 'NumberOfVacancies', 'SalaryStart', 
                    'EndSalary', 'JobLevel', 'AvaliableTime', 'RequiredSkill', 
                    'JobShift', 'RequiredEducation', 'RequiredExperience', 'JobCategory', 
                    'Gender', 'JobDescreptions', 'HiringBanner', 'JobExpiryDate']


    # def __init__(self, *args, **kwargs):
    #     super(job_post_form, self).__init__(*args, **kwargs)
    #     self.fields['JobExpiryDate'].widget = widgets.AdminSplitDateTime()


    


    


    
