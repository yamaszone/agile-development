import subprocess
import pexpect

import unittest

def execute(cmd):
    output, status = pexpect.run(cmd
                                 , withexitstatus=1
                                 , timeout=600
                                )

    #print(output)
    return output


class test_awscreds(unittest.TestCase):

	def test_awscreds_returns_access_key_given_profile(self):
		self.assertIn('testvalue', execute('./awscreds -field key -profile profile1'))