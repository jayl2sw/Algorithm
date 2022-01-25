def duplicated_letters2(word):
    result = []
    for char in word:
        if word.count(char) >= 2:
            if char not in result:
                result.append(char)
    return result

print(duplicated_letters2('apple'),
duplicated_letters2('banana')) # => ['a', 'n']