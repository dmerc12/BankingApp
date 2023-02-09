from BankingApp.FlaskAPI import create_app
from BankingApp.DAL import config

app = create_app(config)

if __name__ == "__main__":
    app.run(debug=True)
