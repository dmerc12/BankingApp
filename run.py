from BankingApp.DAL import config
from BankingApp.FlaskAPI import create_back_end_api

api = create_back_end_api(config)

if __name__ == "__main__":
    api.run(debug=True)
