# recipes/management/commands/load_data.py
import json
from django.core.management.base import BaseCommand
from recipes.models import Recipe

class Command(BaseCommand):
    help = 'Load data from JSON file'

    def handle(self, *args, **kwargs):
        with open('data.json') as f:
            data = json.load(f)
            for item in data:
                Recipe.objects.create(
                    name=item['name'],
                    type=item['type'],
                    preparation_time=item['preparation_time'],
                    ingredients=item['ingredients'],
                    steps=item['steps']
                )
