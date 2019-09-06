import sys
import os

# Adds "src" to sys.path
# "src" contains a package "big_package"
# Now you can do import with "from big_package.Sub-Package ..."
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', "src")))
