class Solution(object):
    def fullJustify(self, words, width):
        out, line = [], []
        n_chars = 0
        for j, word in enumerate(words):
            if len(word) + n_chars + len(line) > width:
                if len(line) == 1:
                    out.append(line[0] + ' '*(width-n_chars))
                else:
                    n, xtra = divmod(width-n_chars, len(line)-1)
                    for j in range(xtra):
                        line[j] += ' '
                    out.append((' '*n).join(line))
                line, n_chars = [], 0
            line.append(word)
            n_chars += len(word)
        out.append(' '.join(line) + ' '*(width - len(line) + 1 - n_chars))
        return out
