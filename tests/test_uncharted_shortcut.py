import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from paths import ROOT

sys.path.insert(0, str(ROOT / 'launcher'))
import uncharted_launcher


class ShortcutFallbackTests(unittest.TestCase):
    def test_missing_custom_icon_uses_and_saves_original_icon(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            launcher = object.__new__(uncharted_launcher.Launcher)
            launcher.app = {
                'shortcut_name': 'Uncharted',
                'shortcut_icon': str(Path(temp_dir) / 'deleted-icon.png'),
            }
            launcher.messagebox = Mock()
            launcher.collect = Mock()
            process = Mock(returncode=0, stderr=b'')
            config_dir = Path(temp_dir) / 'config'

            with patch.object(uncharted_launcher, 'FROZEN', False), \
                    patch.object(uncharted_launcher, 'CONFIG_DIR', config_dir), \
                    patch.object(uncharted_launcher.subprocess, 'run', return_value=process) as run:
                uncharted_launcher.Launcher.create_shortcut(launcher)

        self.assertEqual(launcher.app['shortcut_icon'], '')
        launcher.collect.assert_called_once_with()
        command = run.call_args.args[0]
        self.assertIn(str(ROOT / 'launcher' / 'uncharted.ico'), command[3])
        launcher.messagebox.showinfo.assert_called_once()


if __name__ == '__main__':
    unittest.main()
