#!/usr/bin/python

import numpy as np
import collections
import pandas as pd
import matplotlib.pyplot as plt
import csv


class UMIStats(object):

    def __init__(self, sequences):
        self.sequences = sequences

    def collect_qc_statistics(self):

        """Input required: The output generated from collect_umi (a list of all UMIs contained
        within one or more FASTQ files)
        Output: a series of baseline statistics indicating total number of UMIs retrieved, unique UMIs and any UMI
        sequences that contain sequencing errors (denoted by N in the read) that are written to csv
        """

        array = np.array(self.sequences)
        # report unique UMI sequences using result converted to array
        unique_umi = np.unique(array)
        filtered_umi = [x for x in unique_umi if "N" not in x]
        unfiltered_umi = [x for x in unique_umi if "N" in x]
        size = 100 * (len(unique_umi)/len(array))
        print("Total Number of UMI sequences: {}".format(len(self.sequences)))
        print("Total Number of unique UMIS: {}".format(len(unique_umi)))
        print("The percentage of UMIs that are unique is: {0:.2f}%".format(size))
        print("Total Number of unique UMIS with a sequencing error: {}".format(len(unfiltered_umi)))
        stat_dict = {"total_umi_sequences": len(self.sequences), "unique_umi_sequences": len(unique_umi),
                     "unique_umi_percentage": size, "unique_umi_count_with_seq_error": len(unfiltered_umi)}

        with open("umiread_qc_statistics.csv", "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(stat_dict.keys())
            writer.writerow(stat_dict.values())

        return array, unique_umi, filtered_umi, unfiltered_umi, size

    def base_distribution(self):

        """Input required: The output generated from collect_umi (a list of all UMIs contained
        within one or more FASTQ files)
        Output: The distribution of total counts for each nucleotide in the UMI read sequences
        """

        array = np.array(self.sequences)
        bases = ['A', 'T', 'C', 'G']
        # report unique UMI sequences using result converted to array
        unique_umi = np.unique(array)
        filtered_umi = [x for x in unique_umi if "N" not in x]
        # unfiltered umis will contain N as the position of a base-calling error from Illumina sequencing
        master_list_filter = ''.join(map(str, filtered_umi))
        base_dist = [collections.Counter(master_list_filter)[i] for i in bases]
        for i, x in zip(bases, base_dist):
                print("Number of {} bases in unique UMIs is: {}".format(i, x))
        return base_dist


# retrieve and plot positional information for each instance of N (undetermined base) in the UMI read (find index
# position
    def show_seq_errors(self):

        """
        Input required: The output generated from collect_umi (a list of all UMIs contained
        within one or more FASTQ files)
        Output: A distribution table of the index position of in all of the UMIs containing
        sequencing errors (N)
        """

        array = np.array(self.sequences)
        unique_umi = np.unique(array)
        non_filtered_umi = [x for x in unique_umi if "N" in x]
        master_list_frame = pd.DataFrame(non_filtered_umi, columns=["sequence"])
        master_list_frame["sequence"] = master_list_frame["sequence"].str.find('N')
        n_position_list = collections.Counter(master_list_frame["sequence"])
        # begin indexing for dictionary keys at 1 for bar-plot
        new_list = [x+1 for x in list(n_position_list.keys())]
        plt.bar(new_list, n_position_list.values(), color='g')
        plt.xlabel("N Position in UMI")
        plt.ylabel("Total N Count")
        plt.show()
