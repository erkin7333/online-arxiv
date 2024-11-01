from http.client import CannotSendRequest

from rest_framework import serializers
from .models import Category, Folders, DocumentType, Files


class CategorySerializer(serializers.ModelSerializer):
    """
    Barcha kategoriyalarni olish uchun serializer
    """
    class Meta:
        model = Category
        fields = ['id', 'name']


class FoldersSerializer(serializers.ModelSerializer):
    """Papkalrani olish uchun serializer"""
    class Meta:
        model = Folders
        fields = ['id', 'category', 'doc_type', 'number', 'name']


class DocumentTypeSerializer(serializers.ModelSerializer):
    """Hujjatlar turini olish uchun"""
    class Meta:
        model = DocumentType
        fields = ['id', 'name']


class FilesSerializer(serializers.ModelSerializer):
    """
    Fayllarni olish uchun serializer
    """
    document = DocumentTypeSerializer()
    class Meta:
        model = Files
        fields = ['id', 'document', 'calendar', 'file_code', 'file', 'created_at']


class AddFilesSerializer(serializers.ModelSerializer):
    """
    Arxiv fayllarni yuklash uchun serializer
    """
    class Meta:
        model = Files
        fields = ['id', 'folder', 'document', 'calendar', 'file_code', 'file', 'created_at']