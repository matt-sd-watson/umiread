#!/usr/bin/python

"""The 10X single cell RNA 3' assay generates Illumina-compatible libraries that can contain valuable sequencing
data corresponding to gene expression levels at single cell resolution. An essential element of the assay is the use
of a unique molecular identifier (UMI) in Read 1, which allows for unique transcript detection and the ability to
filter out amplification duplicates, leading to more accurate analysis of gene expression. umi_read provides the user
with a lightweight utility that can extract these UMI sequences and collect baseline quality-control statistics for
one or more FASTQ files, allowing for evaluation of UMI contents prior to downstream application"""

import gzip
from itertools import islice
import glob


def extract_from_single(filename):

    """
    Input: Single FASTQ files generated from a 10X single cell 3' Gene expression assay (any version
    supported).
    Output: A list containing the 10X unique molecular identified (UMI) sequences from the R1 FASTQ file.
    Note that reading FASTQ files other than the R1 is not supported
    For parsing multiple R1 FASTQ files i.e. multiple FASTQs from the same sample, use extract_from_folder
    """

    umi_append = []
    print("Reading UMI sequences from: {}".format(filename))
    with gzip.open(filename, 'rt') as handle:
            # append every fourth line of the fastq file starting with line 2, corresponding to all R1 sequences
            for line in islice(handle, 1, None, 4):
                # each appended line contains the last 10 characters of the 26 bp read containing the 10x UMI
                umi_append.append(line[16:26])
    return umi_append


def extract_from_folder(path):

    """
    Input: One or more FASTQ files generated from a 10X single cell 3' Gene expression assay (any version
    supported) that are contained within the same folder as specified in path
    Output: A list containing the 10X unique molecular identified (UMI) sequences from the R1 FASTQ file.
    Note that reading FASTQ files other than the R1 is not supported
    For parsing individual R1 FASTQ files specified by the absolute file path, use extract_from_single"""

    fastq_path = glob.glob(path+'*R1*'+'*.fastq.gz')
    umi_append = []
    for file in fastq_path:
        print("Reading UMI sequences from: {}".format(file))
        with gzip.open(file, 'rt') as handle:
            # append every fourth line of the fastq file starting with line 2, corresponding to all R1 sequences
            for line in islice(handle, 1, None, 4):
                # each appended line contains the last 10 characters of the 26 bp read containing the 10x UMI
                umi_append.append(line[16:26])
    return umi_append
