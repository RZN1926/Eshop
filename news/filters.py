from .models import New
import django_filters

class NewFilter(django_filters.FilterSet):
    name = django_filters.CharFilter( lookup_expr = 'icontains', label = 'Title')
    article = django_filters.CharFilter( lookup_expr = 'icontains', label = 'Article')
    views__gte = django_filters.NumberFilter( field_name = 'views', lookup_expr = 'gte', label = 'Views from')
    views__lte = django_filters.NumberFilter( field_name = 'views', lookup_expr = 'lte', label = 'Views to')
class Meta:
    model = New
    fields = ['title', 'article', 'category', 'views__gte', 'views__lte']