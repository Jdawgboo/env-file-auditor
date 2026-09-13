import unittest
from env_file_auditor import audit
class TestAudit(unittest.TestCase):
 def test_issues(self): self.assertEqual([x['issue'] for x in audit('A=1\nA=\nBAD')],['duplicate_key','blank_value','missing_equals'])
if __name__=='__main__': unittest.main()
