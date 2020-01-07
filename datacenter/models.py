from django.db import models
from django.utils import timezone
import time


def format_duration(duration):
    return time.strftime("%H:%M", time.gmtime(duration))


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
        if not visit.leaved_at:
            now = timezone.now()
            delta = now - visit.entered_at
        else:
            delta = visit.leaved_at - visit.entered_at
        return delta.total_seconds()

    def is_visit_long(visit, minutes=60):
        time_of_visit = visit.get_duration()
        return time_of_visit > minutes * 60