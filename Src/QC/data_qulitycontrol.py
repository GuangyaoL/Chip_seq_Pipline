#! -*- utf-8 -*-
########################################################################################################################
# 主要利用fastp进行数据质控，包括去除adaptor，低质量的reads和低复杂reads；
# 如果序列中添加了barcode进行特异性确认，该脚本不适用
# 如果有问题，请联系guangyuel@163.com
########################################################################################################################


import re
import sys
# sys.argv=['']
# del sys
# import sys
import os
import gzip
import itertools
import logging
import time
import subprocess
import argparse
basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if basedir not in sys.path:
    sys.path.append(basedir)
from config import software,config

def qulity_control(fastp, failed_out,splitlines, r1, r2, qulity, Qpercentlimit,o1=None, o2=None,
                   html='qulitycontrol.html',json='qulitycontrol.json',
                   adapterfa=config.adapter,fastfa=os.path.join(basedir,'config','adaper.fa')):
    '''
    书写linux QC 执行脚本，默认使用illumina 测序平台，如果使用其它平台，请更换默认接头序列
    :param fastp: fastp software
    :param failed_out:filtered reads output
    :param splitlines: cleandata output by reads lines number
    :param r1:  reads1 path
    :param r2: reads2 path
    :param o1: reads1 clean data name
    :param o2: reads2 clean data name
    :param qulity: 质量值Q
    :param Qpercentlimit: 低质量值所占reads比例
    :param html: 输出统计结果的html文件名
    :param jason:  输出统计结果的json名
    :param jason:
    :param jason:
    :param adapterfa: ilumina 平台使用的接头序列，可在config文件中修改
    :param fastfa: 一些特殊的接头序列，使用fasta格式存放，文件在config路径中
    :return: 当前路径下质控的Linux脚本
    '''
    try:
        ppsamplename = re.search('(.*)R1.fq.gz', os.path.basename(r1))
        psamplename = ppsamplename.groups()[0]
    except:
        print('R1 name maybe error! please check it!')
        sys.exit(1)
    samplename = psamplename.rstrip('_')
    if not o1:
        o1 = samplename+'_clean_R1.f1.gz'
    if not o2:
        o2 = samplename+'_clean_R2.f1.gz'
    if not re.match('^[a-zA-z0-9]',samplename):
        print('the sample name is out of rules,please used letters and numbers start!')
        sys.exit(1)
    with open(samplename+'.qc.sh','w')as fw:
        fw.write(config.shell_heaader)
        fw.write('date\n')
        if failed_out:
            fw.write('{fastp} -i {r1} -I {r2} -o {o1} -O {o2} --failed_out {failedout} -S {splitlines} -q {qulity} -u {qsp} -j {j} -h {h} -y --detect_adapter_for_pe --adapter_sequence {r1f} --adapter_sequence_r2 {r2f} --adapter_fasta {adpt}\n'.format(
                fastp=fastp,r1=r1,r2=r2,o1=o1,o2=o2,failedout=failed_out,splitlines=splitlines,qulity=qulity,qsp=Qpercentlimit,
                h=html, j=json, adpt=fastfa, r1f=adapterfa['adapter_sequence'], r2f=adapterfa['adapter_sequence_r2']
            ))
        else:
            fw.write(
                '{fastp} -i {r1} -I {r2} -o {o1} -O {o2} -S {splitlines} -q {qulity} -u {qsp} -j {j} -h {h} -y --detect_adapter_for_pe --adapter_sequence {r1f} --adapter_sequence_r2 {r2f} --adapter_fasta {adpt}\n'.format(
                    fastp=fastp, r1=r1, r2=r2, o1=o1, o2=o2, splitlines=splitlines, qulity=qulity,
                    qsp=Qpercentlimit,
                    h=html, j=json, adpt=fastfa, r1f=adapterfa['adapter_sequence'], r2f=adapterfa['adapter_sequence_r2']
                ))
        fw.write('date\n')



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='QC',
        usage='%(prog)s [options]',
        description='the QC script ,depend on fastp'
    )
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('--software', '-p',help='the fastp software path,default get in config',
                        default=software.fastp)
    parser.add_argument('--read1', '-r1', help='reads1 path',required=True)
    parser.add_argument('--read2', '-r2', help='reads2 path',required=True)
    parser.add_argument('--output1', '-o1', help='output fastq1 file name',default=None)
    parser.add_argument('--output2', '-o2', help='output fastq2 file name',default=None)
    parser.add_argument('--failed_out',help='failed output name',default=None)
    parser.add_argument('--qulity', '-q',help=' the quality value that a base is qualified. Default 15 means phred quality >=Q15 is qualified',
                        type=int, default=15 )
    parser.add_argument('--unqualified_percent_limit','-u',help='how many percents of bases are allowed to be unqualified (0~100). Default 40 means 40%',
                        type=int, default=40 )
    args = parser.parse_args()
    if args.unqualified_percent_limit not in range(1,101):
        print('the unqualified_percent_limit are the percent ,so you should input less 100')
        sys.exit(1)
    #(fastp, failed_out,splitlines, r1, r2, qulity, Qpercentlimit,
    qulity_control(args.software, args.failed_out,40000,args.read1,args.read2,args.qulity,args.unqualified_percent_limit)
