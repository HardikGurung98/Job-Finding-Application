# Generated by Django 3.0.9 on 2020-08-18 16:58

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('JobTitle', models.CharField(max_length=500, verbose_name='Job Title')),
                ('Location', models.CharField(choices=[('Kathmandu', 'Kathmandu'), ('Bhaktaput', 'Bhaktaput'), ('Lalitpur', 'Lalitpur'), ('Dhading', 'Dhading'), ('Nuwakot', 'Nuwakot'), ('Kavre', 'Kavre'), ('Pokhara', 'Pokhara'), ('Mahottari', 'Mahottari'), ('Achham', 'Achham'), ('Baglung', 'Baglung'), ('Baghang', 'Baghang'), ('Bajura', 'Bajura'), ('Bake', 'Bake'), ('Bara', 'Bara'), ('Surkhet', 'Surkhet'), ('Dhangadhi', 'Dhangadhi'), ('Biratnagar', 'Biratnagar'), ('Nepaljung', 'Nepaljung'), ('Parsha', 'Parsha'), ('Palpa', 'Palpa'), ('Ilam', 'Ilam'), ('Jhapa', 'JJhapa'), ('RajBiraj', 'RajBiraj'), ('Janakpur', 'Janakpur'), ('Rashuwa', 'Rashwa'), ('Gorkha', 'Gorkha'), ('Manang/Mustang', 'Manang/Mustang'), ('Humla', 'Humla'), ('Jumla', 'Jumla'), ('Karnali', 'Karnali'), ('Mugu', 'Mugu')], max_length=200)),
                ('NumberOfVacancies', models.IntegerField(blank=True, default=0, null=True, verbose_name='Number Of Vancies')),
                ('SalaryStart', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Salary Start With')),
                ('EndSalary', models.FloatField(blank=True, default=0.0, null=True, verbose_name='Salary End With')),
                ('JobLevel', models.CharField(blank=True, choices=[('Internship Level', 'Internship Level'), ('Entry Lavel', 'Entry Level'), ('Intermidate Lavel', 'Intermidate Lavel'), ('Expert Level', 'Expert Level'), ('Internship/Entry Level', 'Internship/Entry Level'), ('Entry/Intermidate Lavel', 'Entry/Intermidate Level'), ('Intermidate/Expert Lavel', 'Intermidate/Expert Lavel'), ('Expert/Entry Level', 'Expert/Entry Level')], max_length=200, null=True, verbose_name='Job Level')),
                ('AvaliableTime', models.CharField(blank=True, choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Work From Home', 'Work From Home'), ('Part/Full Time', 'Part/Full Time'), ('Full/Work From Home Time', 'Full/Work From Home Time'), ('Work From Home/Part Time', 'Work From Home/Part Time'), ('Work From Home/Full Time', 'Work From Home/Full Time')], max_length=200, null=True, verbose_name='Avaliable Time')),
                ('JobShift', models.CharField(blank=True, choices=[('Day', 'Day'), ('Night', 'Night'), ('Morning', 'Morning'), ('Evening', 'Evening'), ('Morning/Day', 'Morning/Day'), ('Evening/Night', 'Evening/Night')], max_length=100, null=True, verbose_name='Job Shift')),
                ('RequiredEducation', models.CharField(blank=True, choices=[('Intermidate Level Complete', 'Intermidate Level Complete'), ('Bacholer Running/Complete', 'Bacholer Running/Complete'), ('Master Running/Complete', 'Master Running/Complete'), ('Ph. D. Running/Complete', 'Ph. D. Running/Complete'), ('OTHER', 'OTHER')], max_length=200, null=True, verbose_name='Required Educations')),
                ('RequiredExperience', models.IntegerField(blank=True, default=0, null=True, verbose_name='Required Experience')),
                ('JobCategory', models.CharField(choices=[('Architecture/Interior Designing', 'Architecture/Interior Designing'), ('Construction/Engineering', 'Construction/Engineering'), ('Commercial/Logistics', 'Commercial/Logistics'), ('Creative/Graphic/Designing', 'Creative/Graphic/Designing'), ('Hospilaty', 'Hospilaty'), ('NGO/INGO/Social Work', 'NGO/INGO/Social Work'), ('Techng/Education', 'Techng/Education'), ('General MGMT./Administration/Operations', 'General MGMT./Administration/Operations'), ('Healthcare/Pharma/Biotech/Medical', 'Healthcare/Pharma/Biotech/Medical'), ('Human Resources/ Org.Development', 'Human Resources/ Org.Development'), ('Sales/Public Relations', 'Sales/Public Relations'), ('Research and Development', 'Research and Development'), ('Production/Maintenance/Quality', 'Production/Maintenance/Quality'), ('Marketing/Advertisement/Custom service', 'Marketing/Advertisement/Custom service'), ('Legal Services', 'Legal Services'), ('Accounting/Finance', 'Accounting/Finance'), ('Banking/Insurance/Finance Services', 'Banking/Insurance/Finance Services'), ('Fashion/Textile Designing', 'Fashion/Textile Designing'), ('Secretarial/Front Office/Data Entry', 'Secretarial/Front Office/Data Entry'), ('IT & Telecommunication', 'IT & Telecommunication'), ('Productive/Securaty Service', 'Productive/Securaty Service'), ('Journalism/Editor/Media', 'Journalism/Editor/Media'), ('Others', 'Others')], max_length=200, verbose_name='Job Category')),
                ('Gender', models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('Both', 'Both')], default='Both', max_length=50, null=True, verbose_name='Required Gender')),
                ('JobDescreptions', ckeditor.fields.RichTextField(verbose_name='Job Descriptions')),
                ('HiringBanner', models.ImageField(blank=True, default='DefaultHireBanner.jpg', null=True, upload_to='Employer/Hire Banners', verbose_name='Hiring Banner')),
                ('JobPostDate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('JobExpiryDate', models.DateTimeField()),
                ('RequiredSkill', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Required Skills')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
