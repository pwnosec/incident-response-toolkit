def match_patterns(data, patterns):
    matches = [pattern for pattern in patterns if pattern in data]
    return matches
