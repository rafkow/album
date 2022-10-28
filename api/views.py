from rest_framework.response import Response
from rest_framework.decorators import api_view
from album.models import Photo
from .serializers import PhotoSerializer, PhotoCreateSerializer
from typing import List
import requests
import shutil


@api_view(['GET'])
def get_photos(request):
    photos = Photo.objects.all()
    result = PhotoSerializer(photos, many=True)
    return Response(result.data)


@api_view(['POST'])
def post_photos(request):
    result = PhotoCreateSerializer(data=request.data, many=True)
    if result.is_valid():
        photo = result.save()
        __save_images(list(photo))
    return Response(result.data)


@api_view(['POST'])
def post_photo(request):
    result = PhotoCreateSerializer(data=request.data)
    if result.is_valid():
        photo = result.save()
        __save_images(list(photo))
    return Response(result.data)


@api_view(['PUT'])
def put_photo(request):
    date = request.date
    photo = Photo.objects.get(date)
    if photo:
        photo.title = request.date['title']
        photo.albumId = request.date['albumId']
        photo.url = request.date['url']
        photo.save()
        __save_image(photo)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)
    return Response({})


async def __save_images(photos: List[Photo]):
    for photo in photos:
        await __save_image(photo)


async def __save_image(photo: Photo):
    url = photo.url if any(ext in photo.url for ext in ['.png', '.jpeg']) else f'{photo.url}.png'
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(f'media/photos/{photo.pk}.png', 'wb+') as file:
            shutil.copyfileobj(response.raw, file)

