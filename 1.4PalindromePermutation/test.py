import string
import unittest

def isPermuationOfPalindrome(str):
    str = str.lower()
    count = 0
    d = dict.fromkeys(string.ascii_letters, False)

    for char in str:
        if (ord(char) > 96 and ord(char) < 123):
            d[char] = not d[char]
    for key in d:
        if d[key] is True:
            count += 1
            if count > 1:
                return False
    return True

class Test(unittest.TestCase):

    def test(self):
        is_p_p = isPermuationOfPalindrome("aa bb cc")
        self.assertEqual(is_p_p, True)

    def tes2(self):
        is_p_p2 = isPermuationOfPalindrome("Tact Coa")
        self.assertEqual(is_p_p2, False)


if __name__ == "__main__":
  unittest.main()

