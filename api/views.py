from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from api.filter import ComputerFilterSet
from api.models import Computer
from api.pagination import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination
from api.serializer import ComputerModelSerializer
from api.throttle import MyThrottle


class UserAPIView(APIView):
    throttle_classes = [MyThrottle]

    def get(self, request, *args, **kwargs):
        return Response("OK")

    def post(self, request):
        return Response("写操作")


class ComputerAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer

    # filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    # search_fields = ["name", "price"]

    ordering = ["price"]

    filter_class = ComputerFilterSet

    # 指定当前视图要使用的分页器
    pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination
