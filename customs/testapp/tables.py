import django_tables2 as tables
from .models import Datax, Dataxx
from django_tables2.utils import A
from testapp.coreAlgrithm import coreTax
from django.db.models.functions import Length

HighestLevel = 'f'
IVLevel = 'e'
IIIlevel = 'd'
IILevel = 'c'
ILevel = 'b'
LowestLevel = 'a'
BigLevel = 'big'
SmallLevel = 'small'


def data_tag(**kwargs):
    tag = kwargs.get("value", None)
    if tag == "1级":
        return "#750000"
    elif tag == "2级":
        return "#ae0000"
    elif tag == "3级":
        return "#ea0000"
    elif tag == "4级":
        return "#ff2d2d"
    elif tag == "5级":
        return "#ff7575"


class DataxTable(tables.Table):
    tag = tables.Column(attrs={"td": {"bgcolor": data_tag}}, verbose_name="风险等级"
                        )
    tag_ins = tables.Column(verbose_name="风险指示")
    # linkify = {"viewname": "datax_chakan", "args": [tables.A("pk")]}
    # product_name = tables.LinkColumn('testapp:datax_chakan', args=[A('pk')], verbose_name="查看")
    chakan = tables.TemplateColumn('<a href="{{record.id}}">查看</a>', verbose_name="详情")

    # product_id = tables.Column(order_by="product_id")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # def order_product_id(self, queryset, is_descending):
    #     queryset = queryset.annotate(amount="product_id").order_by(("-" if is_descending else "") + "amount")
    #     return (queryset, True)

    def render_tag(self, value):
        if value == LowestLevel:
            return "1级"
        elif value == ILevel:
            return "2级"
        elif value == IILevel:
            return "3级"
        elif value == IIIlevel:
            return "4级"
        elif value == IVLevel:
            return "5级"

    class Meta:
        attrs = {"id": "dazi"}
        model = Datax
        template_name = "django_tables2/semantic.html"
        fields = ("customs_id", "product_number", "product_id", "product_name", "tag_ins", "tag", "chakan")
