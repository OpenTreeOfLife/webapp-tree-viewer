webapp-tree-viewer
==================

This is the repository for the Open Tree of Life synthetic-tree viewer, one of many subsystems making up the Open Tree of Life project code. Previously, this was bundled in a common repo with the study-curation app, but we've seperated them as part of our conversion from web2py to Pyramid.

For Open Tree of Life documentation, see [the germinator repository's wiki](https://github.com/OpenTreeOfLife/germinator/wiki).

Installation
============

We strongly recommend using a virtual environment to manage the version of
Python and installed modules. We're currently running opentree with Python
v3.12. If necessary, compile Python3.12 and use it when making your virtualenv.

The included **requirements.txt** file lists known-good versions of all the required
python modules for opentree, plus a few convenience modules. To [install these modules 
using pip](http://www.pip-installer.org/en/latest/cookbook.html#requirements-files), 

The file **requirements.in** captures our intentions, typically following the
latest version of each module unless frozen to address bugs or incompatibilities.
To keep track if intentions vs. actuality, I recommend following this process
whenever the requirements change (or you re-run `pip install` to get the latest).
<pre>
# create a python3 venv inside the top-level folder
cd ~/repos/webapp-tree-viewer
export VENV="$(pwd)/venv"
python3 -m venv $VENV

# install the pinned set of known-good modules
pip install -r requirements.txt

# OR during development, try to update these using `requirements.in`
pip install -r requirements.in

# capture the resulting versions for production deploymentsl
$VENV/bin/pip freeze -r requirements.in > requirements.txt
# capture and save the full dependency tree for all modules
$VENV/bin/pipdeptree > pipdeptree.out
</pre>


**To test your local build with login and proper domain name**, modify your test system's
`/etc/hosts` file (or equivalent) to resolve the domain `devtree.opentreeoflife.org`
to localhost (127.0.0.1). Then run Pyramid on (privileged) port 80.

NB that we now assume HTTPS throughout, so this might require additional setup.

Acknowledgements
----------------
Argus uses Raphaeljs and jQuery libraries.

Arrow icons are from http://raphaeljs.com/icons those icons are licensed under the followin MIT license:

Copyright © 2008 Dmitry Baranovskiy

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

The software is provided “as is”, without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the software.
