from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.http import JsonResponse
from .models import Comment
from .forms import CommentForm
from events.models import Event


@login_required
def add_comment(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            # Make sure userprofile is correctly linked to your User model
            comment.user = request.user.userprofile
            comment.event = event
            comment.save()
            return redirect('events:event_detail', event_id=event_id)
    else:
        form = CommentForm()
    return redirect('events:event_detail', event_id=event_id)


def like_comment(request):
    if request.method == 'POST':
        comment_id = request.POST.get('comment_id')
        comment = get_object_or_404(Comment, pk=comment_id)

        # Implement your logic to handle liking comments here
        # For example, you can toggle a like status and update the like count

        # Example: Toggle like status
        user = request.user
        if user in comment.likes.all():
            comment.likes.remove(user)
            liked = False
        else:
            comment.likes.add(user)
            liked = True

        like_count = comment.likes.count()

        return JsonResponse({'liked': liked, 'like_count': like_count})
