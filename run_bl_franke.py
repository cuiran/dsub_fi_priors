#!/usr/bin/env python

import subprocess
import os
import sys

#assign variables
METHOD = os.environ['METHOD']
FM = os.environ['FM']
CHR = os.environ['CHR']
ANNOT = os.environ['ANNOT']
OUT = os.environ['OUT']

#make directories
subprocess.call(['mkdir','/mnt/data/fm/'])
subprocess.call(['mkdir','/mnt/data/annot/'])
subprocess.call(['mkdir','/mnt/data/result/'])

#copy data
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/data/annot_and_ldscore/UKBB/baselineLF_v2.2_MAF001_UKBB/baselineLF_withID.*','/mnt/data/annot/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/data/annot_and_ldscore/UKBB/Franke/Franke.all.*','/mnt/data/annot/'])
subprocess.call(['gsutil','-m','cp','gs://regularized_sldsc/results/fine-mapping/UKB.Height/Height.SuSiE.snp','/mnt/data/fm/'])

#run script
returncode = subprocess.call(['python','/home/pyscripts/compare_models.py',
    '--method',METHOD,
    '--fm-fname',FM,
    '--leave-chr',CHR,
    '--annot-prefix',ANNOT,
    '--out',OUT])
if returncode!=0:
    sys.exit(1)

subprocess.call(['gsutil','-m','cp','/mnt/data/result/*','gs://regularized_sldsc/FI_priors/compare_models/Height/'])
