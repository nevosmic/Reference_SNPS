#!/bin/bash

################################################################################################
### sbatch configuration parameters must start with #SBATCH and must precede any other commands.
### To ignore, just add another # - like so: ##SBATCH
################################################################################################

#SBATCH --partition main			### specify partition name where to run a job. short: 7 days limit; gtx1080: 7 days; debug: 2 hours limit and 1 job at a time
##SBATCH --time 7-00:00:00			### limit the time of job running. Make sure it is not greater than the partition time limit!! Format: D-H:MM:SS
#SBATCH --job-name bam2bcf_CACTIG010000012.1
#SBATCH --output=bam2bcf_CACTIG010000012.1.%J.out
#SBATCH --mail-user=nevosmic@post.bgu.ac.il	### user's email for sending job status messages
#SBATCH --mail-type=ALL			### conditions for sending the email. ALL,BEGIN,END,FAIL, REQUEU, NONE
#SBATCH --mem=500g				### ammount of RAM memory
#SBATCH --cpus-per-task=16			### number of CPU cores
##SBATCH --gres=gpu:1				### number of GPUs, ask for more than 1 only if you must parallelize your code for multi GPU
#SBATCH --output=bam2bcf_CACTIG010000012.1.%J.out
#SBATCH --error=bam2bcf_CACTIG010000012.1.%J.err


### Print some data to output file ###
echo `date`
echo -e "\nSLURM_JOBID:\t\t" $SLURM_JOBID
echo -e "SLURM_JOB_NODELIST:\t" $SLURM_JOB_NODELIST "\n\n"

### Start your code below ####
module load anaconda              ### load anaconda module
source activate ITtest            ### activating environment, environment must be configured before running the job

REF=/sise/vaksler-group/IsanaRNA/FISH_DATA/AcipenserRuthenusFemaleGenome/FemaleAssembly/GCA_902713425.1_fAciRut3.1_maternal_haplotype_genomic.fna
bams=/sise/vaksler-group/IsanaRNA/FISH_DATA/AcipenserRuthenusFemaleGenome/bcftools_P2/merged_bams/merge_males.bam
BCF=/sise/vaksler-group/IsanaRNA/FISH_DATA/AcipenserRuthenusFemaleGenome/bcftools_P2/Regions/Males_CACTIG010000012.1.bcf


bcftools mpileup --regions CACTIG010000012.1:9459214-29288882 --output-type b --output $BCF -f $REF $bams
