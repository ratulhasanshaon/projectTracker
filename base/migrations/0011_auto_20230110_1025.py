# Generated by Django 3.2.9 on 2023-01-10 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_auto_20211026_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_due_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_status',
            field=models.CharField(blank=True, choices=[('1', 'Pending'), ('2', 'Active'), ('3', 'Waiting'), ('4', 'Completed')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_due_date',
            field=models.DateField(null=True),
        ),
    ]
