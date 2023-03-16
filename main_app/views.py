from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Vinyl, RecordPlayer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.


def home(request):
    return HttpResponse('<h1>Vinyl Collector</h1>')


def about(request):
    return render(request, 'about.html') 

def vinyls_index(request):
    vinyls = Vinyl.objects.filter(user=request.user)
    return render(request,'vinyls/index.html', {'vinyls': vinyls})

def vinyls_detail(request, vinyl_id):
    vinyl = Vinyl.objects.get(id=vinyl_id)
    return render(request, 'vinyls/detail.html', {'vinyl': vinyl})

class VinylCreate(CreateView):
    model = Vinyl
    fields = ['title', 'artist', 'genre', 'year_released', 'description', 'image']
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class VinylUpdate(UpdateView):
    model = Vinyl
    fields = ['genre', 'year_released', 'description']

class VinylDelete(DeleteView):
    model = Vinyl
    success_url = '/vinyls/'


def signup (request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'INVALID, PLEASE TRY AGAIN.'
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request, 'registration/signup.html', context)

class RecordPlayerList(ListView):
    model = RecordPlayer
    
    
class RecordPlayerDetail(DetailView):
    model = RecordPlayer

class RecordPlayerCreate(CreateView):
    model = RecordPlayer
    fields = '__all__'

class RecordPlayerUpdate(UpdateView):
    model = RecordPlayer
    fields = '__all__'

class RecordPlayerDelete(DeleteView):
    model = RecordPlayer
    success_url = '/recordplayers/'
    

