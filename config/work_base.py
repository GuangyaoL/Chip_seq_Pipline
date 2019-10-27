#! -*- utf-8 -*-
import os
import sys
import time
import yaml
import os
import logging

basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def logger(loger_type):
    # yaml file get
    yamfile = get_ymal_load(os.path.join(basedir, 'config', 'conf.YAML'))
    log_type = time.strftime("%Y_%m_%d", time.localtime()) + ".log"
    # create logger
    logger = logging.getLogger(loger_type)
    logger.setLevel(yamfile['Info']['LOG_Level'])
    # creat console handler
    ch = logging.StreamHandler()
    ch.setLevel(yamfile['Info']['LOG_Level'])
    log_file = os.path.join(basedir, 'log', log_type)
    fh = logging.FileHandler(log_file)
    fh.setLevel(yamfile['Info']['LOG_Level'])
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    return logger


def get_ymal_load(yamlfile):
    """
    load yaml file by yaml
    :param yamlfile: filename
    :return: yamldata
    """
    with open(yamlfile, 'r', encoding='utf-8') as fr:
        filedata = fr.read()
    yamldata = yaml.full_load(filedata)
    return yamldata

