---
title: Share data
toc: true
menu:
    top_actions:
        weight: 40
        pre: <i class="bi bi-server mr-2"></i>
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

The [European Bioinformatics Institute (EBI)](https://www.ebi.ac.uk/) hosts many different international data repositories which should be used if appropriate. For data types where no suitable international repository is available, your data can be deposited to the [SciLifeLab Data Repository](https://scilifelab.se/data/repository) which is run by the SciLifeLab Data Centre (submissions accepted from all life science researchers in Sweden).

## Share data with controlled access

For human data which needs to be stored in a safe environment with controlled access, SciLifeLab [can help with publishing and access control](https://www.scilifelab.se/data/humandata/) (available to all life science researchers at a Swedish academic institution).

## Overview of recommended repositories per data type

Below are our data submission guidelines for each specific data type. You can also find similar recommendations per data type on [The European COVID-19 Data Portal data submission information](https://www.covid19dataportal.org/submit-data).

* ##### Genomics & transcriptomics data

    We suggest that raw virus sequence data as well as assembled and annotated genomes are submitted to [ENA](https://www.ebi.ac.uk/ena). In order to provide further support to users, the Swedish COVID-19 & Pandemic Preparedness Data Portal team has also produced a [detailed tutorial on submission to ENA](/support_services/tutorial_ena/tutorial_ena_intro). ENA also provide their own documentation to help with submission at [SARS-CoV-2 submission](https://ena-browser-docs.readthedocs.io/en/latest/help_and_guides/sars-cov-2-submissions.html).

    Before submission of raw sequence data (e.g. shotgun sequencing) it is necessary to remove contaminating human reads. Host (human) sequence data requires restricted access, and NBIS is building a local federated version of the European Genome-phenome Archive (EGA) in Sweden (EGA-SE), allowing for the publication of sensitive personal data within a legal framework. Until local EGA is available, the dataset should remain in the secure analysis environment (e.g., at Bianca on [UPPMAX](https://www.uppmax.uu.se/)). SciLifeLab [can help with publishing and access control](https://www.scilifelab.se/data/humandata/). In any case, we recommend to make a metadata-only record in the [SciLifeLab Data Repository](/support_services/general_data_repository/) with contact details on how to get access, and for which a DOI (i.e., a persistent identifier) can be issued. The DOI can then be used in the article to refer to the dataset. Once the Swedish EGA is operational, and the dataset is deposited there, the access information can be changed to point to the EGA ID. See [DOI: 10.17044/scilifelab.12292778](https://doi.org/10.17044/scilifelab.12292778.v1) for an example.

    * [The European Nucleotide Archive (ENA)](https://www.ebi.ac.uk/ena)
    * [ENA SARS-CoV-2 submission tutorial](https://covid19dataportal.se/support_services/tutorial_ena/tutorial_ena_intro/)
    * [SciLifeLab Data Repository for metadata records of sequence data with restricted access](https://scilifelab.se/data/repository)

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

    Other types of proteomics data should also be made available, we recommend [SciLifeLab Data Repository](/support_services/general_data_repository/). In order to make the data useful and ready for analyses and integration, a detailed description of the data format and how the variables are organized should be provided. Each protein variable should come with a unique identifier such as UniProt ID or ENGS ID (and stating the versions used to link the data).

    Metadata: For proteomics, use the minimal information model specified in [MIAPE](https://doi.org/10.25504/FAIRsharing.8vv5fc), and fill them using the controlled vocabularies specified by the Proteomics Standards Initiative: [PSI CVs](https://doi.org/10.25504/FAIRsharing.sxh2dp).

    * [PRIDE repository](https://www.ebi.ac.uk/pride/) and [PX Submission Tool](https://www.ebi.ac.uk/pride/markdownpage/pridesubmissiontool)
    * [SciLifeLab Data Repository for other types of proteomics data](https://scilifelab.se/data/repository)

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

    In cases where data cannot be deposited into a public repository due to privacy restrictions we suggest creating a metadata-only record on the [SciLifeLab Data Repository](https://scilifelab.se/data/repository) ((submissions accepted from all life science researchers in Sweden)) with information about what data is available upon request and how such a request can be made. The repository is managed locally by the SciLifeLab Data Centre, and it allows to obtain a DOI which can then be referred to in the publication.

    * [SciLifeLab Data Repository](https://scilifelab.se/data/repository)

    ***

* ##### General data repositories

    Most life science data types can be published as raw or processed data in repositories at the [EMBL-EBI](https://www.ebi.ac.uk). When no archive is suitable, use a general purpose repository such as the [SciLifeLab Data Repository](https://scilifelab.se/data/repository) (submissions accepted from all life science researchers in Sweden), [Figshare](https://figshare.com) or [Zenodo](https://zenodo.org). Besides scientific data, here you can publish documents, presentations, figures, protocols, or other information that you want to make public at any stage in the research process. A publication here is permanent, and provides a Digital Object Identifier, DOI.

    ***

## Data sharing support

All researchers affiliated with a university or research institute in Sweden working on research topics relevant to pandemic preparedness can receive free individual consultations and hands-on help within reasonable bounds from the *Swedish COVID-19 & Pandemic Preparedness Portal* team. Simply send an email to datacentre@scilifelab.se. Your question will be assigned to a data steward with relevant expertise who can either help you directly or point you to the correct tool or service.

You are welcome to send both general questions about best approaches to research data management, data management plans (DMPs), reproducibility, FAIR, and open science as well as specific questions about your research projects such as which repository to choose to deposit data, what the suitable metadata standards would be, which file formats to use, etc. In some cases the data stewards can act as brokers and submit data to repositories on your behalf.
