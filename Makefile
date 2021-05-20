MANAGE = python manage.py
PROJECT_VERSION = 1.0.0

# Builds the project using 'development' settings.
dev:
	pip install -r requirements/dev.txt;
	$(MANAGE) clearcache;
	$(MANAGE) migrate;
	$(MAKE) -f $(THIS_FILE) fixtures-core;
	$(MAKE) -f $(THIS_FILE) docs-html;

run:
	$(MANAGE) runserver;