from django.http import HttpResponse

from django.core.exceptions import ObjectDoesNotExist

from proj.main.models import CreditApplication


def test(request, contract_id):
    try:
        producers_ids = list(
            CreditApplication.objects.select_related('products').filter(contract_id=contract_id).values_list(
                'products__producer_id', flat=True).distinct())
    except ObjectDoesNotExist:
        producers_ids = []
    return HttpResponse(f"<html><body><h1>Unique producers IDs: {producers_ids}</h1></body></html>",
                        content_type="text/html")
