from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path(
        "<int:year>/<int:month>/<int:day>/<slug:post>/",
        views.post_detail,
        name="post_detail",
    ),
    path(
        "<int:post_id>/share/",
        views.PostShareView.as_view(),
        name="post_share",
    ),
    path("<int:post_id>/comment/", views.add_comment, name="add_comment"),
    path(
        "tag/<slug:tag_slug>/",
        views.PostListByTagview.as_view(),
        name="post_list_by_tag",
    ),
]
