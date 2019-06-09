from django.http import HttpResponse , Http404
from django.template import loader
from django.db.models import Q
from django.shortcuts import render
from .models import Data_set
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
import os
import re
from functools import reduce
from operator import __or__



def all_data(request):
    list_of_all = []
    a = []
    b = []
    c = []
    d = []
    Barrel_Num = []
    Barrel_Type = []
    Plot_num = []
    Trial_name = []
    get_all = Data_set.objects.all()
    inpo = request.GET.get('rs','')
    BarNumber = request.GET.get('Barrel_Number','')
    BarType = request.GET.get('Barrel_Type','')
    TriName = request.GET.get('Trial_Name','')
    PlotNumber = request.GET.get('Plot_Number','')

    print(inpo)
    for item in get_all:
        a.append(item.Barrel_No)
        b.append(item.Barrel_type)
        c.append(item.Trial_Name)
        d.append(item.Plot_No)
    all_resources=zip(a,b,c,d)
    for a,b,c,d in all_resources:
        if BarNumber == 'Barrel_Number':
            if inpo in a :
                Barrel_Num.append(a)
                Barrel_Type.append(b)
                Plot_num.append(d)
                Trial_name.append(c)
        elif BarType == 'Barrel_Type':
            if inpo in b :
                Barrel_Num.append(a)
                Barrel_Type.append(b)
                Plot_num.append(d)
                Trial_name.append(c)

        elif TriName == 'Trial_Name':
            if inpo in c :
                Barrel_Num.append(a)
                Barrel_Type.append(b)
                Plot_num.append(d)
                Trial_name.append(c)

        elif PlotNumber == 'Plot_Number':
            if inpo in d :
                Barrel_Num.append(a)
                Barrel_Type.append(b)
                Plot_num.append(d)
                Trial_name.append(c)

    all_dataset=zip(Barrel_Type,Barrel_Num,Plot_num,Trial_name)



    return render(request, 'search.html',context={'all_dataset':all_dataset,'inpo':inpo})

