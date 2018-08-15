import unittest

# O(N)


def isSubstring(str1: str, str2: str):
    if len(str1) != len(str2):
        return False
    else:
        str1 += str1
        return True if str2 in str1 else False

class Test(unittest.TestCase):
    """Test Case"""

    def test_isSubstring(self):
        self.assertEqual(isSubstring("waterbottle", "erbottlewat"), True)

if __name__ == "__main__":
    unittest.main()