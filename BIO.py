import sys
from Bio import SeqIO
import pandas as pd
from Bio.SeqFeature import SeqFeature, FeatureLocation


class TargetFeatures:

    def __init__(self, table_file, male_ref_genome, output_file_name):
        self.features_table = df_from_features_table(table_file)
        self.genome_file = male_ref_genome
        self.output = output_file_name

    def extract_target(self):
        """Iterate the genome records
        for each record, grab a mRNA feature from the features table data frame,
        create a feature object and write it to an output fasta file. """

        out = open(self.output, "a")
        genome_file = open(self.genome_file)
        genome_sequence_iterator = SeqIO.parse(genome_file, 'fasta')
        feature_counter = 0
        for curr_record in genome_sequence_iterator:
            print('CURRENT RECORD: {}'.format(curr_record.id))
            print('feature counter: ', feature_counter)
            # select only the rows for the current record
            # (select only rows for the current record) AND (select only mRNAs)
            ft = self.features_table
            subset = ft.loc[(ft.genomic_accession == curr_record.id) & (ft['# feature'] == 'mRNA'), :]
            feature_counter = 0
            for row in subset.itertuples():  # itertuples is MUCH faster then iterrows, but doesn't handle all possible column names (pandas named tuple object)
                feature_counter = feature_counter + 1
                chr = row.genomic_accession
                start = row.start
                stop = row.end
                strand = row.strand
                product_accession = row.product_accession
                related_accession = row.related_accession
                name = row.name

                assert strand == '+' or strand == '-', "strand value incorrect {}".format(strand)
                strand = 1 if strand == '+' else -1
                target_feature = SeqFeature(FeatureLocation(start, stop, strand=strand))
                feature = target_feature.location.extract(curr_record.seq)

                line = '>{}|{}|{}|{}|{}|{}|{}|{}\n{}\n'.format(curr_record.id, start, stop, strand, product_accession,
                                                               related_accession, name, stop - start + 1, feature)
                out.write(line)

        genome_file.close()


def df_from_features_table(table_file):
    features_df = pd.read_csv(table_file, sep="\t")
    return features_df


if __name__ == '__main__':

    genome = sys.argv[-3]
    features_data_file = sys.argv[-2]
    out = sys.argv[-1]
    print('genome: ', genome)
    print('feature table: ', features_data_file)
    print('out: ', out+'\n')

    target_features = TargetFeatures(features_data_file, genome, out)
    print('AFTER CREATE target_features')
    target_features.extract_target()
    print('AFTER extract target')