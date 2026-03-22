from django.urls import path
from main.views import BookListView, BookDetailView

app_name = 'main'

urlpatterns = [
    path('', BookListView.as_view(), name='index'),
    path('book/<int:book_id>/', BookDetailView.as_view(), name='detail'),
    path(
        'book/<int:book_id>/chapter/<int:chapter_id>/',
        BookDetailView.as_view(),
        name='chapter_detail',
    ),
]
