from django.shortcuts import render
from django.http import HttpResponse
from .models import ATC, NetherlandsDrug, PolandDrug

def search_leki(request):
    substance = ATC.objects.get(code='N07XX04')
    netherlands_drugs = NetherlandsDrug.objects.filter(atc=substance)
    poland_drugs = PolandDrug.objects.filter(atc=substance)

    return HttpResponse({'netherlands_drugs': netherlands_drugs, 'poland_drugs': poland_drugs})