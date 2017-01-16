from django import forms
from django.contrib.auth import ( authenticate, get_user_model,
                                  login,logout,)
from django.contrib.auth.hashers import check_password
from .models import data_member,data_admin,berita
from pagedown.widgets import PagedownWidget

#----------------------------------------- form untuk register atau mendaftar beasiswa ---------------------------
tahun_lahir_pilihan = [thn for thn in range(1945,2016)]
class isi_data_member(forms.ModelForm):
    TanggalLahir = forms.DateField(
        widget=forms.SelectDateWidget(years=tahun_lahir_pilihan)
    )
    class Meta:
        model = data_member
        fields = [
            "nama",
            "fakultas",
            "prodi",
            "nim",
            "ktm",
            "alamat",
            "TanggalLahir",
            "semester",
            "ipk",
            "transkrip",
            "tan",
            "pot",
            "pre",
            "bukti_prestasi",
            "org",
            "bukti_organisasi",
        ]

class isi_data_admin(forms.ModelForm):
    TanggalLahir = forms.DateField(
        widget=forms.SelectDateWidget(years=tahun_lahir_pilihan)
    )
    class Meta:
        model = data_admin
        fields = [
            "nama",
            "jabatan",
            "fakultas",
            "prodi",
            "nik",
            "alamat",
            "TanggalLahir",
        ]
# class perhitungan(forms.Form):


class form_berita(forms.ModelForm):
    judul = forms.CharField(label='Judul Berita', error_messages={'required': 'Mohon diisi judul'})
    image = forms.ImageField(label='Sematkan Gambar', error_messages={'required': 'Mohon diisi gambar'})
    publish = forms.DateField(label='publish', error_messages={'required': 'Mohon diisi tanggal publikasi'},
                              widget=forms.TextInput(attrs={'class': 'datepicker'}))
    content = forms.CharField(widget=PagedownWidget())
    class Meta:
        model = berita
        fields = [
            'judul',
            'image',
            'content',
            'draft',
            'publish',
        ]
