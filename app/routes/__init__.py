import importlib
import inspect
import pkgutil
from flask import Blueprint

def register_blueprints(app):
    from . import __path__ as routes_path

    for _, module_name, _ in pkgutil.iter_modules(routes_path):
        module = importlib.import_module(f'app.routes.{module_name}')

        for name, obj in inspect.getmembers(module):
            if isinstance(obj, Blueprint):
                app.register_blueprint(obj)
                print(f"Registered blueprint: {name} from {module_name}")
