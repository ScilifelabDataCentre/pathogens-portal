---
title: Data management
menu:
    main:
        identifier: data_management
        parent: support_services
        weight: 20
---

[SciLifeLab](https://www.scilifelab.se) and [NBIS](http://www.nbis.se/) can support you with Data Management Planning early on in the project to make data sharing more efficient, both through [personal consultations](https://nbis.se/support/supportform/index.php?form=consultation) and by providing a [customised tool](https://dsw.scilifelab.se/) to create Data Management Plans.
We can also assist you in identifying relevant repositories and common international standards for describing and publishing your data, as well as guide you through the submission process.

## Depositing data in a public repository

By depositing data in a public repository, you accept that the data will be published and may be used and redistributed according to specific terms set by yourself or the repository in question. Data deposition is considered important and you may get credit and acknowledgement for sharing data. A publication often results in getting a unique identifier for your dataset, which is often required for a journal to accept a manuscript for publication. Data sharing is often required by funders.

If required, data can often be published with a set moratorium, which means that data will not go public until a date that you set.

_Note that data from human individuals might need special considerations when it comes to publishing._

## Storing the data at your university or SNIC

In Sweden, raw measurement data that is generated in a project belongs to the university, while the results are owned by the researcher - the so called teacher's exception. Unless the data needs protection because of contractual obligations or personal privacy, for example in sensitive personal data such as biomedical measurements of humans, data is considered public.

The university has the legal responsibility to archive the data. Data publishing as supported here is important for the research process, but does not replace the legal responsibility of the university. As a researcher, you are recommended to ensure long term storage of your data in facilities provided by your university. While a project is active, compute and storage services can be provided by [Swedish National Infrastructure for Computing, SNIC](https://snic.se).

## Metadata
Metadata provides 'data about data' , and may include information on the methodology used to collect the data, analytical and procedural information, definitions of variables, units of measurement, any assumptions made, the format and file type of the data and software used to collect and/or process the data. Researchers are strongly encouraged to use community metadata standards where these are in place. It is highly recommended to, from the very beginning of the project, structure e.g. sample metadata in a way that enables sequence data submission  without having to reformat the metadata.

Here are our metadata guidelines for each specific data type:

* ##### Genomics & transcriptomics data

[MINSEQE](https://doi.org/10.25504/FAIRsharing.a55z32) (Minimal Information about a high throughput SEQuencing Experiment) is the preferred minimal metadata standard for transcriptomics data in general. For viral data, consider using the [ENA virus pathogen reporting standard checklist](https://www.ebi.ac.uk/ena/data/view/ERC000033).

***

* ##### Protein data

For proteomics, use the minimal information model specified in [MIAPE](https://doi.org/10.25504/FAIRsharing.8vv5fc), and fill them using the controlled vocabularies specified by the Proteomics Standards Initiative: [PSI CVs](https://doi.org/10.25504/FAIRsharing.sxh2dp).

***

[More information about metadata standards](https://scilifelab-data-guidelines.readthedocs.io/en/latest/docs/covid-19/index.html#guidelines-about-repositories-data-formats-and-metadata-standards)
