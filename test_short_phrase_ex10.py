
class TestPhrase:
    def test_short_phrase(self):
        phrase = input("Set a phrase: ")
        max_len = 15

        assert len(phrase) <= max_len, f"Your phrase has more than {max_len} characters"
