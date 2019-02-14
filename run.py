import os
from app import createApp
from app.api.database.migrations.migrations import migrate

# configMode = os.getenv("APP_SETTINGS")
app = createApp("development")
migrate()


@app.route("/")
def test():
    return "This is the root url"


if __name__ == "__main__":
    app.run()
