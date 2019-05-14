# __umiread__

umiread is a lightweight utility that allows for seamless parsing of R1 FASTQ files generated from 10x single cell 3' gene expression assays. The functions contained within this package show the user very important baseline quality control metrics about the unique molecular identifiers (UMIs) contained within one or more R1 FASTQs, including total number of unique and non-unique sequences, nucleotide distribution, and basecalling errors. umiread can be used for preliminary parsing of 10x single cell FASTQ files prior to downstream analysis. 
For more information on 10x single cell 3' gene expression assays, visit https://support.10xgenomics.com/single-cell-gene-expression/sequencing/doc/specifications-sequencing-requirements-for-single-cell-3


__Installation & Dependencies__

umiread requires the following packages: 

    - pandas
    
    - numpy
    
    - matplotlib
    

In PyCharm or another Python IDE (Python 3 or greater), installation can be completed as follows: 

    pip install umiread

__Reading & Extracting from FASTQ files__

umiread has the ability to parse one or more R1 FASTQ files from a 10x 3' single cell assay (any version). 

For parsing a single FASTQ file: 

    from umiread import extract_from_single
    umi_data = extract_from_single("path/to/FASTQ file/~.fastq.gz")

For parsing multiple FASTQ files contained within the same folder (i.e. multiple FASTQs corresponding to the same sample): 

    from umiread import extract_from_folder
    umi_data = extract_from_folder("path/to/FASTQ folder/")

The parser will collect the 10bp UMI at the beginning of each R1 sequence contained within the targeted FATSQ files. Assigning the parsed sequences to an object such as umi_data will allow for the user to generate quality control metrics. 

__Collecting Quality Control Metrics & Sequencing Errors__

Having information about the total number of UMI sequences, unique UMI sequences, and nucleotide distribution can be useful for tracking the quality of wet lab workflows and overall data quality before downstream applications and further data analysis. umiread possesses a handful of functions that can print these statistics to console. 

For basic statistics such as total number of UMIs, unique UMIs, percentage of UMIs that are unique, and the number of UMIs with a sequencing error, use the following command: 

    from umiread import UMIStats
    UMIStats(umi_data).collect_qc_statistics()

This function will output a simple csv with all aforementioned QC metrics. 

For nucleotide distributions (i.e. the number of A, C, T, G in all unique UMIS): 

    UMIStats(umi_data).base_distribution()

For a graph of the positional distribution of sequencing errors in the UMI (denoted by "N" in the FASTQ file): 

    UMIStats(umi_data).show_seq_errors()
    
