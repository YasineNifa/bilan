import django_filters
from dal import autocomplete

from compte.models import Transaction


class TransactionFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(
        label="search",
        method="search_filter",
    )
    
    class Meta:
        model = Transaction
        fields = [
            "partie",
            "contrepartie",
            "report",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.form.fields["partie"].widget = autocomplete.Select2(
            url="compte:comptes_autocomplete"
        )



    def search_filter(self, queryset, _, value):
        queryset_filtered = (
            queryset.filter(**{"description__icontains": value})
            | queryset.filter(**{"partie__name__icontains": value})
            | queryset.filter(**{"contrepartie__name__icontains": value})
        )
        return queryset_filtered