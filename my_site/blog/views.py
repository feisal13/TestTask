from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, render
from django.urls import reverse
from django.utils import timezone
from .models import News
from .forms import UserRegisterForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormView


def home(request):
    return render(request, 'blog/home.html')
    # news_list = News.objects.all()
    # paginator = Paginator(news_list, 5)
    # page = request.GET.get('page', 1)
    # try:
    #     news = paginator.page(page)
    # except PageNotAnInteger:
    #     news = paginator.page(1)
    # except EmptyPage:
    #     news = paginator.page(paginator.page(paginator.num_pages))
    # return render(request, 'blog/home.html', {'page': page, 'news': news})



def detail(request, news_id):
    try:
        a = News.objects.get(id=news_id)
    except:
        raise Http404('Not found')

    comments = a.comment_set.order_by('-id')[:10]
    return render(request, 'blog/post.html', {'news': a, 'comments': comments})


def leave_comment(request, news_id):

    try:
        a = News.objects.get(id=news_id)
    except:
        raise Http404('Not found')

    a.comment_set.create(author_name=request.user, comment_text=request.POST['text'], pub_date = timezone.now())
    return HttpResponseRedirect(reverse('detail', args=(a.id,)))

def register(request):
    form = None
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с єтим адресом уже зарегестрирован!')
        else:
            if form.is_valid():
                ins = form.save()
                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']

                user = authenticate(username=username, password=password, email=email)
                ins.email = email
                ins.save()
                form.save_m2m()
                messages.success(request, 'Вы успешно заресестрировались')
                return redirect('/')

    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)