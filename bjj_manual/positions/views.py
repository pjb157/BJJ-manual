from django.shortcuts import render
from django.http import HttpResponse
from .models import Position, Move

# Create your views here.
def index(request):
    all_positions = Position.objects.all()
    return render(request, template_name="home.html", context={"all_positions": all_positions})

def position_options(request, position_id):
    # position = Position.objects.get(id=position_id)
    # all_moves = Move.objects.filter(position_id=position_id)

    position = Position.objects.get(id=position_id)
    all_moves = position.moves.all()
    return render(request, template_name="position_options.html", context={"all_moves": all_moves, "position": position})