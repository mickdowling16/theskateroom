from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from .models import Comment
from .forms import CommentForm
from events.models import Event
from profiles.models import UserProfile
from django.contrib.auth.decorators import login_required


@login_required
def add_comment(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user.userprofile
            comment.event = event
            comment.save()

            # Return a JSON response indicating success
            return JsonResponse({
                'success': True,
                'user': comment.user.username,
                'date': comment.created_at,
                'text': comment.text,
                'id': comment.id,
            })

            return redirect('events:event_detail', event_id=event_id)
        else:
            # Return a JSON response indicating failure
            return JsonResponse({'success': False})

    return redirect('events:event_detail', event_id=event_id)


@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    user = request.user
    if user in comment.likes.all():
        comment.likes.remove(user)
        liked = False
    else:
        comment.likes.add(user)
        liked = True
    like_count = comment.likes.count()
    return JsonResponse({'liked': liked, 'like_count': like_count})
