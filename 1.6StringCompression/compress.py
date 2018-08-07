import unittest


# O(n)
def string_compression(mystr: str):
    new_str = []
    previous = ""
    count = 0  # number of repeated characters

    for char in mystr:
        if char == previous:
            count += 1
        else:
            if previous != "":
                new_str.append(previous + str(count))
            count = 1  # reset counter
        previous = char

    new_str.append(previous + str(count))
    new_str = "".join(new_str)
    if (len(mystr) < len(new_str)):
        return mystr
    else:
        return new_str


class MyTest(unittest.TestCase):
    def test_string_compression(self):
        self.assertEqual(string_compression("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(string_compression("abc"), "abc")
        self.assertEqual(string_compression("aabCCCC"), "a2b1C4")


if __name__ == "__main__":
    unittest.main()
