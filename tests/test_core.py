import unittest,copy,json
from stacked_action_anchor_audit import run
DEMO={'states': [[0, 0], [1, 1]], 'observation_deltas': [-1, 0], 'actions': [[0, 0], [2, 2]]}
class DomainTests(unittest.TestCase):
 def test_roundtrip_can_hide_stale_anchor(self):
  x=run(DEMO);self.assertTrue(x['legacy_roundtrip_matches']);self.assertFalse(x['anchor_current']);self.assertEqual(x['current_anchor_relative'][0],[-1,-1])
 def test_newest_first_is_already_correct(self):
  x=run(dict(DEMO,observation_deltas=[0,-1]));self.assertTrue(x['anchor_current']);self.assertEqual(x['current_anchor_relative'],x['first_anchor_relative'])
 def test_missing_current_never_guessed(self):
  with self.assertRaises(ValueError):run(dict(DEMO,observation_deltas=[-2,-1]))
