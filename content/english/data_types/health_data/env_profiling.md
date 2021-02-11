---
title: Environmental virus profiling data, SciLifeLab/KAW projects
toc: false
menu:
    main:
        identifier: env_profiling
        parent: health_data
        weight: 20
---

Because the genome of the coronavirus can be found in the feces of patients with COVID-19, it is possible to follow the infection in the population through so-called wastewater-based epidemiology. This is done by looking at the amount of the virus genome present in the wastewater, measured using PCR techonology. Samples are periodically taken at a wastewater treatment facility, allowing to make comparisons of the viral load over time. It has been shown that the virus content in wastewater can predict increases in infection in the population and follows the epidemic trend measured by the number of COVID-19 cases and hospitalization rate (see Peccia et al. 2020, *Nat. Biotechnol.*, DOI: [10.1038/s41587-020-0684-z](https://doi.org/10.1038/s41587-020-0684-z)).

Note that because different sample collection and data analysis methods are used in different research projects (i.e., in different cities), it is not possible to make comparisons of viral load across projects (i.e., across cities). Comparisons are supposed to made within each project (i.e., city) since the methodology remains across different weeks of measurement.

## Viral load in wastewater treatment facilities in Uppsala

<div class="container my-4 ml-4"><div class="row"><img src="/env_profiling/uppsala_vatten_logo.jpg" alt="Uppsala Vatten" height="50" class="mr-4"><img src="/env_profiling/slu_logo.png" alt="SLU, Swedish University of Agricultural Sciences" height="60" class="mr-4"></div></div>

This project is run by Anna J. Székely (SLU, Swedish University of Agricultural Sciences) in collaboration with Uppsala Vatten. The amount of SARS-CoV-2 virus in the wastewater is measured in two wastewater treatment facilities in Uppsala city: one that processes water in the south-western part of city ('AB'), the other processes wastewater in the north-eastern part of the city ('C'). Please [consult this map for the exact sources of wastewater in each treatment facility](/env_profiling/avrinningskarta_inlopp_kungsangsverket.pdf). Measurements are taken one day a week, with several measurements taken during that day. A single score is calculated for that day per facility taking into account the flow of water at every measurement. A combined measure based on results from both facilities is calculated as well.

Note that the scores provided in this dataset and depicted in plots are preliminary. The team is still conducting method efficiency checks that might slightly modify the final results.

[Dowload the data: mean and SD per treatment facility and overall per week, CSV file](#)  

**Principal investigator:** Anna J. Székely, SLU, Swedish University of Agricultural Sciences.  
**Contact:** anna.szekely@slu.se

##### Wastewater treatment facility AB, south-western part of Uppsala

<div class="d-lg-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div id="uppsala_ab"></div>
</div>

##### Wastewater treatment facility C, north-eastern part of Uppsala

<div class="d-lg-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div id="uppsala_c"></div>
</div>

##### Wastewater treatment facilities in Uppsala combined

<div class="d-lg-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div id="uppsala_combined"></div>
</div>

{{< env_profiling_method_pubs city="uppsala" >}}

## Viral load in wastewater treatment facilities in Stockholm

Description of the project.. [...]

**Principal investigator:** X X  
**Contact:** x.x@x.se

{{< env_profiling_method_pubs city="stockholm" >}}

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.12.2"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/6ca12c9d3d0b4c838441a67b65751c54.js?id=uppsala_combined"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/2cdc7dfbb44a47fd9ca027767913cafa.js?id=uppsala_ab"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/1aa540b5f5c3491eb2413b876c52bba8.js?id=uppsala_c"></script>
