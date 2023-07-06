import os
import shutil
import tempfile
import zipfile
from dateutil.relativedelta import relativedelta
from django.core.files import File
from django.db.models import FileField
from django.shortcuts import render
from django.utils.timezone import now
from rest_framework.decorators import action
from rest_framework.utils import json
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .utils import *
from .models import DbDownload
from .serializers import DocumentSerializer
import sqlite3

# ViewSets define the view behavior.
class DocumentViewSet(ModelViewSet):
    queryset = DbDownload.objects.all()
    serializer_class = DocumentSerializer

    @action(methods=['post'], detail=False)
    def post(self, request):
        data = request.data
        row_for_check_ip = DbDownload.objects.filter(ip=data['ip'])
        
        if row_for_check_ip.exists():
            row_for_check_ip = row_for_check_ip.last()
            delta = relativedelta(now(), row_for_check_ip.time_create)
            if delta.minutes >= 30:
                content, status = main_unpacker(data)
                return Response({'post': content}, status=status)

            else:
                return Response({'post': 'Превышен лимит допустимых загрузок (2 загрузки в 1 час)'}, status=202)
        else:
            content, status = main_unpacker(data)
            return Response({'post': content}, status=status)
