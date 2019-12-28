import os
import sys

# Adds "poetry_template" to sys.path
# Now you can do import with "from poetry_template.Sub-Package ..."
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "poetry_template"))
)
