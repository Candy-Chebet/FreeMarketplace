from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import completedTaskss  # Corrected model name
from .forms import CompletedTasksForm, updateCompletedTasksForm
from django.contrib import messages


def upload_task(request):
    form = CompletedTasksForm(request.POST or None)
    total_tasks = completedTaskss.objects.count()
    queryset = completedTaskss.objects.order_by('-completionDate')[:5]
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully saved the task')
        return redirect("/completedtasks/list")

    context = {
    "form": form,
	"title": "Add Completed Task",
 	"total_tasks": total_tasks,
	"queryset": queryset,
        }
    return render(request, "uploadFile.html", context)

@login_required
def listTasks(request):
    title = 'Completed Tasks'
    queryset = completedTaskss.objects.all()  # Corrected model name
    form = CompletedTasksForm(request.POST, request.FILES)
    
    if request.method == 'POST':
        form = CompletedTasksForm(request.POST, request.FILES)
        if form.is_valid():
            queryset = completedTaskss.objects.filter(name__icontains=form.cleaned_data['taskName'])
    
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    return render(request, 'listCompletedTasks.html', context)


# @login_required
# def download_attachment(request, task_id):
#     task = get_object_or_404(completedTasks, id=task_id)
#     file_path = task.attachment.path
#     with open(file_path, 'rb') as f:
#         response = HttpResponse(f.read())
#         response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(file_path)
#         return response
    


@login_required
def update_task(request, pk):
    queryset = completedTaskss.objects.get(id=pk)
    form = updateCompletedTasksForm(instance=queryset)
    if request.method == 'POST':
        form = updateCompletedTasksForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully saved the task')
            return redirect('/completedtasks/list')
        
    context = {
    "form": form,
    
        }
    return render(request, 'uploadFile.html', context)