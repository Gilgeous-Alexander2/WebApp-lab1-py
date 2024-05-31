from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import When,Case
from rest_framework import status
from stocks.serializers import StockSerializer
from stocks.serializers import FullStockSerializer,UserSerializer,SubjectSerializer,UslugiSerializer, FullUserSerializer
from rest_framework import viewsets
from stocks.models import Stock,AppUser
from stocks.models import AuthUser,Teacher,Subject,Uslugi
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes, authentication_classes
from .miniooo import add_pic 
import datetime
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import SessionAuthentication
from stocks.permissions import IsAdmin, IsTeacher, IsUser

from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework import permissions, status
from .validations import custom_validation, validate_email, validate_password

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from rest_framework.permissions import AllowAny
from django.views.decorators.csrf import csrf_exempt





# def user(userid):
#     try:
#         user1 = AuthUser.objects.get(id=userid)
#     except:
#         user1 = AuthUser(id=1, first_name="Иван", last_name="Иванов", password=1234)
#         user1.save()
#     return user1
# def teacher(teacherid):
#     try:
#         teacher1 = Teacher.objects.get(id=teacherid)
#     except:
#         teacher1 = Teacher(id=1, first_name="Иван", last_name="Иванов", password=1234)
#         teacher1.save()
#     return teacher1
# def uslugi1(uslugaid):
#     uslugii = []
#     for i in range(len(uslugaid)):
#         uslugii.append(Uslugi.objects.get(id=uslugaid))
#     return uslugii

   

class StockList(APIView):
    model_class = Stock
    serializer_class = StockSerializer

    def get(self, request, format=None):
        stocks = self.model_class.objects.all()
        serializer = self.serializer_class(stocks, many=True)
        return Response(serializer.data)

class PostStock(APIView):
    queryset = Stock.objects.all()
    model_class = Stock
    serializer_class = StockSerializer
    permission_classes = [IsUser]
    

    @swagger_auto_schema(request_body=StockSerializer)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():

            stock=serializer.save()
            
            # user1 = user(stock.userid)
            # teacher1 = teacher(stock.teacherid)
            # # Назначаем создателем акции польователя user1
            # stock.user = user1
            # stock.teacher = teacher1
            stock.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class StockDetail(APIView):
    queryset = Stock.objects.all()
    model_class = Stock
    serializer_class = FullStockSerializer


    def get_queryset(self):
        user = self.request.user
        if user.role == 'teacher':
            return Stock.objects.filter(teacher=user)
        return Stock.objects.filter(user=user)
    

    def get(self, request, pk, format=None):
        stock = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(stock)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=FullStockSerializer)
    def put(self, request, pk, format=None):
        stock = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(stock, data=request.data, partial=True)
        if serializer.is_valid():
            # if stock.status == "Завершено" or stock.status == "Отклонено" :
            #     stock.end_date = datetime.datetime.now()
            #     stock.is_active = False
            stock.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stock = get_object_or_404(self.model_class, pk=pk)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@swagger_auto_schema(method='put', request_body=StockSerializer)
@api_view(['Put'])
def put_detail(self,request, pk, format=None):
    stock = get_object_or_404(self.model_class, pk=pk)
    serializer = self.serializer_class(stock, data=request.data, partial=True)
    if 'pic' in serializer.initial_data:
        pic_result = add_pic(stock, serializer.initial_data['pic'])
        if 'error' in pic_result.data:
            return pic_result
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





# class UsersList(APIView):
#     model_class = AuthUser
#     serializer_class = UserSerializer

#     def get(self, request, format=None):
#         user = self.model_class.objects.all()
#         serializer = self.serializer_class(user, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class TeachersList(APIView):
#     model_class = Teacher
#     serializer_class = TeacherSerializer

#     def get(self, request, format=None):
#         user = self.model_class.objects.all()
#         serializer = self.serializer_class(user, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
# class TeacherDetail(APIView):
#     model_class = Teacher
#     # serializer_class = FullTeacherSerializer

