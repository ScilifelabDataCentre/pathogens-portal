---
title: Proteomic profiling in COVID-19 patients as biomarkers to monitor disease severity
date: 2021-04-13
summary: Recent study examined a large number of inflammatory, immune response, cardiovascular, and neurological markers in the blood of patients variously impacted by COVID-19. Data and analysis code were shared in public repositories.
banner: /news/banners/proteomic_blood_profiling.png
banner_large: /news/banners/proteomic_blood_profiling_large.png
banner_caption: "Figure 2 from Patel, Ashton, et al (2021) showing 269 proteins significantly differentially expressed in COVID-19 patients."
needs_translation: no
---

The current COVID-19 pandemic has increased the burden on healthcare and has a large socioeconomical impact on society. SARS-CoV-2 infection may manifest as a mild respiratory tract infection in most individuals, but in some individuals the infection progresses to severe pneumonia and acute respiratory distress syndrome which may lead to severe illness and mortality. Understanding proteomic differences between those individuals which are affected only mildly or not at all and those which are affected to a larger extent is important for understanding disease progression and identifying potential drug targets.

In a [recently published study](https://doi.org/10.1038/s41598-021-85877-0), Hamel Patel, Nicholas Ashton and colleagues examined a large number of inflammatory, immune response, cardiovascular, and neurological markers in blood using OLINK inflammation, autoimmune, cardiovascular and neurology panels. The blood protein profiling was performed on mild (N=26), severe (N=9) or critical (N=24) COVID-19 cases (total N=59), as well as healthy controls (N=28). The researchers performed differential expression analysis within and between disease groups (mild, severe, and critical) to generate nine different analyses. They analyzed and measured in total 368 proteins per individual. The collected proteomic data as well as analysis code were openly shared through public repositories.

One important part of the study by Patel, Ashton and colleagues was to further investigate central nervous system (CNS) injury markers which have previously been reported to be associated with COVID-19 disease severity. Specifically, an earlier study by the same research group ([Kanberg and colleagues *Neurology 95* (12), DOI: 10.1212/WNL.0000000000010111](https://doi.org/10.1212/WNL.0000000000010111)) described neurochemical evidence of neuronal injury and glial activation in patients with moderate and severe COVID-19.

The results showed that for eleven proteins the expression differed significantly between the control, mild, severe, and critical symptom groups, and eight of these proteins were consistently perturbed as infection symptoms increased (control → mild → severe → critical). Out of these, six were associated with disease severity (IL6, CKAP4, Gal-9, IL-1ra, LILRB4 and PD-L1). The same expression was observed for all six proteins, increasing more for each step, control group to the mild group, to severe group, and to the critical group.  

Notably, the results support previous reports that Interleukin 6 (IL-6) expression increases with disease severity. IL6 is an inflammatory cytokine that may induce fever in patients with autoimmune diseases or infection. Previous research has shown elevated values of IL-6 in COVID-19 patients and associated with increased COVID-19 mortality ([Aziz and colleagues, *J Med Virol* 2020, DOI: 10.1002/jmv.25948](https://onlinelibrary.wiley.com/doi/10.1002/jmv.25948)).

In addition, the researchers found that Neurofibromin 2 (NF2 protein) was found to be the most perturbed protein in “control vs. mild”, “control vs. critical” and “control vs. case” analyses and the most perturbed protein in all nine analyses. NF2 was also significantly down-regulated in all COVID-19 patients. The NF2 protein is also known as Merlin protein (moesin-ezrin-radixin-like protein). Previous research has shown that it functions as a tumor suppressor and activates anti-mitogenic signaling at tight-junctions, which means an inactivation of NF2 causes uncontrolled mitogenic signaling and tumorigenesis.

The researchers shared the proteomic data in the BioStudies database [under the accession number S-BSST416](https://www.ebi.ac.uk/biostudies/studies/S-BSST416?query=S-BSST416). To increase usefulness of the results, the researchers have made all results from this study available through [an interactive web-based application for instant data exploration and visualization](https://phidatalab-shiny.rosalind.kcl.ac.uk/COVID19/). The application allows other researchers to quickly visualize the expression of specific proteins across the control, mild, severe and severe symptom groups. Finally, all data analysis scripts used in the study have also been shared openly under the DOI [10.5281/zenodo.3895885](https://doi.org/10.5281/zenodo.3895885) as well as through a [GitHub repository](https://github.com/hamelpatel/COVID19_proteomic/tree/v1.0).

> "It has become increasingly apparent that neurological symptoms are common in patients suffering from COVID-19, during acute infection as well as long-term and it is of great importance to evaluate the potential usefulness of biomarkers in both understanding CNS pathogenesis and establishing a diagnosis of CNS infection. A better understanding of the underlying pathogenetic mechanisms in neuro-COVID is vital and has important implications when considering future CNS-targeted treatment interventions. We think it is important to share data, especially during the COVID-19-pandemic, to allow other researchers and society to validate and use the data. We have therefore shared the proteomic data in an open database," says Magnus Gisslén, professor of infectious diseases at the Sahlgrenska Academy at the University of Gothenburg and one of the senior authors of the paper.

In summary, Patel, Ashton and colleagues suggest that changes in blood proteins may be associated with disease severity in COVID-19 patients. Blood protein could therefore be used for monitoring disease severity, but also be investigated as potential therapeutic targets.

*The research was supported by Swedish Research Council, the Swedish Alzheimer Foundation, the Swedish Dementia Foundation (Demensförbundet), Hjärnfonden, Anna Lisa and Brother Björnsson’s Foundation. Sweden, the Swedish state under the agreement between the Swedish government and the County Councils, the ALF-agreement (ALF), and European Union Joint Program for Neurodegenerative Disorders. In addition, SciLifeLab/KAW national COVID-19 research program, Swedish Research Council, the European Research Council as well as a large number of international grantees, for example, NIHR BioResource Centre Maudsley at South London and Maudsley NHS Foundation Trust (SLaM) & Institute of Psychiatry, Psychology and Neuroscience (IoPPN), King’s College London, Health and Social Care Research and Development Division (Welsh Government), Public Health Agency (Northern Ireland), British Heart Foundation and Wellcome Trust, The National Institute for Health Research, University College London Hospitals Biomedical Research Centre.*

#### Data

* Proteomic data: [BioStudies, accession number S-BSST416](https://www.ebi.ac.uk/biostudies/studies/S-BSST416?query=S-BSST416)
* Data analysis code: [DOI 10.5281/zenodo.3895885](https://doi.org/10.5281/zenodo.3895885) or [GitHub](https://github.com/hamelpatel/COVID19_proteomic/tree/v1.0).
* [Interactive web-based application for instant data exploration and visualization (R Shiny app)](https://phidatalab-shiny.rosalind.kcl.ac.uk/COVID19/)

#### Article

DOI: [10.1038/s41598-021-85877-0](https://doi.org/10.1038/s41598-021-85877-0)

Patel, H. Ashton, N. J.  Dobson, R. J. B.  Andersson, L.-M., Yilmaz, A. Blennow, K. Gisslen, M. & Zetterberg H. Proteomic blood profiling in mild, severe and critical COVID-19 patients. *Sci Rep*, **11** 6357 (2021).
