from doctest import debug
from app import ProjApp
from models import create_user_table

app = ProjApp()

if __name__ == "__main__":
    create_user_table()
    app.run(debug=True)