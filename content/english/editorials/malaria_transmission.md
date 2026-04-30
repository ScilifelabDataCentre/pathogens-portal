---
title: "Mind the Gap: How high-resolution omics is transforming our understanding of malaria transmission biology"
date: 2026-04-23
summary: High-resolution omics approaches are uncovering critical bottlenecks in malaria transmission, providing new insights into host–parasite interactions and opportunities for next-generation interventions.
banner: /editorials/malaria_transmission.png
banner_caption: Visualisation depicting transmission cycle of the malarial parasite
tags:
  [
    Pathogens,
    Infectious disease,
    malaria,
    Plasmodium falciparum,
    transmission biology,
    host–parasite interactions,
    single-cell transcriptomics,
    spatial transcriptomics,
    gametocytes,
    liver stage infection,
  ]
editorials_topics: [Infectious Diseases]
editorials_authors: ["Johan Ankarklev, Ylva Veith, and Miren Urrutia Iturritza"]
images: [/editorials/malaria_transmission.png]
---

A pathogen’s success is defined by its capacity to survive, multiply, and transmit to new hosts. Malaria parasites (_Plasmodium_ _spp_) exemplify this particularly well, as their complex lifecycle requires them to constantly adapt between the human host and the _Anopheles_ mosquito vector - a strategy that has proven highly successful given the estimated 282 million annual infections. Despite major control strategies, malaria continues to persist across a large region of the world, where this devastating disease is still endemic in 85 countries, and causes over 600,000 deaths each year ([World Health Organization, 2025](https://iris.who.int/server/api/core/bitstreams/fb74be70-6749-40fd-a985-373fe0b3c949/content)).

Today, malaria control is heavily focused on keeping mosquitoes and humans apart through the use of insecticide-treated bed nets, indoor spraying, and other forms of vector control, as well as antimalarial drugs that have been used for decades ([Charavanamuttu _et al._, 2026](https://doi.org/10.3390/pathogens15020137)). These measures have saved millions of lives, but their effectiveness is under increasing pressure as resistance to both insecticides and antimalarial compounds continues to rise ([World Health Organization, 2025](https://iris.who.int/server/api/core/bitstreams/fb74be70-6749-40fd-a985-373fe0b3c949/content)). More recently, two WHO-recommended vaccines - RTS,S/AS01 and R21/Matrix-M - have added an important new layer of protection for young children, although the efficacy remains moderate and short lived ([RTS, S Clinical Trials Partnership, 2015](<https://doi.org/10.1016/S0140-6736(15)60721-8>), [Datoo _et al._, 2024](<https://doi.org/10.1016/S0140-6736(23)02511-4>)).

To build the next generation of malaria interventions, we need a better understanding of the host-parasite interplay during the transmission stages. This is the core objective of the Ankarklev Lab.

**What does transmission biology actually involve?**

Malaria infection is initiated by the bite of an infected mosquito which, during a blood meal, deposits parasites under the skin of a human host. From there, the parasites rapidly enter the circulatory system and travel to the liver, where they undergo a first massive round of replication while remaining clinically silent. Only after this obligatory differentiation and developmental stage can the parasites successfully enter the blood stage of infection, where they undergo asexual replication inside the erythrocytes. The repeated cycles of erythrocyte infections are what cause the characteristic symptoms of malaria — from fever and vomiting to anemia and, in severe cases, organ damage or death. While most parasites continue this asexual cycle, a small subset differentiates into gametocytes — the sexual stage, which is the only stage that can be taken up by a mosquito during a blood meal and continue development ([Bousema and Drakeley, 2011](https://doi.org/10.1128/cmr.00051-10)).

Through this lengthy journey, there are two instances where parasite numbers decrease dramatically: i) the pre-erythrocytic stage in the human, and ii) the transmission-stage from the human to the mosquito. These lifecycle stages represent biological bottlenecks, where only a small fraction of parasites thrive onwards. These bottlenecks are especially attractive targets for malaria control, because small parasite populations are easier to interrupt than the vast numbers generated during blood-stage infection, where parasites may reach the billions ([Brancucci _et al._, 2015](https://doi.org/10.1038/nprot.2015.072)).

In principle, interventions at these stages could stop an infection before it is established, prevent parasites from becoming transmissible, and avoid symptoms altogether ([Prudêncio _et al._, 2006](https://doi.org/10.1038/nrmicro1529), [Mohammed _et al._, 2023](https://journals.asm.org/doi/full/10.1128/spectrum.03671-22)). In practice, however, these same stages have long remained among the most difficult to study. They are brief, clinically silent, and composed of small, heterogeneous parasite populations that are easily missed by traditional experimental approaches. This is where new high-resolution omics and data-driven methods are transforming the field.

**A closer look at gametocytes - when malaria gets ready to transmit**

Transmission of the parasite to the mosquito relies on the differentiation of a small subset of blood stage parasites to become the gametocytes (precursor gametes). But gametocytes are not a single, uniform cell type; they emerge through a dynamic developmental process and diverge into distinct male and female lineages, each with its distinct molecular pathways.

Recent advances in single-cell transcriptomics have made it possible to resolve this complexity. In a series of studies from the Ankarklev Lab, we have characterised early _Plasmodium_ parasite development inside the _Anopheles_ mosquito ([Mohammed _et al._, 2023](https://journals.asm.org/doi/full/10.1128/spectrum.03671-22)) and the mosquito immune response ([Kwon _et al._, 2021](https://doi.org/10.7554/eLife.66192)) at single-cell resolution. In the most recent study, [Mohammed _et al._ (2024)](https://doi.org/10.1038/s41467-024-51201-3) mapped the transcriptional landscape of _Plasmodium falciparum_ gametocyte development at single-cell resolution, identifying distinct developmental trajectories and sex-specific programs. The work highlighted candidate regulatory factors, including members of the ApiAP2 transcription factor family, and suggested lineage-specific roles for genes involved in parasite structure and development, along with a panel of candidate genes involved in male and female sexual cell fate.

Importantly, we have made the data available through an interactive resource (which can be accessed [in a Shiny app](https://mubasher-mohammed.shinyapps.io/mohammedetal/)). Building on this foundation, the Ankarklev Lab is now adapting epigenomic approaches to ask not only which genes are active in specific gametocyte lineages, but how those lineages are established and regulated.

**The hidden bottleneck in the liver… not so hidden?**

The clinically silent liver stage of malaria infection is difficult to study because only a small number of parasites successfully establish infection, and they do so within a large, structurally complex organ.

This is where omics technologies are beginning to change the picture. In the Ankarklev Lab, we first optimised spatial transcriptomics for studies of the liver, creating a computational framework to resolve liver zonation and tissue architecture at high resolution ([Hildebrandt _et al._, 2021](https://doi.org/10.1038/s41467-021-27354-w)). We then applied this approach to _Plasmodium_\-infected livers, combining spatial transcriptomics with single-nuclei RNA sequencing to map host–parasite interactions across space and time ([Hildebrandt _et al._, 2024](https://doi.org/10.1038/s41467-024-51418-2)). This revealed localised changes in lipid metabolism around infection sites, distinct inflammatory programs across the metabolic liver zones, and previously unrecognised “inflammatory hotspots” - aggregates of immune cells. These findings, together with work from other groups, indicate that the liver stage is not truly silent, but actively sensed by the host immune system — a shift in perspective that we have recently reviewed in [Quin _et al._ (2025)](https://doi.org/10.1016/j.pt.2025.10.007).

As these datasets grow in scale and complexity, a new challenge emerges: how to integrate and interpret them. To address this, we are developing data-driven tools such as the Liver ITA resource ([Quin _et al._, 2025](https://doi.org/10.1101/2025.03.17.643687)), which utilises and integrates liver transcriptome datasets, across both disease states and species, into an interactive gene network. This approach allows researchers to define novel genes and pathways of interest, gene–gene interactions and regulatory programs, in an unsupervised manner - by avoiding bias in knowledge-based resources such as GO and KEGG. Together with the SciLifeLab Data Centre, we are currently making this resource available to the broad liver research community.

**Resolving the remaining questions**

Halting malaria transmission will require more than mosquito control. It will require a much deeper understanding of host-parasite interaction linked to parasite persistence and transmission. Outstanding key questions include parasite survival and immune mechanisms that lead to sterile immunity in the liver, how protective immunity can more effectively be induced in risk groups in malaria endemic regions, how gametocyte development and sexual cell fate are regulated, and thereby how transmission to the mosquito can successfully be inhibited. High-resolution omics technologies coupled with advancements in data-driven approaches are much needed tools to help bridging these knowledge gaps.
