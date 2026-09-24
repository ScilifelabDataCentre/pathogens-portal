---
title: Investigating growth interactions in the human gut microbiome
date: 2026-09-24
summary: Systematic profiling of human gut bacteria reveals predominantly inhibitory growth interactions, although some factors did promote growth.
banner: /highlights/banners/growth_interaction.png
banner_large: /highlights/banners/growth_interaction.png
banner_caption: "Figure 1 from Buyanbadrakh et al. (2026)"
highlights_topics: [Infectious diseases]
tags:
  [
    Human gut microbiome,
    microbial interactions,
    gut bacteria,
    microbial community composition,
    interspecies interactions,
    Veillonella parvula,
    Parabacteroides merdae,
    extracellular vesicles,
    environmental pH,
    microbial cross-feeding.
  ]
images: [/highlights/banners/growth_interaction.png]
---

The human gut microbiome is a complex microbial ecosystem in which hundreds of bacterial species interact with one another and their surrounding environment. These interactions can determine which species successfully colonise the gut and influence the stability and resilience of the microbial community. Bacteria can compete for nutrients, release inhibitory compounds, exchange metabolites, or modify environmental conditions, such as pH. Understanding these interactions is therefore important for predicting microbiome composition and, ultimately, developing approaches to manipulate microbial communities.

