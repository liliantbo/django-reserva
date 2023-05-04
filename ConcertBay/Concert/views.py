from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Concierto, Localidad, Ticket
from .forms import LoginForm, RegistroForm
from django.contrib import messages

@login_required
def comprar_entrada(request, concierto_id):
    concierto = Concierto.objects.get(pk=concierto_id)
    localidades = concierto.localidad_set.all()
    if request.method == 'POST':
        localidad_id = request.POST.get('localidad')
        localidad = Localidad.objects.get(pk=localidad_id)
        if localidad.cantidad_disponible > 0:
            localidad.cantidad_disponible -= 1
            localidad.save()
            Ticket.objects.create(
                usuario=request.user,
                concierto=concierto,
                localidad=localidad,
            )
            return redirect('Concert:compra_list')
        else:
            messages.error(request, f'La localidad {localidad.nombre} está agotada.')
    context = {'concierto': concierto, 'localidades': localidades}
    return render(request, 'Concert/comprar_entrada.html', context)

def login_request(request):
 if request.method == 'POST':
   form = LoginForm(request, data=request.POST)
   if form.is_valid():
     username = form.cleaned_data.get('username')
     password = form.cleaned_data.get('password')
     user = authenticate(username=username, password=password)
     if user is not None:
       login(request, user)
       messages.info(request, f'Ha iniciado sesión como: {username}')
       return redirect("Concert:index")
     messages.error(request, 'Credenciales incorrectas')
 messages.error(request, 'Credenciales incorrectas')
 # Método no válido, retorna formulario vacío
 form = LoginForm()
 return render(request=request,
               template_name='Concert/login.html',
               context={'login_form': form})

def logout_view(request):
    logout(request)
    return redirect('Concert:index')

def registro_request(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Concert:index')
    else:
        form = RegistroForm()
    return render(request, 'Concert/signup.html', {'form': form})

def index(request):
    conciertos = Concierto.objects.all().order_by('fecha')
    tickets_disponibles = Localidad.objects.values('concierto').annotate(total_disponibles=Sum('cantidad_disponible'))
    context = {
        'conciertos': conciertos,
        'tickets_disponibles': tickets_disponibles
    }
    return render(request, 'Concert/index.html', context)

@login_required
def compra_list(request):
    compras = Ticket.objects.filter(usuario=request.user)
    return render(request, 'Concert/compra_list.html', {'compras': compras})

def concierto_detalle(request, concierto_id):
    concierto = get_object_or_404(Concierto, pk=concierto_id)
    localidades = Localidad.objects.filter(concierto=concierto)
    compras = Ticket.objects.filter(usuario=request.user, concierto=concierto)
    return render(request, 'Concert/concierto_detalle.html', {'concierto': concierto, 'localidades': localidades, 'çompras': compras})
