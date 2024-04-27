from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from stocks.serializers import StockSerializer
from stocks.models import Teachers
from rest_framework.views import APIView
from .miniooo import add_pic
from rest_framework.decorators import api_view

class TeachersList(APIView):
    model_class = Teachers
    serializer_class = StockSerializer

    # Возвращает список акций
    def get(self, request, format=None):
        stocks = self.model_class.objects.all()
        serializer = self.serializer_class(stocks, many=True)
        return Response(serializer.data)

    # Добавляет новую акцию
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            stock=serializer.save()
            pic = request.FILES.get("pic")
            pic_result = add_pic(stock, pic)
            # Если в результате вызова add_pic результат - ошибка, возвращаем его.
            if 'error' in pic_result.data:    
                return pic_result
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StockDetail(APIView):
    model_class = Teachers
    serializer_class = StockSerializer

    # Возвращает информацию об акции
    def get(self, request, pk, format=None):
        stock = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(stock)
        return Response(serializer.data)

    # Обновляет информацию об акции (для модератора)
    def put(self, request, pk, format=None):
        stock = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(stock, data=request.data, partial=True)
        # Изменение фото логотипа
        if 'pic' in serializer.initial_data:
            pic_result = add_pic(stock, serializer.initial_data['pic'])
            if 'error' in pic_result.data:
                return pic_result
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Удаляет информацию об акции
    def delete(self, request, pk, format=None):
        stock = get_object_or_404(self.model_class, pk=pk)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Обновляет информацию об акции (для пользователя)    
@api_view(['Put'])
def put(self, request, pk, format=None):
    stock = get_object_or_404(self.model_class, pk=pk)
    serializer = self.serializer_class(stock, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
