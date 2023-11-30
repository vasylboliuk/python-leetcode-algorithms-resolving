from src.tasks.palindrome_number import PalindromeNumberSolution


class TestPalindromeNumberSolution:

    def test_simple_number(self):
        assert PalindromeNumberSolution.is_palindrome(121) is True

    def test_negative_number(self):
        assert PalindromeNumberSolution.is_palindrome(-121) is False

    def test_zero_number(self):
        assert PalindromeNumberSolution.is_palindrome(0) is True

    def test_number_negative_case(self):
        assert PalindromeNumberSolution.is_palindrome(123) is False
