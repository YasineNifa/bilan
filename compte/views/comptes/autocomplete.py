from abc import abstractmethod
from dal.autocomplete import Select2QuerySetView

from compte.models import Compte



class AbstractAutocompleteView(Select2QuerySetView):
    @classmethod
    @abstractmethod
    def _MODEL(cls):
        pass

    def get_queryset(self):

        queryset = self._MODEL.objects.all()

        if self.q:
            if hasattr(self._MODEL, "name"):
                queryset = queryset.filter(name__istartswith=self.q)

        return queryset

class CompteAutocompleteView(AbstractAutocompleteView):
    _MODEL = Compte
