# Generated by Django 3.1.4 on 2020-12-21 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_type', models.CharField(choices=[('HP-ProBook', 'HP-ProBook'), ('HP-Compaq', 'HP-Compaq'), ('HP-Elitebook', 'HP-Elitebook'), ('Asus-N46VM', 'Asus-N46VM'), ('Lenovo-Thinkpad', 'Lenovo-Thinkpad')], max_length=20)),
                ('serial_number', models.CharField(max_length=50)),
                ('processor', models.CharField(choices=[('I3', 'I3'), ('I5', 'I5'), ('I7', 'I7')], max_length=2)),
                ('ram', models.CharField(choices=[('4GB', '4GB'), ('6GB', '6GB'), ('8GB', '8GB'), ('12GB', '12GB'), ('16GB', '16GB')], max_length=4)),
                ('storage_type', models.CharField(choices=[('HDD', 'HDD'), ('SSD', 'SSD')], max_length=4)),
                ('storage_model', models.CharField(choices=[('Hitachi (HGST)', 'Hitachi (HGST)'), ('WD (Westernd Digital)', 'WD (Westernd Digital)'), ('Seagate', 'Seagate'), ('Toshiba', 'Toshiba'), ('OCZ Vertex', 'OCZ Vertex'), ('Samsung 860 Vevo', 'Samsung 860 Vevo')], max_length=21)),
                ('sotrage_capacity', models.PositiveIntegerField()),
                ('dvd_cd_exists', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
