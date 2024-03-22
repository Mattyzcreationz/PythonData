def friend_date(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date(elmo, sauron)
        False

        >>> friend_date(sauron, gandalf)
        True
    """
    hobbies_a = set(a[2])
    hobbies_b = set(b[2])

    return not hobbies_a.isdisjoint(hobbies_b)
elmo = ('Elmo', 5, ['hugging', 'being nice'])
sauron = ('Sauron',  5000, ['killing hobbitrs', 'chess'])
gandalf = ('Gandalf', 1000, ['wavings wands', 'chess'])

print(friend_date(elmo, sauron))
print(friend_date(sauron, gandalf))
