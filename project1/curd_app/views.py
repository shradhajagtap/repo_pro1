from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import SchoolTeacherForm
from .models import SchoolTeacher


@login_required(login_url="login_url")
def teacher_view(request):
    form = SchoolTeacherForm()
    if request.method == "POST":
        form = SchoolTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    template_name = "curd_app/info.html"
    return render(request, template_name, context)


@login_required(login_url="login_url")
def show_info(request):
    template_name = "curd_app/show_info.html"
    school = SchoolTeacher.objects.all()
    context = {"school": school}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = SchoolTeacher.objects.get(id=pk)
    form = SchoolTeacherForm(instance=obj)
    if request.method == "POST":
        form = SchoolTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "curd_app/info.html"
    context = {"form": form}
    return render(request, template_name, context)


def delete_view(request, pk):
    obj = SchoolTeacher.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, 'curd_app/cancel.html')
