# Generated by Django 4.1.6 on 2023-02-17 22:32

from django.db import migrations
from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType

def createGroups(apps, schema_editor):
    contentType = ContentType.objects.get_for_model(User)
    groups = ["User", "Employee", "Manager"]
    for groupName in groups:
        permission = Permission.objects.create(codename=groupName, name=groupName, content_type= contentType)
        newGroup =   Group.objectscreate(name=groupName)
        newGroup.permissions.add(permission)

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(createGroups),
    ]
