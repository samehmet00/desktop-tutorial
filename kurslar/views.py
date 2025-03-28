from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

data = {
    "programlama": "programlama kategorisine ait kurslar",
    "web-gelistirme": "web-gelistirme kategorisine ait kurslar",
    "mobil": "mobil kategorisine ait kurslar",
}

def kurslar(request):
    list_items = ""
    category_list = list(data.keys())
    
    for category in category_list:
        redirect_url = reverse("courses_by_category",args=[category])
        list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"

    html = f"<h1>kurs listesi</h1><br><ul>{list_items}</ul>"
    return HttpResponse(html)


def details(request,kurs_adi):
    return HttpResponse(f"{kurs_adi} detay sayfası")

def getCoursesByCategory(request,category_name):
    try:
        category_text =  data[category_name]
        return HttpResponse(category_text) 
    except:
        return HttpResponse("<h1>Yanlış kategori seçimi!</h1>")

def getCoursesByCategoryId(request,category_id):
    category_list = list(data.keys())
    if(category_id > len(category_list)):
        return HttpResponse("yanlış kategori seçimi!")
    category_name = category_list[category_id-1]

    redirect_url = reverse("courses_by_category",args=[category_name])

    return redirect(redirect_url)
