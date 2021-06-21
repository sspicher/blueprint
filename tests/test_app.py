# test_app.py
from .context import helloworld


def test_app(capsys, example_fixture):
    # pylint: disable=W0612,W0613
    helloworld.Blueprint.run()
    captured = capsys.readouterr()

    assert "Hello World..." in captured.out