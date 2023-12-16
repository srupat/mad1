from main import app
from application.database import db

def test_no_articles_home():
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()

    db.create_all()
    response = client.get('/')
    assert b"<title>All Articles</title>" in response.data

    ctx.pop()
    db.drop_all()