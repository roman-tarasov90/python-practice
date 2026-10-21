from main import make_greeting # type: ignore

def test_make_greeting():
  assert make_greeting({"name": "Alex"}) == "Привет, Alex!"

