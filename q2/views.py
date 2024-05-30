import math

from django.shortcuts import render

def home(request):
    return render(request, "index.html")

def triangle_area_calculator(request):
    triangle_base = ""
    triangle_height = ""
    triangle_area = ""

    if request.method == "POST":
        triangle_base = request.POST.get("triangle_base")
        triangle_height = request.POST.get("triangle_height")
        button = request.POST.get("button")

        if button == "Очистить":
            triangle_base = ""
            triangle_height = ""

        elif button == "Вычислить" and len(triangle_base) > 0 and len(triangle_height) > 0:
            triangle_area = round(float(triangle_base) * float(triangle_height) / 2, 2)

    context = {"triangle_base": triangle_base, "triangle_height": triangle_height, "triangle_area": triangle_area}
    return render(request, "triangle_area_calculator.html", context)
