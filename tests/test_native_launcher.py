from paths import ROOT
import importlib.util
import os
import subprocess
import sys
import unittest

sys.path.insert(0, str(ROOT / 'launcher'))
spec = importlib.util.spec_from_file_location('native_launcher', ROOT / 'launcher/uncharted_launcher.py')
launcher = importlib.util.module_from_spec(spec)
spec.loader.exec_module(launcher)


@unittest.skipIf(os.name == 'nt', 'Linux launcher checks')
class NativeLauncherTests(unittest.TestCase):
    def test_linux_preserves_portable_settings_location(self):
        self.assertEqual(launcher.CONFIG_DIR, launcher.DATA_DIR)

    def test_linux_stdio_does_not_use_msvcrt(self):
        launcher.attach_stdio()

    def test_stop_terminates_linux_game_process_group(self):
        process = subprocess.Popen([sys.executable, '-c', 'import time; time.sleep(60)'],
                                   start_new_session=True)
        try:
            job = launcher.GameJob(process)
            job.terminate()
            process.wait(timeout=5)
            job.close()
        finally:
            if process.poll() is None:
                process.terminate()
                process.wait(timeout=5)


if __name__ == '__main__':
    unittest.main()
