from PythonAPI.API import create_app
from PythonAPI.API import config

app = create_app(config)

if __name__ == '__main__':
    app.run(debug=True)
