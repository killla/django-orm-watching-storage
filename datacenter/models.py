from django.db import models
from django.utils import timezone

def format_duration(duration):
    hours = int(duration.total_seconds() // 3600)
    minutes = str(int((duration.total_seconds() % 3600) // 60))
    if len(minutes) == 1:
        minutes = '0'+minutes
    return f'{hours}:{minutes}'

class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved= "leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )

    def get_duration(visit):
        if visit.leaved_at == None:
            now = timezone.now()
            delta = now - visit.entered_at
        else:
            delta = visit.leaved_at - visit.entered_at
        return delta

    def is_visit_long(visit, minutes=60):
        time_of_visit = visit.get_duration()
        return time_of_visit.total_seconds() > minutes * 60