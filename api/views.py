from rest_framework.generics import ListCreateAPIView
from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from drf_spectacular.utils import extend_schema
from rest_framework.generics import RetrieveUpdateDestroyAPIView

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

@extend_schema(
    summary="Получение списка категорий книг",
    description="Этот эндпоинт позволяет получить список всех категорий книг в базе данных. "
                "Вы также можете добавить новую категорию с помощью POST-запроса.",
    responses={200: CategorySerializer(many=True)}
)
class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

@extend_schema(
    summary="Работа с конкретной категорией книг",
    description="Позволяет получить информацию о категории, обновить её описание или удалить.",
    responses={
        200: CategorySerializer,
        204: None
    }
)
class CategoryDetailAPIView(RetrieveUpdateDestroyAPIView):
    """
    Представление для работы с отдельной категорией книг: просмотр, обновление и удаление.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer