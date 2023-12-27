from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    context = {'lst':'Python',
        'lt':['Monday', 'Tuesday', 'Wednesday'],
        'value':'20',
        'birthday':datetime.datetime.now(),
        'data' : [
            {'name': 'Josh', 'age': 19},
            {'name': 'Dave', 'age': 22},
            {'name': 'Joe', 'age': 31},
            ],
        'value':['China', 'India', 'Thailand'],
        'var':["States", ["Kansas", ["Lawrence", "Topeka"], "Illinois"]]
        }

    return render(request, 'home.html', context)