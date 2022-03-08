class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        count = 0
        indices = []

        for index, word in enumerate(words):
            count += len(word) + 1

            # check if length is exceeded
            if count - 1 > maxWidth:

                # count spaces
                total_spaces = maxWidth - sum(len(words[idx]) for idx in indices)

                # compose the line
                if len(indices) == 1:
                    line = f"{words[indices[0]]}{' ' * total_spaces}"
                else:
                    space_counts = [0] * (len(indices) - 1)
                    for i in range(total_spaces):
                        space_counts[i % (len(indices) - 1)] += 1

                    line = words[indices[0]]
                    for space_count, idx in zip(space_counts, indices[1:]):
                        line += f"{' ' * space_count}{words[idx]}"

                ret.append(line)

                count = len(word) + 1
                indices = []

            indices.append(index)

        # handle the last line
        line = " ".join(words[idx] for idx in indices)
        line += " " * (maxWidth - len(line))
        ret.append(line)

        return ret
