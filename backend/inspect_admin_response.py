import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
import django
django.setup()
from django.test import RequestFactory
from django.contrib.admin.sites import AdminSite
from django.contrib.auth import get_user_model
from transactions.admin import TransactionAdmin
from transactions.models import Transaction

User = get_user_model()
user = User.objects.filter(is_active=True, is_superuser=True).first() or User.objects.filter(is_active=True, is_staff=True).first() or User.objects.first()
print('user', user)
request = RequestFactory().get('/admin/transactions/transaction/')
request.user = user
site = AdminSite()
admin_instance = TransactionAdmin(Transaction, site)
response = admin_instance.changelist_view(request)
print('response type', type(response))
print('template_name', getattr(response, 'template_name', None))
print('templates', getattr(response, 'template_name', response.template_name))
print('template object', getattr(response, 'template', None))
print('template names', response.template_name if hasattr(response, 'template_name') else 'no template_name')
print('context keys', list(response.context_data.keys()) if hasattr(response, 'context_data') else 'no context_data')
# attempt to render only the custom template manually if possible
from django.template.loader import get_template
try:
    tmp = get_template('admin/transactions/transaction/change_list.html')
    print('custom template loaded name', tmp.name)
except Exception as e:
    print('custom template load error', type(e), e)
