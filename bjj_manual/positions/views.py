from django.shortcuts import render
from .models import Position, Move, Step

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

def move_steps(request, move_id):
    move = Move.objects.get(id=move_id)
    all_steps = move.steps.all()
    return render(request, template_name="move_steps.html", context={"all_steps": all_steps, "move": move})
