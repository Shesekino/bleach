import os
import unittest
import subprocess

class TestPullRequest(unittest.TestCase):

    def test_pullrequest(self):
        ENV = os.environ.copy()
        CMD = [
          "python3",
          "./bleach/__main__.py",
          "shesekino",
          "bleach",
          "pr",
        ]
        prOutput = subprocess.check_output(CMD, stdin=None, stderr=None, env=ENV)
        
        self.assertTrue('*bleach*' in prOutput)
        self.assertTrue('[USED IN MANUAL TESTS] insignificant PR' in prOutput)
        self.assertTrue('open for' in prOutput)
        self.assertTrue('owner is Shesekino' in prOutput)
        self.assertTrue('https://github.com/Shesekino/bleach/pull/3' in prOutput)
        
        self.assertTrue('*bleach*' in prOutput)
        self.assertTrue('[USED IN MANUAL TESTS] sweet touch, you\'ve given me too much to feel' in prOutput)
        self.assertTrue('open for' in prOutput)
        self.assertTrue('owner is Shesekino' in prOutput)
        self.assertTrue('https://github.com/Shesekino/bleach/pull/4' in prOutput)
