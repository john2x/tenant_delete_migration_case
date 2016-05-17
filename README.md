This repo provides minimal test case for failing migrations when deleting a model
that uses `django-taggit`' for tags.

# Step A

Clone this repo and checkout branch `step-a` and create a Postgres database named `tenant_delete_migration_case`. Modify the database config in `settings.py` as necessary.

    $ git checkout step-a
    $ pip install -r requirements.txt
    $ ./manage.py migrate_schemas
    $ ./manage.py bootstrap_test_data


# Step B

After the test data have been created, checkout branch `step-b`. This branch deletes the `ToBeDeletedModel` with the relevant migrations.

    $ git checkout step-b
    $ ./manage.py migrate_schemas

    === Running migrate for schema public
    Operations to perform:
      Apply all migrations: customers, sessions, admin, contenttypes, auth, taggit, shared_app
    Running migrations:
      Rendering model states... DONE
      Applying shared_app.0002_delete_model... OK
    The following content types are stale and need to be deleted:
    
        shared_app | tobedeletedmodel
    
    Any objects related to these content types by a foreign key will also
    be deleted. Are you sure you want to delete these content types?
    If you're unsure, answer 'no'.

    Type 'yes' to continue, or 'no' to cancel: yes
    Traceback (most recent call last):
      File "./manage.py", line 10, in <module>
        execute_from_command_line(sys.argv)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 353, in execute_from_command_line
        utility.execute()
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/core/management/__init__.py", line 345, in execute
        self.fetch_command(subcommand).run_from_argv(self.argv)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/core/management/base.py", line 348, in run_from_argv
        self.execute(*args, **cmd_options)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/core/management/base.py", line 399, in execute
        output = self.handle(*args, **options)
      File "/var/www/tenant_delete_migrations_case/venv/src/django-tenant-schemas/tenant_schemas/management/commands/migrate_schemas.py", line 40, in handle
        self.run_migrations(self.schema_name, settings.SHARED_APPS)
      File "/var/www/tenant_delete_migrations_case/venv/src/django-tenant-schemas/tenant_schemas/management/commands/migrate_schemas.py", line 58, in run_migrations
        command.execute(*self.args, **self.options)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/core/management/base.py", line 399, in execute
        output = self.handle(*args, **options)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/core/management/commands/migrate.py", line 204, in handle
        emit_post_migrate_signal(self.verbosity, self.interactive, connection.alias)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/core/management/sql.py", line 50, in emit_post_migrate_signal
        using=db)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/dispatch/dispatcher.py", line 192, in send
        response = receiver(signal=self, sender=sender, **named)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/contrib/contenttypes/management.py", line 81, in update_contenttypes
        ct.delete()
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/db/models/base.py", line 870, in delete
        return collector.delete()
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/db/models/deletion.py", line 292, in delete
        count = qs._raw_delete(using=self.using)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/db/models/query.py", line 614, in _raw_delete
        return sql.DeleteQuery(self.model).delete_qs(self, using)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/db/models/sql/subqueries.py", line 81, in delete_qs
        cursor = self.get_compiler(using).execute_sql(CURSOR)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/db/models/sql/compiler.py", line 848, in execute_sql
        cursor.execute(sql, params)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/db/backends/utils.py", line 79, in execute
        return super(CursorDebugWrapper, self).execute(sql, params)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/db/backends/utils.py", line 64, in execute
        return self.cursor.execute(sql, params)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/db/utils.py", line 95, in __exit__
        six.reraise(dj_exc_type, dj_exc_value, traceback)
      File "/var/www/tenant_delete_migrations_case/venv/local/lib/python2.7/site-packages/django/db/backends/utils.py", line 64, in execute
        return self.cursor.execute(sql, params)
    django.db.utils.ProgrammingError: relation "taggit_taggeditem" does not exist
    LINE 1: DELETE FROM "taggit_taggeditem" WHERE "taggit_taggeditem"."c...
