from __future__ import unicode_literals

from django.db import models
from tenant_schemas.models import TenantMixin

# Create your models here.

class Client(TenantMixin):
    pass
