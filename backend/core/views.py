from django.shortcuts import render
from core.models import *
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from datetime import datetime
from django.utils import timezone
import json

def events(request):
    if request.method == "GET":
        events = Event.objects.all().order_by('start_time')
        events = serializers.serialize('json', events)
        
        return JsonResponse(events, safe = False, json_dumps_params = {'ensure_ascii': False})


def event(request, event_id):
    if request.method == "GET":
        event = Event.objects.get(id = event_id)
        event = serializers.serialize('json', [event])

        return JsonResponse(event, safe = False, json_dumps_params = {'ensure_ascii': False})

    if request.method == "POST":
        event = Event.objects.get(id = event_id)
        live = request.POST.dict()
        live = list(live.keys())[0]
        live = json.loads(live)
        live = live['live']
        event.live = live
        event.save()
        print(event)
        print('saved')
        return HttpResponse('')


def event_players_k(request, event_id):
    if request.method == "GET":
        event = Event.objects.get(id = event_id)
        players_k = Player.objects.filter(events_k = event)
        players_k = serializers.serialize('json', players_k)
        print(players_k)
        return JsonResponse(players_k, safe = False, json_dumps_params = {'ensure_ascii': False})


def event_players_p(request, event_id):
    if request.method == "GET":
        event = Event.objects.get(id = event_id)
        players_p = Player.objects.filter(events_p = event)
        players_p = serializers.serialize('json', players_p)
        print(players_p)
        return JsonResponse(players_p, safe = False, json_dumps_params = {'ensure_ascii': False})


def event_messages(request, event_id):
    if request.method == "GET":
        event = Event.objects.get(id = event_id)
        messages = CheerMessage.objects.filter(event = event).order_by('-time')
        messages = serializers.serialize('json', messages)
        print(messages)
        return JsonResponse(messages, safe = False, json_dumps_params = {'ensure_ascii': False})


def messages(request):
    if request.method == "GET":
        messages = CheerMessage.objects.all().order_by('-time')

        messages = serializers.serialize('json', messages)

        return JsonResponse(messages, safe = False, json_dumps_params = {'ensure_ascii': False})


def videos(request):
    if request.method == "GET":
        videos = Video.objects.all().order_by('-time')
        videos = serializers.serialize('json', videos)
        
        return JsonResponse(videos, safe = False, json_dumps_params = {'ensure_ascii': False})


def video(request, pk):
    if request.method == "GET":
        video = Video.objects.get(id = pk)
        video = serializers.serialize('json', [video])

        return JsonResponse(video, safe = False, json_dumps_params = {'ensure_ascii': False})
