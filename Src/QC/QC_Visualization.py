#! -*- utf-8 -*-

import os
import argparse
from argparse import RawTextHelpFormatter
import json
import time
help(json)


if __name__ == '__main__':
    print(time.strftime("%Y-%m-%d %X", time.localtime()))
    visual_argv = argparse.ArgumentParser(
        prog='QC Visualization',
        usage='%(QC Visualization)s [options]',
        description="the visualization of data qulity by used software fastp .\nif you have some qusition, please Contact:guangyuel@163.com",
        formatter_class=RawTextHelpFormatter,
    )
    visual_argv.add_argument('--json', '-j', help='fastp software result',)