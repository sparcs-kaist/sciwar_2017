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
    
    type = models.IntegerField(default=0, choices=TYPE)
    name_eng = models.CharField(max_length=30)
    name_kor = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True)
    winner = models.IntegerField(default=0, choices=SCHOOLS)
    location = models.IntegerField()
    score_k = models.IntegerField(default=0)
    score_p = models.IntegerField(default=0)
    players_k = models.ManyToManyField(Player, related_name="player_kaist")
    players_p = models.ManyToManyField(Player, related_name="player_postech")

    def __str__(self):
        return f'{self.name_kor}'


class Video(models.Model):
    link = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    event = models.ManyToManyField(Event)

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
    time = models.DateTimeField(auto_now_add=True)
    score_baseball_k = models.IntegerField()
    score_baseball_p = models.IntegerField()
    score_basketball_k = models.IntegerField()
    score_basketball_p = models.IntegerField()
    score_esports_k = models.IntegerField()
    score_esports_p = models.IntegerField()
    score_soccer_k = models.IntegerField()
    score_soccer_p = models.IntegerField()
    winner_basketball = models.IntegerField(choices=SCHOOLS)
    winner_baseball = models.IntegerField(choices=SCHOOLS)
    winner_esports = models.IntegerField(choices=SCHOOLS)
    winner_soccer = models.IntegerField(choices=SCHOOLS)
    winner_quiz = models.IntegerField(choices=SCHOOLS)
    winner_AI = models.IntegerField(choices=SCHOOLS)
    winner_hacking = models.IntegerField(choices=SCHOOLS)
