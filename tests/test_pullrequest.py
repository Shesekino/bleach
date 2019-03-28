import unittest

from bleach.commands import pullrequest

class TestPullRequest(unittest.TestCase):

    def test_pullrequest(self):
        prResult = pullrequest.main('shesekino', 'bleach')
