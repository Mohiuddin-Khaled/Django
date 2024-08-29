from django.shortcuts import render
import datetime

d = {
    "author": "Rahim Uddin",
    "age": 24,
    # "lst": [1, 2, 3],
    "lst": ["python", "is", "best"],
    "birthday": datetime.datetime.now(),
    "courses": [
        {
            "id": 1,
            "name": "python",
            "fee": 5000,
        },
        {
            "id": 2,
            "name": "django",
            "fee": 10000,
        },
        {
            "id": 3,
            "name": "C",
            "fee": 1000,
        },
    ],
    "val": "",
}


# Create your views here.
def context_data(request):
    # way 1
    # return render(request, "context_app/context.html", d)
    # way 2
    # return render(request, "context_app/context.html", context=d)
    # way 3
    # return render(
    #     request,
    #     "context_app/context.html",
    #     {
    #         "author": "Rahim",
    #         "age": 24,
    #     },
    # )
    # way 4
    return render(request, "context_app/context.html", d)
