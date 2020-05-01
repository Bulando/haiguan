import django_tables2 as tables
from .models import Datax

class DataxTable(tables.Table):
    class Meta:
        model = Datax
        template_name = "django_tables2/bootstrap.html"
        fields = ("customs_id", "product_number", "product_id", "product_name", "guige", )
