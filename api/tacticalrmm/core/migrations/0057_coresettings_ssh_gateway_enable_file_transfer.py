from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0056_ssh_gateway_rate_limit_max_entries'),
    ]

    operations = [
        migrations.AddField(
            model_name='coresettings',
            name='ssh_gateway_enable_file_transfer',
            field=models.BooleanField(default=True),
        ),
    ]
