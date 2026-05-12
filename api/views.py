from .serializers import BookSerializer, CategoryDetailSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from .models import Book, Category
from drf_spectacular.utils import extend_schema, extend_schema_view


@extend_schema(
    summary="Получение списка книг",
    description="Этот эндпоинт позволяет получить список всех книг в базе данных. "
                "Вы также можете добавить новую книгу с помощью POST-запроса.",
    responses={200: BookSerializer(many=True)}
)
class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

@extend_schema(
    summary="Работа с конкретной книгой",
    description="Позволяет получить информацию о книге, обновить её данные или удалить.",
    responses={
        200: BookSerializer,
        204: None
    }
)
class BookDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Представление для работы с отдельной книгой: просмотр, обновление и удаление.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

###
@extend_schema(
    summary="Получение списка категорий книг",
    description="Этот эндпоинт позволяет получить список всех категорий книг в базе данных. "
                "Вы также можете добавить новую категорию с помощью POST-запроса.",
    responses={200: CategoryDetailSerializer(many=True)}
)
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer

###
@extend_schema_view(
       get=extend_schema(
           description="Получение категории с вложенными данными (книги в категории).",
           summary="Детальная категория с книгами"
       )
   )

class CategoryDetailView(RetrieveAPIView):
    """
    Представление для работы с отдельной категорией книг: просмотр, обновление и удаление.
    """
    queryset = Category.objects.prefetch_related('books')
    serializer_class = CategoryDetailSerializer

###   
@extend_schema(
    summary="Работа с конкретной книгой",
    description="Позволяет получить информацию о категории книг, обновить её данные или удалить.",
    responses={
        200: CategoryDetailSerializer,
        204: None
    }
)
class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    """
    Представление для работы с отдельной категорией книг: просмотр, обновление и удаление.
    """
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
