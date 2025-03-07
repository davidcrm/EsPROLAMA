from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from .forms import VolcadoForm
from .models import Estrategia, Principio, Descriptor, Autoevaluacion, Volcado

# Create your views here.
def login(request):
    return redirect('users/login')

@login_required
def main(request):
    return render(request, 'elama/main.html')

@login_required
def crear_individual(request):
    autoevaluacion = Autoevaluacion()
    autoevaluacion.save()
    return redirect('elama:individual', id_autoevaluacion=autoevaluacion.id)

@login_required
def individual(request, id_autoevaluacion):
    estrategias = Estrategia.objects.order_by('titulo')
    principios = Principio.objects.order_by('titulo')
    descriptores = Descriptor.objects.order_by('titulo')
    autoevaluacion = Autoevaluacion.objects.get(pk=id_autoevaluacion)
    volcados_autoevaluacion = Volcado.objects.filter(autoevaluacion__id=id_autoevaluacion).values_list('descriptor')
    v_a = [id[0] for id in volcados_autoevaluacion]
    context = {'estrategias': estrategias, 'principios': principios, 'descriptores': descriptores,
               'autoevaluacion': autoevaluacion, 'volcados_autoevaluacion': v_a}
    return render(request, 'elama/individual.html', context)

@login_required
def volcar_autoevaluacion(request, id_autoevaluacion, id_descriptor):
    autoevaluacion = Autoevaluacion.objects.get(pk=id_autoevaluacion)
    descriptor = Descriptor.objects.get(pk=id_descriptor)
    valoracion = '-1'
    existe = True
    try:
        volcado = Volcado.objects.get(autoevaluacion__id=id_autoevaluacion, descriptor__id=id_descriptor)
        valoracion = volcado.valoracion
    except ObjectDoesNotExist:
        existe = False

    if request.method != 'POST':
        if existe:
            form = VolcadoForm(instance=volcado)
        else:
            form = VolcadoForm()
    else:
        if existe:
            form = VolcadoForm(instance=volcado, data=request.POST)
            if form.is_valid():
                volcado.save()
                return redirect('elama:individual', id_autoevaluacion=id_autoevaluacion)
        else:
            form = VolcadoForm(data=request.POST)
            if form.is_valid():
                nuevo_volcado = form.save(commit=False)
                nuevo_volcado.autoevaluacion = autoevaluacion
                nuevo_volcado.descriptor = descriptor
                nuevo_volcado.save()
                return redirect('elama:individual', id_autoevaluacion=id_autoevaluacion)

    context = {'autoevaluacion': autoevaluacion, 'descriptor': descriptor, 'valoracion': int(valoracion),
               'form': form, 'valores': [i for i in range(1,5)]}
    return render(request, 'elama/volcado.html', context)

@login_required
def finalizar_individual(request, id_autoevaluacion):
    autoevaluacion = Autoevaluacion.objects.get(pk=id_autoevaluacion)
    autoevaluacion.finalizada = True
    autoevaluacion.save()
    return redirect('elama:individual', id_autoevaluacion=id_autoevaluacion)