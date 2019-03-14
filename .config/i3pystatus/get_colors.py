import json
from pathlib import Path
from os.path import join

colors = json.load(open(join(Path.home(), ".cache/wal/colors.json")))
