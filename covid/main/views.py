from django.shortcuts import render
import requests
import json


def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querstring={"country":"India"}

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "738662f3a7mshd14f930521be1c1p179d3djsn32bc0d1d4aca"
        }

    response = requests.request("GET", url, headers=headers,params=querstring).json()
    data=response['response']
    d=data[0]

    print(d)
    context={
       'all':d['cases']['total'],
       'recovered':d['cases']['recovered'],
       'deaths':d['deaths']['total'],
       'new':d['cases']['new'],
       'critical':d['cases']['critical']
    }
    return render(request,'index.html',context)
# Create your views here.
