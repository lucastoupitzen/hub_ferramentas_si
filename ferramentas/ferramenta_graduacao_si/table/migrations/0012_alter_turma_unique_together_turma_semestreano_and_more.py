# Generated by Django 4.1.6 on 2023-10-06 03:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("table", "0011_alter_restricao_semestre"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="turma",
            unique_together=set(),
        ),
        migrations.AddField(
            model_name="turma",
            name="SemestreAno",
            field=models.CharField(
                choices=[("P", "par"), ("I", "impar")], default="P", max_length=1
            ),
        ),
        migrations.AlterUniqueTogether(
            name="turma",
            unique_together={("Ano", "CodTurma", "CoDisc", "SemestreAno")},
        ),
    ]
