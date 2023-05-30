---
title: METTL3 localization during SARS-CoV-2 infection could highlight new novel antiviral strategy
date: 2023-06-02
summary: Vaid and collaborators studied how the gene expression profile of  m6A mRNA is affected during, and post COVID-19 infection. All sequencing data, and the source code used for analysis are shared.
banner: /highlights/banners/mettl3_localization_small.png
banner_large: /highlights/banners/mettl3_localization.png
banner_caption: Graphical abstract (Image courtesy Vaid et al. 2023)
highlights_topics: [COVID-19, Infectious Diseases]
announcement: "This data highlight was also [published on the SciLifeLab Data Platform](https://data.scilifelab.se/highlights/mettl3_localization/), as the work described in this highlight constitutes data-driven life science. The Platform is a hub for data-driven life science in Sweden, containing multiple relevant resources, tools, and services. It includes information on multiple subjects, including infectious diseases, please check out the [Data Platform](https://data.scilifelab.se/) for more."
---

Over the latest years, the rapid development of COVID-19 treatment and vaccines have been crucial for the societal efforts to mitigate the spread of the SARS-COV-2 virus and control the COVID-19 pandemic. While the COVID-19 pandemic has now reached an endemic phase, lessons and knowledge related to SARS-COV-2 pathogenesis e.g. the basic mechanisms of how the virus infect, host-virus interactions, and host response, are still warranted. For example, the N6-Methyladenosine modification (m6A) is one of the most common cellular RNA modifications, and known to play a crucial role in the regulation of RNA metabolism during stress response.

However, little is known about how the expression is altered during COVID-19 infection and its effects. This knowledge may hold clues for novel or improved antiviral therapeutics for SARS-CoV-2. It may also increase our general knowledge about the mechanism of coronaviruses, and other potential pandemic threats.

In a recent publication in _Genome Res_, researchers from Sweden, in collaboration with researchers from South Korea, India and France (_First authors:_ Roshan Vaid and Akram Mendez; _Corresponding author:_ Tanmoy Mondal), studied how the gene expression profile of  m6A mRNA is affected during, and post COVID-19 infection.

Vaid and Mendez and colleagues used Vero cells and air/liquid interface (ALI) cultures of human airway epithelia to study SARS-CoV-2 infection. The researchers choose to study three SARS-CoV-2 variants B.1, B.1.1.7, and B.1.351. All three SARS-CoV-2 variants showed changes in the expression of genes related to RNA catabolism, including m6A readers and erasers. While m6A was found to be abundantly detected in viral RNA, infection with SARS-CoV-2 variants causes a loss of m6A in cellular RNAs.

The methyltransferase METTL3/METTL14 complex, is the key cellular enzyme complex responsible for depositing m6A modifications. Normally it is localized in the nucleus. The finding from this article of global loss of m6A peaks during SARS-CoV-2 infection may mean that the function of the METTL3/METTL14 is altered. Vaid and Mendez et al. continued to investigate this finding, and found that during SARS-CoV-2 infection, the METTL3 is partially relocalized from the nucleus to the cytoplasm. This change in localization from nucleus to was more prominent in the SARS-CoV-2 B.1 and B.1.1.7 variants, compared with SARS-CoV-2 B.1.351 variant. These results were consistent with the finding that m6A level was more reduced in the SARS-CoV-2 B.1 and B.1.1.7 infections, than in the B.1.351 infection.  In addition, the researchers were able to restore the localization of the METTL3 by inhibiting the export protein XPO1. This inhibition also means that a recovery of m6A on cellular RNA, and increased mRNA expression.

> Tanmoy Mondal, the corresponding author says "We were surprised by the drastic loss of host cell m6A RNA modification during SARS-CoV-2 infection. We do not know how long it takes to regain m6A post-infection. SARS-COV-2 may leave a long-lasting mark in the infected cells and this might provide clues to why some people have chronic symptoms that persist long after COVID”

In conclusion,  future pandemic preparedness efforts to tackle future pandemics will require the development of new antiviral strategies and antiviral drugs. The findings from Vaid and Mendez and  colleagues highlight how SARS-CoV-2 perturbs the m6A RNA modification pathway to deregulate cellular RNAs and thereby limit stress granule formation.  The METTL3 localization during SARS-CoV-2 infection could highlight a new novel antiviral strategy for treatment of COVID-19. Further studies into this potential novel strategy are warranted.

#### Data

The researchers, first published their articles as a preprint Dec 22 2022 on BioRXiv. The also adhere to Open Science by sharing data and code openly.

* All raw and processed sequencing data generated in this study have been submitted to the NCBI Gene Expression Omnibus ([GEO](https://www.ncbi.nlm.nih.gov/geo/) under accession number [GSE188477](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE188477).
* The source code used for the analysis of data in this study is available at [GitHub](https://github.com/AkramMendez/m6a_sarscov2) and [here](https://genome.cshlp.org/content/suppl/2023/03/24/gr.276407.121.DC1).

#### Article

DOI: [10.1101/gr.276407.121](https://doi.org/10.1101/gr.276407.121)

Vaid, R., Mendez, A., Thombare, K., Burgos-Panadero, R., Robinot, R., Fonseca, B. F., Gandasi, N. R., Ringlander, J., Hassan Baig, M., Dong, J.-J., Cho, J. Y., Reinius, B., Chakrabarti, L. A., Nystrom, K., & Mondal, T. (2023). Global loss of cellular m6A RNA methylation following infection with different SARS-CoV-2 variants. In Genome Research (Vol. 33, Issue 3, pp. 299–313).

#### Funding

This work was funded by grants from the Swedish Research Council, Sweden-South Korea COVID-19 grant from the Swedish Research Council, Svenska Läkaresällskapet; Kungl. Vetenskaps- och Vitterhets-Samhället (KVVS), as well as several international funders.

#### Infrastructure

The core facility at Novum, BEA, Bioinformatics and Expression Analysis has supported with sequencing, and the Proteomic core facility at Gothenburg University supported with LC-MS/MS. Swedish National Infrastructure for Computing (SNIC) at UPPMAX has supported computations and data handling.
