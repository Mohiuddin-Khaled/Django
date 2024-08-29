from django.shortcuts import render

# way -- 1
# d = {
#     "author": "khaled",
#     "age": 24,
# }


def home(request):
    # way -- 2
    d = {
        "author": "khaled",
        "age": 24,
    }
    return render(request, "index.html", d)
