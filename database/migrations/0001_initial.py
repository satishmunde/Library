# Generated by Django 4.2.5 on 2023-09-14 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('average_rating', models.CharField(max_length=4)),
                ('isbn', models.CharField(max_length=13)),
                ('isbn13', models.CharField(max_length=13)),
                ('language_code', models.CharField(max_length=10)),
                ('num_pages', models.CharField(max_length=5)),
                ('ratings_count', models.CharField(max_length=5)),
                ('text_reviews_count', models.CharField(max_length=5)),
                ('publication_date', models.DateField()),
                ('publisher', models.CharField(max_length=255)),
                ('quantity_in_stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LibraryMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memid', models.CharField(max_length=200)),
                ('outstanding_debt', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='LibraryTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.CharField(max_length=10)),
                ('member', models.CharField(max_length=200)),
                ('issue_date', models.DateField()),
                ('return_date', models.DateField()),
                ('fee', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]