from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from itertools import chain

from . import forms, models


@login_required()
def home(request):
    """
    Function working on the feed of the blog
    """
    user_follows = request.user.following
    following_users_ids = list(user_follows.values_list('followed_user', flat=True))
    following_users_ids.append(request.user.id)

    tickets = models.Ticket.objects.filter(user_id__in=following_users_ids).annotate(review_count=Count('review'))
    reviews = models.Review.objects.filter(user_id__in=following_users_ids)

    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )

    paginator = Paginator(posts, 5)
    page = request.GET.get('page')

    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'blog/home.html', context=context)


@login_required()
def create_ticket(request):
    """
    Function creating a ticket
    """
    ticket_form = forms.TicketForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
        return redirect('home')
    return render(request, 'blog/create_ticket.html', {'ticket_form': ticket_form})


@login_required
def edit_ticket(request, ticket_id):
    """
    Function editing a ticket
    """
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    edit_form = forms.TicketForm(instance=ticket)
    delete_form = forms.DeleteTicketForm()
    if request.method == 'POST':
        if 'edit_ticket' in request.POST:
            edit_form = forms.TicketForm(request.POST, request.FILES, instance=ticket)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_ticket' in request.POST:
            delete_form = forms.DeleteTicketForm(request.POST)
            if delete_form.is_valid():
                ticket.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        }

    return render(request, 'blog/edit_ticket.html', context=context)


@login_required()
def create_review(request, ticket_id):
    """
    Function creating a review for an existing ticket
    """
    ticket = get_object_or_404(models.Ticket, id=ticket_id)
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        review_form = forms.ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
        return redirect('home')

    context = {
        'review_form': review_form,
        'ticket': ticket
    }

    return render(request, 'blog/create_review.html', context=context)


@login_required
def edit_review(request, review_id):
    """
    Function editing an existing review
    """
    review = get_object_or_404(models.Review, id=review_id)
    edit_form = forms.ReviewForm(instance=review)
    delete_form = forms.DeleteReviewForm()
    if request.method == 'POST':
        if 'edit_review' in request.POST:
            edit_form = forms.ReviewForm(request.POST, instance=review)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('home')
        if 'delete_review' in request.POST:
            delete_form = forms.DeleteReviewForm(request.POST)
            if delete_form.is_valid():
                review.delete()
                return redirect('home')
    context = {
        'edit_form': edit_form,
        'delete_form': delete_form,
        'ticket': review.ticket
        }

    return render(request, 'blog/edit_review.html', context=context)


@login_required()
def create_ticket_and_review(request):
    """
    Function creating a ticket and a review at the same time
    """
    ticket_form = forms.TicketForm()
    review_form = forms.ReviewForm()
    if request.method == 'POST':
        ticket_form = forms.TicketForm(request.POST, request.FILES)
        review_form = forms.ReviewForm(request.POST)
        if all([ticket_form.is_valid(), review_form.is_valid()]):
            ticket = ticket_form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            review = review_form.save(commit=False)
            review.user = request.user
            review.ticket = ticket
            review.save()
            return redirect('home')
    context = {
        "ticket_form": ticket_form,
        "review_form": review_form,
        }

    return render(request, 'blog/create_ticket_and_review.html', context=context)


@login_required
def follow_user(request):
    """
    Function to be able to follow an user 
    """
    user = request.user
    following = request.user.following.all()
    followers = request.user.followers.all()
    followed_users_ids = following.values_list('followed_user', flat=True)
    all_users = get_user_model().objects.exclude(id__in=followed_users_ids).exclude(id=request.user.id)
    search_form = forms.SearchUserForm(request.GET)
    searched_users = None

    if search_form.is_valid():
        searched_username = search_form.cleaned_data["username"]
        searched_users = all_users.filter(username__icontains=searched_username)

    if request.method == "POST":
        user_to_follow = get_object_or_404(get_user_model(), id=request.POST.get('user_id'))
        models.UserFollows.objects.create(user=request.user, followed_user=user_to_follow)

    context = {
        "user": user,
        "following": following,
        "followers": followers,
        "search_form": search_form,
        "searched_users": searched_users
    }

    return render(request, 'blog/follow_user.html', context=context)


@login_required
def unfollow(request):
    """
    Function unfollowing an user
    """

    user_id = request.POST.get('user_id')
    user_to_follow = get_object_or_404(get_user_model(), id=user_id)
    follow_object = models.UserFollows.objects.filter(user=request.user, followed_user=user_to_follow)

    if follow_object.exists():
        follow_object.delete()

    return redirect('follow_user')


@login_required
def my_posts(request):
    """
    Function showing only the post of the logged user
    """

    tickets = models.Ticket.objects.filter(user=request.user).annotate(review_count=Count('review'))
    reviews = models.Review.objects.filter(user=request.user)

    posts = sorted(
        chain(tickets, reviews),
        key=lambda post: post.time_created,
        reverse=True
    )

    paginator = Paginator(posts, 5)
    page = request.GET.get('page')

    page_obj = paginator.get_page(page)

    context = {
        'page_obj': page_obj
    }

    return render(request, 'blog/my_posts.html', context=context)
