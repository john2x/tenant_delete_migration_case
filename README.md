This repo provides a minimal test case replicating https://github.com/bernardopires/django-tenant-schemas/issues/336

```
(test) vagrant@vagrant-ubuntu-trusty-64:~/kombu_tenant_minimal_case$ ./manage.py migrate_schemas
=== Running migrate for schema public
Operations to perform:
  Apply all migrations: customers, app1, nested_app2, sessions, admin, kombu_transport_django, contenttypes, auth, shared_app
Running migrations:
  Rendering model states... DONE
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying app1.0001_initial... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying customers.0001_initial... OK
  Applying kombu_transport_django.0001_initial... OK
  Applying nested_app2.0001_initial... OK
  Applying sessions.0001_initial... OK
  Applying shared_app.0001_initial... OK

(test) vagrant@vagrant-ubuntu-trusty-64:~/kombu_tenant_minimal_case$ ./manage.py shell
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
> from nested.app1.models import App1
> App1.objects.all()  # ok
[]

> from nested.app2.models import App2
> App2.objects.all()  # can't find the table
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/models/query.py", line 234, in __repr__
    data = list(self[:REPR_OUTPUT_SIZE + 1])
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/models/query.py", line 258, in __iter__
    self._fetch_all()
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/models/query.py", line 1074, in _fetch_all
    self._result_cache = list(self.iterator())
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/models/query.py", line 52, in __iter__
    results = compiler.execute_sql()
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 848, in execute_sql
    cursor.execute(sql, params)
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/backends/utils.py", line 79, in execute
    return super(CursorDebugWrapper, self).execute(sql, params)
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/backends/utils.py", line 64, in execute
    return self.cursor.execute(sql, params)
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/utils.py", line 95, in __exit__
    six.reraise(dj_exc_type, dj_exc_value, traceback)
  File "/home/vagrant/test/local/lib/python2.7/site-packages/django/db/backends/utils.py", line 64, in execute
    return self.cursor.execute(sql, params)
ProgrammingError: relation "nested_app2_app2" does not exist
LINE 1: ...d_app2_app2"."id", "nested_app2_app2"."name" FROM "nested_ap...
                                                             ^
```
