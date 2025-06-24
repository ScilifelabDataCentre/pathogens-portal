---
title: Automated SARS-CoV-2 Nanopore Sequencing Analysis for Pandemic-Scale Diagnostics
date: 2025-06-24
summary: Researchers from Uppsala University Hospital, developed and validated two automated workflows within the GUI-based software Geneious Prime 2022.1.1. Validation data and tools are openly available via GitHub and the Sequence Read Archive.
banner: /highlights/banners/nanopore_sequencing.png
banner_large: /highlights/banners/nanopore_sequencing.png
banner_caption: "Source: Figure 4 of Cumlin et al. 2024"
highlights_topics: [COVID-19, Infectious diseases]
tags: [SARS-CoV-2 genome sequencing , Single nucleotide variant (SNV) detection , Oxford Nanopore Technology (ONT) , National pathogen surveillance, Outbreak response infrastructure]
images: [/highlights/banners/drug_repurposing_small.jpeg]
---

The global COVID-19 pandemic exposed key bottlenecks in the ability of health systems to rapidly process and interpret pathogen [genomic](https://www.genome.gov/about-genomics/fact-sheets/A-Brief-Guide-to-Genomics) data. Although command-line bioinformatics pipelines enabled automation and high-throughput [SARS-CoV-2](https://www.cancer.gov/publications/dictionaries/cancer-terms/def/sars-cov-2) genome analysis, their reliance on programming expertise limited their adoption in many diagnostic and clinical labs. As sequencing data became central to understanding viral evolution and guiding public health interventions, there emerged a critical need for tools that were powerful yet accessible to users without coding backgrounds.

[Oxford Nanopore Technology](https://www.nature.com/articles/s41587-021-01108-x) (ONT) has gained recognition for its capacity to deliver long-read sequencing data cost-effectively and with short turnaround times—making it suitable for real-time outbreak tracking. However, many ONT data analysis pipelines (e.g., Artic, NanoCoV19, Viralrecon) remained confined to command-line environments. Bridging this usability gap, graphical user interface (GUI) software such as [Geneious Prime](https://www.geneious.com/features/prime) emerged as a promising platform to empower lab personnel with limited bioinformatics training to perform complex sequencing analyses efficiently.

The research aimed to develop automated, plugin-based workflows that allow users to perform SARS-CoV-2 ONT sequencing analysis—including consensus generation and phylogenetic assignment—without requiring programming skills. The workflows are designed to be modular, cross-platform, and adaptable for future pathogen outbreaks.

Two validated workflows were developed:

- SARS-CoV-2_Assembly_Basic: Performs trimming, alignment, consensus sequence generation, and annotation of ONT data.
- SARS-CoV-2_Assembly_WrapperPlugins: Enhances the basic workflow by integrating pangolin and Nextclade as plugins for real-time lineage assignment.

Validation was performed using 96 clinical samples and benchmarked against results from the web interfaces of pangolin and Nextclade, showing 100% concordance. The automated workflow reduced hands-on time and simplified analysis across Linux, macOS, and Windows. Visual inspection features within Geneious Prime enabled mutation tracking and quality control, with real-world use in Sweden’s national surveillance programme.

> "By embedding SARS-CoV-2 sequencing workflows within Geneious Prime, we aimed to eliminate the bioinformatics barrier in clinical diagnostics. These tools empower local labs to contribute to global surveillance efforts without needing in-house programming expertise—supporting real-time response in both ongoing and future pandemics."
— Authors

The development and deployment of GUI-based, plugin-supported workflows for SARS-CoV-2 sequencing data address a pressing gap in pandemic preparedness infrastructure. Their adoption within Uppsala University Hospital and integration into Sweden’s national surveillance program illustrates their utility at scale. Beyond SARS-CoV-2, the modular design allows adaptation to other pathogens by altering primers and reference genomes—positioning this toolset as a flexible resource for future outbreaks, mutation surveillance, and antimicrobial resistance tracking. These workflows exemplify how democratized data analysis—via intuitive platforms—can advance the goals of data platforms and pathogen portals: enhancing global collaboration, reducing diagnostic inequity, and enabling timely public health action.


#### Data

Workflows available at [Github](https://github.com/clinical-genomics-uppsala/Geneious_SARS-CoV-2) (accessed on 5 May 2024). Sequence test data for workflow validation available at NCBI (Accession number PRJNA1048178). Instruction videos available at the research group’s YouTube channel (@EpiTaxEvo). Informed consent was obtained from all subjects involved in the study. All raw data processing was conducted in a clinical setting for method development. This study used only existing sequence data, with all consensus files having been made publicly available beforehand.

#### Article

DOI: [10.3390/ijms25126645](https://doi.org/10.3390/ijms25126645)

Cumlin, T., Karlsson, I., Haars, J., Rosengren, M., Lennerstrand, J., Pimushyna, M., ... & Kaden, R. (2024). From SARS-CoV-2 to Global Preparedness: A Graphical Interface for Standardised High-Throughput Bioinformatics Analysis in Pandemic Scenarios and Surveillance of Drug Resistance. **International Journal of Molecular Sciences, 25(12)**, 6645.

#### Funding

This research was funded by: (1) Wallenberg foundation (KAW 2020.0241) ‘High throughput SARS-CoV-2 variants surveillance’ (Lars Feuk, Rene Kaden) and (2) Gullstrand foundation (ALF-938076): ‘Development, evaluation and implementation of molecular epidemiological source tracing methods and variant surveillance’ (Rene Kaden).