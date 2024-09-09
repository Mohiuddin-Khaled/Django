from django.shortcuts import render, redirect
from category.forms import CategoryForm


# Create your views here.
def createCategory(request):
    category_data = CategoryForm()
    if request.method == "POST":
        category_data = CategoryForm(request.POST)
        if category_data.is_valid():
            category_data.save(commit=True)
            return redirect("homePage")
    return render(
        request, "category/category_data.html", {"category_data": category_data}
    )
