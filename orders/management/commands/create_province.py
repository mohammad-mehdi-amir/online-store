from products.models import Color
from typing import Any
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
import datetime


from  orders.models import Province


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def handle(self, *args, **options):
        province= ("آذربایجان شرقی", "آذربایجان غربی", "اردبیل", "اصفهان", "البرز", "ایلام", "بوشهر", "تهران", "چهارمحال و بختیاری", "خراسان جنوبی", "خراسان رضوی", "خراسان شمالی", "خوزستان", "زنجان", "سمنان", "سیستان و بلوچستان", "فارس", "قزوین", "قم", "كردستان", "كرمان", "كرمانشاه", "گلستان", "گیلان", "لرستان", "مازندران", "مرکزی", "هرمزگان", "همدان", "یزد")

        for p in province:
            Province.objects.create(name=p)
            

