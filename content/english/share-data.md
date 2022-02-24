---
title: Share data
toc: false
menu:
    top_actions:
        weight: 40
        pre: <i class="bi bi-server mr-2"></i>
    main:
        identifier: submit_data
        parent: support_services
        weight: 50
        pre: <i class="fas fa-paper-plane"></i>
aliases:
  - /data_types/genomics_transcriptomics/guidelines/
  - /data_types/compound_and_target_data/guidelines/
  - /data_types/imaging_data/guidelines/
  - /data_types/protein_data/guidelines/
  - /support_services/general_data_repository/
  - /submit/
---

Publish your COVID-19 research data to make it available for the rest of the research community. The data should be deposited in a public repository together with descriptive metadata. For many biological datatypes, there are international databases that can be considered _de facto_ standards.

## Submitting data

[SciLifeLab](https://www.scilifelab.se/) (datacentre@scilifelab.se) or [NBIS](https://nbis.se/) (support@nbis.se)
can provide personal consultations for where and how to share data in a public database. Do not hesitate to get in touch with us if you have any questions. Your research group does not have to be affiliated with any particular institution to get our help, we are available to help everyone affiliated with a university in Sweden.

The European Bioinformatics Institute (EBI) hosts many different international data repositories which should be used if appropriate. For further information, see their [COVID-19 Data Portal data submission page](https://www.covid19dataportal.org/submit-data). For data types where no suitable international repository is available, your data can be deposited to the [SciLifeLab Data Repository](https://scilifelab.se/data/repository) which is run by the SciLifeLab Data Centre. For human data which needs to be stored in a safe environment with controlled access, SciLifeLab [can help with publishing and access control](https://www.scilifelab.se/data/humandata/).

Below are our data submission guidelines for each specific data type. you can also find information in [The European COVID-19 Data Portal data submission information](https://www.covid19dataportal.org/submit-data).

* ##### Genomics & transcriptomics data

    We suggest that raw virus sequence data as well as assembled and annotated genomes are submitted to [ENA](https://www.ebi.ac.uk/ena). ENA have produced documentation to help with submission at [SARS-CoV-2 submission](https://ena-browser-docs.readthedocs.io/en/latest/help_and_guides/sars-cov-2-submissions.html). In order to provide further support to users, we have also produced a tutorial regarding submission, see [here](/support_services/tutorial_ena/tutorial_ena_intro).

    Before submission of raw sequence data (e.g. shotgun sequencing) it is necessary to remove contaminating human reads. Host (human) sequence data requires restricted access, and NBIS is building a local federated version of the European Genome-phenome Archive (EGA) in Sweden (EGA-SE), allowing for the publication of sensitive personal data within a legal framework. Until local EGA is available, the dataset should remain in the secure analysis environment (e.g., at Bianca on [Uppmax](https://www.uppmax.uu.se/)). SciLifeLab [can help with publishing and access control](https://www.scilifelab.se/data/humandata/). In any case, we recommend to make a metadata-only record in the [SciLifeLab Data Repository](/support_services/general_data_repository/) with contact details on how to get access, and for which a DOI (i.e., a persistent identifier) can be issued. The DOI can then be used in the article to refer to the dataset. Once the Swedish EGA is operational, and the dataset is deposited there, the access information can be changed to point to the EGA ID. See [DOI: 10.17044/NBIS/G000014](https://doi.org/10.17044/NBIS/G000014) for an example.

    * [The European Nucleotide Archive (ENA)](https://www.ebi.ac.uk/ena)
    * [ENA SARS-CoV-2 submission guildelines](https://ena-browser-docs.readthedocs.io/en/latest/help_and_guides/sars-cov-2-submissions.html)
    * [SciLifeLab Data Repository for metadata records of sequence data with restricted access](https://scilifelab.se/data/repository)

    ***

* ##### Protein data

    For a curated list of relevant proteomics repositories see [FAIRsharing](https://fairsharing.org/) using the query ’[proteomics](https://fairsharing.org/search/?q=proteomics&content=biodbcore&name=&taxonomies=&organisations=&shortname=&description=&supportlinks=&licenses=&countries=&maintainers=&expanded_onto_domains=&expanded_onto_disciplines=&user_defined_tags=&record_id=&miriam_id=&search_state=hidden)’.

    We recommend to use the [PRIDE](https://www.ebi.ac.uk/pride/) repository provided by the [ProteomeXchange](http://www.proteomexchange.org/) Consortium. The repository admits protein and peptide identification/quantification data with the accompanying mass spectra evidence and any other related data types. Submission is done using the [PX Submission Tool](https://www.ebi.ac.uk/pride/markdownpage/pridesubmissiontool).

    Other types of proteomics data should also be made available, we recommend [SciLifeLab Data Repository](/support_services/general_data_repository/). In order to make the data useful and ready for analyses and integration, a detailed description of the data format and how the variables are organized should be provided. Each protein variable should come with a unique identifier such as UniProt ID or ENGS ID (and stating the versions used to link the data).

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

    In cases where data cannot be deposited into a public repository due to privacy restrictions we suggest creating a metadata-only record on the [SciLifeLab Data Repository](https://scilifelab.se/data/repository) with information about what data is available upon request and how such a request can be made. The repository is managed locally by the SciLifeLab Data Centre, and it allows to obtain a DOI which can then be referred to in the publication.

    * [SciLifeLab Data Repository](https://scilifelab.se/data/repository)

    ***

### General data repositories

Most life science data types can be published as raw or processed data in repositories at the [EMBL-EBI](https://www.ebi.ac.uk) as described under [Data types](https://covid19dataportal.se/data_types/). When no archive is suitable, use a general purpose repository such as [Figshare](https://figshare.com) or [Zenodo](https://zenodo.org). This includes documents, presentations, figures, protocols, or other information that you want to make public at any stage in the research process. A publication here is permanent, and provides a Digital Object Identifier, DOI.

SciLifeLab supports COVID-19 related data to be published in the [SciLifeLab Data Repository](https://scilifelab.figshare.com).

If you have datasets related to COVID-19 research that are best suited for this type of repository, please contact the SciLifeLab Data Centre at [datacentre@scilifelab.se](mailto:datacentre@scilifelab.se) or visit our [repository support page](https://www.scilifelab.se/data/repository).

#### Published data at General Data Repositories

[Figshare COVID-19 open research data](https://covid19.figshare.com)

[Zenodo Coronavirus Disease Research Community](https://zenodo.org/communities/covid-19/)
