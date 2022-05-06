---
title: Study of host-viral interactions of Crimean-Congo haemorrhagic fever identified potential new drugs
date: 2022-05-06
summary: New study from Neogi and research collaborators gives insight into host-viral interactions of Crimean-Congo hemorrhagic fever, an infectious disease without available treatments. Raw RNAseq, Mass spectrometry proteomics data and codes shared.
banner: /highlights/banners/crimean_congo_interactions.jpg
banner_large: /highlights/banners/crimean_congo_interactions_large.jpg
banner_caption: Fig 3c. from Neogi et al. (2022). Heatmap of significant correlation (adj. p < 0.05) between key metabolic and signaling pathways. Column and row annotation denotes corresponding pathways.
highlights_topics: [Infectious diseases]
---

The COVID-19 pandemic is now moving into a more endemic phase in Sweden, as well as many other parts of the world. Regardless, SARS-CoV-2 still poses a serious global health threat, particularly when considering the potential effects of novel variants. Continuous pandemic preparedness efforts are therefore warranted. Global preparedness is also beneficial to safeguard against the threat of pandemics caused by other emerging pathogens.

At present, Crimean-Congo hemorrhagic fever virus (CCHFV) is uncommon in most parts of the world. However, it is endemic to almost 30 countries across sub-Saharan Africa, South-Eastern Europe, the Middle East, and Central Asia ([Bente et al., 2013](https://doi.org/10.1016/j.antiviral.2013.07.006); [Zivcec et al., 2016](https://doi.org/10.3390/v8040106)), and is spreading into new populations. CCHFV has been capable of infecting humans for thousands of years; archeological blood samples indicate that it was endemic to Celtic Iron Age populations near the Danube river. CCHFV is an RNA virus that belongs to the *Nairoviridae* family, and causes Crimean-Congo hemorrhagic fever (CCHF) disease. CCHF is transmitted through bites from infected ticks and can pass from animals to humans as well as between humans. Symptoms of the disease include fever, joint pain, vomiting, and uncontrolled bleeding, which can ultimately lead to organ failure. To date. there are no effective treatments for or vaccine against CCHF, and mortality rates for the disease vary between 3 and 40%.

Knowledge about the pathogenesis of CCHFV, and how it interacts with host cells is key to enable future drug and vaccine development. However, very little is currently known, primarily because outbreaks of CCHF are sporadic and usually occur in regions lacking the infrastructure to conduct the necessary studies.

In an article recently published eLife, many researchers collaborated to study the pathogenesis and host-viral interactions of the CCHFV. The work involved researchers from multiple Swedish institutions, including Karolinska Institutet, the Public Health Agency, Stockholm University, Bioinformatics Infrastructure Sweden (NBIS), Science for Life Laboratory (SciLifeLab), and the National Veterinary Institute of Sweden. They were joined by research groups from India, Turkey, Germany and the UK, making this a truly international effort.

Neogi and colleagues used a *multi-omics systems biology approach* to study the complex host-viral interaction of the CCHFV. The same approach was recently used by the team to study the response of other viruses e.g. HIV-1, SARS, MERS and SARS-CoV-2, ([Appelberg et al., 2020](https://doi.org/10.1080/22221751.2020.1799723); [Krishnan et al., 2021](https://doi.org/10.1016/j.mcpro.2021.100159)). We previously wrote a [Data Highlight](https://covid19dataportal.se/highlights/metabolic_perturbation_therapeutic_target) about some of their earlier work on the *Swedish COVID-19 & Pandemic Preparedness Data Portal*. In that study, the researchers aimed to mimic the alternations that occur during the acute CCHFV viral phases.

In the present study, the researchers completed a longitudinal study of a CCHFV patient cohort originating from Turkey (initial N=18, mortality rate 5.6%, 12 were included in the study). They analyzed peripheral blood mononuclear cells (PBMCs) during both the acute and convalescent (after one year of recovery) phases of the disease. They used a differential gene expression (DGE) profile to compare gene expression in the two phases. This showed that 2891 genes were up-regulated, and 2738 genes were down-regulated (adj. p<0.05). The researchers then used RNAseq analysis of PBMCs in order to compare the metabolic pathways used in the acute and convalescent phases. In brief, the results showed a number of changes (N=205), with ~30% up-regulated and ~10% down-regulated in the interferon signaling-related pathways, which are known to be involved in viral response during CCHFV infection. In addition, pathways involved in central carbon and energy metabolism (CCEM) were found to be important during the CCHFV infection. Notably, an up-regulation of oxidative phosphorylation (OXPHOS) was detected in both transcriptomics and Huh7 proteomics data from patients. In addition, a time-series analysis of a Huh-1 cell culture confirmed that OXPHOS was increasingly up-regulated during the productive viral replication phase. The researchers then directly tested how viral replication was affected by blocking two key CCEM pathways fueling OXPHOS in the Huh7 cells; glycolysis and glutaminolysis. Specifically, they used 2-deoxy-D-glucose (2-DG) and 6-diazo-5-oxo-L-norleucine (DON), both of which are known drug candidates. This resulted in suppressed CCHFV-replication and successfully controlled viral replication in the lab setting.

> “Our main goal to take this approach targeting host to limit the viral replication subsequently disease severity to the clinic, and we are initiating the pre-clinical studies in animal experiments.” said Ujjwal Neogi, professor at the Department of Laboratory Medicine, Karolinska Institutet.

In summary, the findings in this article could represent the first step towards the new antiviral drug treatment against CCHF disease. It is clear that further studies into the CCHF pathogenesis are required to investigate the host-virus interactions of CCHF. However, this study showed that targeting OXPHOS, and increasing the host antiviral response, may be one way to develop an attractive host-directed therapy during the acute CCHFV infection. CCHFV has been infecting human populations for thousands of years, and remains rare globally. However, CCHF is already an endemic in some parts of the world and continues to spread. This, taken together with the fact that no effective vaccines or treatments available for the disease, means that it poses a serious risk to human health that cannot be ignored. The development of treatments and vaccines against infectious diseases for which none are currently available is an important part of pandemic preparedness efforts.

#### Data

* All data needed to evaluate the conclusions in the paper are present in the paper and/or in the Supplementary Materials.
* Raw RNAseq data is available in Sequence Read Archive (SRA) with ID [PRJNA680886](https://www.ncbi.nlm.nih.gov/sra/?term=PRJNA680886).
* Mass spectrometry proteomics data have been deposited to the ProteomeXchange Consortium via the PRIDE partner repository with the dataset identifier [PXD022672](http://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD022672).
* All the codes are available [here](https://github.com/neogilab/CCHF-Turkey) in GitHub.
* The raw Western blot images are provided as Source data 1 in the article.

#### Article

DOI: [10.7554/eLife.76071](https://doi.org/10.7554/eLife.76071)

*Multi-omics insights into host-viral response and pathogenesis in Crimean-Congo hemorrhagic fever viruses for novel therapeutic target.* Ujjwal Neogi , Nazif Elaldi, Sofia Appelberg, Anoop Ambikan, Emma Kennedy, Stuart Dowall, Binnur K Bagci, Soham Gupta, Jimmy E Rodriguez, Sara Svensson-Akusjärvi, Vanessa Monteil, Akos Vegvari, Rui Benfeitas, Akhil Banerjea, Friedemann Weber, Roger Hewson, Ali Mirazimi. eLife 2022;11:e76071.

#### Funding

This study was supported by grants from the Swedish Research Council, the Public Health England Grant In Aid, Karolinska Institutet and the European Union Horizon 2020 CCHF Vaccine Grant.
