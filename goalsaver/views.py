"""goalsaver Views."""

from django.shortcuts import render

def render_index(request):
    return render(request, 'goalsaver/index.html')
