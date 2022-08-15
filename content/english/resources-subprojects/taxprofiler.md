---
title: "Highly parallelised multi-taxonomic profiling of shotgun metagenomic data (taxprofiler)"
category: "plp1"
resource_info:
    name: "Highly parallelised multi-taxonomic profiling of shotgun metagenomic data (taxprofiler)"
    funded_project_title: "Joint contributions from 3 PLP projects: Rapid establishment of comprehensive laboratory pandemic preparedness – RAPID-SEQ (PLP1 capability), Genomic Pandemic Preparedness Portfolio (G3P) (PLP1 capability), and Next generation clinical virology (PLP TDP project)."
    pi: Jan Albert (RAPID-SEQ), Valtteri Wirta (G3P), Tobias Allander (Next generation clinical virology)
    host_organisation: Taxprofiler is an international initiative with Swedish contributions from Karolinska Institutet, Karolinska University Hospital, SciLifeLab, Region Östergötland and Genomic Medicine Sweden
    use: "The development version of the pipeline is already publicly available for taxonomic classification of metagenomic data and it can be used for Pandemic Preparedness research as soon as the first stable release is available."
    access: "The nf-core/taxprofiler is open-source pipeline."
    data_etc: "All code related to the pipeline for taxprofiler is available on [GitHub](https://github.com/nf-core/taxprofiler)."
    publications_etc: "Instructions about how to use the pipeline are available on [nf-core](https://nf-co.re/taxprofiler/dev/usage)."
    webpage: "[https://nf-co.re/taxprofiler/dev](https://nf-co.re/taxprofiler/dev)"
    contact: "Sofia Stamouli<br>Bioinformatician<br>Email: [sofia.stamouli@scilifelab.se](mailto:sofia.stamouli@scilifelab.se)"
---

A pipeline for taxonomic profiling of shotgun metagenomic data. It is currently in development and does not yet have any stable releases.

The pipeline supports metagenomic data generated both from Illumina and Nanopore sequencing technology. It performs in-parallel taxonomic profiling with multiple taxonomic classifiers against multiple databases and produces standardised output tables. In addition, it performs quality control and optional read pre-processing (adapter trimming, low-complexity filtering and host read removal).

The pipeline is written in Nextflow DSL-2 workflow manager and it uses Docker/Singularity containers.

For more information on the [Pandemic Laboratory Preparedness resources](/resources/) associated with this subproject, see [Genomic Pandemic Preparedness Portfolio (G3P)](/resources/g3p/) and [Rapid establishment of comprehensive laboratory pandemic preparedness – RAPID-SEQ](/resources/rapid-seq/). Please also refer to other associated subprojects; [GMS Arctic](/resources-subprojects/gms-arctic/) and [SC2 Reporter](/resources-subprojects/sc2reporter/).
