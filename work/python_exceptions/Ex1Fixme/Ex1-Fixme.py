#!/usr/bin/env python3
def save(filename, data):
    with open(filename, 'w') as fn:
        fn.write(str(data))

blog_posts = [{'Photos': 3, 'Likes': 21, 'Comments': 2}, {'Likes': 13, 'Comments': 2, 'Shares': 1}, {'Photos': 5, 'Likes': 33, 'Comments': 8, 'Shares': 3},
{'Comments': 4, 'Shares': 2}, {'Photos': 8, 'Comments': 1, 'Shares': 1}, {'Photos': 3, 'Likes': 19, 'Comments': 3}]
total_likes = 0

for post in blog_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

print('Total likes count', total_likes)

try:
    from unittest.gui import TestCaseGui
except ModuleNotFoundError:
    from unittest import TestCase

class myTests(TestCase):
    def testA(self):
        self.assertEqual(total_likes, 86, "Testing that total_likes has the correct value.")
    def testB(self):
        accum = 0
        for d in blog_posts:
            if 'Likes' in d:
                accum += 1
        try:
            self.assertEqual(accum, 6, "Testing that blog_post dictionaries all have a 'Likes' key.")
        except AssertionError:
            print(f'{0} != 6'.format(accum))
            save('output.txt', f'{0} != 6'.format(accum))
    def main(self):
        self.testA()
        self.testB()
myTests().main()
