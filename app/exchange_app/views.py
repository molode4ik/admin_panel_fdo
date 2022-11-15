from django.shortcuts import render


def exchange(request):
    world = 'World'
    context = {
        'world': world,
    }
    return render(request=request, template_name='exchange_app/index.html', context=context)
