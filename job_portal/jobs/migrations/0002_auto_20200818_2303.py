# Generated by Django 3.0.9 on 2020-08-18 17:18

from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpost',
            name='AvaliableTime',
            field=models.CharField(choices=[('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Work From Home', 'Work From Home'), ('Part/Full Time', 'Part/Full Time'), ('Full/Work From Home Time', 'Full/Work From Home Time'), ('Work From Home/Part Time', 'Work From Home/Part Time'), ('Work From Home/Full Time', 'Work From Home/Full Time')], max_length=200, null=True, verbose_name='Avaliable Time'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='EndSalary',
            field=models.FloatField(default=0.0, null=True, verbose_name='Salary End With'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='Gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Both', 'Both')], default='Both', max_length=50, null=True, verbose_name='Required Gender'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='HiringBanner',
            field=models.ImageField(default='DefaultHireBanner.jpg', null=True, upload_to='Employer/Hire Banners', verbose_name='Hiring Banner'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='JobLevel',
            field=models.CharField(choices=[('Internship Level', 'Internship Level'), ('Entry Lavel', 'Entry Level'), ('Intermidate Lavel', 'Intermidate Lavel'), ('Expert Level', 'Expert Level'), ('Internship/Entry Level', 'Internship/Entry Level'), ('Entry/Intermidate Lavel', 'Entry/Intermidate Level'), ('Intermidate/Expert Lavel', 'Intermidate/Expert Lavel'), ('Expert/Entry Level', 'Expert/Entry Level')], max_length=200, null=True, verbose_name='Job Level'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='JobPostDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='JobShift',
            field=models.CharField(choices=[('Day', 'Day'), ('Night', 'Night'), ('Morning', 'Morning'), ('Evening', 'Evening'), ('Morning/Day', 'Morning/Day'), ('Evening/Night', 'Evening/Night')], max_length=100, null=True, verbose_name='Job Shift'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='NumberOfVacancies',
            field=models.IntegerField(default=0, null=True, verbose_name='Number Of Vancies'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='RequiredEducation',
            field=models.CharField(choices=[('Intermidate Level Complete', 'Intermidate Level Complete'), ('Bacholer Running/Complete', 'Bacholer Running/Complete'), ('Master Running/Complete', 'Master Running/Complete'), ('Ph. D. Running/Complete', 'Ph. D. Running/Complete'), ('OTHER', 'OTHER')], max_length=200, null=True, verbose_name='Required Educations'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='RequiredExperience',
            field=models.IntegerField(default=0, null=True, verbose_name='Required Experience'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='RequiredSkill',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Required Skills'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='SalaryStart',
            field=models.FloatField(default=0.0, null=True, verbose_name='Salary Start With'),
        ),
    ]
