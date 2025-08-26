---
title: "Integrative Outbreak Simulation: A One Health Approach for Enhanced Pandemic Preparedness"
category: "test"
banner: "/resources_thumbs/nanopore_seq_cropped.jpg"
resource_info:
  name: "Integrative Outbreak Simulation: A One Health Approach for Enhanced Pandemic Preparedness"
  pi: René Kaden
  host_organisation: Uppsala University Hospital/Akademiska Sjukhuset Clinical Microbiology, Dept. of Medical Sciences, Uppsala University
  contact: "René Kaden<br>Uppsala University Hospital/Akademiska Sjukhuset Clinical Microbiology, Dept of Medical Sciences, Uppsala University<br>Email: [rene.kaden@medsci.uu.se](mailto:rene.kaden@medsci.uu.se) or [rene.kaden@akademiska.se](mailto:rene.kaden@akademiska.se)"
for_background_table:
  pi: René Kaden
  pi_affiliation: Uppsala University
  lab: Uppsala University Hospital
plotly: true
---

This collaborative project, including 6 PLP partners, the National Veterinary Institute (SVA), and the Swedish Defence Research Agency (FOI) (see the [full list of participants](#list-of-participants) below), is designed to simulate an outbreak scenario by dispatching clinical samples that are spiked with unusual microorganisms to the contributing clinical microbiology laboratories. These samples are delivered in a manner that facilitates enrichment and mimick authentic patient and wastewater samples. The scenarios may encompass complex, potentially zoonotic outbreaks, thus embracing the One Health concept by engaging partners from both human and animal health.

All project phases will be meticulously documented, and progress updates on the outbreak scenario will be shared via the Swedish Pathogens Portal. This approach ensures real-time project monitoring and public accessibility to information.

The primary objectives include assessing response times and the laboratory's capacity to detect and identify the pathogen, developing diagnostic methods, treatment recommendations, but also scaling up sequencing, bioinformatics, and investigate storage capacities at the National Pandemic Center (NPC). The project leverages the synergistic effects of collaborations between laboratories. Participating laboratories will receive samples in a time series, emulating a natural pathogen distribution.

The project serves to evaluate pandemic preparedness effectiveness and identify areas for potential enhancement. Through these concerted efforts, this initiative aims to strengthen our collective capacity to respond swiftly and effectively to emerging infectious threats.

##### Outcomes

###### Summary of the sequence of events

- *Weeks 33–38:* Samples for the project were prepared.
- *Week 39 (Sept 23–29):* Samples were sent out and held by the delivery company until October 2nd (13:00), and were delivered to labs with case information.
- *Weeks 39–41 (Oct 2–21):* Labs tested the first set of samples, logging activities chronologically. The testing deadline was October 21 (8:00).
- *23rd Oct 2024:*  Stage 1 Discussion Meeting. Analysis methods and procedures were discussed and compared.
- *Week 41 (Oct 21–27):* Second set of samples, sent out on October 23 (13:00).
- *Weeks 42–44 (Oct 23–Nov 4):* Labs tested the second set of samples, logging their activities chronologically. The deadline was November 4 (8:00).
- *Week 47 (26th Nov):* Stage 2 Discussion Meeting. Analysis methods and procedures were discussed and compared.

The labs recorded their procedures chronologically in a pre-prepared log template.
The granularity of data which labs could share was limited by data governance regulation.
All the labs received different samples and their analysis methods remained unique to address the sample.
During the first phase of the outbreak simulation the labs were given an unidentified sample for pathogen identification, the analysis time varied from 6 days to 26 days with an average of 14 days.
The second phase included testing a larger sample size of unidentified samples to deduce and group them based on results, the analysis time was between 12 days to 26 days with an average of 12 days. 

The different analysis methods used during the course of pathogen identification were reported as:

- Incubation/Cultivation
- RNA and DNA Extractions
- Nanopore Squencing, Amplicon sequencing, RNA Immunoprecipitation Sequencing (RIP-seq), Sequencing
- Metagenomics
- Matrix-assisted laser desorption/ionization
- Risk Assessment
- Technical and Medical Assessment
    
The pathogens identified during the outbreak simulation were reported as *Christensenella hongkongensis* by Lab 2 and *Catabacter hongkongensis* by Lab 3.
These names refer to the same species, as they have been recognised as synonyms due to taxonomic reclassification.

###### Lab activities visualisations: Phase 1

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 800px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/PLP-TEST-labs-analysis-phase-1.json" height="550px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/PLP/PLP-TEST-labs-analysis-phase-1.py).


###### Lab activities visualisations: Phase 2

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 800px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/PLP-TEST-labs-analysis-phase-2.json" height="550px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/PLP/PLP-TEST-labs-analysis-phase-2.py).

##### Research findings:

Detecting pathogens directly from blood samples proved to be more difficult than expected. Pathogens are typically present in extremely low concentrations, making it statistically unlikely to capture even a single cell when extracting DNA from a standard extraction volume of a 200 µl blood sample.

Additionally, blood culture bottles may contain chemicals that inhibit DNA extraction or interfere with sequencing steps. In the second phase of the study, EDTA tubes with 4 ml of blood and a higher sample extraction volume was used. While this improved detection rates, blood remains a challenging sample type for comprehensive metagenomic pathogen analysis. Further research is necessary to develop effective methods that enhance pathogen detection from blood, leading to better diagnostic tools. 

A centralized follow up of all results and data requires a reporting standard. This needs to be
developed in future.

##### Impact on prepardness for future pandemics:

The next epidemic or pandemic could be caused by an unexpected pathogen, making it impossible to predict which clinical samples will be most relevant for diagnosis. To ensure preparedness, reliable detection methods must be available for a wide range of sample types.

Our project focused on blood, driving significant advancements in metagenomic analysis for pathogen detection. However, many other sample types, such as respiratory secretions, stool, or tissue samples, also require further method development to ensure accurate and efficient microbia detection. Strengthening diagnostic capabilities across diverse sample types will enhance early detection, improve patient outcomes, and bolster global readiness for future infectious disease
outbreaks.

##### List of participants:

In total, there are 11 participants in 12 institutes:

- Akademiska Sjukhus Uppsala
- Clinical Genomics Stockholm (SciLifeLab infrastructure unit)
- Clinical Genomics Umeå (SciLifeLab infrastructure unit)
- Clinical Genomics Örebro (SciLifeLab infrastructure unit)
- Karolinska Institute (P3 facility)
- KTH Royal Institute of Technology
- Linköping University Hospital
- National Pandemic Centre (NPC)
- National Veterinary Institute (SVA)
- Swedish Defence Research Agency (FOI)
- Swedish Pathogens Portal
- Swedish University of Agricultural Sciences (SLU)