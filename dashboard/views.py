from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse, Http404,HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import isi_data_member,isi_data_admin,form_berita,form_pesan_admin,form_pesan_user,form_timeline_penerimaan,form_timeline_pengumuman,form_timeline_seleksi,form_timeline_review,form_timeline_pendaftaran,form_faq
from .models import data_member,data_admin,hasil_kalkulasi,berita,pesan_admin,pesan_user,timeline,faq
from django.utils import timezone
from django import template
import datetime
from django.db import connection
from django.db.models import Q
from django.contrib.gis.geoip2 import GeoIP2


@login_required
def dashboard_home(request):
    kota = GeoIP2().city('36.73.70.173')
    # kotaa = request.META.get('HTTP_X_FORWARDED_FOR')
    # kota = GeoIP2().city(kotaa)

    # print request.META.get('REMOTE_ADDR')
    # print request.META.get('REMOTE_HOST')
    kota,provinsi,negara = kota['city'],kota['region'],kota['country_name']
    waktu = datetime.datetime.now()
    tahun,bulan,tanggal = waktu.year,waktu.month,waktu.day
    jam, menit = waktu.hour, waktu.minute
    arr_bulan = {'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'Mei','6':'Jun','7':'Jul','8':'Agu','9':'Sep','10':'Okt','11':'Nov','12':'Des'}
    bulan = arr_bulan[str(bulan)]
    salam,tanda ='',''
    if waktu.hour < 12 :
        salam = 'Pagi'
        tanda = 'AM'
    elif waktu.hour < 18 and waktu.hour >= 12 :
        salam = 'Siang'
        tanda = 'PM'
    elif waktu.hour >=18:
        salam = 'Malam'
        tanda = 'PM'
    context ={
        'salam':salam,
        'jam': jam,'menit': menit,'tahun':tahun,'bulan':bulan,'tanggal':tanggal,
        'tanda':tanda,
        'kota':kota,'provinsi':provinsi,'negara':negara,
    }

    akun = request.user
    if akun.is_superuser:
        data = data_admin.objects.filter(akun=akun)
        if data:
            user = data_admin.objects.get(akun=akun)
            namaLengkap = akun.first_name+' '+akun.last_name
            request.session['nama']=namaLengkap
            request.session['fakultas']=user.fakultas
            request.session['ava_url']=user.avatar.url
            context['fakultas']=request.session['fakultas']
            context['ava_url']=request.session['ava_url']
        else:
            namaLengkap = akun.first_name+' '+akun.last_name
            request.session['nama']=namaLengkap
            request.session['fakultas']=''
    else:
        data = data_member.objects.filter(akun=akun)
        if data:
            user = data_member.objects.get(akun=akun)
            namaLengkap = akun.first_name+' '+akun.last_name
            request.session['nama']=namaLengkap
            request.session['fakultas']=user.fakultas
            request.session['ava_url']=user.avatar.url
            context['fakultas']=request.session['fakultas']
            context['ava_url']=request.session['ava_url']
        else:
            namaLengkap = akun.first_name+' '+akun.last_name
            request.session['nama']=namaLengkap
            request.session['fakultas']=''
    context['username']=request.session['nama']
    return render(request,"dash/dash_home.html",(context))

@login_required
def listBerita(request):
    if berita.objects.all().exists():
        instance = berita.objects.all()
    else:
        instance = None
    context={
        'instance':instance
    }
    kunci = request.GET.get('kunci')
    if kunci:
        queryset_list=instance.filter(Q(judul__icontains=kunci)|Q(content__icontains=kunci)).distinct()
        context['instance']=queryset_list
    context['username']=request.session['nama']
    context['fakultas']=request.session['fakultas']
    context['ava_url']=request.session['ava_url']
    return render(request,"dash/dash_berita.html",(context))

@login_required
def view_timeline(request):
    instance=get_object_or_404(timeline,id=1)
    f1=form_timeline_pendaftaran(request.POST or None,instance=instance)
    f2=form_timeline_review(request.POST or None,instance=instance)
    f3=form_timeline_seleksi(request.POST or None,instance=instance)
    f4=form_timeline_pengumuman(request.POST or None,instance=instance)
    f5=form_timeline_penerimaan(request.POST or None,instance=instance)
    context={
        'obj':instance,
        'formPendaftaran':f1,
        'formReview':f2,
        'formSeleksi':f3,
        'formPengumuman':f4,
        'formPenerimaan':f5,
    }
    if f1.is_valid():
        instance = f1.save(commit=False)
        instance.save()
        return redirect('dashboard:timeline')
    elif f2.is_valid():
        instance = f2.save(commit=False)
        instance.save()
        return redirect('dashboard:timeline')
    elif f3.is_valid():
        instance = f3.save(commit=False)
        instance.save()
        return redirect('dashboard:timeline')
    elif f4.is_valid():
        instance = f4.save(commit=False)
        instance.save()
        return redirect('dashboard:timeline')
    elif f5.is_valid():
        instance = f5.save(commit=False)
        instance.save()
        return redirect('dashboard:timeline')

    context['username']=request.session['nama']
    context['fakultas']=request.session['fakultas']
    context['ava_url']=request.session['ava_url']
    return render(request,"dash/dash_timeline.html",(context))

@login_required
def profile(request):
    akun = request.user
    data = data_member.objects.filter(akun=akun)
    form = isi_data_member(request.POST or None, request.FILES or None)
    if data :
        data = data_member.objects.get(akun=akun)
        form = None
        context = {
        'status':True,
        'form':form,
        'user':data,
        'akun':akun,
        }
    else:
        if form.is_valid():
            instance = form.save(commit=False)
            instance.akun = request.user
            instance.daftar = True
            instance.tgl_daftar = timezone.now().date()
            instance.save()

        context = {
            "form" : form,
            'akun':akun,
        }
    context['username']=request.session['nama']
    context['fakultas']=request.session['fakultas']
    context['ava_url']=request.session['ava_url']
    return render(request,"dash/dash_profile.html",(context))

@login_required
def pesan(request):
    akun  = request.user
    if akun.is_superuser and akun.is_staff:
        return redirect('dashboard:adm_pesan')

    listPesan = pesan_admin.objects.all()
    form=form_pesan_user(request.POST or None)
    context = {
        'formPesan':form,
        'listPesan':listPesan,
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.pengirim = request.user
        instance.save()
        return redirect('dashboard:pesan')
    context['username']=request.session['nama']
    context['fakultas']=request.session['fakultas']
    context['ava_url']=request.session['ava_url']
    return render(request,"dash/dash_pesan.html",(context))

@login_required
def view_faq(request):
    instance = faq.objects.all()
    form = form_faq(request.POST or None)
    context={
        'instance':instance,
        'formFaq':form,
    }
    if form.is_valid():
        i = form.save(commit=False)
        i.save()
        return redirect('dashboard:faq')
    kunci = request.GET.get('kunci')
    if kunci:
        queryset_list=instance.filter(Q(pertanyaan__icontains=kunci)|Q(jawaban__icontains=kunci)).distinct()
        context['instance']=queryset_list
    context['username']=request.session['nama']
    context['fakultas']=request.session['fakultas']
    context['ava_url']=request.session['ava_url']
    return render(request,"dash/dash_faq.html",(context))

@login_required
def pengaturan(request):
    context={

    }
    context['username']=request.session['nama']
    context['fakultas']=request.session['fakultas']
    context['ava_url']=request.session['ava_url']
    return render(request,"dash/dash_pengaturan.html",(context))
