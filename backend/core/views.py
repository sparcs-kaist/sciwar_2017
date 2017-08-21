from django.views.decorators.csrf import csrf_exempt
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


@csrf_exempt
def event(request, event_id):
    if request.method == "GET":
        event = Event.objects.get(id = event_id)
        event = serializers.serialize('json', [event])

        return JsonResponse(event, safe = False, json_dumps_params = {'ensure_ascii': False})

    if request.method == "POST":
        event = Event.objects.get(id = event_id)
        live = request.POST
        live = list(live.keys())[0]
        live = json.loads(live)
        live = live['live']
        print(live)
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


@csrf_exempt
def messages(request):
    if request.method == "GET":
        messages = CheerMessage.objects.all().order_by('-time')

        messages = serializers.serialize('json', messages)

        return JsonResponse(messages, safe = False, json_dumps_params = {'ensure_ascii': False})
    

    if request.method == "PUT":
        data = json.loads(request.body)
        print(data['content'])
        cheerMessage = CheerMessage(content = data['content'], school = data['school'])
        cheerMessage.event_id = data['event']
        print(cheerMessage.event)
        cheerMessage.save()

        return HttpResponse('')


@csrf_exempt
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


def video(request, pk):
    if request.method == "GET":
        video = Video.objects.get(id = pk)
        video = serializers.serialize('json', [video])

        return JsonResponse(video, safe = False, json_dumps_params = {'ensure_ascii': False})


@csrf_exempt
def supporters(request):
    if request.method == "GET":
        supporters = Supporter.objects.all()
        supporters = serializers.serialize('json', supporters)
        
        return JsonResponse(supporters, safe = False, json_dumps_params = {'ensure_ascii': False})

    if request.method == "PUT":
        data = json.loads(request.body)
        print(data)
        print(data['teamName'])
        supporterReg = SupporterReg(nickname = data['teamName'], contact = data['contact'], password = data['password'])
        supporterReg.save()
        for sup in data['supporters']:
            print(sup)
            supporter = Supporter(name = sup['name'], student_id = sup['studentID'], department = sup['department'], size = sup['size'], registry = supporterReg)
            supporter.save()

        return HttpResponse('')

    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        SupporterReg.objects.get(id = data['pk']).supporters.all().delete()
        supporterReg = SupporterReg(id = data['pk'], nickname = data['nickname'], contact = data['contact'], password = data['password'])
        supporterReg.save()
        for instance in data['supporters']:
            supporter = Supporter(name = instance['name'], student_id = instance['studentID'], department = instance['department'], size = instance['size'], registry = supporterReg)
            supporter.save()

        return HttpResponse('')


def supporterReg(request):
    if request.method == "GET":
        supporters = SupporterReg.objects.all()
        supporters = serializers.serialize('json', supporters)
        
        return JsonResponse(supporters, safe = False, json_dumps_params = {'ensure_ascii': False})


@csrf_exempt
def supportersView(request, reg_id):
    if request.method == "GET":
        data = serializers.serialize('json', [SupporterReg.objects.get(id = reg_id)], fields=('password'))
        print(data)

        return JsonResponse(data, safe = False, json_dumps_params = {'ensure_ascii': False})

    if request.method == "DELETE":
        reg = SupporterReg.objects.get(id = reg_id)
        reg.supporters.all().delete()
        reg.delete()

        return HttpResponse('')


def SupportersViewComplete(request, reg_id):
    if request.method == "GET":
        data = {
            'reg': serializers.serialize('json', [SupporterReg.objects.get(id = reg_id)]),
            'supporters': serializers.serialize('json', SupporterReg.objects.get(id = reg_id).supporters.all())
        }
        print(data)

    return JsonResponse(data, safe = False, json_dumps_params = {'ensure_ascii': False})


def totoContent(request):
    if request.method == "GET":
        toto = TotoContent.objects.all()
        toto = serializers.serialize('json', toto)

        return JsonResponse(toto, safe = False, json_dumps_params = {'ensure_ascii': False})


def totoView(request, pk):
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
        data['winnerSoccer'] = toto.soccer_toto.all()[0].winner
        data['winnerBaseball'] = toto.baseball_toto.all()[0].winner
        data['winnerBasketball'] = toto.basketball_toto.all()[0].winner
        data['winnerLol'] = toto.esports_toto.all()[0].winner
        data['winnerQuiz'] = toto.quiz_toto.all()[0].winner
        data['winnerAI'] = toto.ai_toto.all()[0].winner
        data['winnerHacking'] = toto.hacking_toto.all()[0].winner
        
        data = json.dumps(data)

        return JsonResponse(data, safe = False, json_dumps_params = {'ensure_ascii': False})


@csrf_exempt
def toto(request):
    if request.method == "PUT":
        data = json.loads(request.body)
        print(data)
        soccer = Event.objects.get(name_kor = '축구')
        baseball = Event.objects.get(name_kor = '야구')
        basketball = Event.objects.get(name_kor = '농구')
        LOL = Event.objects.get(name_kor = '롤')
        quiz = Event.objects.get(name_kor = '과학퀴즈')
        AI = Event.objects.get(name_kor = '인공지능')
        hacking = Event.objects.get(name_kor = '해킹')
        school = {'KAIST': 1, 'POSTECH': 2}

        totoContent = TotoContent(student_id = data['studentID'], name = data['name'], password = data['password'], total = 0)
        totoContent.save()

        soccerToto = SoccerToto(event = soccer, bet = totoContent, score_k = data['scoreSoccerK'], score_p = data['scoreSoccerP'], winner = school[data['winnerSoccer']])
        print(data)
        soccerToto.save()

        baseballToto = BaseballToto(event = baseball, bet = totoContent, score_k = data['scoreBaseballK'], score_p = data['scoreBaseballP'], winner = school[data['winnerBaseball']])
        baseballToto.save()

        basketballToto = BasketballToto(event = basketball, bet = totoContent, score_k = data['scoreBasketballK'], score_p = data['scoreBasketballP'], winner = school[data['winnerBasketball']])
        basketballToto.save()

        LOLToto = EsportsToto(event = LOL, bet = totoContent, score_k = data['scoreLolK'], score_p = data['scoreLolP'], winner = school[data['winnerLol']])
        LOLToto.save()

        quizToto = QuizToto(event = quiz, bet = totoContent, winner = school[data['winnerQuiz']])
        quizToto.save()

        AiToto = AIToto(event = AI, bet = totoContent, winner = school[data['winnerAI']])
        AiToto.save()

        hackingToto = HackingToto(event = hacking, bet = totoContent, winner = school[data['winnerHacking']])
        hackingToto.save()


        return HttpResponse('')
