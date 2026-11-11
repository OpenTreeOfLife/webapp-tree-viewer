#import sys
import os
os.environ["SYNTH_TREE_VIEW_ROOT"] = "/home/deploy/repos/webapp-tree-viewer/synthetic_tree_viewer"
from pyramid.paster import get_app, setup_logging
ini_path = '/home/deploy/repos/webapp-tree-viewer/mth_production.ini'
setup_logging(ini_path)
application = get_app(ini_path, 'main')

