# Generated by Django 4.2.7 on 2023-11-26 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("report", "0002_remove_report_activated_remove_report_archived_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="report",
            options={
                "ordering": ["created_at"],
                "verbose_name": "Report",
                "verbose_name_plural": "Reports",
            },
        ),
    ]
