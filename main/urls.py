from django.urls import path
from .views import (CategoriesAPIView, FoldersAPIView, AddFoldersAPIView, SearchFolderAPIView,
                    AddDocumentTypeAPIView, GetFilesAPIView, AddFilesAPIView, SearchFilesAPIView)


app_name = 'main'

urlpatterns = [
    path('categories/', CategoriesAPIView.as_view(), name='categories'),

    path('folders/<int:pk>/', FoldersAPIView.as_view(), name='folders'),

    path('add-folders/<int:pk>/', AddFoldersAPIView.as_view(), name='add-folders'),

    path('get-doc-type/', AddDocumentTypeAPIView.as_view(), name='get-doc-type'),

    path('get-file/<int:pk>/', GetFilesAPIView.as_view(), name='get-file'),

    path('add-file/', AddFilesAPIView.as_view(), name='add-file'),

    path('search-file/', SearchFilesAPIView.as_view(), name='search-file'),

    path('search-folder/', SearchFolderAPIView.as_view(), name='search-folder')
]