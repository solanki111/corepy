# Given a words.txt file containing a newline-delimited list of dictionary
# words, please implement the Anagrams class so that the get_anagrams() method
# returns all anagrams from words.txt for a given word.
#
# Requirements:
#   - Optimise the code for fast retrieval - I believe the current implementation is the fastest approach as its of
#                                            order n.
#   - Write more tests
#   - Thread safe implementation        - Since its a cpu bound operation multiprocessing would be a good fit for this
#                                         use case instead of threading. With the current implementation of the
#                                         get_anangrams method its only of order n but say if we were to send a list of
#                                         words and needed to find an anagram for each that will be a good use case for
#                                         multiprocessing as each word can be evaluated in separate processes.


from collections import Counter, defaultdict
import unittest


class Anagrams:

    def __init__(self):
        # self.words = open('words.txt').readlines()
        with open('words.txt') as f:
            self.words = f.read().splitlines()

    def get_anagrams(self, word):
        a_list = list(word)
        a_list.sort()
        possible_anags = []
        for w in self.words:
            new_w = w.rstrip('\n')
            b_list = list(new_w)
            if len(a_list) == len(b_list):
                b_list.sort()
                if a_list == b_list:
                    possible_anags.append(new_w)

        return possible_anags

    def word_count(self):
        word_dict = {}
        for w in self.words:
            word = w.rstrip('\n')
            if word in word_dict.keys():
                value = word_dict.get(word)
                word_dict.update({word: value + 1})
            else:
                word_dict[word] = 1

        word_more_than_five = [k for k, v in word_dict.items() if v > 2]
        # for k, v in word_dict.items():
        #     if v > 2:
        #         word_more_than_five.append(k)

        print('---------------------')
        print(len(word_more_than_five))
        return word_more_than_five

    def get_anagrams_two(self, word):
        possible_anags = [w.rstrip('\n') for w in self.words if Counter(w.rstrip('\n')) == Counter(word)]
        return possible_anags


class TestAnagrams(unittest.TestCase):

    def test_anagrams(self):
        anagrams = Anagrams()
        l1 = anagrams.get_anagrams('eat')
        l2 = anagrams.get_anagrams('plates')
        l3 = ['ate', 'eat', 'tea', 'eta']
        l4 = ['palest', 'pastel', 'petals', 'plates', 'staple', 'pleats']
        self.assertEqual(l2.sort(), l4.sort())
        self.assertEqual(l1.sort(), l3.sort())
        self.assertCountEqual(l2, l4)
        self.assertCountEqual(l1, l3)

    def test_anagrams_two(self):
        anagrams = Anagrams()
        l1 = anagrams.get_anagrams_two('eat')
        l2 = anagrams.get_anagrams_two('plates')
        l3 = ['ate', 'eat', 'tea', 'eta']
        l4 = ['palest', 'pastel', 'petals', 'plates', 'staple', 'pleats']
        self.assertEqual(l2.sort(), l4.sort())
        self.assertEqual(l1.sort(), l3.sort())
        self.assertCountEqual(l2, l4)
        self.assertCountEqual(l1, l3)

    def test_anagrams_three(self):
        # testing with non-existing word, should return 0.
        anagrams = Anagrams()
        # l1 = anagrams.get_anagrams_two('word')
        # self.assertEqual(len(l1), 0)
        l3 = anagrams.word_count()
        print(l3)


if __name__ == '__main__':
    unittest.main()
