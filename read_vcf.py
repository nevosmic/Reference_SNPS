

if __name__ == '__main__':
    line = "NC_048323.1     321     .       T       G       110.475 .       DPB=5;EPPR=9.52472;GTI=0;MQMR=32.6667;NS=1;NUMALT=1;ODDS=2.11219;PAIREDR=1;PQR=0;PRO=0;QR=74;RO=3;RPPR=9.52472;SRF=0;SRP=9.52472;SRR=3;DP=29;AB=0;ABP=0;AF=1;AO=5;CIGAR=1X;DPRA=0;EPP=3.44459;LEN=1;MEANALT=1;MQM=23.4;PAIRED=1;PAO=0;PQA=0;QA=184;RPL=3;RPP=3.44459;RPR=2;RUN=1;SAF=2;SAP=3.44459;SAR=3;TYPE=snp;AN=44;AC=33     GT:DP:AD:RO:QR:AO:QA    ./././././././.:.:.:.:.:.:.     0/0/0/0/0/1/1/1:5:3,2:3:74:2:65 0/1/1/1:3:1,2:1:37:2:74 1/1/1/1/1/1/1/1:5:0,5:0:0:5:185       ./././././././.:.:.:.:.:.:.     0/0/0/1/1/1/1/1:6:2,4:2:71:4:147        ./././././././.:.:.:.:.:.:.   0/0/1/1/1/1/1/1:5:1,4:1:37:4:149        1/1/1/1/1/1/1/1:5:0,5:0:0:5:184 ./././././././.:.:.:.:.:.:."
    line_1,line_2 = line.split('AF=',1)
    line_2_split = line_2.split(';',1)
    line_2 = line_2.replace(line_2_split[0],"AF=12")
    line_new = line_1+line_2
