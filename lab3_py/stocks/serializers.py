from stocks.models import Stock
from stocks.models import AuthUser,Teacher,Subject,Uslugi
from rest_framework import serializers
from collections import OrderedDict



class UslugiSerializer(serializers.ModelSerializer):

    class Meta:
        model = Uslugi
        fields = ["id","name","url"]


class StockSerializer(serializers.ModelSerializer):

    # uslugi_set = UslugiSerializer(many=True,read_only=True)

    class Meta:
        # Модель, которую мы сериализуем
        model = Stock
        # Поля, которые мы сериализуем
        fields = ["pk", "status","date_and_time","create_date","change_date","end_date","is_active","user","teacher","uslugi"]

        def get_fields(self):
            new_fields = OrderedDict()
            for name, field in super().get_fields().items():
                field.required = False
                new_fields[name] = field
            return new_fields 

class FullStockSerializer(serializers.ModelSerializer):
    # StringRelatedField вернет строковое представление объекта, то есть его имя
    user = serializers.StringRelatedField()
    # uslugi_set = UslugiSerializer(many=True,read_only=True)

    class Meta:
        model = Stock
        # Сериализуем все поля
        fields = ["pk","status", "date_and_time","create_date","change_date","end_date","is_active","user","teacher","uslugi"]


class UserSerializer(serializers.ModelSerializer):
    stock_set = StockSerializer(many=True, read_only=True)

    class Meta:
        model = AuthUser
        fields = ["id", "first_name", "last_name", "stock_set"]



class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ["id","name","teacher"]
      


class TeacherSerializer(serializers.ModelSerializer):
    stock_set = StockSerializer(many=True, read_only=True)
    subject_set = SubjectSerializer(many=True, read_only=True)


    class Meta:
        model = Teacher
        fields = ["id", "first_name", "last_name", "stock_set","subject_set"]

class FullTeacherSerializer(serializers.ModelSerializer):
    # StringRelatedField вернет строковое представление объекта, то есть его имя
    # uslugi_set = UslugiSerializer(many=True,read_only=True)

    subject_set = SubjectSerializer(many=True, read_only=True)
    stock_set = StockSerializer(many=True, read_only=True)


    class Meta:
        model = Teacher
        # Сериализуем все поля
        fields = ["id", "first_name", "last_name", "stock_set","subject_set"]


