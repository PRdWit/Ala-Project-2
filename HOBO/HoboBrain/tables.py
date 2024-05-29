import django_tables2 as tables
from .models import Stream  # Replace with your actual model name

class streamTable(tables.Table):
    class Meta:
        model = Stream
        template_name = "django_tables2/table.html"