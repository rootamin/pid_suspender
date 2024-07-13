from django.shortcuts import render, redirect, HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .forms import ProcessForm
import os, signal, psutil

def index(request):
    if request.user.is_staff:
        form = ProcessForm()
        processes = [{'pid': p.pid, 'name': p.name()} for p in psutil.process_iter(attrs=['name'])]
        context = {'processes': processes, 'form': form}
        return render(request, 'index.html', context=context)
    else:
        return HttpResponse('You are not authorized to view this page.')

@csrf_exempt
def stop_process(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = ProcessForm(request.POST)
            if form.is_valid():
                pid = form.cleaned_data['pid']
                os.kill(pid, signal.SIGSTOP)
        return redirect('/')
    else:
        return HttpResponse('You are not authorized to view this page.')

@csrf_exempt
def resume_process(request):
    if request.user.is_staff:
        if request.method == 'POST':
            form = ProcessForm(request.POST)
            if form.is_valid():
                pid = form.cleaned_data['pid']
                os.kill(pid, signal.SIGCONT)
        return redirect('/')
    else:
        return HttpResponse('You are not authorized to view this page.')