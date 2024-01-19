---
title: CoViMAPP – analysing changes in soluble blood proteome alterations due to COVID-19
date: 2024-01-19
summary: Babačić and colleagues expanded the coverage of the soluble blood proteome using mass spectrometry. In order to support further research in this area, their results have been added to an open-access app.
banner: /highlights/banners/covimapp_logo.png
banner_large: /highlights/banners/covimapp_logo.png
banner_caption: CoViMAPP logo.
highlights_topics: [COVID-19]
tags:
  [
    COVID-19,
    Covimapp,
    Meta-analysis,
    R shiny,
    App,
    Proteome,
    SciLifeLab,
    Serve,
    Blood,
    Proteins,
    SARS-CoV-2,
  ]
authors: [Katarina Öjefors Stark]
announcement: "This data highlight was also published on the <a target='_blank' href='https://data.scilifelab.se/highlights/covimapp/'>SciLifeLab Data Platform</a>, as the work described in this highlight constitutes data-driven life science. The Platform is a hub for data-driven life science in Sweden, containing multiple relevant resources, tools, and services. It includes information on multiple subjects, including infectious diseases, please check out the <a target='_blank' href='https://data.scilifelab.se/'>Data Platform</a> for more."
images: [/highlights/banners/covimapp_logo.png"]
---

Over the last few years, the COVID-19 pandemic has greatly impacted both society and healthcare. Although the effects of COVID-19 have now been mitigated using vaccines and non-pharmaceutical measures, COVID-19 can still cause severe disease and even death in some individuals. Continued research is essential in increasing our understanding of COVID-19, and therefore in protecting the elderly and other individuals with a relatively increased risk of developing severe disease.

Research has shown that cytokine storms (elevated release of cytokines in the blood) cause systemic hyperinflammation in patients with COVID-19. Systemic hyperinflammation is considered to be one of the most important pathophysiological mechanisms behind severe COVID-19, and can lead to multi-organ damage and death. The inflammation is caused by systemic immunological perturbations in the human body that are mediated by the blood. Therefore, plasma (the liquid component of blood) is often used for studies into the systemic biological processes involved in COVID-19 pathogenesis.

Multiple types of circulating molecules (e.g. lipids, metabolites, mRNAs, and proteins) have been studied in COVID-19 patients, but proteins remain the most commonly used in clinical practice. Using global mass spectrometry (MS) methods, studies have identified a few hundred protein biomarkers in plasma or serum. However, the soluble blood proteome is known to contain more than 4,500 proteins, meaning that much of the proteome remains unexplored. Continued research in this area is crucial in order to allow us to prevent the onset of severe COVID-19.

In a recent Nature Communications article by [Babačić _et al._ (2023)](https://doi.org/10.1038/s41467-023-41159-z), researchers from Karolinska Institutet, Karolinska University Hospital, The Laboratory for Molecular Infection Medicine Sweden (MIMS) at Umeå University, Linköping University, and Science for Life Laboratory (SciLifeLab), led by Jonas Klingström and Maria Pernemalm, expanded the coverage of the soluble bood proteome using systematic analyses of circulating soluble proteins and mass spectrometry.

Babačić and colleagues used serum samples from twenty hospitalised COVID-19 patients (ancestral SARS-CoV-2), and seven PCR-negative and seronegative controls. More information about the cohort used is available in [Varnaitė _et al._ (2020)](https://doi.org/10.4049/jimmunol.2000717). The samples were analysed using high-resolution isoelectric focusing (HiRIEF) coupled with liquid chromatography tandem mass spectrometry (LC-MS/MS). In addition, the researchers performed _in vitro_ SARS-CoV-2 infection experiments in human lung adenocarcinoma (Calu-3) cells to compare to proteome and phosphoproteome changes evident in the blood of COVID-19 patients. The results showed that a large part of the soluble blood proteome was altered in COVID-19 patients compared to healthy controls. COVID-19 patients were, for example, found to have elevated serum levels of NF-kB-, interferon-, purine metabolism-, heat shock-, and proteasomal- proteins. Furthermore, many of these proteins were also found to be changed in _in vitro_ SARS-CoV-2 infection experiments. Additionally, changes were identified in phosphorylated peptides in the serum of both COVID-19 patients and SARS-CoV-2-infected cells.

In order to provide estimates of the alterations that occurred due to COVID-19, Babačić and colleagues performed a meta-analysis of global MS proteomics datasets, as well as their own dataset (1709 individuals, including 1039 patients), and identified over 1500 proteins that were present in at least two cohorts. In order to aid further research and clinical use of these state-of-the-art MS results, the researchers developed an open-access app called [CoViD-19 Meta-Analysis of Plasma Proteins (CoViMAPP)](https://covimapp.serve.scilifelab.se). CoViMAPP includes information about the effect sizes of alterations and the diagnostic potential of soluble blood proteins in COVID-19. The app also includes summary estimates obtained from published studies of plasma proteome profiling in COVID-19 using unbiased mass-spectrometry proteomics.

In summary, this study is a comprehensive analysis of the soluble blood proteome alterations that occur in COVID-19. The results validate multiple previous findings and pinpoint new alterations. Furthermore, this study provides the current MS-based state-of-the-art concluding estimates for soluble blood proteome alterations in COVID-19. The researchers aim for CoViMAPP to be used as a dynamic tool for future meta-analyses. Additional curated studies can and will be included to update the summary estimates.

#### Data and code availability

- All results described in the manuscript are presented in main or supplementary figures or datasets. All results from the meta-analysis are available as an R Shiny app, [CoViMAPP](https://covimapp.serve.scilifelab.se), which is available on [SciLifeLab Serve](https://serve.scilifelab.se/apps/). To understand more about CoViMAPP, please see the associated entry in the [SciLifeLab Data Repository](https://doi.org/10.17044/scilifelab.22293148).
- Raw and processed MS data are deposited via ProteomeXchange to the PRIDE database, with accession numbers [PXD037486](https://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD037486), [PXD037451](https://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD037451), and [PXD040982](https://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD040982).
- [Source data](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10516886/bin/41467_2023_41159_MOESM20_ESM.zip) are provided with the publication.
- The custom code for the Nextflow proteomics workflow is deposited in [this GitHub repository](https://github.com/lehtiolab/ddamsproteomics).
- The R code used for the analyses is deposited in [this GitHub repository](https://github.com/harbab/covid19proteomics)

#### Article

DOI: [10.1038/s41467-023-41159-z](https://doi.org/10.1038/s41467-023-41159-z)

Babačić, H., Christ, W., Araújo, J. E., Mermelekas , G., Sharma, N., Tynell , J., García, M., Varnaite, R., Asgeirsson, H., Glans, H., Lehtiö, J., Gredmark-Russ, S., Klingström, J., & Pernemalm, M. (2023) Comprehensive proteomics and meta-analysis of COVID-19 host response. In: Nature communications (Vol. 14, Issue 1, 5921).

#### Funding

This study was supported grants from the Knut and Alice Wallenberg foundation (KAW), within the SciLifeLab KAW COVID-19 national research program, the Swedish Research Marianne and Marcus Wallenberg Foundation (SGR), Region Stockholm (clinical research appointment), and by Centre for Innovative Medicine.

#### Infrastructure

The Clinical Proteomics Facility and the Data Centre at Science for Life Laboratory (SciLifeLab) were used for parts of this study.
