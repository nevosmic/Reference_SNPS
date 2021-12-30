#!/bin/bash

################################################################################################
### sbatch configuration parameters must start with #SBATCH and must precede any other commands.
### To ignore, just add another # - like so: ##SBATCH
################################################################################################

#SBATCH --partition main			### specify partition name where to run a job. short: 7 days limit; gtx1080: 7 days; debug: 2 hours limit and 1 job at a time
##SBATCH --time 7-00:00:00			### limit the time of job running. Make sure it is not greater than the partition time limit!! Format: D-H:MM:SS
#SBATCH --job-name NC_048323.1			### name of the job
#SBATCH --output job-%J.out			### output log for running job - %J for job number
#SBATCH --mail-user=nevosmic@post.bgu.ac.il	### user's email for sending job status messages
#SBATCH --mail-type=ALL			### conditions for sending the email. ALL,BEGIN,END,FAIL, REQUEU, NONE
##SBATCH --mem=50g				### ammount of RAM memory
#SBATCH --cpus-per-task=16			### number of CPU cores
##SBATCH --gres=gpu:1				### number of GPUs, ask for more than 1 only if you must parallelize your code for multi GPU
#SBATCH --output=NC_048323.1.%J.out
#SBATCH --error=NC_048323.1.%J.err


### Print some data to output file ###
echo `date`
echo -e "\nSLURM_JOBID:\t\t" $SLURM_JOBID
echo -e "SLURM_JOB_NODELIST:\t" $SLURM_JOB_NODELIST "\n\n"

### Start your code below ####
module load anaconda              ### load anaconda module
source activate mic            ### activating environment, environment must be configured before running the job

REF=/sise/vaksler-group/IsanaRNA/FISH_DATA/MappingToAcipenserRuthenusGenome/Heidi_Lischer_pipeline/AcipenserRuthenusIndex/GCF_010645085.1_ASM1064508v1_genomic.fna
OUTPUT=/sise/vaksler-group/IsanaRNA/FISH_DATA/MappingToAcipenserRuthenusGenome/Freebayes/Ploidy4/Regions/Females_NC_048323.1.vcf
bams=/sise/vaksler-group/IsanaRNA/FISH_DATA/MappingToAcipenserRuthenusGenome/Freebayes/Ploidy4/merge/merge_females.bam

freebayes -f $REF --region NC_048323.1:4135478-120726758 --ploidy 4 $bams > $OUTPUT
