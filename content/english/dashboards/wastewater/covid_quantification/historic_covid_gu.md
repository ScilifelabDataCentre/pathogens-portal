---
title: Historic SARS-CoV-2 data from Gothenburg
plotly: true
aliases:
  - /dashboards/wastewater/historic_covid_gu/
---

This page shows historic wastewater epidemiology data related to SARS-CoV-2 that was collected in Gothenburg, Sweden. The data was collected by the group led by Professor Helene Norder (University of Gothenburg, GU), supported by co-workers from the University of Gothenburg and Sahlgrenska University Hospital (Hao Wang, Marianela Patzi Churqui, Timur Tunovic, Fredy Saguti, and Kristina Nyström). The data shown on this page was collected between week 7 of 2020, and week 43 of 2023 (i.e. between 10th February 2020 and 23rd October 2023). The group started to use a new method from week 20 of 2023. Data produced using this new method continues to be updated approximately weekly, and is available on the ['Amount of SARS-CoV-2 in wastewater (GU)' page](/dashboards/wastewater/covid_quantification/covid_quant_gu/).

## Wastewater collection sites

Influent wastewater samples were collected from Ryaverket wastewater treatment plant (WWTP) in Gothenburg by Lucica Enache at Ryaverket, Gryaab AB, Gothenburg. Wastewater sample collection began on February 10th (week 7) of 2020. Ryaverket WWTP receives wastewater from the households of more than 790,000 residents of Gothenburg, as well as from industry in the area. Wastewater is also received from residents and industry in surrounding municipalities, including Ale, Härryda, Kungälv, Lerum, Mölndal, and Partille, as well as storm and snow-melt water from older parts of Gothenburg. The amount of wastewater from households remains relatively consistent throughout the year. However, the amount of wastewater overall can be affected by the weather (with higher precipitation resulting in greater amounts). More information about the sample location, sample week, volume, and influent wastewater flow, is available in [Wang _et al._ (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/).

### Visualisation

<div class="alert alert-info">Last updated: 2023-11-17</div>

_The blue block on the graph indicates the period where sample collection was not completed (week 45 2022 - week 2 2023)._

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

 <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/historic_wastewater_gothenburg.json" height="550px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/gothenburg_covid.py).

## Commentary from the research group

<div><b>Date:</b> 2023-11-07<br><b>Commentary:</b>There are still low amounts of SARS-CoV-2 in Gothenburg's wastewater. However, there was a small increase in weeks 41, 42, and 43 but there are still low levels.</div>

{{< ww_dynamic_content >}}

### Dataset

**Download the data:** [Quantification of SARS-CoV-2 and enteric viruses in wastewater](https://blobserver.dc.scilifelab.se/blob/wastewater_data_gu_allviruses.xlsx). Results are available for SARS-CoV-2 from week 7 of 2020 (with a small gap over winter 2022-2023), and for enteric viruses from week 2 of 2023. The last data entry is week 43 of 2023 for both types of data.

**Contact:** <helene.norder@gu.se>

**How to cite the dataset:** Norder, H., Nyström, K. Patzi Churqui, M., Tunovic, T., Wang, H. (2023). Detection of SARS-CoV-2 and other human enteric viruses in wastewater from Gothenburg. [https://doi.org/10.17044/scilifelab.22510501](https://doi.org/10.17044/scilifelab.22510501).

**How to cite method:**
Saguti, F., Magnil, E., Enache, L., Churqui, M.P., Johansson, A., Lumley, D., Davidsson, F., Dotevall, L., Mattsson, A., Trybala, E., Lagging, M., Lindh, M., Gisslen, M., Brezicka, T., Nystrom, K. and Norder, H. (2021). Surveillance of wastewater revealed peaks of SARS-CoV-2 preceding those of hospitalized patients with COVID-19. [https://doi.org/10.1016/j.watres.2020.116620](https://doi.org/10.1016/j.watres.2020.116620).

Wang, H., Churqui, M.P., Tunovic, T., Enache, L., Johansson, A., Karmander, A., Nilsson, S., Lagging, M., Andersson, M., Dotevall, L., Brezicka, T., Nystrom, K. and Norder, H. (2022). The amount of SARS-CoV-2 RNA in wastewater relates to the development of the pandemic and its burden on the health system. [https://doi.org/10.1016/j.isci.2022.105000](https://doi.org/10.1016/j.isci.2022.105000).

## Methods

Samples of wastewater were collected using a fixed-site sampler that collected 30ml per 10,000m<sup>3</sup> of the incoming wastewater. For the purposes of analysis, seven samples (each representing a 24 hour period) were pooled to create a weekly sample. The weekly sample, which consisted of 1.5-15l of wastewater (depending on the flow) was sent to the Clinical Microbiology Laboratory at Sahlgrenska University Hospital for analysis. Analyses were conducted on the Monday after the sample was collected.

At the Clinical Microbiology Laboratory, viruses were concentrated to a final volume of 2.5ml, using a method that was developed in-house. This method uses the NanoCeram electropositive filter (Argonide, Florida, USA) as the primary means of concentration, and then ultracentrifugation as secondary concentration method ([Saguti _et al._, 2021](https://pubmed.ncbi.nlm.nih.gov/33212338/)). Nucleic acids were extracted from 1ml of the concentrated sample using the QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Real-time quantitative PCR (RT-qPCR) was performed to detect the RNA-dependent RNA polymerase (RdRP) region of SARS-CoV-2. In all runs, a 10-fold serial diluted plasmid (Eurofins Genomics, Ebersberg, Germany) that contained the target SARS-CoV-2 region was used as a positive control. Nuclease-free water was used as a negative control. The Ct values from the qPCR were used to quantify the amount of SARS-CoV-2 genome in the sample. Details about the method of calculation are provided in [Saguti _et al._ (2021)](https://pubmed.ncbi.nlm.nih.gov/33212338/). The relative amount of viral genome in the wastewater was calculated by dividing the amount of viral genome in the sample by the amount of SARS-CoV-2 genome in the incoming wastewater during week 11 (mid-March) of 2020. Samples from all subsequent weeks contained detectable SARS-CoV-2 genome.
