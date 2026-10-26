from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0045_add_ssh_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='can_ssh_file_transfer',
            field=models.BooleanField(default=False),
        ),
    ]
