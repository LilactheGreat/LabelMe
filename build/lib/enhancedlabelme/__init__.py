# flake8: noqa

import logging
import sys

from qtpy import QT_VERSION


__appname__ = 'Enhanced LabelMe'

# Semantic Versioning 2.0.0: https://semver.org/
# 1. MAJOR version when you make incompatible API changes;
# 2. MINOR version when you add functionality in a backwards-compatible manner;
# 3. PATCH version when you make backwards-compatible bug fixes.
__version__ = '1.6.4'

QT4 = QT_VERSION[0] == '4'
QT5 = QT_VERSION[0] == '5'
del QT_VERSION

PY2 = sys.version[0] == '2'
PY3 = sys.version[0] == '3'
del sys

from enhancedlabelme.label_file import LabelFile
from enhancedlabelme import utils
