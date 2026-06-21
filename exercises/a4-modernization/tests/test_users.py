from modernized.users import User, find_by_email, load_users


def test_load_users_filters_incomplete():
    users = load_users([{"email": "a@x.com", "name": "A"}, {"email": "bad"}])
    assert len(users) == 1
    assert users[0].email == "a@x.com"


def test_find_by_email():
    users = load_users([{"email": "a@x.com", "name": "A"}, {"email": "b@x.com", "name": "B"}])
    assert find_by_email(users, "b@x.com") == User(email="b@x.com", name="B")
