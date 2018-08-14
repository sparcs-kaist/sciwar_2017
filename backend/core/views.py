# from django.views.decorators.csrf import csrf_exempt
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


# @csrf_exempt
def event(request, event_id):
    if request.method == "GET":
        event = Event.objects.get(id = event_id)
        event = serializers.serialize('json', [event])

        return JsonResponse(event, safe = False, json_dumps_params = {'ensure_ascii': False})

    if request.method == "POST":
        event = Event.objects.get(id = event_id)
        data = request.POST
        data = list(data.keys())[0]
        data = json.loads(data)
        live = data['live']
        score_k = int(data['score_k'])
        score_p = int(data['score_p'])
        pk = data['pk']
        winner = data['winner']
        event.live = live
        event.score_k = score_k
        event.score_p = score_p
        event.winner = winner
        event.save()

        if live == 2:
            # Toto score update
            totos = event.totos.all()
            for toto in totos:
                if event.type == 0:
                    if score_k == toto.score_k and score_p == toto.score_p:
                        toto.bet.total += event.score_weight
                if winner == toto.winner:
                    toto.bet.total += event.win_weight
                toto.bet.save()

        # Live video
        videos = event.video_set.all()
        for video in videos:
            if len(video.event.filter(live=1)) == 0:
                video.type = 1
            else:
                video.type = 0
            video.save()

        return HttpResponse('')


# @csrf_exempt
def rescore_toto(request):
    if request.method == "POST":
        totos = TotoContent.objects.all()
        hacking_event = Event.objects.get(name_eng = "Hacking")
        ai_event = Event.objects.get(name_eng = "AI")
        for toto in all_totoes:
            hacking_toto = toto.hacking_toto.all()[0]
            ai_toto = toto.ai_toto.all()[0]
            if hacking_event.winner == hacking_toto.winner:
                toto.total -= 1
            if ai_event.winner == ai_toto.winner:
                toto.total -= 1
            if ai_event.score_k == ai_toto.score_k and ai_event.score_p == ai_toto.score_p:
                toto.total -= 0.2
            toto.save()
        print(1)

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
        messages = CheerMessage.objects.filter(event = event)
        messages = serializers.serialize('json', messages)
        print(messages)
        return JsonResponse(messages, safe = False, json_dumps_params = {'ensure_ascii': False})


# @csrf_exempt
def messages(request):
    if request.method == "GET":
        messages = CheerMessage.objects.all()

        messages = serializers.serialize('json', messages)

        return JsonResponse(messages, safe = False, json_dumps_params = {'ensure_ascii': False})


    if request.method == "PUT":
        data = json.loads(request.body)
        cheerMessage = CheerMessage(content = data['content'], school = data['school'])
        cheerMessage.event_id = data['event']
        cheerMessage.save()

        return HttpResponse('')


def messageLike(request, pk):
    if request.method == "POST":
        data = json.loads(request.body)
        message = CheerMessage.objects.get(id=pk)
        if (data['add']):
            message.likes += 1
        else:
            message.likes -= 1
        message.save()

        return HttpResponse('')


# @csrf_exempt
def videos(request):
    if request.method == "GET":
        videos = Video.objects.all().order_by('-time')
        videos = serializers.serialize('json', videos)

        return JsonResponse(videos, safe = False, json_dumps_params = {'ensure_ascii': False})

    if request.method == "PUT":
        data = json.loads(request.body)
        events = []
        for i in data['event']:
            events.append(Event.objects.get(id = i))
        video = Video()
        video.link = data['source']
        video.name = data['title']
        video.type = int(data['type'])
        video.save()
        video.event = events
        video.save()

        return HttpResponse('')


# @csrf_exempt
def video(request, pk):
    if request.method == "GET":
        video = Video.objects.get(id = pk)
        video = serializers.serialize('json', [video])

        return JsonResponse(video, safe = False, json_dumps_params = {'ensure_ascii': False})

    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        video = Video.objects.get(id = pk)
        video.type = data['type']
        video.save()

        return HttpResponse('')

    if request.method == "DELETE":
        video = Video.objects.get(id = pk).delete()

        return HttpResponse('')


