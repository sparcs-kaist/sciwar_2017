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
    name_en = models.CharField(max_length=30)
    name_kr = models.CharField(max_length=30)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    winner = models.IntegerField(default=0, choices=SCHOOLS)
    location = models.IntegerField()
    score_KAIST = models.IntegerField(default=0)
    score_POSTECH = models.IntegerField(default=0)
    players_KAIST = models.ManyToManyField(Player, related_name="player_kaist")
    players_POSTECH = models.ManyToManyField(Player, related_name="player_postech")

    def __str__(self):
        return f'{self.name_kr}'


class Video(models.Model):
    link = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    event = models.ForeignKey(Event)

    def __str__(self):
        return f'{self.event.name_kr}: {self.name}'


class CheerMessage(models.Model):
    content = models.CharField(max_length=140)
    school = models.IntegerField(choices=SCHOOLS)
    time = models.DateTimeField(auto_now_add=True)
    event = models.ForeignKey(Event)

    def __str__(self):
        return f'<{self.get_school_display()}>: {self.content}, {self.event.name_kr}'


class TotoContent(models.Model):
    student_id = models.CharField(max_length=8)
    name = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    score_baseball_KAIST = models.IntegerField()
    score_baseball_POSTECH = models.IntegerField()
    score_basketball_KAIST = models.IntegerField()
    score_basketball_POSTECH = models.IntegerField()
    score_esports_KAIST = models.IntegerField()
    score_esports_POSTECH = models.IntegerField()
    score_soccer_KAIST = models.IntegerField()
    score_soccer_POSTECH = models.IntegerField()
    winner_basketball = models.IntegerField(choices=SCHOOLS)
    winner_baseball = models.IntegerField(choices=SCHOOLS)
    winner_esports = models.IntegerField(choices=SCHOOLS)
    winner_soccer = models.IntegerField(choices=SCHOOLS)
    winner_quiz = models.IntegerField(choices=SCHOOLS)
    winner_AI = models.IntegerField(choices=SCHOOLS)
    winner_hacking = models.IntegerField(choices=SCHOOLS)
