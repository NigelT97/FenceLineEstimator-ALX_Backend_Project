from doctest import debug
from app import app
from models import create_user_table

if __name__ == "__main__":
    create_user_table()
    app.run(debug=True)