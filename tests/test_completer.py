from completer import Completer

def test_completer_returns_matches():
    c = Completer()
    c.set_keywords(["apple", "banana", "grape"])

    result = c.completer("app", 0)

    assert result == "apple"