def supporters(request):
    if request.method == "GET":
        supporter_teams = SupporterTeam.objects.all().order_by('-id')
        supporter_teams = serializers.serialize('json', supporter_teams)

        return JsonResponse(supporter_teams, safe = False, json_dumps_params = {'ensure_ascii': False})

    if request.method == "PUT":
        if len(Supporter.objects.all()) > 10:
            return HttpResponse('')

        data = json.loads(request.body)
        print(data)
        supporter_team = SupporterTeam(name = data['teamName'], contact = data['contact'], password = data['password'])
        supporter_team.save()
        for member in data['supporters']:
            print(member)
            supporter = Supporter(
                name = member['name'],
                sex = member['sex'],
                student_id = member['studentID'],
                department = member['department'],
                size = member['size'],
                is_leader = member['isLeader'],
                team = supporter_team
            )
            supporter.save()

        return HttpResponse('')


    if request.method == "POST":
        data = json.loads(request.body)

        print(data)
        SupporterTeam.objects.get(id = data['pk']).members.all().delete()
        supporter_team = SupporterTeam(
            id = data['pk'],
            name = data['teamName'],
            contact = data['contact'],
            password = data['password']
        )
        supporter_team.save()
        for instance in data['supporters']:
            supporter = Supporter(
                name = instance['name'],
                sex = instance['sex'],
                student_id = instance['studentID'],
                department = instance['department'],
                size = instance['size'],
                is_leader = instance['isLeader'],
                team = supporter_team
            )
            supporter.save()

        return HttpResponse('')


def supportersView(request, pk):
    if request.method == "GET":
        data = serializers.serialize('json', [SupporterTeam.objects.get(id = pk)], fields=('password'))

        return JsonResponse(data, safe = False, json_dumps_params = {'ensure_ascii': False})

    if request.method == "DELETE":
        supporter = SupporterTeam.objects.get(id = pk)
        supporter.delete()

        return HttpResponse('')


def SupportersViewComplete(request, pk):
    if request.method == "GET":
        data = {
            'supporter_team': serializers.serialize('json', [SupporterTeam.objects.get(id = pk)]),
            'members': serializers.serialize('json', SupporterTeam.objects.get(id = pk).members.all().order_by('sex', '-is_leader'))
        }

    return JsonResponse(data, safe = False, json_dumps_params = {'ensure_ascii': False})


def totoContent(request):
    if request.method == "GET":
        toto = TotoContent.objects.all()
        toto = serializers.serialize('json', toto)

        return JsonResponse(toto, safe = False, json_dumps_params = {'ensure_ascii': False})


def totoView(request, pk):
    if request.method == "GET":
        data = serializers.serialize('json', [TotoContent.objects.get(id = pk)], fields=('password'))
        print(data)

        return JsonResponse(data, safe = False, json_dumps_params = {'ensure_ascii': False})


def totoViewComplete(request, pk):
    if request.method == "GET":
        totoContent = TotoContent.objects.get(id = pk)
        data = {}
        data['studentId'] = totoContent.student_id
        data['name'] = totoContent.name

        for toto in totoContent.totos.all():
            if toto.event.type == 0:
                data[f'{toto.event.name_eng}K'] = toto.score_k
                data[f'{toto.event.name_eng}P'] = toto.score_p
            data[f'{toto.event.name_eng}Winner'] = toto.winner

        data = json.dumps(data)

        return JsonResponse(data, safe = False, json_dumps_params = {'ensure_ascii': False})


# @csrf_exempt
def toto(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        school = {'NONE': 0, 'KAIST': 1, 'POSTECH': 2}
        events = Event.objects.all()

        totoContent = TotoContent(student_id = data['studentID'], name = data['name'], password = data['password'], total = 0)
        totoContent.save()

        for totoData in data['toto']:
            event = Event.objects.get(id = totoData['event'])
            if event.type == 0:
                toto = Toto(event=event, bet=totoContent, score_k=totoData[f'{event.name_eng}K'], score_p=totoData[f'{event.name_eng}P'], winner=school[totoData[f'{event.name_eng}Winner']])
                toto.save()
            elif event.type == 1:
                toto = Toto(event=event, bet=totoContent, winner=school[totoData[f'{event.name_eng}Winner']])
                toto.save()

        return HttpResponse('')
