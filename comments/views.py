from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.contrib import messages
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
            messages.success(request, f'You added a comment')

            # Return a JSON response indicating success
            return JsonResponse({
                'success': True,
                'user': comment.user.user.username,
                'date': comment.created_at,
                'text': comment.text,
                'id': comment.id,
            })

        # Return a JSON response indicating failure
        return JsonResponse({'success': False, 'error': 'Invalid form data'})

    return JsonResponse({'success': False, 'error': 'Invalid request method'})


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
    messages.success(request, f'You liked a comment')
    return JsonResponse({'liked': liked, 'like_count': like_count})


@login_required
def delete_comment(request, comment_id):
    try:
        comment = Comment.objects.get(pk=comment_id)

        # Check if the user is authorized to delete the comment
        if comment.user == request.user.userprofile or request.user.is_superuser:
            comment.delete()
            messages.success(request, f'Successfully deleted comment')
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'You are not authorized to delete this comment.'})
    except Comment.DoesNotExist:
        return JsonResponse({'success': False, 'error': 'Comment does not exist.'})
