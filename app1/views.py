from django.shortcuts import render

# Create your views here.


def UserDefined_Filter(request):
    d={'data':'Hai This IS a Achyuth KUmar','dt':'HI my naME is Achyuth kumar is always Unique but is always own rules'}
    return render(request,'UserDefined_Filter.html',d)