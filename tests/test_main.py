from jinja2_env.main import add


def test_add():
    assert add(1, 1) == 2
