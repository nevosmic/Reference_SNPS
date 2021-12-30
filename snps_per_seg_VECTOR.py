import sys


def _create_file_list(filename):
    file_list = ''

    for i in range(23,83):
        file_list = file_list+'/sise/vaksler-group/IsanaRNA/FISH_DATA/MappingToAcipenserRuthenusGenome/Freebayes' \
                              '/Ploidy4-old_way/Analysis/NumOfSnpsPerSegment/5_5/NC_0483{}.1_P4_10000.txt,'.format(i)
    _file = open(filename, 'w')
    _file.write(file_list)


def create_file_list(filename):
    file_list = []
    _file = open(filename, 'r')
    line = _file.readline()
    line = line.split(",")
    for x in line:
        file_list.append(x)
    return file_list


def collect_snps(filename, snps_vector):
    _file = open(filename, 'r')

    line = _file.readline()
    line = line[17:-2]  # remove chars {[chr: ]}
    line = line.split(",")
    for x in line:

        snps_vector.append(int(x))


if __name__ == '__main__':
    # file1 = 'NC_048326.1_P4_10000.txt'
    # file2 = 'NC_048327.1_P4_10000.txt'
    # output_file = 'snps_vector.txt'

    file_of_list = sys.argv[-2]
    output_file = sys.argv[-1]
    file_list = create_file_list(file_of_list)
    print(file_list)
    snps_vector = []
    for filename in file_list:
        collect_snps(filename, snps_vector)

    out = open(output_file, 'w')
    out.write(str(snps_vector))

