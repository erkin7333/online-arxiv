from time import sleep

from django.db import models
from account.models import User


class Category(models.Model):
    """Kategoruyalar uchun model"""
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = "Kategoriyalar"


class Folders(models.Model):
    """Kategoriyalar uchun papkalar modeli"""
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name="Kategoriya")
    number = models.CharField(max_length=25, verbose_name="Papke nomeri")
    name = models.CharField(max_length=500, verbose_name="Papka nomi")
    doc_type = models.BooleanField(default=False, verbose_name="Hujjat turi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")

    def __str__(self):
        return f"{self.category} -- {self.name}"

    class Meta:
        verbose_name = "Papka"
        verbose_name_plural = "Papkalar"


class DocumentType(models.Model):
    """Hujjat turlari"""

    name = models.CharField(max_length=200, verbose_name="Hujjat turi")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Hujjat turi"
        verbose_name_plural = "Hujjat turlari"


class Files(models.Model):
    """Fayillar uchun model"""

    folder = models.ForeignKey(Folders, on_delete=models.SET_NULL, blank=True, null=True,
                               verbose_name="Papka")
    document = models.ForeignKey(DocumentType, on_delete=models.SET_NULL, blank=True, null=True,
                                 verbose_name="Hujjat turi")
    calendar = models.CharField(max_length=25, verbose_name="Hujjat sanasi", blank=True, null=True)
    file_code = models.CharField(max_length=20, verbose_name="Fayl kodi")
    file = models.FileField(verbose_name='Fayil', upload_to="file/%Y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Kiritilgan vaqti")

    def __str__(self):
        return self.file_code

    class Meta:
        verbose_name = "Fayil"
        verbose_name_plural = "Fayillar"