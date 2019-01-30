from app.create_app import create_app
from app.config import current_config

app = create_app(current_config)

if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True)