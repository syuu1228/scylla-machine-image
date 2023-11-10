import os
import sys

MACHINE_IMAGE_ROOT = os.path.dirname(os.path.realpath(__file__))
MACHINE_IMAGE_VENDOR = os.sep.join([MACHINE_IMAGE_ROOT, 'vendor'])
sys.path.append(MACHINE_IMAGE_VENDOR)