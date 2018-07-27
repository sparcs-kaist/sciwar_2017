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


class Location(models.Model):
    school = models.IntegerField(choices=SCHOOLS)
    name_eng = models.CharField(max_length=30)
    name_kor = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.name_kor}'


class Event(models.Model):
    TYPE = (
        (0, 'Sports'),
        (1, 'Science'),
        (2, 'Others'),
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
    end_time = models.DateTimeField()
    winner = models.IntegerField(default=0, choices=SCHOOLS)
    location = models.ForeignKey(Location, null=False, related_name="events")
    score_k = models.IntegerField(blank=True, null=True, default=0)
    score_p = models.IntegerField(blank=True, null=True, default=0)
    players_k = models.ManyToManyField(Player, related_name="events_k")
    players_p = models.ManyToManyField(Player, related_name="events_p")
    live = models.IntegerField(default = 0, choices = STATUS)
    score_weight = models.FloatField(blank=True, null=True, default = 0.0)
    win_weight = models.FloatField(blank=True, null=True, default = 1.0)


    def __str__(self):
        return f'{self.name_kor} {self.live}'


class Video(models.Model):
    TYPE = (
        (0, 'Live streaming'),
        (1, 'Others'),
    )
    link = models.CharField(max_length=300)
    name = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
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
    event = models.ForeignKey(Event, blank=True, null=True)
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'<{self.get_school_display()}>: {self.content}, {self.event.name_kor}'

    class Meta:
        ordering = ['likes']


class Supporter(models.Model):
    SIZE = (
        (0, 'XS'),
        (1, 'S'),
        (2, 'M'),
        (3, 'L'),
        (4, 'XL'),
        (5, 'XXL'),
    )
    name = models.CharField(
        max_length = 30,
    )
    contact = models.CharField(
        max_length = 11,
        default = '0'
    )
    password = models.CharField(
        max_length = 64,
        null = False,
        default = '1234',
    )
    student_id = models.CharField(
        max_length = 8,
        default = '0'
    )
    department = models.CharField(
        max_length = 50,
    )
    size = models.IntegerField(
        default = 0,
        choices = SIZE,
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ['-id']


class TotoContent(models.Model):
    student_id = models.CharField(max_length=8)
    name = models.CharField(max_length=30)
    time = models.DateTimeField(auto_now_add = True)
    total = models.FloatField(default=0.0)
    password = models.CharField(
        max_length = 64,
        null = False,
        default = '1234',
    )

    class Meta:
        ordering = ['-total', '-id']


class Toto(models.Model):
    bet = models.ForeignKey(
        TotoContent,
        related_name = 'totos',
        null = False,
    )
    event = models.ForeignKey(
        Event,
        related_name = 'totos',
        null = False,
    )
    score_k = models.IntegerField(
        blank = True,
        null = True,
    )
    score_p = models.IntegerField(
        blank = True,
        null = True,
    )
    winner = models.IntegerField(
        null = False,
        choices = SCHOOLS,
    )
