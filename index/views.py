from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from .models import Project, ProjectCategory
from .forms import ContactForm
# Create your views here.

def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['nasr528@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')

    projects = Project.objects.all()
    categories = ProjectCategory.objects.all()

    ctx = {'projects': projects, 'categories': categories, 'form':form}
    return render(request, 'index/index.html', ctx)

def project(request, project_id):
    project = Project.objects.get(id=project_id)
    ctx = {'project': project}
    return render(request, 'index/Project.html', ctx)


def resume(request):
    return render(request, 'index/my_resume.html')


