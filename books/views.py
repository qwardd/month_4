from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from books.models import Books


def book_detail(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(Books, id=id)
        context = {
            'book_id': book_id
        }
        return render(request, template_name='book_detail.html', context=context)
    


def book_list(request):
    if request.method == 'GET':
        book_list = Books.objects.all().order_by('-id')
        context = {
            'book_list': book_list,
        }
        return render(request, template_name='book.html', context=context)








def book_ru(request):
    if request.method == 'GET':
        return HttpResponse("Русские книги охватывают широкий диапазон жанров и эпох, от древних летописей, таких как «Повесть временных лет», до классических романов XIX века, включая «Евгения Онегина» Пушкина и «Войну и мир» Толстого. Среди наиболее известных произведений также выделяются «Мёртвые души» Гоголя, «Преступление и наказание» Достоевского и «Мастер и Маргарита» Булгакова. Для знакомства с современной русской прозой можно обратить внимание на произведения Евгения Водолазкина, Алексея Сальникова или Владимира Сорокина. ")
    
def book_en(request):
    if request.method == 'GET':
        return HttpResponse("Книги, связанные с Великобританией, включают произведения классической и современной литературы, книги об истории и культуре страны, а также издания о британских традициях и образе жизни. Важными литературными источниками являются произведения таких авторов, как Шекспир, Бронте, Диккенс, а также современные писатели, например, Иэн Макьюэн и Кадзуо Исигуро. Информация о Великобритании также содержится в исторической и культурологической литературе, например, в работах Джорджа Оруэлла и Наташи Лэнг. ")
    
def book_us(request):
    if request.method == "GET":
        return HttpResponse("Книги из США включают в себя американскую классику, такую как Великий Гэтсби и Убить пересмешника а также произведения современных авторов, например, Сюзанну Коллинз и Стивена Кинга. Популярные подборки книг можно найти на сайтах, таких как LiveLib, а также узнать о книгах, изучаемых в американских школах, на сайтах с образовательной тематикой. ")
    

