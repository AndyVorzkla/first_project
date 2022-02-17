from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def main_view(request):
    return render(request, 'index.html', context={})


def tour_view(request, id: int):
    return render(request, 'tour.html', context={})


def departure_view(request, departure: str):
    return render(request, 'departure.html', context={})


def custom_handler404(request, exception):
    return HttpResponseNotFound('404 ошибка!')


def custom_handler500(request):
    return HttpResponseServerError('500 ошибка!')
