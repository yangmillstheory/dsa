def _get_term(word, ind):
    buf = []
    for i, ch in enumerate(word):
        d = ind[ch]
        if i == 0 and d == '0' and len(word) > 1:
            return None, False
        buf.append(d)
    return int(''.join(buf)), True


def isCryptSolution(words, key):
    ind = dict(key)
    lhs = 0
    for i, word in enumerate(words):
        term, is_valid = _get_term(word, ind)
        if not is_valid:
            return False
        lhs += term if i < len(words)-1 else -term
    return not lhs
