from .models import New
import django_filters

class NewsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter( lookup_expr = 'icontains', label = 'Title')
    article = django_filters.CharFilter( lookup_expr = 'icontains', label = 'article')
    views__gte = django_filters.NumberFilter( field_name = 'views', lookup_expr = 'gte', label = 'Views from')
    views__lte = django_filters.NumberFilter( field_name = 'views', lookup_expr = 'lte', label = 'Views to')
    category = django_filters.CharFilter( lookup_expr = 'icontains', label = 'category')
