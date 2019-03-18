# Generated by Django 2.1.7 on 2019-03-18 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('role', models.IntegerField(choices=[(1, 'Learner'), (1000, 'Instructional Assistant'), (2000, 'Grad Student Instructor'), (5000, 'Instructor'), (10000, 'Administrator')], default=1)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='many.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=128, unique=True)),
                ('name', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='many.Person'),
        ),
        migrations.AddField(
            model_name='course',
            name='members',
            field=models.ManyToManyField(related_name='courses', through='many.Membership', to='many.Person'),
        ),
    ]
