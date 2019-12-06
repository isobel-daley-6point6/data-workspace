# Generated by Django 2.2.4 on 2019-12-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [('datasets', '0024_auto_20191118_1349')]

    operations = [
        migrations.CreateModel(
            name='DataCutDataset',
            fields=[],
            options={
                'verbose_name': 'Data Cut Dataset',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('datasets.dataset',),
        ),
        migrations.CreateModel(
            name='MasterDataset',
            fields=[],
            options={
                'verbose_name': 'Master Dataset',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('datasets.dataset',),
        ),
        migrations.AddField(
            model_name='dataset',
            name='type',
            field=models.IntegerField(
                choices=[(1, 'Master Dataset'), (2, 'Data Cut')], default=2
            ),
        ),
        migrations.CreateModel(
            name='DataCutDatasetUserPermission',
            fields=[],
            options={'proxy': True, 'indexes': [], 'constraints': []},
            bases=('datasets.datasetuserpermission',),
        ),
        migrations.CreateModel(
            name='MasterDatasetUserPermission',
            fields=[],
            options={'proxy': True, 'indexes': [], 'constraints': []},
            bases=('datasets.datasetuserpermission',),
        ),
        migrations.RemoveField(model_name='dataset', name='redactions'),
        migrations.RemoveField(model_name='dataset', name='volume'),
        migrations.AddField(
            model_name='sourcetable',
            name='frequency',
            field=models.IntegerField(
                choices=[
                    (1, 'Daily'),
                    (2, 'Weekly'),
                    (3, 'Monthly'),
                    (4, 'Quarterly'),
                    (5, 'Annually'),
                ],
                default=1,
            ),
        ),
        migrations.AddField(
            model_name='sourceview',
            name='frequency',
            field=models.IntegerField(
                choices=[
                    (1, 'Daily'),
                    (2, 'Weekly'),
                    (3, 'Monthly'),
                    (4, 'Quarterly'),
                    (5, 'Annually'),
                ],
                default=1,
            ),
        ),
    ]
