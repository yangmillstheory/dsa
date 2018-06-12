class Solution(object):
    def fullJustify(self, words, width):
        out, line = [], []
        n_chars = 0
        for j, word in enumerate(words):
            if not line or 1+len(word)+n_chars <= width:
                line.append(word)
                n_chars += len(word)
                if len(line) > 1:
                    n_chars += 1
            else:
                out.append(self._make_justified_line(line, width))
                line = [word]
                n_chars = len(word)
        if line:
            # make the last line, which is special
            last = ' '.join(line)
            last += ' '*(width-len(last))
            out.append(last)
        return out

    def _make_justified_line(self, line, width):
        if len(line) == 1 and len(line[0]) < width:
            places = 1
        elif len(line) > 1:
            places = len(line)-1
        else:
            # single word that fits width exactly
            return line[0]
        # count of spaces to place after each word
        spaces = [1 for _ in range(places)]
        filled = sum([len(word) for word in line]) + sum(spaces)
        n, xtra = divmod(width-filled, places)
        for i in range(places):
            spaces[i] += n
        for i in range(1, xtra+1):
            spaces[i-1] += 1
        out = ''
        for word, n in zip(line, spaces + [0]):
            out += word + ' '*n
        return out
