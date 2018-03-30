import os
import yaml
from flask import Flask
from flask import jsonify

app = Flask(__name__)
app.config.from_pyfile(os.path.join(app.root_path, 'project_settings.py'))

SETTINGS_FILE_YAML = os.path.join(app.root_path, "settings.yml")
SETTINGS_FILE_PY = os.path.join(app.root_path, "settings.py")

try:
    with open(SETTINGS_FILE_YAML, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
        if not cfg:
            raise IOError
        for section, params in cfg.items():
            for param_name, param_value in params.items():
                app.config[param_name] = param_value
except IOError:
    try:
        app.config.from_pyfile(SETTINGS_FILE_PY)
    except ImportError:
        print("Setting file ({}, {}) not found".format(SETTINGS_FILE_YAML, SETTINGS_FILE_PY))


@app.route('/settings/', methods=['GET'])
def get_all_settings():
    return jsonify({k: str(v) for k, v in app.config.items()})


if __name__ == '__main__':
    app.run(debug=app.config.get('FLASK_DEBUG', 0))
