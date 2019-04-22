import os
import unittest
import subprocess

class TestPullRequest(unittest.TestCase):

    def test_branch(self):
        ENV = os.environ.copy()
        CMD = [
          "python3",
          "./bleach/__main__.py",
          "shesekino",
          "bleach",
          "branch",
          "test-branch-discrepancy-1",
          "test-branch-discrepancy-2",
        ]
        prOutput = subprocess.check_output(CMD, stdin=None, stderr=None, env=ENV)
        
        self.assertTrue('*bleach*' in prOutput)
        self.assertTrue('primary branch `test-branch-discrepancy-1` seems to be missing commits from secondary branch `test-branch-discrepancy-2`' in prOutput)

    def test_branch_silent(self):
        ENV = os.environ.copy()
        ENV['BLEACH_PRINT_ONLY_ACTIONABLE'] = 'True'
        CMD = [
          "python3",
          "./bleach/__main__.py",
          "shesekino",
          "bleach",
          "branch",
          "test-branch-discrepancy-1",
          "test-branch-discrepancy-1",
        ]
        prOutput = subprocess.check_output(CMD, stdin=None, stderr=None, env=ENV)

        self.assertFalse(prOutput)
        self.assertEqual(prOutput, '')
