from django.urls import path

from .views import post_delete, post_detail, post_edit, post_list, post_new

urlpatterns = [
    path("", post_list, name="post_list"),
    path("<int:post_id>/", post_detail, name="post_detail"),
    path("new/", post_new, name="post_new"),
    path("<int:post_id>/edit/", post_edit, name="post_edit"),
    path("<int:post_id>/delete/", post_delete, name="post_delete"),
]
