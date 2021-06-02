from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import QuizzForm, ContatoForm, ComentarioForm
from .models import Quizz, Contato


def home_page_view(request):
    return render(request, 'website/index.html')


def teoria_page_view(request):
    return render(request, 'website/about_colors.html')


def about_site_page_view(request):
    return render(request, 'website/about_site.html')


def form_page_view(request):
    return render(request, 'website/form.html')


def new_quizz_view(request):
    form = QuizzForm(request.POST or None)
    if form.is_valid():
        form.save()
        nota = grade(form)
        return render(request, 'website/show_quizz.html', {'nota': nota})

    context = {'form': form}

    return render(request, 'website/quizz.html', context)


def grade(form):
    acertos = 0

    if form.cleaned_data['pergunta1'] == 'Branco' or form.cleaned_data['pergunta1'] == 'branco':
        acertos += 1

    if form.cleaned_data['pergunta2'] == 'Preto' or form.cleaned_data['pergunta2'] == 'preto':
        acertos += 1

    if form.cleaned_data['pergunta3'] == '3':
        acertos += 1

    if form.cleaned_data['pergunta4'] == '2':
        acertos += 1

    if form.cleaned_data['pergunta5'] == '2':
        acertos += 1

    if form.cleaned_data['pergunta6'] == '4':
        acertos += 1

    if form.cleaned_data['pergunta7'] == 4:
        acertos += 1

    if form.cleaned_data['pergunta8'] == '1':
        acertos += 1

    if form.cleaned_data['pergunta9'] == '2':
        acertos += 1

    return acertos


def show_quizz_page_view(request):
    context = {'quizzs': Quizz.objects.all()}
    return render(request, 'website/show_quizz.html', context)


def new_contato_view(request):
    form = ContatoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:show_contato'))

    context = {'form': form}

    return render(request, 'website/contatos.html', context)


def show_contato_page_view(request):
    context = {'contatos': Contato.objects.all()}
    return render(request, 'website/show_contato.html', context)


def edita_contato_view(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    form = ContatoForm(request.POST or None, instance=contato)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:show_contato'))

    context = {'form': form, 'contato_id': contato_id}
    return render(request, 'website/edita_contato.html', context)


def apaga_contato_view(request, contato_id):
    Contato.objects.get(id=contato_id).delete()
    return HttpResponseRedirect(reverse('website:show_contato'))


def new_comentario_view(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('website:index'))

    context = {'form': form}

    return render(request, 'website/comentarios.html', context)


def color_page_001(request):
    return render(request, 'website/color-pages/color-page-001.html')


def color_page_002(request):
    return render(request, 'website/color-pages/color-page-002.html')


def color_page_003(request):
    return render(request, 'website/color-pages/color-page-003.html')


def color_page_004(request):
    return render(request, 'website/color-pages/color-page-004.html')


def color_page_005(request):
    return render(request, 'website/color-pages/color-page-005.html')


def color_page_006(request):
    return render(request, 'website/color-pages/color-page-006.html')


def color_page_007(request):
    return render(request, 'website/color-pages/color-page-007.html')


def color_page_008(request):
    return render(request, 'website/color-pages/color-page-008.html')


def color_page_009(request):
    return render(request, 'website/color-pages/color-page-009.html')


def color_page_010(request):
    return render(request, 'website/color-pages/color-page-010.html')


def color_page_011(request):
    return render(request, 'website/color-pages/color-page-011.html')


def color_page_012(request):
    return render(request, 'website/color-pages/color-page-012.html')
