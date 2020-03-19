from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import Post, Feedback
from .forms import FeedbackForm
from django.core.paginator import Paginator
from django.db.models import Q

class Index(View):
	def get(self, request):
		search_query = request.GET.get('search', '')
		posts = Post.objects.filter(Q(title__icontains=search_query)|Q(body__icontains=search_query)) if search_query else Post.objects.all()

		form = FeedbackForm()
		paginator = Paginator(posts, 5)

		page_number = request.GET.get('page', default=1)
		page = paginator.get_page(page_number)
		is_paginated = page.has_other_pages()
		prev_url = '?page={}'.format(page.previous_page_number()) if page.has_previous() else ''
		next_url = '?page={}'.format(page.next_page_number()) if page.has_next() else ''
		context = {
		'page_object': page,
		'is_paginated': is_paginated,
		'next_url':next_url,
		'prev_url':prev_url,
		'form':form,
		'posts':posts
		}

		return render(request,
			'base.html',
			context=context)

	def post(self, request):
		bound_form = FeedbackForm(request.POST)
		flag = False
		if bound_form.is_valid():
			new = bound_form.save()
			flag = True
		return render(request,
					'createfeedback.html',
					context={'flag':flag})


def projects_list(request):
	return render(request,
				'projects.html',
				context={})

def articles_list(request):
	return render(request,
				'articles.html',
				context={})

class Contacts(View):
 	def get(self, request):
 		form = FeedbackForm()
 		return render(request,
				'contacts.html',
				context={'form':form})


class PostDetail(View):
	def get(self, request, slug):
		post = get_object_or_404(Post, slug__iexact=slug)
		return render(request,
					  'post_detail.html',
					  context={'post':post})

	def post(self, request, slug):
		post = get_object_or_404(Post, slug__iexact=slug)
		return render(request,
					  'post_detail.html',
					  context={'post':post})
