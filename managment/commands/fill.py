from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        category_list = [
            {'category':'FC', 'description': 'fifth category'}
            {'category':'SC', 'description': 'sixth category'}
            {'category':'SC', 'description': 'seventh category'}
        ]

        # for category in category_list:
        #     Category.objects.create(**category_list)

        category_for_create = []
        for category in category_list:
            category_for_create.append(
                Category(**category)
            )

        Category.objects.bulk_create(category_for_create)