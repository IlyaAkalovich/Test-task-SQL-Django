from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.views import View
from users.forms import UserCreationForm,ShortenerForm
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from .models import Shortener

class Register(View):
    template_name = 'registration/register.html'

    def get(self, request, ):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


def home_view(request):
    template = 'home.html'
    context = {}
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, template, context)

    elif request.method == 'POST':
        print("POST")
        used_form = ShortenerForm(request.POST)
        used_form.instance.user = request.user
        if used_form.is_valid():
            shortened_object = used_form.save()
            new_url = request.build_absolute_uri('/') + shortened_object.short_url
            long_url = shortened_object.long_url

            context['new_url'] = new_url
            context['long_url'] = long_url

            return render(request, template, context)

        context['errors'] = used_form.errors

        return render(request, template, context)


def redirect_url_view(request, shortened_part):
    try:
        shortener = Shortener.objects.get(short_url=shortened_part)
        shortener.save()
        return HttpResponseRedirect(shortener.long_url)

    except:
        raise Http404('Sorry this link is broken :(')


def history_view(request):
    template = 'history.html'
    context = {}
    shortened_links = Shortener.objects.filter(user_id=request.user.id)
    links = []
    for link in shortened_links:
        new_url = request.build_absolute_uri('/') + str(link)
        links.append(new_url)

    context['shortened_links'] = links
    return render(request, template, context)
