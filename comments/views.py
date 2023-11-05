from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm
from .models import Comment


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

    comments = Comment.objects.filter(event=event)

    return render(request, 'events/event_detail.html', {'event': event, 'form': form, 'comments': comments})


@login_required
def like_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    user_profile = request.user.userprofile

    if user_profile in comment.likes.all():
        comment.likes.remove(user_profile)
        liked = False
    else:
        comment.likes.add(user_profile)
        liked = True

    return JsonResponse({"liked": liked, "like_count": comment.likes.count})


@login_required
def add_reply(request, comment_id):
    parent_comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.event = parent_comment.event
            reply.parent_comment = parent_comment
            reply.save()
            return redirect('event_detail', event_id=parent_comment.event.pk)
    else:
        form = CommentForm()
    return render(request, 'comments/add_reply.html', {'form': form, 'parent_comment': parent_comment})
