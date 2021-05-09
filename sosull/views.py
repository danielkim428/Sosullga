from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db.models import Count, Avg
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers
from datetime import datetime
import math
import json

# Create your views here
from .models import *

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    recent = Marker.objects.filter(user=request.user).all().latest('time')

    if request.method == 'POST':
        query = request.POST['search']

        print(query)

        result = Novel.objects.filter(title__contains=query)

        if result:
            context = {
                "user": request.user,
                "novels": Novel.objects.all(),
                "recent": recent,
                "recentNovel": Novel.objects.get(title=recent.novel),
                "result": result,
            }
        else:
            context = {
                "user": request.user,
                "novels": Novel.objects.all(),
                "recent": recent,
                "recentNovel": Novel.objects.get(title=recent.novel),
                "resultNone": "결과가 없습니다.",
            }

        return render(request, "sosull/index.html", context)
    else :
        context = {
            "user": request.user,
            "novels": Novel.objects.all(),
            "recent": recent,
            "recentNovel": Novel.objects.get(title=recent.novel),
        }
        return render(request, "sosull/index.html", context)

def request(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']

        new_request = Request(user=request.user, title=title, author=author)

        new_request.save()

        return HttpResponseRedirect(reverse('request'))

    quest = Request.objects.all()

    context = {
        'quest': quest,
    }

    return render(request, "sosull/request.html", context)

def series(request, series_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    try:
        novel = Novel.objects.get(pk=series_id)
        try:
            novel.rating = round(Comment.objects.filter(novel=novel).all().aggregate(Avg('rating'))['rating__avg'], 1)
        except:
            novel.rating = "-"
        novel.save()
    except novel.DoesNotExist:
        raise Http404("Post does not exist")

    if request.method == 'POST':
        rating = request.POST['rating']
        content = request.POST['content']

        if (rating == ""):
            new_comment = Comment(author=request.user, novel=novel, content=content)
        else:
            new_comment = Comment(author=request.user, novel=novel, rating=rating, content=content)

        new_comment.save()
        return HttpResponseRedirect(reverse('series', kwargs={'series_id': series_id}))

    try:
        marker = Marker.objects.get(user=request.user, novel=novel)
    except:
        marker = Marker(user=request.user, novel=novel, time=datetime.now())
        marker.save()

    comment = Comment.objects.filter(novel=novel).all()

    context = {
        "novel": novel,
        "comment": comment,
        "marker": marker
    }
    return render(request, "sosull/series.html", context)

def account(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    marker = Marker.objects.filter(user=request.user).order_by("-time").all()
    bookmark = Bookmark.objects.filter(user=request.user).order_by("-time").all()
    comment = Comment.objects.filter(author=request.user).order_by("-time").all()
    quest = Request.objects.filter(user=request.user).all()

    context = {
        'history': marker,
        'bookmark': bookmark,
        'comment': comment,
        'quest': quest,
    }
    return render(request, "sosull/account.html", context)

def setting(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    try:
        setting = Setting.objects.get(user=request.user)
    except:
        setting = Setting(user=request.user)
        setting.save()

    if request.method == 'POST':
        if request.POST['dark'] == "on":
            dark = True
        else:
            dark = False
        size = request.POST['size']
        height = request.POST['height']
        width = request.POST['width']

        setting.dark = dark
        setting.size = size
        setting.height = height
        setting.width = width
        setting.save()
        return HttpResponseRedirect(reverse('setting'))

    context = {
        'setting': setting
    }

    return render(request, "sosull/setting.html", context)

def read(request, read_id, read_page):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    try:
        novel = Novel.objects.get(pk=read_id)
        novel.file.path
    except:
        return HttpResponseRedirect(reverse('series', kwargs={'series_id': read_id}))

    content = ""

    linePerPage = 100

    try:
        with open(novel.file.path, encoding='utf-8') as f:
            count = sum(1 for _ in f)

        total = math.ceil(count/linePerPage)

        if read_page > total:
            return HttpResponseRedirect(reverse('series', kwargs={'series_id': read_id}))

        with open(novel.file.path, "r", encoding='utf-8') as file:
            for i, line in enumerate(file):
                if (i >= (read_page-1)*linePerPage) and (i < read_page*linePerPage):
                    content = content+line
    except:
        with open(novel.file.path, encoding='utf-16') as f:
            count = sum(1 for _ in f)

        total = math.ceil(count/linePerPage)

        if read_page > total:
            return HttpResponseRedirect(reverse('series', kwargs={'series_id': read_id}))

        with open(novel.file.path, "r", encoding='utf-16') as file:
            for i, line in enumerate(file):
                if (i >= (read_page-1)*linePerPage) and (i < read_page*linePerPage):
                    content = content+line

    percent = round((read_page*100)/total)

    try:
        marker = Marker.objects.get(user=request.user, novel=novel)
        marker.page = read_page
        marker.percent = percent
        marker.time = datetime.now()
        marker.save()
    except:
        marker = Marker(user=request.user, novel=novel, page=read_page, percent=percent)
        marker.save()

    try:
        setting = Setting.objects.get(user=request.user)
    except:
        setting = Setting(user=request.user)
        setting.save()

    context = {
        "novel": novel,
        "content": content,
        "total": total,
        "page": read_page,
        "setting": setting,
    }
    return render(request, "sosull/read.html", context)

def pageSetting(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        user = request.user
        dark = request.headers.get('dark')
        size = request.headers.get('size')
        height = request.headers.get('height')
        width = request.headers.get('width')

        try:
            setting = Setting.objects.get(user=user)
            setting.user = user
            setting.dark = dark
            setting.size = size
            setting.height = height
            setting.width = width
            setting.save()
        except:
            setting = Setting(user=user, dark=dark, size=size, height=height, width=width)
            setting.save()
        data = {
            'result': 'Success!'
        }
        return JsonResponse(data)

def bookmark(request, read_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        read_page = int(request.headers.get('page'))
        novel = Novel.objects.get(pk=read_id)

        try:
            bookmark = Bookmark.objects.get(user=request.user, novel=novel, page=int(request.headers.get('page')))
            bookmark.time = datetime.now()
            bookmark.save()
        except:
            bookmark = Bookmark(user=request.user, novel=novel, page=int(request.headers.get('page')))
            bookmark.save()

        data = {
            'result': 'Success!'
        }
        return JsonResponse(data)

def next(request, read_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        read_page = int(request.headers.get('page'))+1

        novel = Novel.objects.get(pk=read_id)

        content = ""

        linePerPage = 100

        try:
            with open(novel.file.path, encoding='utf-8') as f:
                count = sum(1 for _ in f)

            total = math.ceil(count/linePerPage)

            with open(novel.file.path, "r", encoding='utf-8') as file:
                for i, line in enumerate(file):
                    if (i >= (read_page-1)*linePerPage) and (i < read_page*linePerPage):
                        content = content+line
        except:
            with open(novel.file.path, encoding='utf-16') as f:
                count = sum(1 for _ in f)

            total = math.ceil(count/linePerPage)

            with open(novel.file.path, "r", encoding='utf-16') as file:
                for i, line in enumerate(file):
                    if (i >= (read_page-1)*linePerPage) and (i < read_page*linePerPage):
                        content = content+line


        if read_page > total:
            data = {
                'nextPage': "end",
                'current': int(request.headers.get('page')),
                "total": total,
            }

            try:
                marker = Marker.objects.get(user=request.user, novel=novel)
                marker.page = int(request.headers.get('page'))
                marker.percent = 100
                marker.time = datetime.now()
                marker.save()
            except:
                marker = Marker(user=request.user, novel=novel, page=int(request.headers.get('page')), percent=100)
                marker.save()

        else:
            data = {
                'nextPage': content,
                'current': read_page,
                "total": total,
            }
            percent = round((read_page*100)/total)
            try:
                marker = Marker.objects.get(user=request.user, novel=novel)
                marker.page = read_page
                marker.percent = percent
                marker.time = datetime.now()
                marker.save()
            except:
                marker = Marker(user=request.user, novel=novel, page=read_page, percent=percent)
                marker.save()

        return JsonResponse(data)

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'sosull/login.html', {"message": "아이디 또는 비밀번호를 다시 확인하세요."})
    else:
        return render(request, 'sosull/login.html')

def logout_view(request):
    logout(request)
    return render(request, "sosull/login.html", {"message": "로그아웃 되었습니다."})

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))

    if request.method == 'POST':
        code = request.POST['code']

        if code != "woodstock":
            return render(request, 'sosull/register.html', {"message": "잘못된 코드입니다."})

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            new_user = User.objects.create_user(username, email, password)
            new_user.save()

        except IntegrityError:
            return render(request, 'sosull/register.html', {"message": "이미 사용중인 아이디이거나 이미 가입되어 있습니다."})
        except:
            return render(request, 'sosull/register.html', {"message": "잘못된 정보입니다."})

        return HttpResponseRedirect(reverse('login'))

    else:
        return render(request, 'sosull/register.html')
