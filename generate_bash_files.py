import sys


def create_chromosomes_dict(vcf_file):
    chromosomes_dict = {}
    chrom = "NC_048323.1"
    chromosomes_dict[chrom] = [4135578-100]

    with open(vcf_file) as vcf_object:
        while True:
            line = vcf_object.readline()
            if not line:
                break
            line_items = line.split()
            if line_items[0].startswith("NC"):
                    new_chrom = line_items[0]
                    if new_chrom != chrom: # new chrom
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
        file = open(f'Females_{chrom}.sh', "a")
        bash = open(bash_template_file, "r")
        while True:
            line = bash.readline()
            if not line:
                break
            if line.startswith("\n"):
                file.write(line)
            else:
                line_items = line.split()
                if line.startswith("OUTPUT="):
                    line = f'OUTPUT=/sise/vaksler-group/IsanaRNA/FISH_DATA/MappingToAcipenserRuthenusGenome/Freebayes/Ploidy4/Regions/Females_{chrom}.vcf'
                    file.write(line + "\n")
                elif len(line_items) == 1:
                    file.write(line)
                elif line_items[1].startswith("--job-name"):
                    line = f'#SBATCH --job-name {chrom}			### name of the job'
                    file.write(line+"\n")
                elif line_items[1].startswith("--output="):
                    line = f'#SBATCH --output={chrom}.%J.out'
                    file.write(line + "\n")
                elif line_items[1].startswith("--error"):
                    line = f'#SBATCH --error={chrom}.%J.err'
                    file.write(line + "\n")
                elif line_items[0].startswith("freebayes"):
                    line = f'freebayes -f $REF --region {chrom}:{start}-{end} --ploidy 4 $bams > $OUTPUT'
                    file.write(line + "\n")
                else:
                    file.write(line)
        file.close()


if __name__ == '__main__':

    vcf_file = 'Males_equal_to_ref_p4_unfiltered.vcf'
    bash_template_file = 'bash_template.sh'

    # bash_template = template(bash_template_file)
    chromosomes_dict = create_chromosomes_dict(vcf_file)
    print(chromosomes_dict)
    create_bash_files(chromosomes_dict, bash_template_file)

