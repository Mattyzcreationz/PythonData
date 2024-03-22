def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
def is_palindrom(phrase):
    normalized_phrase = ''.join(phrase.lower().split())
    return normalized_phrase ==  normalized_phrase[::-1]
print(is_palindrom('tacocat'))
print(is_palindrom('noon'))
print(is_palindrom('robert'))
