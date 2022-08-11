---
title: "SARS-CoV-2 bioinformatics pipeline – GMS Arctic"
category: "plp1"
resource_info:
    name: "SARS-CoV-2 bioinformatics pipeline – GMS Arctic"
    funded_project_title: "Joint contributions from 3 PLP projects: Rapid establishment of comprehensive laboratory pandemic preparedness – RAPID-SEQ (PLP1 capability), Genomic Pandemic Preparedness Portfolio (G3P) (PLP1 capability), and Next generation clinical virology (PLP TDP project)."
    pi: Jan Albert (RAPID-SEQ), Valtteri Wirta (G3P), Tobias Allander (Next generation clinical virology)
    host_organisation: This is a jointly developed resource with multiple contributers; Karolinska Institutet, Karolinska University Hospital, Region Östergötland, SciLifeLab, Genomics Medicine Sweden.
    use: "The pipeline is publicly available for analyzing SARS-CoV-2 samples generated on various sequencing platforms. This includes short read data, such as Illumina sequence data, as well as long read data from Nanopore sequencing."
    access: "The code for the pipeline is publicly available and can be utilized free of charge."
    data_etc: "All code related GMS-Arctic is available on [GitHub](https://github.com/genomic-medicine-sweden/gms-artic)."
    publications_etc: "Instructions about how to use the GMS-Arctic, how to set it up, and requirements are available on [GitHub](https://github.com/genomic-medicine-sweden/gms-artic/blob/master/README.md)."
    webpage: "[https://github.com/genomic-medicine-sweden/gms-artic](https://github.com/genomic-medicine-sweden/gms-artic)"
    contact: "Sofia Stamouli<br>Email: [sofia.stamouli@scilifelab.se](mailto:sofia.stamouli@scilifelab.se)"
---

A pipeline for taxonomic profiling of shotgun metagenomic data. It is currently in development and does not yet have any stable releases.

The pipeline supports metagenomic data generated both from Illumina and Nanopore sequencing technology. It performs in-parallel taxonomic profiling with multiple taxonomic classifiers against multiple databases and produces standardised output tables. In addition, it performs quality control and optional read pre-processing (adapter trimming, low-complexity filtering and host read removal).

The pipeline is written in Nextflow DSL-2 workflow manager and it uses Docker/Singularity containers.

For more information on the [Pandemic Laboratory Preparedness resources](/resources/) associated with this subproject, see [Genomic Pandemic Preparedness Portfolio (G3P)](/resources/g3p/) and [Rapid establishment of comprehensive laboratory pandemic preparedness – RAPID-SEQ](/resources/rapid-seq/). Please also refer to other associated subprojects; [taxprofiler](/resources-subprojects/taxprofiler/) and [SC2 Reporter](/resources-subprojects/sc2reporter/).
