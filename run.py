import os
from app import createApp

configMode = os.getenv("APP_SETTINGS")
app = createApp(configMode)

@app.route("/")
def test():
    return "hello world"

if __name__ == "__main__":
    app.run()