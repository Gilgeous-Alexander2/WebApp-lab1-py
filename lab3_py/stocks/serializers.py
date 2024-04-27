from stocks.models import Teachers
# from stocks.models import AuthUser
from rest_framework import serializers


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        # Модель, которую мы сериализуем
        model = Teachers
        # Поля, которые мы сериализуем
        fields = ["id","first_name","second_name","degree1","degree2","url"]

        