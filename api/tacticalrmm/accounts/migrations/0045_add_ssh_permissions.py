from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0044_alter_sshpublickey_id_alter_sshsession_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='can_ssh_open_terminal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='role',
            name='can_ssh_send_commands',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='role',
            name='can_ssh_use_functions',
            field=models.BooleanField(default=False),
        ),
    ]
