import json
from collections import defaultdict

import pymorphy3

INVERTED_INDEX_PATH = "inverted.txt"


class BooleanSearch:
    AND = "&"
    OR = "|"
    NOT = "~"
    OPERATORS = (AND, OR, NOT)

    def __init__(self) -> None:
        self.inverted_index = self.get_inverted_index()
        self.morph = pymorphy3.MorphAnalyzer()

    def get_normal_form(self, word):
        morph = self.morph.parse(word)
        return morph[0].normal_form

    def search(self, string):
        words = string.strip().split()
        all_indexes = set.union(*self.inverted_index.values())
        result = set()
        i = 0
        while i < len(words):
            word = words[i]
            if i + 1 != len(words) and (word in (self.AND or self.OR)):
                next_word = words[i + 1]
                if word == self.AND:
                    result = result.intersection(
                        self.inverted_index[self.get_normal_form(next_word)]
                    )
                elif word == self.OR:
                    result = result.union(
                        self.inverted_index[self.get_normal_form(next_word)]
                    )
                i += 1
            elif word.startswith(self.NOT):
                result = result.union(
                    all_indexes.difference(
                        self.inverted_index[self.get_normal_form(word[1:])]
                    )
                )
            else:
                result = result.union(self.inverted_index[self.get_normal_form(word)])
            i += 1

        return result

    def get_inverted_index(self):
        inverted_index = defaultdict(set)
        with open(INVERTED_INDEX_PATH) as f:
            for line in f.readlines():
                index = json.loads(line.replace("'", '"').strip())
                inverted_index[index["word"]] = set(index["inverted_array"])

        return inverted_index


if __name__ == "__main__":
    boolean_search = BooleanSearch()
    search_string = input("Enter query ")
    print(boolean_search.search(search_string))
