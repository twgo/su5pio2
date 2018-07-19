
from django.core.management.base import BaseCommand

from docker轉詞表 import _main


class Command(BaseCommand):
    def handle(self, *args, **參數):
        _main()