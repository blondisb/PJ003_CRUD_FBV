from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, JsonResponse, Http404
from .models import MO_project, MO_task, MO_deleteme
from . import forms as fo

# Create your views here.


def VW_home(request):
    # return HttpResponse('Home')
    title = 'Welcome 2 Jamrock'
    return render(request, 'index.html', {
        'title': title
    })


def VW_about(request):
    username = 'user003'
    return render(request, 'about.html', {
        'username': username
    })


def VW_project_list(request):
    try:
        # OB_project = list(MO_project.objects.values()) return JsonResponse(OB_project, safe=False)
        OB_project = MO_project.objects.all()
        return render(request, 'projects/projects.html', {
            'OB_project': OB_project
        })

    except MO_project.DoesNotExist:
        raise Http404("Not found")


def VW_empty_table(request):
    try:
        OB_project = list(MO_deleteme.objects.all())
        return JsonResponse(OB_project, safe=False)
    except MO_deleteme.DoesNotExist:
        raise Http404("Not found")


def VW_task(request, id_tsk):
    OB_task = get_object_or_404(MO_task, id=id_tsk)
    return HttpResponse('Task %s' % OB_task)


def VW_task2(request):
    OB_task = MO_task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'OB_task': OB_task
    })


def VW_addtask_SIN_USAR(request):
    OB_task_title = request.GET['title']
    OB_task_desc = request.GET['description']

    MO_task.objects.create(
        tittle=OB_task_title,
        descrip=OB_task_desc,
        project_id=2)

    return render(request, 'tasks/addtask.html', {
        'form': fo.FO_addtask()
    })


def VW_addtask(request):
    if request.method == 'POST':
        OB_task_title = request.POST['title']        # Form variable name
        OB_task_desc = request.POST['description']   # Form variable name

        MO_task.objects.create(
            tittle=OB_task_title,
            descrip=OB_task_desc,
            project_id=2)
        return redirect('URL_tasks2')

    elif request.method == 'GET':
        return render(request, 'tasks/addtask.html', {
            'form': fo.FO_addtask()
        })


def VW_addproject(request):
    if request.method == 'POST':
        OB_project_name = request.POST['name']
        MO_project.objects.create(
            name=OB_project_name)
        return redirect('URL_projects')

    elif request.method == 'GET':
        return render(request, 'projects/addproject.html', {
            'form': fo.FO_addproject()
        })


def VW_projectdetails(request, id_pj):
    OB_projectdetails = get_object_or_404(MO_project, id=id_pj)
    # OB_rel_tasks = get_list_or_404(MO_task, project_id=id_pj)
    OB_rel_tasks = MO_task.objects.filter(project_id=id_pj)#.order_by('title')
    # print(OB_rel_tasks)
    return render(request, 'projects/projectdetails.html', {
        'project': OB_projectdetails,
        'rel_tasks': OB_rel_tasks
    })