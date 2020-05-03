import django_tables2 as tables
from .models import Datax, Dataxx
from django_tables2.utils import A


def data_tag(**kwargs):
    tag = kwargs.get("value", None)
    if tag == 1:
        return "#FF0000"
    else:
        return "#00FF00"


class DataxTable(tables.Table):
    tag = tables.Column(attrs={"td": {"bgcolor": data_tag}}, verbose_name="风险税率"
                        )
    # linkify = {"viewname": "datax_chakan", "args": [tables.A("pk")]}
    # product_name = tables.LinkColumn('testapp:datax_chakan', args=[A('pk')], verbose_name="查看")
    chakan = tables.TemplateColumn('<a href="{{record.id}}">查看</a>', verbose_name="详情")

    class Meta:
        model = Datax
        template_name = "django_tables2/bootstrap.html"
        fields = ("customs_id", "product_number", "product_id", "product_name", "guige", "tag", "chakan")
