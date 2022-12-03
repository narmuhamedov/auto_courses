from django.shortcuts import render
from . import models

def index_page(request):
    blog = models.Blog.objects.all()
    advantages = models.Advantages.objects.all()
    instructions = models.Instructions.objects.all()
    success = models.Success.objects.all()
    instruction1 = models.Instruction1.objects.all()
    courses = models.Course.objects.all()
    context = {
        'blog': blog,
        'adv': advantages,
        'ins': instructions,
        'su': success,
        'i1': instruction1,
        'courses': courses
    }
    return render(request, 'index.html', context)