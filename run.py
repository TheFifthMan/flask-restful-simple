from app import create_app
app = create_app('dev')
from app.auth.models import User
