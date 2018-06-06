from app.create_app import create_app
from app.config import current_config

app = create_app(current_config)
