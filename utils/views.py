from django.shortcuts import render

# Create your views here.

def group_queryset(n,queryset):
    result = []
    temp = []
    for q in queryset:
        temp.append(q)
        if len(temp) == n:
            result.append(temp)
            temp = []
    return result
