---
title: Drug repurposing identifies Fostamatinib as a drug with potentially high efficacy in COVID-19 treatment
date: 2021-11-19
summary: Recent study finds that drug repurposing can offer an average of an 11-fold increase in disease coverage and demonstrates its value for COVID-19. All data and code that support the findings have been made publicly available.
banner: /highlights/banners/drug_repurposing_small.jpeg
banner_large: /highlights/banners/drug_repurposing.jpeg
banner_caption: "Source: Figure 4 of Rivero-García et al. 2021"
---

The COVID-19 pandemic has over almost two years challenged global healthcare. Vaccines towards COVID-19 have been developed in record-time but therapeutics to treat the novel disease are still warranted. World-wide efforts to identify new and effective therapeutics candidates for COVID-19 have been going on since the beginning of the pandemic, for example the [Coronavirus Treatment Acceleration Program](https://www.fda.gov/drugs/coronavirus-covid-19-drugs/coronavirus-treatment-acceleration-program-ctap) started by the FDA in the US. The traditional *“one drug—one gene—one disease”* in Drug discovery has been successful in many cases in past but may have economical downsides as well as risk leaving patients suffering from rare conditions with limited therapeutic options. *Polypharmacology* which refers to a drugs' ability to target more than one protein and *drug repurposing ("repositioning")* defined as using an already approved drug for a new therapeutic indication are approaches to mitigate these problems. [In addition, the idea of combining these two concepts has been proposed.]

In a recent study, researchers from Stockholm University/SciLifeLab (first author: Inés Rivero-García, corresponding author: Prof. Erik L. L. Sonnhammer) therefore choose to approach drug repurposing from a network and module-based perspective and also to demonstrate its value for COVID-19.

Rivero-García and colleagues performed three levels of analyses to gain further knowledge into not yet elucidated therapeutic opportunities. Firstly, at the drug target level the researchers quantified the number of direct targets per drug, as well as extended these to consider their first neighbors in the human functional interactome. Secondly, at the disease level and disease module level the researchers quantified the number of diseases each drug can be linked to by mapping drug targets to diseases. Notably, the results show that using FDA-approved indications as a reference level, drug repurposing is more efficient than previously thought and can offer an 11-fold increase in disease coverage. The highest number of diseases covered per drug increased from 134 to 167 after extending the drug targets with their high confidence first neighbors in the network. Furthermore, network analysis connecting drugs to disease modules showed that, on average, drugs target four disease modules. Another notable finding from the study was that calculating the maximum number of diseases that a small number of drugs can cover showed that three drugs, Fostamatinib, Zinc, and Neonatal foreskin keratinocyte, can cover 95% of all diseases.

In addition, the researchers applied their new drug repurposing and network module analysis to study COVID-19. The results indicates that Fostamatinib, a tyrosine kinase inhibitor used to treat chronic immune thrombocytopenia (in Sweden available under the brand name Tavlesse) is the drug with the highest module coverage.

> “This study further strengthens and supports the use of drug repurposing for future combinatorial therapeutic opportunities both for COVID-19 and other diseases,” says Erik Sonnhammer, professor at Stockholm University and the corresponding author of the paper.

Importantly, the researchers have made all the data and code that support the findings of this study publicly available [through a BitBucket respository](https://bitbucket.org/sonnhammergroup/unadrug).

In summary, *drug repurposing* was found to offer an 11-fold leverage in drug-disease associations, and depends to a larger extent on target proteins being shared between diseases than on polypharmacological drug properties. Using the drug repurposing and network module analysis, the researchers identified Fostamatinib in the COVID-19 case as a drug that may potentially achieve higher efficacy because the drug interferes with more mechanisms.

*The project that gave rise to these results received support for a fellowship from Fundación Margit y Folke Pehrzon. The Open access funding was provided by Stockholm University.*

#### Data

- [BitBucket repository containing scripts (R), data files, result files](https://bitbucket.org/sonnhammergroup/unadrug/src/master/)

#### Article

DOI: [10.1038/s41598-021-99721-y](https://doi.org/10.1038/s41598-021-99721-y)

Rivero-García, I., Castresana-Aguirre, M., Guglielmo, L., Guala, D. & Sonnhammer, E. L. L. Drug repurposing improves disease targeting 11-fold and can be augmented by network module targeting, applied to COVID-19. *Scientific Reports* **11**, 20687 (2021).
