"""Offline YAML and shell-syntax regression checks, not full Actions validation."""
from pathlib import Path
import subprocess
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]


class WorkflowContractTests(unittest.TestCase):
    def test_workflow_yaml_and_run_steps(self):
        # BaseLoader preserves the YAML key 'on' as text (not a YAML 1.1 boolean).
        paths = sorted((ROOT / '.github/workflows').glob('*.y*ml'))
        self.assertTrue(paths)
        for path in paths:
            workflow = yaml.load(path.read_text(), Loader=yaml.BaseLoader)
            self.assertIn('on', workflow)
            self.assertEqual(workflow['permissions'], {'contents': 'read'})
            self.assertNotIn('pull_request_target', workflow['on'])
            for job in workflow['jobs'].values():
                self.assertIn('timeout-minutes', job)
                for step in job['steps']:
                    if 'run' in step:
                        self.assertIsInstance(step['run'], str)
                        checked = subprocess.run(['bash', '-n'], input=step['run'],
                                                 text=True, capture_output=True, check=False)
                        self.assertEqual(checked.returncode, 0, checked.stderr)

    def test_old_missing_block_scalar_is_rejected(self):
        broken = "steps:\n  - run: python - <<'PY'\n    print('schema: PASS')\n    PY\n"
        with self.assertRaises(yaml.YAMLError):
            yaml.load(broken, Loader=yaml.BaseLoader)
