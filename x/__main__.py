import bjoern

from x.app import init_app

bjoern.run(init_app(), "0.0.0.0", 5000)
