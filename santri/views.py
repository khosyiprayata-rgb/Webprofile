from django.shortcuts import render, redirect
from .models import Feedback

def santri_home(request):
    return render(request, "profile_home.html")

def biodata(request):
    return render(request, "biodata.html")

def jadwal(request):
    return render(request, "jadwal.html")

def galeri(request):
    return render(request, "galeri.html")

def feedback(request):
    if request.method == 'POST':
        Feedback.objects.create(
            nama=request.POST.get('nama'),
            email=request.POST.get('email'),
            kategori=request.POST.get('kategori'),
            pesan=request.POST.get('pesan')
        )
        return redirect('feedback')

    data = Feedback.objects.all().order_by('-id')
    return render(request, "feedback.html", {'data': data})