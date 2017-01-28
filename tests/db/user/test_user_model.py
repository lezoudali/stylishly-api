from db.user.model import User


def test_user_model(save_model, user_data, session, compare_attributes):
    user = User(**user_data)

    assert not user.id

    save_model(user)

    assert user.id

    queried_user = session.query(User).get(user.id)

    compare_attributes(queried_user, user_data)
