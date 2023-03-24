from BankingApp.DAL.Database import config
from BankingApp.FlaskAPI import create_back_end_api

app = create_back_end_api(config)

if __name__ == "__main__":
    app.run(debug=True)
