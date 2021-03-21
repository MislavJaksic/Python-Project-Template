import cProfile
from poetry_template import runner

cProfile.run("runner.main(None)")
