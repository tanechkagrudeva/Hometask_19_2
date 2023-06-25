from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):
    help = 'Команда для очистки таблицы и заполнения данными'

    def handle(self, *args, **options):
        # Очистка таблицы категорий от данных
        Category.objects.all().delete()
        # Список категорий для добавления
        categories_list = [
            {"name": "Online игры", "description": "Online игры для развития IQ"},
            {"name": "Online курс по тайм-менеджменту", "description": "Готовые решения по управлению вашего времени"},
            {"name": "Электронные книги", "description": "Электронные книги для чтения в любом месте и в любое время"},

                           ]

        category_for_create = []
        for category_item in categories_list:
            category_for_create.append(
                Category(**category_item)
            )

        Category.objects.bulk_create(category_for_create)
