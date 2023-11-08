from flask import render_template
from app import app



@app.errorhandler(403)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def handler(e):

    return render_template('error.html', code=e.code)