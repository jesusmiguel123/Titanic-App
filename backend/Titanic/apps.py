from django.apps import AppConfig
from joblib import load
from pathlib import Path

class TitanicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Titanic'
    model_path = Path(__file__).parent / 'model' / 'model.joblib'
    model = load(model_path)