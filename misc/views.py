from django.shortcuts import render
from django.http import HttpResponse
import json
from misc.models import Province, City, Region


def get_location(request):
    ct = request.GET.get("ct")
    cv = request.GET.get("cv")
    out = {
        "status": "ERROR",
    }
    data = None
    if ct and cv:
        if ct == "p": #province
            p = Province.objects.filter(id=cv).first()
            if p:
                cities = City.objects.filter(province=p)
                data = [{
                    "name": c.name,
                    "id": c.id,
                } for c in cities]
        elif ct == "c": #city
            p = City.objects.filter(id=cv).first()
            if p:
                regions = Region.objects.filter(city=p)
                data = [{
                    "name": c.name,
                    "id": c.id,
                } for c in regions]
    if data:
        out["data"] = data
        out["status"] = "OK"
    return HttpResponse(json.dumps(out), content_type="application/json")

