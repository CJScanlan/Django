from typing import Set, Tuple

from django.db import models

SUFFIX_CHOICES: set[tuple[str, str]] = {
    ('Mr.','Mr.'),
    ('Ms.','Ms.'),
    ('Mrs.','Mrs.'),
    ('Miss','Miss'),
}


class Profiles(models.Model):
    suffix = models.CharField(max_length=60, choices=SUFFIX_CHOICES)
    first_name = models.CharField(max_length=60, default="", blank=False)
    last_name = models.CharField(max_length=60, default="", blank=False)
    email = models.CharField(max_length=100, default="", blank=False)
    username = models.CharField(max_length=60, default="", blank=False)

    objects = models.Manager()

    def __str__(self):
        return self.first_name