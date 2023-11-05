from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CommentForm


@login_required
def add_comment(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.event = event
            comment.save()
            return redirect('event_detail', event_id=event_id)
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form})

