# Generated by Django 2.2.1 on 2019-05-06 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("brutaldon", "0021_client_version")]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="version",
            field=models.CharField(default="1.0", max_length=80),
        )
    ]
