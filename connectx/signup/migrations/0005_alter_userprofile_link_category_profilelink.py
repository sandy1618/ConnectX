# Generated by Django 4.1.7 on 2023-05-17 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_alter_userprofile_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='link_category',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.CreateModel(
            name='ProfileLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_category', models.CharField(max_length=100, null=True)),
                ('link', models.URLField(null=True)),
                ('user_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profile_links', to='signup.userprofile')),
            ],
        ),
    ]
