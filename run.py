import os
from app import createApp

configMode = os.getenv("APP_SETTINGS")
app = createApp(configMode)


@app.route("/")
def test():
    return "This is the root url"


if __name__ == "__main__":
    app.run()
