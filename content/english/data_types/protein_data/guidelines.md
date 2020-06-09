---
title: Guidelines for protein data
menu:
    main:
        name: Guidelines for data producers
        identifier: protein_data_guidelines
        parent: protein_data
        weight: 20
---

## Guidelines for COVID-19 data
Make your COVID-19 research data useful and accessible for the rest of the research community by publishing in a public repository together with descriptive metadata.

[NBIS](http://www.nbis.se/) can support you with Data Management Planning early on in the projects to make data sharing more efficient, both through [personal consultations](https://nbis.se/support/supportform/index.php?form=consultation) and by providing a [customised tool](https://dsw.scilifelab.se/) to create Data Management Plans. We can also assist you in identifying relevant repositories and common international standards for describing and publishing your data, as well as guide you through the submission process.

### Repositories
For a curated list of relevant proteomics repositories see [FAIRsharing](https://fairsharing.org/) using the query ’[proteomics](https://fairsharing.org/search/?q=proteomics&content=biodbcore&name=&taxonomies=&organisations=&shortname=&description=&supportlinks=&licenses=&countries=&maintainers=&expanded_onto_domains=&expanded_onto_disciplines=&user_defined_tags=&record_id=&miriam_id=&search_state=hidden)’.

We recommend to use the [PRIDE](https://www.ebi.ac.uk/pride/) repository provided by the [ProteomeXchange](http://www.proteomexchange.org/) Consortium. The repository admits protein and peptide identification/quantification data with the accompanying mass spectra evidence and any other related data types. Submission is done using the [PX Submission Tool](https://www.ebi.ac.uk/pride/markdownpage/pridesubmissiontool)

Other types of proteomics data should also be made available, we recommend [SciLifeLab Data Repository](https://scilifelab.figshare.com/). In order to make the data useful and ready for analyses and integration, a detailed description of the data format and how the variables are organized should be provided. Each protein variable should come with a unique identifier such as UniProt ID or ENGS ID (and stating the versions used to link the data).

### Metadata
Metadata provides 'data about data' , and may include information on the methodology used to collect the data, analytical and procedural information, definitions of variables, units of measurement, any assumptions made, the format and file type of the data and software used to collect and/or process the data. Researchers are strongly encouraged to use community metadata standards where these are in place.

For proteomics, use the minimal information model specified in [MIAPE](https://doi.org/10.25504/FAIRsharing.8vv5fc), and fill them using the controlled vocabularies specified by the Proteomics Standards Initiative: [PSI CVs](https://doi.org/10.25504/FAIRsharing.sxh2dp).

It is highly recommended to, already from the beginning of the project, structure e.g. sample metadata in a way that enables sequence data submission  without having to reformat the metadata.

* [More information about repositories, data formats and metadata standards](https://scilifelab-data-guidelines.readthedocs.io/en/latest/docs/covid-19/index.html#guidelines-about-repositories-data-formats-and-metadata-standards)
