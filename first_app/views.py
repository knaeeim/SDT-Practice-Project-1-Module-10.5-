from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    dic = { "list" : [1, 2, 3 , 4], "str" : "I'm Naeeim", "name" : "naeeim", 'date' : datetime.datetime.now(), "value" : '', "list1" : [
        {"name" : "Naeeim", "age" : 20},
        {"name" : "Imran", "age" : 21},
        {"name" : "Rahim", "age" : 22},
        {"name" : "Karim", "age" : 23},
    ], "val": 20935785}
    return render(request, "index.html", dic)