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
superuser = User.objects.filter(is_active=True, is_superuser=True).first()
print('SUPERUSER:', superuser)
if not superuser:
    staff = User.objects.filter(is_active=True, is_staff=True).first()
    print('STAFF:', staff)
    user = staff or User.objects.first()
else:
    user = superuser
print('USING USER:', user)
request = RequestFactory().get('/admin/transactions/transaction/')
request.user = user
site = AdminSite()
admin_instance = TransactionAdmin(Transaction, site)
try:
    response = admin_instance.changelist_view(request)
    print('RESPONSE TYPE:', type(response))
    print('STATUS CODE:', getattr(response, 'status_code', None))
    print('RENDERING...')
    if hasattr(response, 'render'):
        x = response.render()
        print('RENDERED length', len(x.content))
except Exception as exc:
    import traceback
    traceback.print_exc()
