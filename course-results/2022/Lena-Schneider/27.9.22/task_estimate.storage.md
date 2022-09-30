# Task: Estimate Storage Requirements for 1000 Genomes


### - WES and WGS ☣️
1000 whole genomes are 1/1400 petabyte which is abour 715 Gigabyte



### - Different formats: ℹ️
##### SAM: 
Sequence alignment map. Consists of a header (starts with @) and an alignment section.
<img width="654" alt="Screen Shot 2022-09-28 at 14 01 02" src="https://user-images.githubusercontent.com/113988381/192773682-8206eb80-74bb-4014-95bc-14c78fb301f9.png">

##### BAM: 
A single 30x BAM file is 100 GB. Binary version of SAM (so compressed but contain same information). 

##### VCF 
Variant call format: Databank to store information of genomes. It only prints the variations of a base of interest.
This format is only useful if there are not too many samples. Otherwise, too many variations will be detected. 
<img width="655" alt="Screen Shot 2022-09-28 at 14 06 30" src="https://user-images.githubusercontent.com/113988381/192774643-3c791ebb-c6a8-49b0-9d38-05c8d33c005b.png">


##### FASTA
Starts with a header with information about the sample. Then there is the sequence of nucleotides or amino acids.

<img width="667" alt="Screen Shot 2022-09-28 at 14 07 52" src="https://user-images.githubusercontent.com/113988381/192774850-37054d71-e3cc-4b1e-a143-6f1af5055536.png">

##### FASTQ: 
For a whole genome



### - Associated costs 💸
To store 1000 genomes in BAM costs about 50000 CHF, but only about half of this is for the raw storage.
Other cost factors are for example duplication and facilities.





