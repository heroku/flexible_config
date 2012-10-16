# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import unittest

import flexible_config
import pdb


class DatabaseTestSuite(unittest.TestCase):

    def test_truth(self):
        assert True

    def test_load_env(self):
        os.environ['OPT1'] = "value1"
        os.environ['OPT2'] = "value2"

        globals().update(flexible_config.load_local_config(['OPT1','OPT2'], config_file = "nofile"))
        self.assertIn('OPT1', globals())
        self.assertEqual("value1", globals()['OPT1'])

        flexible_config.check_required_options(['OPT1', 'OPT2', 'OPT3'], globals())

    def test_load_file(self):
        with open("/tmp/opts", "w") as f:
            f.write("[dev]\n")
            f.write("FOPT1=fval1\n")
            f.write("FOPT2=fval2\n")

            f.write("[prod]\n")
            f.write("FOPT1=fprod1\n")
            f.write("FOPT2=fprod2\n")

        self.assertNotIn('FOPT1', globals())
        if 'CCENV' in os.environ:
            del os.environ['CCENV']

        globals().update(flexible_config.load_local_config(['FOPT1','FOPT2'], config_file = "/tmp/opts"))
        self.assertIn('FOPT1', globals())
        self.assertEqual(FOPT1, "fval1")

        os.environ['CCENV'] = 'prod'

        globals().update(flexible_config.load_local_config(['FOPT1','FOPT2'], config_file = "/tmp/opts"))
        self.assertEqual(FOPT1, "fprod1")
        self.assertEqual(FOPT2, "fprod2")


if __name__ == '__main__':
    unittest.main()