[Buyanbadrakh _et al._ (2026)](https://www.nature.com/articles/s41467-026-76526-z) systematically investigated growth interactions among 36 representative bacterial strains from the human gut microbiome, spanning six major bacterial phyla. A spent-medium approach was used, in which each bacterial strain was first grown for 24 hours before the cell-free spent medium was collected. Each strain was subsequently grown in the spent medium produced by every other strain, and bacterial growth was monitored for 48 hours by measuring optical density. This resulted in a large-scale dataset comprising 1,224 binary growth interactions.

The interaction map revealed that inhibitory interactions were considerably more common than growth-promoting interactions. Using a two-fold change in growth as the threshold, 307 interactions (25.1%) were inhibitory, whereas only 51 (4.2%) promoted bacterial growth. When nutrients were replenished in the spent medium, inhibitory interactions decreased more than eight-fold, from 307 to 38. This suggests that many negative interactions arise from nutrient depletion or environmental changes caused by bacterial growth, rather than from the production of specific antimicrobial compounds. In contrast, nearly half of the growth-promoting interactions persisted after nutrient replenishment, suggesting that metabolic cross-feeding may contribute to some positive interactions.

One particularly interesting positive interaction involved _Clostridium perfringens_ and _Mediterraneibacter gnavus_. The growth of _M. gnavus_ increased in spent medium produced by _C. perfringens_. Proteomic analysis indicated changes in nucleotide-related pathways, prompting the researchers to investigate how _C. perfringens_ might provide growth-promoting components. They found extracellular vesicles in the _C. perfringens_ spent medium and demonstrated that an isolated vesicle fraction increased _M. gnavus_ growth approximately 1.4-fold. The growth-promoting effect disappeared after heat treatment of the vesicles, indicating that vesicle integrity or heat-sensitive components carried within them are important for the interaction. The experiments therefore identify extracellular vesicles as a mechanism through which one gut bacterial species can promote the growth of another.

Environmental pH emerged as another major determinant of bacterial interactions. Across the dataset, lower spent-medium pH was associated with poorer bacterial growth, although the strength of this relationship differed among bacterial groups. Importantly, the researchers could reasonably predict the growth response of individual strains from the pH of the spent medium alone. When the pH of selected spent media was experimentally restored to pH 7, most inhibitory interactions became neutral. Together, these findings indicate that bacterial acidification of the local environment can itself act as an important mechanism of interspecies growth inhibition.

The researchers subsequently identified _Veillonella parvula_ as having an unusual role in these pH-dependent interactions. Unlike many of the other bacteria examined, _V. parvula_ was able to increase environmental pH, particularly under acidic conditions. When grown at an initial pH of 5, _V. parvula_ increased the medium pH by 0.85 units. This ability had consequences for other bacteria: _Parabacteroides merdae_, which is sensitive to acidic conditions, showed impaired growth in acidified _Streptococcus parasanguinis_ spent medium. However, after _V. parvula_ increased the pH of this medium from approximately 5.8 to 6.2, _P. merdae_ growth was restored to levels similar to those observed in rich medium.

Proteomic and metabolomic analyses provided further insight into the mechanism underlying this effect. When _V. parvula_ was exposed to _S. parasanguinis_ spent medium, proteins involved in arginine biosynthesis and purine metabolism, including guanine deaminase, changed in abundance. Supplementing the medium with guanine enhanced both _V. parvula_ growth and its ability to increase environmental pH, particularly under acidic conditions. The authors suggest that the effect may be associated with changes in purine metabolism and the consumption of extracellular organic acids, although the precise molecular mechanism remains to be established.

To determine whether this pH-modulating behaviour was relevant in more complex microbial communities, the researchers assembled three-species communities containing the acid-sensitive _P. merdae_, _V. parvula_, and one of several phylogenetically diverse acidifying bacteria. Across these communities, acidifying strains reduced _P. merdae_ growth and lowered environmental pH. Adding _V. parvula_, however, consistently increased the pH and promoted _P. merdae_ growth. Guanine supplementation further strengthened this effect in most of the tested communities. The study illustrates community-level relationships, showing how a relatively low-abundance species can alter the chemical environment and indirectly support another bacterial species.

These findings are particularly interesting because _V. parvula_ is reported to occur in more than half of human gut microbiomes but generally represents less than 1% of the bacterial population. The study therefore suggests that even relatively low-abundance microorganisms may have important ecological effects by modifying their local environment. By increasing pH, _V. parvula_ could potentially create local conditions that favour acid-sensitive bacteria and thereby influence microbiome composition. However, because the experiments were conducted _in vitro_ using rich medium, the authors note that further work is required to determine the extent to which these local pH effects occur within the spatially organised and physiologically buffered environment of the human gut.

By systematically mapping interactions among human gut bacteria and investigating their molecular mechanisms, [Buyanbadrakh _et al._ (2026)](https://www.nature.com/articles/s41467-026-76526-z) demonstrate that microbial community structure is shaped not only by competition for resources but also by mechanisms such as extracellular-vesicle-mediated growth promotion and modification of environmental pH. The resulting interaction dataset provides a framework for predicting microbial community composition and highlights how mechanistic understanding of species-species interactions could eventually support rational strategies for manipulating gut microbial communities.

#### Data

- Raw growth data can be found on [Zenodo](https://zenodo.org/records/17456178) or in the supplementary data section.
- The mass spectrometry proteomics data have been deposited to the ProteomeXchange Consortium via the PRIDE partner repository with the dataset identifier [PXD070029](https://www.ebi.ac.uk/pride/archive/projects/PXD070029).
- The mass spectrometry metabolomics data have been deposited to MassIVE with the dataset identifier [MSV000102556](https://massive.ucsd.edu/ProteoSAFe/dataset.jsp?accession=MSV000102556).

#### Code

The code to reproduce the growth assay data analysis is available on [GitHub](https://github.com/mateuslab-prot/SpeciesSpeciesInteractions).

#### Article

DOI: [10.1038/s41467-026-76526-z](https://www.nature.com/articles/s41467-026-76526-z)

Buyanbadrakh, B., Baland, E., Lambeck, P., Pérez Jiménez, L., Holmberg, S. M., Puértolas-Balint, F., Toh, E., Wai, S. N., Schroeder, B. O., Ramstedt, M., Zhu, S., & Mateus, A. (2026). Systematic profiling of growth interactions in human gut microbiome species. _Nature Communications_, **17**, 8012.
