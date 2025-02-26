from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Post

# Create your views here.


# 게시글 목록 보기
def post_list(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all().order_by("-created_at")
    return render(request, "blog/post_list.html", {"posts": posts})


# 게시글 상세보기
def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})


# 게시글 작성
def post_new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        title: str = request.POST.get("title", "")  # 기본 빈 문자열 추가
        content: str = request.POST.get("content", "")
        Post.objects.create(title=title, content=content)
        return redirect("post_list")
    return render(request, "blog/post_form.html")


# 게시글 수정
def post_edit(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.title = request.POST.get("title", post.title) or post.title  # None 방지
        post.content = request.POST.get("content", post.content) or post.content  # None 방지
        post.save()
        return redirect("post_detail", post_id=post_id)
    return render(request, "blog/post_form.html", {"post": post})


# 게시글 삭제
def post_delete(request: HttpRequest, post_id: int) -> HttpResponse:
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect("post_list")
