import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
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
TransactionAdmin.change_list_template = None
admin_instance = TransactionAdmin(Transaction, site)
response = admin_instance.changelist_view(request)
print('response type', type(response))
print('template_name', getattr(response, 'template_name', None))
print('context keys', list(response.context_data.keys()))
try:
    rendered = response.render()
    print('rendered length', len(rendered.content))
except Exception as e:
    import traceback
    traceback.print_exc()
