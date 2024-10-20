import django_filters
from unicodedata import category

from R_Store.models import Product
from django.db.models import Q

class ProductFilter(django_filters.FilterSet):
    price_range =  django_filters.RangeFilter(field_name='price', label = 'Цена товара от и до')
    stock_product =  django_filters.BooleanFilter(method='stock', label= 'В наличии')
    term = django_filters.CharFilter(method='filter_term', label='Упрощенный поиск (Название/описание)')
    category =  django_filters.MultipleChoiceFilter(field_name='category', label='Категория', choices=Product.CATEGORY_CHOICES)


    class Meta:
        model = Product
        fields = [ 'price_range', 'stock_product', 'term', 'category']


    def stock(self, queryset, name, value):
        if value is None:
            return queryset
        if value:
            return queryset.filter(stock__gt=0)
        return queryset.filter(stock__lte=0)


    def filter_term(self, queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(name__icontains=term) |Q(description__icontains=term)

        return queryset.filter(criteria).distinct()

    def filter_category(self, queryset, name, value):
        if value:
            return queryset.filter(category__in=value)
        return queryset