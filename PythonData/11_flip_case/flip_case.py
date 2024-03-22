def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    modified_chars = []
    for char in phrase:
        if char.lower() == to_swap.lower():
            if char.isLower():
                modified_chars.append(char.upper())
            else:
                modified_chars.append(char.lower())
        else:
            modified_chars.append(char)

            return ''.join(modified_chars)
        

print(flip_case('Aaaahhh', 'a'))
print(flip_case('Aaaahhh', 'A')) 
print(flip_case('Aaaahhh', 'h'))