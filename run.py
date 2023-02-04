import logging
import os

from PythonAPI.FlaskAPI import create_app
from PythonAPI.DAL import config

app = create_app(config)

@app.before_request
def set_up_logs():
    log_level = logging.DEBUG
    for handler in app.logger.handlers:
        app.logger.removeHandler(handler)
    log_directory = "../Logs"
    if not os.path.exists(log_directory):
        os.mkdir(log_directory)
    log_file = os.path.join("PythonAPI/Logs",
                            'BankingLogs.log')
    handler = logging.FileHandler(log_file)
    handler.setLevel(log_level)
    app.logger.addHandler(handler)
    app.logger.setLevel(log_level)

if __name__ == "__main__":
    app.run(debug=True)
