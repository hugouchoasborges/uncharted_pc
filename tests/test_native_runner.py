from paths import ROOT
import importlib.util
import os
import unittest

spec = importlib.util.spec_from_file_location('native_runner', ROOT / 'run.py')
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


@unittest.skipIf(os.name == 'nt', 'Linux runner checks')
class NativeRunnerTests(unittest.TestCase):
    def test_linux_does_not_use_windows_console_flags(self):
        self.assertEqual(runner.no_console(), 0)

    def test_waiting_for_missing_linux_process_returns(self):
        runner.wait_for(1_000_000_000)


if __name__ == '__main__':
    unittest.main()
