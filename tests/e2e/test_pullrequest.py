import os
import unittest
import subprocess

class TestPullRequest(unittest.TestCase):

    def test_pullrequest(self):
        ENV = os.environ.copy()
        CMD = [
          "python3",
          "./bleach/__main__.py",
        ]
        shit = subprocess.check_output(CMD, stdin=None, stderr=None, env=ENV)
        print("shit:", shit)
        
