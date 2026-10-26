from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_coresettings_ssh_gateway_enable_file_transfer'),
    ]

    operations = [
        migrations.AddField(
            model_name='coresettings',
            name='enable_swagger',
            field=models.BooleanField(default=False),
        ),
    ]
