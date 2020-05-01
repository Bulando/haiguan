import django_tables2 as tables
from .models import Datax, Dataxx


def data_tag(**kwargs):
    tag = kwargs.get("value", None)
    if tag == 1:
        return "#FF0000"
    else:
        return "#00FF00"


class DataxTable(tables.Table):
    tag = tables.Column(attrs={"td": {"bgcolor": data_tag}})

    class Meta:
        model = Datax
        template_name = "django_tables2/bootstrap.html"
        fields = ("customs_id", "product_number", "product_id", "product_name", "guige", "tag",)
