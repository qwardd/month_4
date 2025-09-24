from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from books.models import Books
from django.core.paginator import Paginator
from  django.views import generic




class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'
    context_object_name = 'book_id'

    def get_object(self, *args, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(Books, id=book_id)


class BookListView(generic.ListView):
    model = Books
    template_name = 'book.html'
    context_object_name = 'book_list'
    ordering = ['-id']

    def get_queryset(self):
        return Books.objects.all()


class BookruPageView(generic.View):
    def get(self, request):
        return HttpResponse("Русские книги охватывают широкий диапазон жанров и эпох, от древних летописей, таких как «Повесть временных лет», до классических романов XIX века, включая «Евгения Онегина» Пушкина и «Войну и мир» Толстого. Среди наиболее известных произведений также выделяются «Мёртвые души» Гоголя, «Преступление и наказание» Достоевского и «Мастер и Маргарита» Булгакова. Для знакомства с современной русской прозой можно обратить внимание на произведения Евгения Водолазкина, Алексея Сальникова или Владимира Сорокина. ")
    
class BookenPageView(generic.View):
    def get(self, request):
        return HttpResponse("Книги, связанные с Великобританией, включают произведения классической и современной литературы, книги об истории и культуре страны, а также издания о британских традициях и образе жизни. Важными литературными источниками являются произведения таких авторов, как Шекспир, Бронте, Диккенс, а также современные писатели, например, Иэн Макьюэн и Кадзуо Исигуро. Информация о Великобритании также содержится в исторической и культурологической литературе, например, в работах Джорджа Оруэлла и Наташи Лэнг. ")
    
class BookusPageView(generic.View):
    def get(self, request):
        return HttpResponse("Книги из США включают в себя американскую классику, такую как Великий Гэтсби и Убить пересмешника а также произведения современных авторов, например, Сюзанну Коллинз и Стивена Кинга. Популярные подборки книг можно найти на сайтах, таких как LiveLib, а также узнать о книгах, изучаемых в американских школах, на сайтах с образовательной тематикой. ")
    
        

    









