#import sys
#raise RuntimeError(sys.executable)
#del sys.path[:]
#sys.path.extend(['/usr/lib/python312.zip', '/usr/lib/python3.12', '/usr/lib/python3.12/lib-dynload', '/home/deploy/venv_pyramid/lib/python3.12/site-packages'])
import os
os.environ["SYNTH_TREE_VIEW_ROOT"] = "/home/mholder/ot2026/webapp-tree-viewer/synthetic_tree_viewer"
from pyramid.paster import get_app, setup_logging
ini_path = '/home/deploy/repos/webapp-tree-viewer/mth_production.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')

