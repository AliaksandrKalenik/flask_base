##### System requirements:
    python3-dev

##### Install requirements
    pip install -Ur requirements.txt

##### Run:
    python flask_app.py
    uwsgi --http-socket :5000 -w flask_app:app

### Settings docs
    There are two config files:
        - project_settings.py
        - settings.py (or settings.yml)
    
    !Important!: settings variables MUST be in uppercase
    
    In `project_settings.py` file set common settings for project.
    In `settings.py` (`settings.yml`) file set environment dependent settings.
    
    !Important!: If `project_settings.py` and `settings.py` (`settings.yml`) have the same variable it will be value from `settings.py` (`settings.yml`)
