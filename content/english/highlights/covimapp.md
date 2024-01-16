---
title: CoViMAPP – new resources for the analysis of the soluble blood proteome alterations in COVID-19
date: 2024-01-16
summary: Babačić and colleagues expanded the coverage of the soluble blood proteome using mass spectrometry. In order to support further research in this area, their results have been added to an open-access app.
banner: /highlights/banners/covimapp_logo.png
banner_large: /highlights/banners/covimapp_logo.png
banner_caption: CoViMAPP logo.
highlights_topics: [COVID-19]
tags: [COVID-19, Covimapp, Meta-analysis, R shiny, App, proteome, SciLifeLab Serve]
authors: [Katarina Öjefors Stark]
announcement: "This data highlight was also published on the <a target='_blank' href='https://data.scilifelab.se/highlights/covimapp/'>SciLifeLab Data Platform</a>, as the work described in this highlight constitutes data-driven life science. The Platform is a hub for data-driven life science in Sweden, containing multiple relevant resources, tools, and services. It includes information on multiple subjects, including infectious diseases, please check out the <a target='_blank' href='https://data.scilifelab.se/'>Data Platform</a> for more."
images: [/highlights/banners/covimapp_logo.png"]
---

Over the last few years, the COVID-19 pandemic has greatly impacted both society and healthcare. Although the effects of COVID-19 have now been mitigated using vaccines and non-pharmaceutical measures, COVID-19 can still cause severe disease and even death in some individuals. Continued research is essential in increasing our understanding of COVID-19, and therefore in protecting the elderly and other individuals with a relatively increased risk of developing severe disease.

Research has shown that cytokine storms (elevated release of cytokines in the blood) cause systemic hyperinflammation in patients with COVID-19. Systemic hyperinflammation is considered to be one of the most important pathophysiological mechanisms behind severe COVID-19, and can lead to multi-organ damage and death. The inflammation is caused by systemic immunological perturbations in the human body that are mediated by the blood. Therefore, plasma (the liquid component of blood) is often used for studies into the systemic biological processes involved in COVID-19 pathogenesis.

Multiple types of circulating molecules (e.g., lipids, metabolites, mRNAs, and proteins) have been studied in COVID-19 patients, but proteins remain most commonly used in clinical practice. Using global mass spectrometry (MS) methods, studies have identified a few hundred protein biomarkers in plasma or serum. However, the soluble blood proteome is known to contain more than 4,500 proteins, meaning that much of the proteome remains unexplored. Continued research in this area is crucial in order to allow us to prevent the onset of severe COVID-19.
In a recent article by Haris Babačić et al. in Nature Communications, researchers from Karolinska Institutet, Karolinska University Hospital, The Laboratory for Molecular Infection Medicine Sweden (MIMS) at Umeå University, Linköping University, and Science for Life Laboratory (SciLifeLab), led by Jonas Klingström and Maria Pernemalm, performed systematic analyses of circulating, soluble proteins using mass spectrometry proteomics to expand the soluble blood proteome coverage.

Babačić and colleagues used serum samples from twenty hospitalised COVID-19 patients (ancestral SARS-CoV-2), and seven PCR-negative and seronegative controls. More information about the cohort used is available in <a target="_blank" href="https://doi.org/10.4049/jimmunol.2000717">Varnaitė _et al._ (2020)</a>. The samples were analysed using high-resolution isoelectric focusing (HiRIEF) coupled with liquid chromatography tandem mass spectrometry (LC-MS/MS). In addition, the researchers performed _in vitro_ SARS-CoV-2 infection experiments in human lung adenocarcinoma (Calu-3) cells to compare to proteome and phosphoproteome changes evident in the blood of COVID-19 patients. The results showed that a large part of the soluble blood proteome was altered in COVID-19 patients compared to healthy controls. COVID-19 patients were, for example, found to have elevated serum levels of NF-kB-, interferon-, purine metabolism-, heat shock-, and proteasomal- proteins. Furthermore, many of these proteins were also found to be changed in _in vitro_ SARS-CoV-2 infection experiments. Additionally, changes were identified in phosphorylated peptides in the serum of both COVID-19 patients and SARS-CoV-2-infected cells.

In order to provide estimates of the alterations that occurred due to COVID-19, Babačić and colleagues performed a meta-analysis of global MS proteomics datasets, as well as their own dataset (1709 individuals, including 1039 patients), and identified >1500 proteins that were identified in at least two cohorts. In order to aid further research and clinical use of these state-of the art- MS results, the researchers developed an open-access app called <a target="_blank" href="https://covimapp.serve.scilifelab.se">CoViD-19 Meta-Analysis of Plasma Proteins (CoViMAPP)</a>. CoViMAPP includes information about the effect sizes of alterations and the diagnostic potential of soluble blood proteins in COVID-19. The app also includes summary estimates obtained from published studies of plasma proteome profiling in COVID-19 using unbiased mass-spectrometry proteomics.

In summary, this study is a comprehensive analysis of the soluble blood proteome alterations that occur in COVID-19. The results validate multiple previous findings and pinpoint new alterations. Furthermore, this study provides the current MS-based state-of-the-art concluding estimates for soluble blood proteome alterations in COVID-19. The researchers aim for CoViMAPP to be used as a dynamic tool for future dynamic meta-analysis, and additional curated studies may therefore be included to update the summary estimates.

#### Data and code availability

* All results described in the manuscript are presented in main or supplementary figures or datasets. All results from the meta-analysis are available as a <a target="_blank" href="https://doi.org/10.17044/scilifelab.22293148.v1">R Shiny app</a>.
* Raw and processed MS data are deposited via ProteomeXchange to the PRIDE database, with accession codes <a target="_blank" href="https://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD037486">PXD037486</a>, <a target="_blank" href="https://proteomecentral.proteomexchange.org/cgi/GetDataset?ID=PXD037451">PXD037451</a>, and <a target="_blank" href="">PXD040982</a>.
* <a target="_blank" href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10516886/bin/41467_2023_41159_MOESM20_ESM.zip">Source data</a> are provided with this paper.
* The custom code for the Nextflow proteomics workflow is deposited in <a target="_blank" href="https://github.com/lehtiolab/ddamsproteomics">this</a> GitHub repository.
* The R code used for the analyses is deposited in <a target="_blank" href="https://github.com/harbab/covid19proteomics">this</a> GitHub repository.
* The R shiny app <a target="_blank" href="https://covimapp.serve.scilifelab.se">COViMAPP</a> is available on <a target="_blank" href="https://serve.scilifelab.se/apps/">SciLifeLab Serve</a>.

#### Article

DOI: <a target="_blank" href="https://doi.org/10.1038/s41467-023-41159-z">10.1038/s41467-023-41159-z</a>

Babačić, H., Christ, W., Araújo, J. E., Mermelekas , G., Sharma, N., Tynell , J., García, M., Varnaite, R., Asgeirsson, H., Glans, H., Lehtiö, J., Gredmark-Russ, S., Klingström, J., & Pernemalm, M. (2023) Comprehensive proteomics and meta-analysis of COVID-19 host response. In: Nature communications (Vol. 14, Issue 1, 5921).

#### Funding

This study was supported grants from the Knut and Alice Wallenberg foundation (KAW), within the SciLifeLab KAW COVID-19 national research program,  the Swedish Research Marianne and Marcus Wallenberg Foundation (SGR), Region Stockholm (clinical research appointment), and by Centre for Innovative Medicine.

#### Infrastructure

The Clinical Proteomics Facility and the Data Centre at Science for Life Laboratory was used for parts of this study.
