from compte.forms.comptes import CompteModelForm
from compte.forms.ocr import OcrModelForm
from compte.forms.transactions import TransactionModelForm
from compte.forms.confirm_deletion import ConfirmDeleteForm


__all__ = [
    "CompteModelForm",
    "ConfirmDeleteForm",
    "OcrModelForm",
    "TransactionModelForm",
]