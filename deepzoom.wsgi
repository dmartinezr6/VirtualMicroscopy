import os, sys
from deepzoom_multiserver import app as application
application.config.update({
    'SLIDE_DIR': '/home/hpclab/image/',
})

