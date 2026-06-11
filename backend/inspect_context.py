import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
import django
django.setup()
import inspect
from django.template.context import BaseContext
print('DJANGO', django.get_version())
print('BaseContext MRO', [c.__name__ for c in BaseContext.__mro__])
print('Has __copy__', hasattr(BaseContext, '__copy__'))
if hasattr(BaseContext, '__copy__'):
    print(inspect.getsource(BaseContext.__copy__))
else:
    print('BaseContext has no __copy__')
print('Context has __copy__', hasattr(__import__('django.template.context', fromlist=['Context']).Context, '__copy__'))
print(inspect.getsource(__import__('django.template.context', fromlist=['Context']).Context.__copy__))
