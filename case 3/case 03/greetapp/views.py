from django.shortcuts import render
from .forms import VisitorForm



def index(request):
    greeting = ''

    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            visitor = form.save()
            greeting = f'Здравствуйте, {visitor.name}!'
    else:
        form = VisitorForm()

    context = {
        'form': form,
        'greeting': greeting,
    }
    return render(request, 'greetapp/index.html', context)
