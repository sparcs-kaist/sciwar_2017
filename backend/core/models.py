from django.db import models

SCHOOLS = (
    (0, 'NONE'),
    (1, 'KAIST'),
    (2, 'POSTECH'),
)

class Player(models.Model):
    name = models.CharField(max_length=30, blank=True)
    age = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    TYPE = (
        (0, 'Sports'),
        (1, 'Others'),
    )
    STATUS = (
        (0, 'Pre'),
        (1, 'Live'),
        (2, 'Post'),
    )
    
    type = models.IntegerField(default=0, choices=TYPE)
    name_eng = models.CharField(max_length=30)
    name_kor = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True)
    winner = models.IntegerField(default=0, choices=SCHOOLS)
    location = models.IntegerField()
    score_k = models.IntegerField(default=0)
    score_p = models.IntegerField(default=0)
    players_k = models.ManyToManyField(Player, related_name="events_k")
    players_p = models.ManyToManyField(Player, related_name="events_p")
    live = models.IntegerField(
        default = 0,
        choices = STATUS,
    )

    def __str__(self):
        return f'{self.name_kor}'


class Video(models.Model):
    TYPE = (
        (0, 'Live streaming'),
        (1, 'Others'),
    )
    link = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    event = models.ManyToManyField(Event)
    type = models.IntegerField(
        default = 0,
        choices = TYPE,
    )

    def __str__(self):
        return f'{self.name}'


class CheerMessage(models.Model):
    content = models.CharField(max_length=140)
    school = models.IntegerField(choices=SCHOOLS)
    time = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event)

    def __str__(self):
        return f'<{self.get_school_display()}>: {self.content}, {self.event.name_kor}'


class TotoContent(models.Model):
    student_id = models.CharField(max_length=8)
    name = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add = True)

class BasketballToto(models.Model):
    event = models.ForeignKey(
        Event,
        related_name = 'basketball_toto',
    )
    bet = models.ForeignKey(
        TotoContent,
        related_name = 'basketball_toto',
    )
    score_k = models.IntegerField()
    score_p = models.IntegerField()
    winner = models.IntegerField(
        default = 0,
        choices = SCHOOLS,
    )


class BaseballToto(models.Model):
    event = models.ForeignKey(
        Event,
        related_name = 'baseball_toto',
    )
    bet = models.ForeignKey(
        TotoContent,
        related_name = 'baseball_toto',
    )
    score_k = models.IntegerField()
    score_p = models.IntegerField()
    winner = models.IntegerField(
        default = 0,
        choices = SCHOOLS,
    )


class SoccerToto(models.Model):
    event = models.ForeignKey(
        Event,
        related_name = 'soccer_toto',
    )
    bet = models.ForeignKey(
        TotoContent,
        related_name = 'soccer_toto',
    )
    score_k = models.IntegerField()
    score_p = models.IntegerField()
    winner = models.IntegerField(
        default = 0,
        choices = SCHOOLS,
    )


class EsportsToto(models.Model):
    event = models.ForeignKey(
        Event,
        related_name = 'esports_toto',
    )
    bet = models.ForeignKey(
        TotoContent,
        related_name = 'esports_toto',
    )
    score_k = models.IntegerField()
    score_p = models.IntegerField()
    winner = models.IntegerField(
        default = 0,
        choices = SCHOOLS,
    )


class QuizToto(models.Model):
    event = models.ForeignKey(
        Event,
        related_name = 'quiz_toto',
    )
    bet = models.ForeignKey(
        TotoContent,
        related_name = 'quiz_toto',
    )
    winner = models.IntegerField(
        default = 0,
        choices = SCHOOLS,
    )


class AIToto(models.Model):
    event = models.ForeignKey(
        Event,
        related_name = 'ai_toto',
    )
    bet = models.ForeignKey(
        TotoContent,
        related_name = 'ai_toto',
    )
    winner = models.IntegerField(
        default = 0,
        choices = SCHOOLS,
    )


class HackingToto(models.Model):
    event = models.ForeignKey(
        Event,
        related_name = 'hacking_toto',
    )
    bet = models.ForeignKey(
        TotoContent,
        related_name = 'hacking_toto',
    )
    winner = models.IntegerField(
        default = 0,
        choices = SCHOOLS,
    )
