from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import *
from .models import *
from .utils import *


class PromoHome(DataMixin, ListView):
    paginate_by = 4
    model = Promo
    template_name = 'promo/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Promo.objects.filter(is_published=True).select_related('city')


class PromoCities(DataMixin, ListView):
    paginate_by = 4
    model = Cities
    template_name = 'promo/index.html'
    context_object_name = 'cities'
    allow_empty = False

    def get_queryset(self):
        return Promo.objects.filter(city__slug=self.kwargs['city_slug'],
                                    is_published=True).select_related('city')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Cities.objects.get(slug=self.kwargs['city_slug'])
        c_def = self.get_user_context(title='Город - ' + str(c.name),
                                      cits_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Promo
    template_name = 'promo/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'promo/addpage.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление кампании")
        return dict(list(context.items()) + list(c_def.items()))


def about(request):
    return render(request, 'promo/about.html', {'menu': menu, 'title': 'О сайте'})


def PageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try:
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, "Ошибка добавления формы")
#     else:
#          form = AddPostForm()
#     return render(request, 'promo/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление кампании'})

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'promo/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

# def contact(request):
#     return HttpResponse("Обратная связь")


# def login(request):
#     return HttpResponse("Авторизация")


# def show_cities(request, city_id):
#     posts = Promo.objects.filter(city_id=city_id)
#
#     if len(posts) == 0:
#         raise Http404
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по городам',
#         'cits_selected': city_id,
#     }
#     return render(request, 'promo/index.html', context=context)


# def show_post(request, post_slug):
#     post = get_object_or_404(Promo, slug=post_slug)
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.camp,
#         'cits_selected': post.city_id,
#     }
#     return render(request, 'promo/post.html', context=context)
#
#
def show_streets(request, street_slug):
    return HttpResponse(f"Отображение улицы с id={street_slug}")


def show_homes(request, home_slug):
    return HttpResponse(f"Отображение дома с id={home_slug}")


def show_entrances(request, entrance_slug):
    return HttpResponse(f"Отображение подъезда с id={entrance_slug}")


def show_flats(request, flat_slug):
    return HttpResponse(f"Отображение квартиры с id={flat_slug}")


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'promo/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'promo/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')