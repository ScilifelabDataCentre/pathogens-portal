---
title: Rapid microfluidic approach to detect hidden antibiotic resistance in bloodstream infections
date: 2026-06-29
summary: A droplet microfluidics platform combined with image texture analysis enables rapid detection of rare antibiotic-resistant bacterial subpopulations that are often missed by standard diagnostic methods.
banner: /highlights/banners/antibiotic_heteroresistance.png
banner_large: /highlights/banners/antibiotic_heteroresistance.png
banner_caption: "Figure 1 of Agnihotri _et al._ (2026)"
highlights_topics: [Antibiotic Resistance]
tags:
  [
    Heteroresistance,
    Antimicrobial resistance (AMR),
    Droplet microfluidics,
    Antibiotic susceptibility testing (AST),
    Bacterial phenotyping,
    Image texture analysis,
    Digital diagnostics,
    Population analysis profile (PAP),
    Rapid diagnostics
  ]
images: [/highlights/banners/antibiotic_heteroresistance.png]
---

Antimicrobial resistance (AMR) is one of the greatest threats to global health, contributing substantially to morbidity and mortality worldwide. A particularly challenging form of resistance is _heteroresistance (HR)_, in which a small subpopulation of bacterial cells within an otherwise susceptible population can survive antibiotic concentrations many times higher than the [minimum inhibitory concentration (MIC)](https://www.nature.com/articles/s41579-019-0218-1). These resistant subpopulations often occur at frequencies between 10⁻⁷ and 10⁻⁴ and can rapidly expand during treatment, leading to therapeutic failure. However, HR frequently escapes detection because routine antibiotic susceptibility testing (AST) lacks sufficient sensitivity, while the current gold-standard population analysis profile (PAP) test is labor-intensive and requires several days to perform.

To address this diagnostic challenge, [Agnihotri et al. (2026)](https://www.nature.com/articles/s41746-026-02808-x) developed a digital phenotyping platform that combines droplet microfluidics with computational image texture analysis to detect rare antibiotic-resistant bacterial subpopulations from bloodstream infections. The method was evaluated using clinically relevant Gram-negative pathogens (_Klebsiella pneumoniae_, _Pseudomonas aeruginosa_, and _Acinetobacter baumannii_) and the Gram-positive pathogen _Staphylococcus aureus_. By integrating high-throughput droplet technology with automated image analysis, the authors aimed to create a faster and more sensitive alternative to PAP testing.

The workflow began with encapsulating bacterial cultures and antibiotics within hundreds of microfluidic droplets. The droplets were incubated and imaged over time using automated microscopy. Rather than relying on changes in droplet size, as in previous approaches, the researchers quantified image texture characteristics such as homogeneity and correlation using gray-level co-occurrence matrix (GLCM) analysis. These parameters allowed automated identification of droplets containing growing resistant subpopulations, providing an objective measure of HR.

The platform successfully distinguished HR and non-HR strains across all tested species. For non-HR strains, no bacterial growth was observed in antibiotic-containing droplets, and texture measurements remained stable throughout the experiments. In contrast, HR strains exhibited distinct droplets with bacterial growth, resulting in measurable decreases in homogeneity and correlation values. Resistant subpopulations were detected in _A. baumannii_ exposed to amikacin, _K. pneumoniae_ exposed to amikacin, _P. aeruginosa_ exposed to meropenem, and _S. aureus_ exposed to vancomycin. The calculated frequencies of resistant subpopulations ranged from approximately 10⁻⁶ to 10⁻⁴, depending on the species and strain.

Importantly, the method demonstrated high sensitivity and speed. Resistant subpopulations could be detected as early as 6–12 hours for _K. pneumoniae_, around 12 hours for _A. baumannii_ and _P. aeruginosa_, and between 15 and 30 hours for _S. aureus_. Overall testing times were approximately 24 hours for Gram-negative bacteria and 48 hours for Gram-positive bacteria, substantially faster than conventional PAP assays, which typically require 2–3 days.

Performance evaluation demonstrated excellent agreement between automated texture analysis and manually verified classifications. Both homogeneity and correlation correctly identified all non-HR strains, with accuracies approaching 100%. For HR strains, only a small number of false-negative classifications were observed, particularly when using homogeneity as the classification parameter. The strongest performance was observed for _S. aureus_, where both texture features achieved perfect classification. Although correlation was less reliable for _P. aeruginosa_ because residual cellular debris occasionally interfered with image interpretation, overall accuracy remained high.

To validate the approach, the authors compared resistant subpopulation frequencies estimated by texture analysis with those obtained using the PAP test. The frequencies generated by the microfluidic platform closely matched PAP-derived values across all species. For example, HR _K. pneumoniae_ showed resistant subpopulation frequencies of approximately 6–8 × 10⁻⁵, while HR _A. baumannii_ exhibited frequencies around 10⁻⁴. Notably, the platform achieved a detection sensitivity of approximately one resistant bacterium among one million susceptible cells (10⁻⁶), exceeding the sensitivity of standard AST methods.

Beyond improved sensitivity, the microfluidic platform also reduced labor and costs. The assay required only a few hundred droplets rather than millions, minimised manual handling through automated imaging and computational analysis, and reduced technician hands-on time to less than one hour per isolate. The authors estimated that the platform could be approximately 1.5–2.5 times less expensive than PAP testing while providing faster results and greater scalability for routine clinical use.

By combining droplet microfluidics, automated microscopy, and digital image analysis, [Agnihotri et al. (2026)](https://www.nature.com/articles/s41746-026-02808-x) demonstrate a powerful new approach for detecting heteroresistance in clinically important pathogens. The method provides rapid, sensitive, and species-independent identification of rare resistant subpopulations that are often missed by conventional susceptibility testing. These findings highlight the potential of digital microfluidic diagnostics to improve antimicrobial stewardship, support earlier optimisation of antibiotic therapy, and advance precision medicine approaches for the management of bloodstream infections.

#### Data

- All the raw images used for analysis are available on [Figshare](https://doi.org/10.17044/scilifelab.31452181).
- Code used for the analysis is on [Zenodo](https://doi.org/10.5281/zenodo.18717330).

#### Article

DOI: [10.1038/s41746-026-02808-x](https://doi.org/10.1038/s41746-026-02808-x)

Agnihotri, S. N., Fatsis-Kavalopoulos, N., Vikdahl, E., Windhager, J., Corbat, A. A., Andersson, D. I., & Tenje, M. (2026). Droplet microfluidics with image texture quantification for detection of rare antibiotic-resistant subpopulations from bloodstream infections. npj _Digital Medicine_, **9(1)**, 410.
