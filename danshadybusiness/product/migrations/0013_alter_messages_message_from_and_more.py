# Generated by Django 4.1.1 on 2023-04-25 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_messages_message_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='message_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_from', to='product.customuser'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='message_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='message_to', to='product.customuser'),
        ),
    ]
