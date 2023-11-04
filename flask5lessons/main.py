from routes import app

from models import create_db
create_db()
app.run()