#     def get(self, request, pk, format=None):
#         teacher = get_object_or_404(self.model_class, pk=pk)
#         serializer = self.serializer_class(teacher)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         teacher = get_object_or_404(self.model_class, pk=pk)
#         serializer = self.serializer_class(teacher, data=request.data, partial=True)
#         if serializer.is_valid():
#             teacher.save()
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         stock = get_object_or_404(self.model_class, pk=pk)
#         stock.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class SubjectsList(APIView):
    model_class = Subject
    serializer_class = SubjectSerializer

    def get(self, request, format=None):
        subject = self.model_class.objects.all()
        serializer = self.serializer_class(subject, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=SubjectSerializer)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            subject=serializer.save()
            subject.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SubjectsDetail(APIView):
    model_class = Subject
    serializer_class = SubjectSerializer

    def get(self, request, id, format=None):
        usluga = get_object_or_404(self.model_class, id=id)
        serializer = self.serializer_class(usluga)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        usluga = get_object_or_404(self.model_class, id=id)
        serializer = self.serializer_class(usluga, data=request.data, partial=True)
        if 'pic' in serializer.initial_data:
            pic_result = add_pic(usluga, serializer.initial_data['pic'])
            if 'error' in pic_result.data:
                return pic_result
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id, format=None):
        stock = get_object_or_404(self.model_class, id=id)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UslugiList(APIView):
    model_class = Uslugi
    serializer_class = UslugiSerializer


    def get(self, request, format=None):
        usluga = self.model_class.objects.all()
        serializer = self.serializer_class(usluga, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            usluga = serializer.save()
            pic = request.FILES.get("pic")
            pic_result = add_pic(usluga, pic)
            # Если в результате вызова add_pic результат - ошибка, возвращаем его.
            if 'error' in pic_result.data:    
                return pic_result
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    
class UslugiDetail(APIView):
    model_class = Uslugi
    serializer_class = UslugiSerializer

    def get(self, request, pk, format=None):
        usluga = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(usluga)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        usluga = get_object_or_404(self.model_class, pk=pk)
        serializer = self.serializer_class(usluga, data=request.data, partial=True)
        if 'pic' in serializer.initial_data:
            pic_result = add_pic(usluga, serializer.initial_data['pic'])
            if 'error' in pic_result.data:
                return pic_result
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        stock = get_object_or_404(self.model_class, pk=pk)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserRegister(APIView):
    @swagger_auto_schema(request_body=UserRegisterSerializer)
    def post(self, request,format=None):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):

    authentication_classes = (SessionAuthentication,)

    @swagger_auto_schema(request_body=UserLoginSerializer)
    def post(self, request,format=None):
        data = request.data
        assert validate_email(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)

# class PostStock(APIView):
#     model_class = Stock
#     serializer_class = StockSerializer

#     @swagger_auto_schema(request_body=StockSerializer)
#     def post(self, request, format=None):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             stock=serializer.save()
#             # user1 = user(stock.userid)
#             # teacher1 = teacher(stock.teacherid)
#             # # Назначаем создателем акции польователя user1
#             # stock.user = user1
#             # stock.teacher = teacher1
#             stock.save()
            
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

class UserLogout(APIView):
	# permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):

    # permission_classes = (IsUser)

    model_class=AppUser
    authentication_classes = (SessionAuthentication,)
	##
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
    def delete(self, request, format=None):
        stock = get_object_or_404(self.model_class)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    
    
    
class UsersList(APIView):
    model_class = AppUser
    serializer_class = UserSerializer

    def get(self, request, format=None):
        user = self.model_class.objects.all().filter()
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
    
class UsersDetail(APIView):
    model_class = AppUser
    serializer_class = FullUserSerializer

    def get(self, request, user_id, format=None):
        user = get_object_or_404(self.model_class, user_id=user_id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        user = get_object_or_404(self.model_class, user_id=user_id)
        serializer = self.serializer_class(self.model_class, data=request.data, partial=True)
        if serializer.is_valid():
            user.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        user = get_object_or_404(self.model_class, user_id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class TeachersList(APIView):
    model_class = AppUser
    serializer_class = UserSerializer

    def get(self, request, format=None):
        user = self.model_class.objects.all().filter(role="teacher")
        serializer = self.serializer_class(user, many=True)
        return Response(serializer.data)
    
class TeachersDetail(APIView):
    model_class = AppUser
    serializer_class = FullUserSerializer

    def get(self, request, user_id, format=None):
        user = get_object_or_404(self.model_class, user_id=user_id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def put(self, request, user_id, format=None):
        user = get_object_or_404(self.model_class, user_id=user_id)
        serializer = self.serializer_class(self.model_class, data=request.data, partial=True)
        if serializer.is_valid():
            user.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, format=None):
        user = get_object_or_404(self.model_class, user_id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)