import sys
import unittest
from unittest.mock import Mock

from paths import ROOT

sys.path.insert(0, str(ROOT / 'launcher'))
import uncharted_launcher


class LauncherLanguageRebuildTests(unittest.TestCase):
    def test_language_change_recreates_existing_update_notice(self):
        launcher = object.__new__(uncharted_launcher.Launcher)
        child = Mock()
        launcher.root = Mock()
        launcher.root.winfo_children.return_value = [child]
        launcher.current_page = 'game'
        launcher.app = {'ui_language': 'fr'}
        launcher.update_info = ('0.4.0', 'https://example.test/update.zip',
                                'https://example.test/release')
        launcher.update_box = object()
        launcher.vars = {'old': object()}
        launcher.process = None
        launcher.collect = Mock()
        launcher.build = Mock()
        launcher.show = Mock()
        launcher.refresh = Mock()
        launcher.offer_update = Mock()

        uncharted_launcher.Launcher.change_ui_language(launcher)

        child.destroy.assert_called_once_with()
        launcher.build.assert_called_once_with()
        launcher.show.assert_called_once_with('game')
        launcher.refresh.assert_called_once_with()
        launcher.offer_update.assert_called_once_with(*launcher.update_info)


if __name__ == '__main__':
    unittest.main()
