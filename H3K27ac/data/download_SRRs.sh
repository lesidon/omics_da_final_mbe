#!/bin/bash

while read SAMPLE; do
	echo "Downloading ${SAMPLE}"
	fastq-dump --gzip --split-files ${SAMPLE}
	mkdir ${SAMPLE}_dir	
	mv ${SAMPLE}_?.fastq.gz ${SAMPLE}_dir/
done < SRR_collection.txt
