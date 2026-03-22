from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from main.models import Book


class BookListView(ListView):
    model = Book
    template_name = 'main/index.html'
    paginate_by = 10

    def get_queryset(self):
        return Book.objects.select_related('author').all()


class BookDetailView(DetailView):
    model = Book
    template_name = 'main/book_detail.html'
    context_object_name = 'book'
    pk_url_kwarg = 'book_id'

    def get_queryset(self):
        return Book.objects.filter(is_published=True).select_related(
            'author'
        ).prefetch_related('chapters').all()

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        # obj.views_count += 1
        # obj.save(update_fields=['views_count'])
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = context['book']
        chapters = book.chapters.all()
        context['chapters'] = chapters

        chapter_id = self.kwargs.get('chapter_id')
        is_first_page = (chapter_id is None)

        if chapter_id:
            current_chapter = get_object_or_404(chapters, id=chapter_id)
        else:
            current_chapter = chapters.first()

        context['chapter'] = current_chapter
        context['is_first_page'] = is_first_page

        previous_chapter = next_chapter = None
        if current_chapter:
            previous_chapter = chapters.filter(
                order__lt=current_chapter.order
            ).last()
            next_chapter = chapters.filter(
                order__gt=current_chapter.order
            ).first()
        context['previous_chapter'] = previous_chapter
        context['next_chapter'] = next_chapter
        return context
