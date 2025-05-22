---
title: "SARS-CoV-2 bioinformatics pipeline – GMS Artic"
category: "subproject"
aliases:
  - /resources-subprojects/gms-artic/
  - /resources-subprojects/gms-arctic/
resource_info:
  name: "SARS-CoV-2 bioinformatics pipeline – GMS Artic"
  funded_project_title: "Joint contributions from 3 PLP projects: Rapid establishment of comprehensive laboratory pandemic preparedness – RAPID-SEQ (PLP1 capability), Genomic Pandemic Preparedness Portfolio (G3P) (PLP1 capability), and Next generation clinical virology (PLP TDP project)."
  pi: Jan Albert (RAPID-SEQ), Valtteri Wirta (G3P), Tobias Allander (Next generation clinical virology)
  host_organisation: This is a jointly developed resource with multiple contributers; Karolinska Institutet, Karolinska University Hospital, Region Östergötland, SciLifeLab, Genomics Medicine Sweden.
  use: "The pipeline is publicly available for analysing SARS-CoV-2 samples generated on various sequencing platforms. This includes short read data, such as Illumina sequence data, as well as long read data from Nanopore sequencing."
  access: "The code for the pipeline is publicly available and can be utilised free of charge."
  data_etc: "All code related GMS-Artic is available on [GitHub](https://github.com/genomic-medicine-sweden/gms-artic)."
  publications_etc: "Instructions about how to use the GMS-Artic, how to set it up, and requirements are available on [GitHub](https://github.com/genomic-medicine-sweden/gms-artic/blob/master/README.md)."
  webpage: "[https://github.com/genomic-medicine-sweden/gms-artic](https://github.com/genomic-medicine-sweden/gms-artic)"
  contact: "Sofia Stamouli<br>Bioinformatician<br>Email: [sofia.stamouli@scilifelab.se](mailto:sofia.stamouli@scilifelab.se)"
---

A pipeline for bioinformatical analysis of SARS-CoV-2 data was developed within Genomics Medicine Sweden during the spring of 2021. The pipeline extends on the analysis developed by the international collaboration ArticNetwork and the COG-UK consortium. It is currently in clinical use across Sweden and is continually updated with the latest SARS-CoV-2 variants.

The pipeline performs typing of SARS-CoV-2 data using both the Pangolin and Nextstrain classification systems. In addition, it also runs quality control, variant calling and supplies a genome consensus sequence for each sample. The pipeline has two different modes depending on the sequencing technology used, one for short read data such as Illumina sequencing data, and the other for long read data generated from Nanopore sequencing.

The pipeline is written in Nextflow workflow manager and is already set up to run with conda environments, docker or singularity containers. Support has also been set up for execution with various job schedulers such as slurm, lsf, gls and sge, and is easily adapted for other systems through the Nextflow set up.

For more information on the [Pandemic Laboratory Preparedness resources](/resources/) associated with this subproject, see [Genomic Pandemic Preparedness Portfolio (G3P)](/resources/g3p/), [Rapid establishment of comprehensive laboratory pandemic preparedness – RAPID-SEQ](/resources/rapid-seq/), and [Next generation clinical virology](/resources/ng_clinical_virology/). Please also refer to other associated subprojects; [taxprofiler](/resources/taxprofiler/) and [SC2 Reporter](/resources/sc2reporter/).
