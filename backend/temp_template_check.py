import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.settings'
import django
django.setup()
from django.template.loader import get_template
print('TEMPLATE_DIRS', __import__('django.conf').conf.settings.TEMPLATES[0]['DIRS'])
print('APP_DIRS', __import__('django.conf').conf.settings.TEMPLATES[0]['APP_DIRS'])
print('Trying template')
t = get_template('admin/transactions/transaction/change_list.html')
print('FOUND', getattr(t, 'template', t))
