---
title: "(Micro)bioterrorism: leveraging genomic data to improve anthrax surveillance"
date: 2024-04-03
summary: A perspective on Bacillus Anthracis, a pathogen known as a biological threat,  and how WGS data and surveillance can help researchers respond to cases, and threats.
banner: /editorials/topic_infectious_disease.jpg
banner_caption: 'Splenic tissue from a monkey with inhalation anthrax, showing a red blood cell (red) and rod-shaped bacilli (yellow). (Credit: Arthur Friedlander)'
tags:
  [
    pathogens,
    Bacillus Anthracis,
    WGD data,
    preparedness,
    health threat
  ]
editorials_topics: [Infectious diseases]
editorials_authors: [Laura Carroll]
images: [/editorials/topic_infectious_disease.jpg]
---

### What is anthrax?

Anthrax is a serious, life-threatening infectious disease, which is caused by a rod-shaped bacterium called *Bacillus anthracis* ([CDC, 2024a](https://www.cdc.gov/anthrax/basics/index.html)).
*B. anthracis* is arguably most well-known for its previous use as a biological weapon and bioterrorism agent ([CDC, 2024b](https://www.cdc.gov/anthrax/bioterrorism/threat.html); [Wagar, 2015](https://journals.asm.org/doi/10.1128/cmr.00033-15)).
However, in some parts of the world, *B. anthracis* naturally resides in soil, where it can form highly resilient spores capable of withstanding harsh environmental conditions ([CDC, 2024a](https://www.cdc.gov/anthrax/basics/index.html); [Mock and Fouet, 2001](https://www.annualreviews.org/doi/10.1146/annurev.micro.55.1.647)).
Wild and domestic animals (livestock that graze, in particular; e.g., cattle, goats, sheep) can become infected by ingesting or inhaling *B. anthracis* spores present in soil, water, and other natural environments ([CDC, 2024a](https://www.cdc.gov/anthrax/basics/index.html); [FDA, 2024](https://www.fda.gov/vaccines-blood-biologics/vaccines/anthrax)).
Anthrax cases among humans can occur when *B. anthracis* spores enter the body (e.g., by inhaling or ingesting spores, or when spores come in contact with a cut or lesion); as such, people who interact with infected animals or animal products have an increased risk of exposure ([CDC, 2024a](https://www.cdc.gov/anthrax/basics/index.html); [FDA, 2024](https://www.fda.gov/vaccines-blood-biologics/vaccines/anthrax); [CDC, 2024c](https://www.cdc.gov/anthrax/transmission/index.html)).

### Bacillus anthracis: the original anthrax-causing pathogen

For over a century, *B. anthracis* has been known to be a causative agent of anthrax.
In 1876, scientist Robert Koch demonstrated that *B. anthracis*, when injected into animals, caused disease ([CDC 2024d](https://www.cdc.gov/anthrax/basics/anthrax-history.html); [Blevins and Bronze, 2010](https://www.sciencedirect.com/science/article/pii/S1201971210023143); [Koch, 1876](https://edoc.rki.de/handle/176904/5139)).
Not only did his studies provide insight into *B. anthracis* biology, but they were the first to link a specific bacterium to a specific disease ([Blevins and Bronze, 2010](https://www.sciencedirect.com/science/article/pii/S1201971210023143)).
Further, Koch's work with *B. anthracis* led to the publication of what are now famously known as Koch's Postulates, which serve as formal criteria for establishing a causal relationship between a microbe and a disease ([CDC 2024d](https://www.cdc.gov/anthrax/basics/anthrax-history.html)).

Since Koch's discoveries in the late 1800s, research into *B. anthracis* biology and pathogenesis has led to numerous breakthroughs in anthrax prevention and treatment ([CDC 2024d](https://www.cdc.gov/anthrax/basics/anthrax-history.html)).
Several anthrax vaccines have been developed for both humans and animals, and improvements in anthrax treatment (e.g., antibiotics, anthrax antitoxins) have led to better patient outcomes ([CDC 2024d](https://www.cdc.gov/anthrax/basics/anthrax-history.html); [Person, et al., 2022](https://academic.oup.com/cid/article/75/Supplement_3/S392/6762174)).
However, these breakthroughs are often overshadowed by the use of *B. anthracis* as a bioweapon, with the first documented case occurring during World War I ([CDC 2024d](https://www.cdc.gov/anthrax/basics/anthrax-history.html)).

### "Bacillus cereus" biovar Anthracis: a new type of anthrax

Over 100 years after Koch linked *B. anthracis* to anthrax, researchers at the U.S.
Centers for Disease Control and Prevention (CDC) discovered a novel pathogen capable of causing anthrax-like illness ([Hoffmaster, et al., 2004](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC420414/)).
Later termed "*Bacillus cereus*" biovar Anthracis ([Klee, et al., 2006](https://journals.asm.org/doi/full/10.1128/jb.00303-06); [Antonation, et al., 2016](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5015827/); [Carroll, et al., 2020](https://journals.asm.org/doi/full/10.1128/mbio.00034-20)), this novel pathogen resembled a completely different species, "*Bacillus cereus*", but was able to cause anthrax-like disease like *B. anthracis* ([Hoffmaster, et al., 2004](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC420414/); [Klee, et al., 2006](https://journals.asm.org/doi/full/10.1128/jb.00303-06)).

Since its discovery in 2004, "*B. cereus*" biovar Anthracis has been responsible for several other cases of severe, anthrax-like illness among humans and animals, several of which resulted in fatalities ([Baldwin, 2020](https://www.frontiersin.org/articles/10.3389/fmicb.2020.01731/full)).
Notably, using whole-genome sequencing (WGS), scientists have revealed that "*B. cereus*" biovar Anthracis strains are incredibly diverse, indicating that different strains--and even species--have acquired the ability to cause anthrax; as a result, novel approaches must be developed to prepare for the emergence of novel anthrax-causing pathogens ([Carroll, et al., 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9413466/)).

### Combating anthrax with genomic data

Due to their severity and bioterrorism potential, anthrax-causing *B. anthracis* and "*B. cereus*" biovar Anthracis represent severe global public health threats.
To prepare for potential emergencies, scientists are taking proactive, data-driven approaches.
Specifically, laboratories around the world are routinely using WGS to query the genomes of anthrax-causing bacteria.
This WGS data is deposited in public databases (e.g., the National Center for Biotechnology Information \[NCBI\] databases; ([https://www.ncbi.nlm.nih.gov/](https://www.ncbi.nlm.nih.gov/)), often alongside metadata conveying when, where, and how the anthrax-causing strain was isolated ([Ramnath, et al., 2023](https://www.biorxiv.org/content/10.1101/2023.12.20.572685v1.full)).

WGS data and metadata derived from anthrax-causing pathogens have tremendous potential to be utilized within the realms of public health and emergency preparedness.
Specifically, WGS-based pathogen surveillance tools are allowing scientists to monitor pathogens in close to real-time ([Gardy and Loman, 2018](https://www.nature.com/articles/nrg.2017.88)).
This (meta)data can be used to identify and resolve outbreaks sooner, leading to better public health outcomes and lower burdens of illness ([Gardy and Loman, 2018](https://www.nature.com/articles/nrg.2017.88); [Ramnath, et al., 2023](https://www.biorxiv.org/content/10.1101/2023.12.20.572685v1.full)).
We envision that similar methods can be used for anthrax-causing pathogens.
For example, routine WGS of bacilli can allow public health officials to rapidly identify novel, emerging anthrax-causing pathogens, facilitating faster response times and minimizing the number of human illness cases ([Ramnath, et al., 2023](https://www.biorxiv.org/content/10.1101/2023.12.20.572685v1.full)).
Overall, whether the culprit is *B. anthracis*, "*B. cereus*" biovar Anthracis, or a yet-unknown anthrax-causing pathogen, WGS has the potential to help public health officials and clinicians prepare for and respond to illness cases, outbreaks, and bioterrorism attacks.


#### Cite this editorial

Carroll, L. (2024). Editorial- (Micro)bioterrorism: leveraging genomic data to improve anthrax surveillance. Online resource. DOI: [10.17044/scilifelab.25547476](https://doi.org/10.17044/scilifelab.25547476).
