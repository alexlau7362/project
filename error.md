 Watching for file changes with StatReloader
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "/home/cest7362/.pyenv/versions/3.13.2/lib/python3.13/threading.py", line 1041, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/home/cest7362/.pyenv/versions/3.13.2/lib/python3.13/threading.py", line 992, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
    ~~^^^^^^^^^^^^^^^^^
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/core/management/commands/runserver.py", line 133, in inner_run
    self.check(display_num_errors=True)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/core/management/base.py", line 485, in check
    all_issues = checks.run_checks(
        app_configs=app_configs,
    ...<2 lines>...
        databases=databases,
    )
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/core/checks/registry.py", line 88, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/core/checks/urls.py", line 14, in check_url_config
    return check_resolver(resolver)
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/core/checks/urls.py", line 24, in check_resolver
    return check_method()
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/urls/resolvers.py", line 494, in check
    for pattern in self.url_patterns:
                   ^^^^^^^^^^^^^^^^^
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/utils/functional.py", line 57, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ~~~~~~~~~^^^^^^^^^^
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/urls/resolvers.py", line 715, in url_patterns
    patterns = getattr(self.urlconf_module, "urlpatterns", self.urlconf_module)
                       ^^^^^^^^^^^^^^^^^^^
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/utils/functional.py", line 57, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ~~~~~~~~~^^^^^^^^^^
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/urls/resolvers.py", line 708, in urlconf_module
    return import_module(self.urlconf_name)
  File "/home/cest7362/.pyenv/versions/3.13.2/lib/python3.13/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/home/cest7362/project/project/urls.py", line 13, in <module>
    path('accounts/', include('accounts.urls')),
                      ~~~~~~~^^^^^^^^^^^^^^^^^
  File "/home/cest7362/.virtualenvs/erb10/lib/python3.13/site-packages/django/urls/conf.py", line 38, in include
    urlconf_module = import_module(urlconf_module)
  File "/home/cest7362/.pyenv/versions/3.13.2/lib/python3.13/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1026, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/home/cest7362/project/accounts/urls.py", line 13, in <module>
    path('debug/', debug_user, name='debug_user'),
                   ^^^^^^^^^^
NameError: name 'debug_user' is not defined
Performing system checks...
