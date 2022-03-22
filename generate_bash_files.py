import sys


def create_chromosomes_dict(vcf_file):
    chromosomes_dict = {}
    chrom = "NC_048323.1"
    # chromosomes_dict[chrom] = [4135578-100]
    chromosomes_dict[chrom] = [465637-100]

    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith("NC"):
                    new_chrom = line_items[0]
                    if new_chrom != chrom:  # new chrom
                        chromosomes_dict[chrom].append(int(pos)+100)  # last pos of prev
                        pos = line_items[1]
                        chromosomes_dict[new_chrom] = [int(pos)-100]  # first pos of new
                        chrom = new_chrom
                    pos = line_items[1]
    chromosomes_dict[new_chrom].append(int(pos)+100)
    return chromosomes_dict


def create_bash_files(chromosomes_dict, bash_template_file):
    for chrom,value in chromosomes_dict.items():
        start = value[0]
        end = value[1]
        #file = open(f'Females_{chrom}.sh', "a")
        #file = open(f'Males_{chrom}_bcf.sh', "a")
        file = open(f'Females_{chrom}_vcf.sh', "a")
        #file = open(f'Males_{chrom}_vcf.sh', "a")
        bash = open(bash_template_file, "r")
        while True:
            line = bash.readline()
            if not line:
                break
            if line.startswith("\n"):
                file.write(line)
            else:
                line_items = line.split()
                if line.startswith("#SBATCH --job-name"):
                    line = f'#SBATCH --job-name bcf2vcf_{chrom}'
                    file.write(line + "\n")
                elif line.startswith("#SBATCH --output"):
                    line = f'#SBATCH --output=bcf2vcf_fem_{chrom}.%J.out'
                    file.write(line + "\n")
                elif line.startswith("#SBATCH --error"):
                    line = f'#SBATCH --error=bcf2vcf_fem_{chrom}.%J.err'
                    file.write(line + "\n")
                elif line.startswith("bcf="):
                    line = f'bcf=/sise/vaksler-group/IsanaRNA/FISH_DATA/MappingToAcipenserRuthenusGenome/bcftools-p2/Regions/bcf/Females_{chrom}_bcf.bcf'
                    file.write(line + "\n")
                elif line.startswith("vcf="):
                    line = f'vcf=/sise/vaksler-group/IsanaRNA/FISH_DATA/MappingToAcipenserRuthenusGenome/bcftools-p2/Regions/vcf/Females_{chrom}.vcf'
                    file.write(line + "\n")
                elif len(line_items) == 1:
                    file.write(line)
                elif line_items[0].startswith("bcftools"):
                    line = f'bcftools call --ploidy 2 --output-type v --multiallelic-caller --variants-only --output $vcf $bcf'
                    file.write(line + "\n")
                else:
                    file.write(line)
        file.close()


def create_merge_list():
    # path = '/sise/vaksler-group/IsanaRNA/FISH_DATA/MappingToAcipenserRuthenusGenome/bcftools-p2/Regions/'
    path = '/sise/vaksler-group/IsanaRNA/FISH_DATA/MappingToAcipenserRuthenusGenome/bcftools-p2/Regions/vcf/'
    male = 'Males_NC_048323.1.vcf'
    female = 'Females_NC_048323.1.vcf'
    merge_file = open('merge_file_list.txt', "a")
    for i in range(23,81):
        merge_file.write(f'{path}Females_NC_0483{i}.1.vcf' + "\n")
        # merge_file.write(f'{path}Females_NC_0483{i}.1.vcf' + "\n")


def create_bash_file_test(bash_template_file, new_file):
    file = open(new_file, "a")
    bash = open(bash_template_file, "r")
    while True:
        line = bash.readline()
        if not line:
            break
        if line.startswith("\n"):
            file.write(line)
        else:
            line_items = line.split()
            if line.startswith("#SBATCH --job-name"):
                line = f'#SBATCH --job-name bcf2vcf_test'
                file.write(line + "\n")
            else:
                file.write(line)
    file.close()


if __name__ == '__main__':

    bash_template_file = sys.argv[-2]
    new_file = sys.argv[-1]

    create_bash_file_test(bash_template_file, new_file)

    #chromosomes_dict = create_chromosomes_dict(vcf_file)
    #print(chromosomes_dict)
    #create_bash_files(chromosomes_dict, bash_template_file)
    #create_merge_list()


