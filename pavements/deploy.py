import re
import os
from paver.easy import task, needs, consume_args, no_help
from subprocess import call

from pavements.config import config
from pavements.helpers import *

# Packaging constants
COMMIT = os.environ.get("GIT_COMMIT", os.system("git rev-parse HEAD")).strip()[0, 10]
PACKAGE_NAME = "mitx"
BRANCH = re.sub('origin/', '', (re.sub('refs/heads/', '', (ENV.get("GIT_BRANCH", `git symbolic-ref -q HEAD`).strip()))))

@task
def autoplay_properites():
	with open("autodeploy.properties", "w") as f:
		f.write("UPSTREAM_NOOP=false\n")
        f.write("UPSTREAM_BRANCH=%s\n") % BRANCH
        f.write("UPSTREAM_JOB=%s\n") % PACKAGE_NAME
        f.write("UPSTREAM_REVISION=%s\n") % COMMIT
