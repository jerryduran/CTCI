import unittest

def is_one_away(first: str, other: str) -> bool:
    """Given two strings, check if they are one edit away. An edit can be any one of the following.
    1) Inserting a character
    2) Removing a character
    3) Replacing a character"""
    if len(first) < len(other):
        first, other = other, first

    if len(first) - len(other) > 1:
        return False

    elif len(first) - len(other) == 1:
        for pos in range(len(first)):
            if first[:pos] + first[pos+1:] == other:
                return True
        return False

    else:
        num_different_chars = sum(1 for pos in range(len(first)) if first[pos] != other[pos])
        return num_different_chars < 2


class MyTest(unittest.TestCase):
    def test_is_one_away(self):
        self.assertEqual(is_one_away('pale', 'ale'), True)
        self.assertEqual(is_one_away('pales', 'pale'), True)
        self.assertEqual(is_one_away('pale', 'bale'), True)
        self.assertEqual(is_one_away('pale', 'bake'), False)
        self.assertEqual(is_one_away('ale', 'pale'), True)
        self.assertEqual(is_one_away('aale', 'ale'), True)
        self.assertEqual(is_one_away('aael', 'ale'), False)
        self.assertEqual(is_one_away('motherinlaw', 'womanhitler'), False)
        self.assertEqual(is_one_away('motherinlaw','motherinlow'), True)


if __name__ == "__main__":
    unittest.main()