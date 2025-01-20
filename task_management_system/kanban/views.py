from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def kanban_board(request):
    tasks = Task.objects.all()
    return render(request, 'kanban/board.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('kanban_board')
    else:
        form = TaskForm()
    return render(request, 'kanban/add_task.html', {'form': form})



from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

@require_POST
@csrf_exempt
def update_task_status(request):
    data = json.loads(request.body)
    task_id = data.get('task_id')
    new_status = data.get('new_status')
    
    try:
        task = Task.objects.get(id=task_id)
        task.status = new_status
        task.save()
        return JsonResponse({'success': True})
    except Task.DoesNotExist:
        return JsonResponse({'success': False}, status=404) 
    

@require_POST
@csrf_exempt
def delete_task(request):
    try:
        data = json.loads(request.body)
        task_id = data.get('task_id')
        task = Task.objects.get(id=task_id)
        task.delete()
        return JsonResponse({'success': True})
    except Task.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Task not found'}, status=404)
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)
    



