# __umiread__

umiread is a lightweight utility that allows for seamless parsing of R1 FASTQ files generated from 10x single cell gene expression assays. The functions contained within this package show the user very importnat baseline quality control metrics about the unique molecular identifiers (UMIs) contained within one or more R1 FASTQs, including total number of unique and non-unique sequences,nucleotide distribution, and basecalling errors. umiread can be used for preliminary poarsing of 10x single cell FASTQ files prior to downstream analysis. 

__Installation & Dependencies__

umiread requires the following packages: 

    - pandas
    
    - numpy
    
    - matplotlib
    

In PyCharm or another Python IDE (Python 3 or greater), installation can be completed as follows: 

    pip install umiread
    
