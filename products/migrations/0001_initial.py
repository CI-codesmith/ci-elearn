from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=128, unique=True)),
                ("slug", models.SlugField(blank=True, max_length=160, unique=True)),
            ],
            options={"ordering": ["name"]},
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(db_index=True, max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField(blank=True)),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="products",
                        to="products.category",
                        db_index=True,
                    ),
                ),
            ],
            options={"ordering": ["-created"]},
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["name", "category"], name="products_na_name_c545fb_idx"),
        ),
        migrations.AddIndex(
            model_name="product",
            index=models.Index(fields=["category", "-created"], name="products_ca_cate_3b78d9_idx"),
        ),
    ]

