---
title: Large effort study to elucidate replication initiation in bacteria
date: 2023-09-20
summary: This study by Knöppel, Broström et al is a large effort to elucidate replication initiation in bacteria. The authors have openly shared over 3 TB of microscopy imaging data.
banner: /highlights/banners/ELF_banner.png
banner_large: /highlights/banners/ELF_large.png
banner_caption: Image courtesy Johan Elf lab
highlights_topics: [Infectious Diseases]
tags: [Infectious diseasese, Replication, Escherichia coli]
announcement: "This data highlight was also [published on the SciLifeLab Data Platform](https://data.scilifelab.se/highlights/bacterial_replication/), as the work described in this highlight constitutes data-driven life science. The Platform is a hub for data-driven life science in Sweden, containing multiple relevant resources, tools, and services. It includes information on multiple subjects, including infectious diseases, please check out the [Data Platform](https://data.scilifelab.se/) for more."
---

It is commonly known that all cells must coordinate DNA replication with cell growth; each chromosome should, on average, replicate once per generation. Bacteria, e.g. _Escherichia coli_, have optimised their division speed in order to survive in a very competitive environment. Fast division makes replication coordination extra challenging, especially in cases when the bacterial generation times are shorter than the time it takes to replicate the chromosome. This means that bacteria must have two complete copies of their chromosome ready before cell division, but still keep the ratio between the number of chromosome copies and cell divisions constant.

The research community has, for over 50 years, studied how DNA copying and cell division are coordinated in bacteria. These studies have revealed the importance of a protein known as DNaA in the replication of _E. coli_. DnaA triggers the initiation of chromosome replication when bound to ATP, and there is a negative correlation between cell size at initiation and the intracellular concentration of DnaA. Whilst traditional methods of genetics and molecular biology have been essential for elucidating parts of the _E. coli_ replication processes, advances in microscopy have allowed for more insights into the phenotypic outcome that the interactions between these parts should accomplish. For example, recent studies have used high-throughput microscopy to observe ongoing cell replication in bacteria on a single-cell level. However, a number of key research questions are yet to be addressed, e.g. how the cell decides it’s time to initiate replication. Three main models have been proposed; the inhibitor dilution model, the initiation accumulation model, and the initiator activations/deactivation cycling.

In a recent article in PNAS, researchers from Uppsala University and Science for Life Laboratory (SciLifeLab), Sweden, (First authors: Anna Knöppel and Oscar Broström, Corresponding authors: Johan Elf and David Fange) used high-throughput fluorescence microscopy to study the coordination of replication and division cycles in _E.coli_. By systematically exploring the replication-initiation control, the researchers aimed to find the most likely replication initiation model used in _E. coli_.

In this study, Knöppel, Broström, and colleagues created mutant strains by inserting chromosomal modifications. The replisome can be described as the multiprotein molecular machinery responsible for the replication of DNA. In order to compare how important different parts implicated in replication control are in _E. coli_ replication, the researchers tracked the fluorescently labeled replisomes in individual cells through thousands of division cycles in the wild-type and mutant strains, thereby gaining knowledge of the importance of each regulator.

In one experiment, Knöppel _et al_. used a specific mutant _E. coli_ strain with a sole DnaA gene under the control of an inducible promotor. The results showed that DnaA synthesis is not a requirement for triggering accurate initiation of replication. In addition, initiation size increased marginally as DnaA was diluted by growth after DnaA expression had been turned off. This led the researchers to conclude that the conversion of DnaA between its active ATP-bound state and inactive ADP-bound states is more important for initiation size control than the total free concentration of DnaA.

Further, the researchers studied different pathways known to be important for the DnaA-ATP/ADP conversion. For these experiments, they created mutant _E.coli_ strains with combinations of deletions in the DARS1, DARS2, and datA loci. The results showed that DARS and datA can compensate for each other, e.g. deletion of DARS could be compensated for by deleting datA and, additionally, also by overexpressing DnaA. Among the DnaA-ATP/ADP conversion mechanisms tested, deletion of the regulatory inactivation of DnaA (RIDA) was found to have the most severe impact on replication initiation.

In conclusion, this study is one of the largest efforts to date to elucidate replication initiation in bacteria. It contains over 3 TB of microscopy imaging data. The findings outlined above support the third model suggested for replication initiation: initiator activation/deactivation cycling. However, additional studies into this model are warranted.

#### Data

- Data and all code have been deposited in the [SciLifeLab data repository](https://figshare.scilifelab.se/articles/dataset/Regulatory_elements_coordinating_initiation_of_chromosome_replication_to_the_Escherichia_coli_cell_cycle/22139918/1).
- Proteomics data have been deposited in PRIDE [(Project PXD036580)](https://www.ebi.ac.uk/pride/archive/projects/PXD036580/).

#### Article

DOI: [10.1073/pnas.2213795120](https://doi.org/10.1073/pnas.2213795120)

Knöppel, A., Broström, O., Gras, K., Elf, J., & Fange, D. (2023). Regulatory elements coordinating initiation of chromosome replication to the Escherichia coli cell cycle. In: PNAS (Vol. 120, Issue 22, e2213795120).

#### Funding

This work was funded by grants from the European Research Council (advanced grant no. 885360), the Swedish Research Council (grant nos. 2016-06213 and 2018-03958), the Knut and Alice Wallenberg Foundation (grant nos. 2016.0077, 2017.0291, and 2019.0439), and the eSSENCE e-science initiative.

#### Infrastructure

Resources provided by Swedish National Infrastructure for Computing (SNIC) (now known as National Academic Infrastructure for Super­computing in Sweden, NAISS) at UPPMAX enabled data management and computing.
