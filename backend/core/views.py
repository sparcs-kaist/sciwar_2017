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

        events = Event.objects.all()
        event_dict = {}
        for event in events:
            event_dict[event.id] = event.name_eng.lower()
        if live == 2:
            # Toto score update
            event = Event.objects.get(id = pk)
            if event_dict[pk] == 'quiz':
                event_totoes = event.quiz_toto.all()
            elif event_dict[pk] == 'hacking':
                event_totoes = event.hacking_toto.all()
            elif event_dict[pk] == 'baseball':
                event_totoes = event.baseball_toto.all()
                for toto in event_totoes:
                    if score_k == toto.score_k and score_p == toto.score_p:
                        toto.bet.total += 0.5
            elif event_dict[pk] == 'basketball':
                event_totoes = event.basketball_toto.all()
                for toto in event_totoes:
                    if score_k == toto.score_k and score_p == toto.score_p:
                        toto.bet.total += 0.5
            else:
                if event_dict[pk] == 'soccer':
                    event_totoes = event.soccer_toto.all()
                elif event_dict[pk] == 'lol':
                    event_totoes = event.esports_toto.all()
                elif event_dict[pk] == 'ai':
                    event_totoes = event.ai_toto.all()
                for toto in event_totoes:
                    if score_k == toto.score_k and score_p == toto.score_p:
                        toto.bet.total += 0.2
            for toto in event_totoes:
                if winner == toto.winner:
                    toto.bet.total += 1
                toto.bet.save()
            # Live video
            videos = Video.objects.all()
            for video in videos:
                live = 1
                for event in video.event.all():
                    if event.live == 1 and event.pk != pk:
                        live = 0
                        break
                video.type = live
                video.save()

        return HttpResponse('')


# @csrf_exempt
def rescore_toto(request):
    if request.method == "POST":
        all_totoes = TotoContent.objects.all()
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
        messages = CheerMessage.objects.filter(event = event).order_by('-time')
        messages = serializers.serialize('json', messages)
        print(messages)
        return JsonResponse(messages, safe = False, json_dumps_params = {'ensure_ascii': False})


# @csrf_exempt
def messages(request):
    if request.method == "GET":
        messages = CheerMessage.objects.all().order_by('-time')

        messages = serializers.serialize('json', messages)

        return JsonResponse(messages, safe = False, json_dumps_params = {'ensure_ascii': False})


    if request.method == "PUT":
        data = json.loads(request.body)
        cheerMessage = CheerMessage(content = data['content'], school = data['school'])
        cheerMessage.event_id = data['event']
        cheerMessage.save()

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
        supporters = Supporter.objects.all()
        supporters = serializers.serialize('json', supporters)

        return JsonResponse(supporters, safe = False, json_dumps_params = {'ensure_ascii': False})

    if request.method == "PUT":
        if len(Supporter.objects.all()) >= 180:
            return HttpResponse('')
        data = json.loads(request.body)
        supporter = Supporter(name = data['name'], contact = data['contact'], password = data['password'], student_id = data['studentID'], department = data['department'], size = data['size'])
        supporter.save()

        return HttpResponse('')

    if request.method == "POST":
        data = json.loads(request.body)
        supporter = Supporter.objects.get(id = data['pk'])
        supporter.name = data['name']
        supporter.contact = data['contact']
        supporter.password = data['password']
        supporter.student_id = data['studentID']
        supporter.department = data['department']
        supporter.size = data['size']
        supporter.save()

        return HttpResponse('')


def supportersView(request, pk):
    if request.method == "GET":
        data = serializers.serialize('json', [Supporter.objects.get(id = pk)], fields=('password'))
        print(data)

        return JsonResponse(data, safe = False, json_dumps_params = {'ensure_ascii': False})

    if request.method == "DELETE":
        supporter = Supporter.objects.get(id = pk)
        supporter.delete()

        return HttpResponse('')


def SupportersViewComplete(request, pk):
    if request.method == "GET":
        data = Supporter.objects.get(id = pk)
        data = serializers.serialize('json', [data])

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
        toto = TotoContent.objects.get(id = pk)
        data = {}
        data['studentId'] = toto.student_id
        data['name'] = toto.name
        data['scoreSoccerK'] = toto.soccer_toto.all()[0].score_k
        data['scoreSoccerP'] = toto.soccer_toto.all()[0].score_p
        data['scoreBaseballK'] = toto.baseball_toto.all()[0].score_k
        data['scoreBaseballP'] = toto.baseball_toto.all()[0].score_p
        data['scoreBasketballK'] = toto.basketball_toto.all()[0].score_k
        data['scoreBasketballP'] = toto.basketball_toto.all()[0].score_p
        data['scoreLolK'] = toto.esports_toto.all()[0].score_k
        data['scoreLolP'] = toto.esports_toto.all()[0].score_p
        data['scoreAiK'] = toto.ai_toto.all()[0].score_k
        data['scoreAiP'] = toto.ai_toto.all()[0].score_p
        data['winnerSoccer'] = toto.soccer_toto.all()[0].winner
        data['winnerBaseball'] = toto.baseball_toto.all()[0].winner
        data['winnerBasketball'] = toto.basketball_toto.all()[0].winner
        data['winnerLol'] = toto.esports_toto.all()[0].winner
        data['winnerQuiz'] = toto.quiz_toto.all()[0].winner
        data['winnerAI'] = toto.ai_toto.all()[0].winner
        data['winnerHacking'] = toto.hacking_toto.all()[0].winner

        data = json.dumps(data)

        return JsonResponse(data, safe = False, json_dumps_params = {'ensure_ascii': False})


# @csrf_exempt
def toto(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        soccer = Event.objects.get(name_eng = 'Soccer')
        baseball = Event.objects.get(name_eng = 'Baseball')
        basketball = Event.objects.get(name_eng = 'Basketball')
        LOL = Event.objects.get(name_eng = 'LOL')
        quiz = Event.objects.get(name_eng = 'Quiz')
        AI = Event.objects.get(name_eng = 'AI')
        hacking = Event.objects.get(name_eng = 'Hacking')
        school = {'None': 0, 'KAIST': 1, 'POSTECH': 2}

        totoContent = TotoContent(student_id = data['studentID'], name = data['name'], password = data['password'], total = 0)
        totoContent.save()

        quizToto = QuizToto(event = quiz, bet = totoContent, winner = school[data['winnerQuiz']])
        quizToto.save()

        soccerToto = SoccerToto(event = soccer, bet = totoContent, score_k = data['scoreSoccerK'], score_p = data['scoreSoccerP'], winner = school[data['winnerSoccer']])
        soccerToto.save()

        baseballToto = BaseballToto(event = baseball, bet = totoContent, score_k = data['scoreBaseballK'], score_p = data['scoreBaseballP'], winner = school[data['winnerBaseball']])
        baseballToto.save()

        basketballToto = BasketballToto(event = basketball, bet = totoContent, score_k = data['scoreBasketballK'], score_p = data['scoreBasketballP'], winner = school[data['winnerBasketball']])
        basketballToto.save()

        LOLToto = EsportsToto(event = LOL, bet = totoContent, score_k = data['scoreLolK'], score_p = data['scoreLolP'], winner = school[data['winnerLol']])
        LOLToto.save()

        AiToto = AIToto(event = AI, bet = totoContent, score_k = data['scoreAiK'], score_p = data['scoreAiP'], winner = school[data['winnerAI']])
        AiToto.save()

        hackingToto = HackingToto(event = hacking, bet = totoContent, winner = school[data['winnerHacking']])
        hackingToto.save()


        return HttpResponse('')
