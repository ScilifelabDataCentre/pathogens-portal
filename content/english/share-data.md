---
title: Share data
toc: true
menu:
    top_actions:
        weight: 40
        pre: <i class="bi bi-server me-2"></i>
aliases:
  - /data_types/genomics_transcriptomics/guidelines/
  - /data_types/compound_and_target_data/guidelines/
  - /data_types/imaging_data/guidelines/
  - /data_types/protein_data/guidelines/
  - /support_services/general_data_repository/
  - /submit/
  - /support_services/submit
---

## Share data in a public repository

Publish your COVID-19 & Pandemic Preparedness research data to make it available for the rest of the research community. The data should be deposited in a public repository together with descriptive metadata. For many biological datatypes, there are international databases that can be considered de facto standards.

The [European Bioinformatics Institute (EBI)](https://www.ebi.ac.uk/) hosts many different international data repositories which should be used if appropriate.

## Overview of recommended repositories per data type

Below are our data submission guidelines for each specific data type. You can also find similar recommendations per data type on [The European COVID-19 Data Portal data submission information](https://www.covid19dataportal.org/submit-data).

* ##### Genomics & transcriptomics data

    We suggest that raw virus sequence data as well as assembled and annotated genomes are submitted to [ENA](https://www.ebi.ac.uk/ena). In order to provide further support to users, the Swedish COVID-19 & Pandemic Preparedness Data Portal team has also produced a [detailed tutorial on submission to ENA](/support_services/tutorial_ena/tutorial_ena_intro). ENA also provide their own documentation to help with submission at [SARS-CoV-2 submission](https://ena-browser-docs.readthedocs.io/en/latest/help_and_guides/sars-cov-2-submissions.html).

    Before submission of raw sequence data (e.g. shotgun sequencing) it is necessary to remove contaminating human reads. Host (human) sequence data requires restricted access, and NBIS is building a local federated version of the European Genome-phenome Archive (EGA), allowing for the publication of sensitive personal data within a legal framework.

    * [The European Nucleotide Archive (ENA)](https://www.ebi.ac.uk/ena)
    * [ENA SARS-CoV-2 submission tutorial](https://covid19dataportal.se/support_services/tutorial_ena/tutorial_ena_intro/)

    <div class="container mb-4 ena_tutorial_banner">
      <a href="/support_services/tutorial_ena/tutorial_ena_intro/"><img height="30px"
          src="/img/ena_tutorial/ENA_logo_2021.png"></a> <a
        href="/support_services/tutorial_ena/tutorial_ena_intro/">Tutorial for SARS-CoV-2 genome data submission to
        ENA</a>
    </div>

    ***

* ##### Protein data

    For a curated list of relevant proteomics repositories see [FAIRsharing](https://fairsharing.org/) using the query ’[proteomics](https://fairsharing.org/search/?q=proteomics&content=biodbcore&name=&taxonomies=&organisations=&shortname=&description=&supportlinks=&licenses=&countries=&maintainers=&expanded_onto_domains=&expanded_onto_disciplines=&user_defined_tags=&record_id=&miriam_id=&search_state=hidden)’.

    We recommend to use the [PRIDE](https://www.ebi.ac.uk/pride/) repository provided by the [ProteomeXchange](http://www.proteomexchange.org/) Consortium. The repository admits protein and peptide identification/quantification data with the accompanying mass spectra evidence and any other related data types. Submission is done using the [PX Submission Tool](https://www.ebi.ac.uk/pride/markdownpage/pridesubmissiontool).

    Metadata: For proteomics, use the minimal information model specified in [MIAPE](https://doi.org/10.25504/FAIRsharing.8vv5fc), and fill them using the controlled vocabularies specified by the Proteomics Standards Initiative: [PSI CVs](https://doi.org/10.25504/FAIRsharing.sxh2dp).

    * [PRIDE repository](https://www.ebi.ac.uk/pride/) and [PX Submission Tool](https://www.ebi.ac.uk/pride/markdownpage/pridesubmissiontool)

    ***

* ##### Imaging data

    Depending on the type of image data you have, different public repositories are available, please see the table at [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/).

    * [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/)

    ***

* ##### Biochemistry

    We suggest that users submit data to [ChEMBL](https://www.ebi.ac.uk/chembl/) which is a manually curated database of bioactive molecules with drug-like properties run by EMBL-EBI. It brings together chemical, bioactivity and genomic data to aid the translation of genomic information into effective new drugs.

    * [ChEMBL](https://www.ebi.ac.uk/chembl/)

    ***

* ##### Health data

    ??

    ***

* ##### General data repositories

    Most life science data types can be published as raw or processed data in repositories at the [EMBL-EBI](https://www.ebi.ac.uk). When no archive is suitable, use a general purpose repository such as [Figshare](https://figshare.com) or [Zenodo](https://zenodo.org). Besides scientific data, here you can publish documents, presentations, figures, protocols, or other information that you want to make public at any stage in the research process. A publication here is permanent, and provides a Digital Object Identifier, DOI.

    ***
