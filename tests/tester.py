import django
django.setup()
import settings

#settings.configure()

import tablib
from import_export import resources
from core.models import Book
book_rescource = resources.modelresource_factory(model=Book)()
dataset = tablib.Dataset(['', 'New book'], headers=['id', 'name'])
result = book_rescource.import_data(dataset, dry_run=True)
print(result.has_errors())
False
result = book_rescource.import_data(dataset, dry_run=False)

print(result)
