from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from .models import Post
# Create your views here.

def index(request):
	lastest_post_list=Post.objects.order_by('-date')[:5]
	context={'lastest_post_list' : lastest_post_list}
	return render(request,'posts/index.html',context)

def detail(request, post_id):
	post=get_object_or_404(Post, pk=post_id)
	return render(request,'posts/detail.html',{'post' : post})

def comment(request, post_id):
	p=get_object_or_404(Post, pk=post_id)

	if request.POST['comment'] == '':
		return render(request, 'post/detail.html', {
			'post' : p, 
			'error_message' : "El mensaje esta en blanco",
			})
	else:
		p.comment_set.create(text=request.POST['comment'], date=timezone.now(), user=request.user)
		return HttpResponseRedirect(reverse('posts:detail', args=(p.id,)))
