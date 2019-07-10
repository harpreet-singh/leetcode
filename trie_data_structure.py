#!/usr/bin/env python3

class TrieNode:
    """
    Trie is an efficient information reTrieval data structure.
    """

    def __init__(self):
        # TODO: list or dictionary
        self.children = {}
        self.ends = False
        self.values = set()


class TrieDS:

    def __init__(self, li_strings):
        self.root = TrieNode()
        self.li_strings = li_strings

    def build_trie(self):
        cur = self.root
        for item in self.li_strings:
            li_item = list(item)
            for char in li_item:

                if not char in cur.children:
                    cur.children[char] = TrieNode()
                cur.values.add(item)
                # print(f"{char} : {cur.values}")
                cur = cur.children[char]

            cur.ends = True

    def search(self, lookup):

        cur = self.root
        prev = cur
        for char in list(lookup):

            if not char in cur.children:
                return []
            prev = cur
            cur = cur.children[char]

        return list(prev.values)


if __name__ == "__main__":
    look = "a"
    li_string = ["abc", "abd", 'cba']
    print(f"Input : {li_string}")
    tds = TrieDS(li_string)
    tds.build_trie()
    print(f"Search for <{look}>")
    print(tds.search(look))
