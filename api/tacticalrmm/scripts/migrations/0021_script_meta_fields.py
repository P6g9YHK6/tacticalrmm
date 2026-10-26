import secrets
import string

from django.db import migrations, models


def _generate_script_id() -> str:
    return "".join(
        secrets.choice(string.ascii_lowercase + string.digits)
        for _ in range(10)
    )


def backfill_script_ids(apps, schema_editor):
    Script = apps.get_model("scripts", "Script")
    for script in Script.objects.filter(script_id__isnull=True):
        sid = _generate_script_id()
        while Script.objects.filter(script_id=sid).exists():
            sid = _generate_script_id()
        script.script_id = sid
        script.save(update_fields=["script_id"])


class Migration(migrations.Migration):

    dependencies = [
        ("scripts", "0020_alter_script_shell_alter_scriptsnippet_shell"),
    ]

    operations = [
        migrations.AddField(
            model_name="script",
            name="script_id",
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
        migrations.AddField(
            model_name="script",
            name="version",
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.RunPython(backfill_script_ids),
        migrations.AlterField(
            model_name="script",
            name="script_id",
            field=models.CharField(max_length=10, unique=True, blank=True),
        ),
    ]
