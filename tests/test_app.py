def test_index(client=None):
    from app import app

    with app.test_client() as c:
        resp = c.get("/")
        assert resp.status_code == 200
        assert resp.get_json()["status"] == "ok"


def test_health():
    from app import app

    with app.test_client() as c:
        resp = c.get("/health")
        assert resp.status_code == 200
        assert resp.get_json()["healthy"] is True
