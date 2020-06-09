---
title: Guidelines for genomics & transcriptomics data
menu:
    main:
        name: Guidelines for data producers
        identifier: genomics_transcriptomics_guidelines
        parent: genomics_transcriptomics
        weight: 20
---

## Guidelines for COVID-19 data
Make your COVID-19 research data useful and accessible for the rest of the research community by publishing in a public repository together with descriptive metadata.

[NBIS](http://www.nbis.se/) can support you with Data Management Planning early on in the project to make data sharing more efficient, both through [personal consultations](https://nbis.se/support/supportform/index.php?form=consultation) and by providing a [customised tool](https://dsw.scilifelab.se/) to create Data Management Plans. NBIS can also assist you in identifying relevant repositories and common international standards for describing and publishing your data, as well as guide you through the submission process.

### Repositories
We suggest that raw virus sequence data as well as assembled and annotated genomes are submitted to [ENA](https://www.ebi.ac.uk/ena).
See documentation about submission at [SARS-CoV-2 submission](https://ena-browser-docs.readthedocs.io/en/latest/help_and_guides/sars-cov-2-submissions.html). Before submission of raw sequence data (e.g. shotgun sequencing) it is necessary to remove contaminating human reads.

Host (human) sequence data requires restricted access, and NBIS is building a local federated version of the European Genome-phenome Archive (EGA) in Sweden (EGA-SE), allowing for the publication of sensitive personal data within a legal framework. Until local EGA is available, the dataset should remain in the secure analysis environment (eg at Bianca on [Uppmax](https://www.uppmax.uu.se/)). We suggest to make a metadata-only record in the [SciLifeLab Data Repository](https://scilifelab.figshare.com/) with contact details on how to get access, and for which a DOI (ie a persistent identifier) can be issued. The DOI can then be used in the article to refer to the dataset. Once the Swedish EGA is operational, and the dataset is deposited there, the access information can be changed to point to the EGA ID. See [https://doi.org/10.17044/NBIS/G000014](https://doi.org/10.17044/NBIS/G000014), for an example.

### Metadata
Metadata provides 'data about data' , and may include information on the methodology used to collect the data, analytical and procedural information, definitions of variables, units of measurement, any assumptions made, the format and file type of the data and software used to collect and/or process the data. Researchers are strongly encouraged to use community metadata standards where these are in place.

[MINSEQE](https://doi.org/10.25504/FAIRsharing.a55z32) (Minimal Information about a high throughput SEQuencing Experiment) is the preferred minimal metadata standard for transcriptomics data in general. For viral data, consider using the [ENA virus pathogen reporting standard checklist](https://www.ebi.ac.uk/ena/data/view/ERC000033).

It is highly recommended to, from the very beginning of the project, structure e.g. sample metadata in a way that enables sequence data submission  without having to reformat the metadata.

* [More information about repositories, data formats and metadata standards](https://scilifelab-data-guidelines.readthedocs.io/en/latest/docs/covid-19/index.html#guidelines-about-repositories-data-formats-and-metadata-standards)
