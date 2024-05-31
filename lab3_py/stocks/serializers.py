from stocks.models import Stock
from stocks.models import AuthUser,Teacher,Subject,Uslugi,AppUser
from rest_framework import serializers
from django.core.exceptions import ValidationError

from collections import OrderedDict
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate


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
        
    def validate(self, data):
        if data['user'].role != 'user':
            raise serializers.ValidationError("Только студенты могут создавать заявки.")
        if data['teacher'].role != 'teacher':
            raise serializers.ValidationError("Заявки могут быть отправлены только преподавателям.")
        return data
        
    

class FullStockSerializer(serializers.ModelSerializer):
    # StringRelatedField вернет строковое представление объекта, то есть его имя
    user = serializers.StringRelatedField()
    # uslugi_set = UslugiSerializer(many=True,read_only=True)

    class Meta:
        model = Stock
        # Сериализуем все поля
        fields = ["pk","status", "date_and_time","create_date","change_date","end_date","is_active","user","teacher","uslugi"]

    def validate(self, data):
        if data['user'].role != 'user':
            raise serializers.ValidationError("Только студенты могут создавать заявки.")
        if data['teacher'].role != 'teacher':
            raise serializers.ValidationError("Заявки могут быть отправлены только преподавателям.")
        return data


# class UserSerializer(serializers.ModelSerializer):
#     stock_set = StockSerializer(many=True, read_only=True)

#     class Meta:
#         model = AuthUser
#         fields = ['first_name' , 'last_name','password','stock_set']



class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ["id","name","teacher"]
      
    def validate(self, data):
        if data['teacher'].role != 'teacher':
            raise serializers.ValidationError("Только преподавателю можно назначить предмет.")
        return data


# class TeacherSerializer(serializers.ModelSerializer):
#     stock_set = StockSerializer(many=True, read_only=True)
#     subject_set = SubjectSerializer(many=True, read_only=True)


#     class Meta:
#         model = Teacher
#         fields = ["id", "first_name", "last_name", "stock_set","subject_set"]

# class FullTeacherSerializer(serializers.ModelSerializer):
#     # StringRelatedField вернет строковое представление объекта, то есть его имя
#     # uslugi_set = UslugiSerializer(many=True,read_only=True)

#     subject_set = SubjectSerializer(many=True, read_only=True)
#     stock_set = StockSerializer(many=True, read_only=True)


#     class Meta:
#         model = Teacher
#         # Сериализуем все поля
#         fields = ["id", "first_name", "last_name", "stock_set","subject_set"]


UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
     
	class Meta:
		model = AppUser
		fields = '__all__'
	def create(self, clean_data):
		user_obj = UserModel.objects.create_user(email=clean_data['email'], password=clean_data['password'],role=clean_data['role'])
		user_obj.save()
		return user_obj

class UserLoginSerializer(serializers.Serializer):
	email = serializers.EmailField()
	password = serializers.CharField()
	##
	def check_user(self, clean_data):
		user = authenticate(email=clean_data['email'], password=clean_data['password'])
		if not user:
			raise ValidationError('user not found')
		return user

class UserSerializer(serializers.ModelSerializer):

    user_stocks = StockSerializer(many=True, read_only=True)
    teacher_stocks = StockSerializer(many=True, read_only=True)
    teacher_subjects = SubjectSerializer(many=True,read_only=True)


    class Meta:
        model = AppUser
        fields = ["user_id","email", "is_superuser","role","user_stocks","teacher_stocks","teacher_subjects"]

class FullUserSerializer(serializers.ModelSerializer):
    # StringRelatedField вернет строковое представление объекта, то есть его имя
    # uslugi_set = UslugiSerializer(many=True,read_only=True)

    # subject_set = SubjectSerializer(many=True, read_only=True)
    user_stocks = StockSerializer(many=True, read_only=True)
    teacher_stocks = StockSerializer(many=True, read_only=True)
    teacher_subjects = SubjectSerializer(many=True,read_only=True)

    class Meta:
        model = AppUser
        # Сериализуем все поля
        fields = ["user_id","role", "user_stocks","teacher_stocks","teacher_subjects"]