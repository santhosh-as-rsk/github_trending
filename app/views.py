from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.decorators import login_required
import requests
from bs4 import BeautifulSoup
from django.views import View


def home(request):
    if request.method == 'GET':
        r = requests.get('https://github.com/trending/c++')
        soup = BeautifulSoup(r.content, 'html.parser')
        link = soup.findAll('link')
        trending_datas = soup.findAll('article', class_='Box-row')
        return render(request, 'home.html', {'data': trending_datas, 'link': link})

    if request.method == 'POST':
        trend = request.POST.get('trending')
        print(trend)
        url = f'https://github.com/trending/python'
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        print(soup)
        link = soup.findAll('link')
        trending_datas = soup.findAll('article', class_='Box-row')
        return render(request, 'home.html', {'data': trending_datas, 'link': link})


def search(request):
    search_value=request.GET.get('search')
    return redirect(f'/trend/{search_value}/')


def trend(request,trend):

        url = f'https://github.com/trending/{trend}'
        print(url)
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        link = soup.findAll('link')
        trending_datas = soup.findAll('article', class_='Box-row')
        return render(request, 'home.html', {'data': trending_datas, 'link': link})