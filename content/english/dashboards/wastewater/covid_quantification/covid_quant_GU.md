---
title: Amount of SARS-CoV-2 in wastewater (GU)
plotly: true
aliases:
  - /dashboards/wastewater/covid_quant_gu/
---

<div class="mt-3">
  <a href="/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Go back to SARS-CoV-2 quantification within the wastewater epidemiology dashboard</a>
</div>
<br>

## Introduction

This project is led by Professor Helene Norder (University of Gothenburg, GU), and supported by co-workers from the University of Gothenburg and Sahlgrenska University Hospital (Hao Wang, Marianela Patzi Churqui, Timur Tunovic, Fredy Saguti, and Kristina Nyström). The wastewater sample collections were performed by Lucica Enache at Ryaverket, Gryaab AB, Gothenburg.

The group began collecting samples on 10th February (week 7) 2020. They updated the methods related to analysing the samples during 2023, and began to use this updated method on 15th May (week 20) 2023. This page concerns only the data collected using their updated method. The associated data and visualisation are **updated approximately weekly**. Corresponding information about data collected using an earlier method is available in the ['Historic SARS-CoV-2 data from Gothenburg' page](/dashboards/wastewater/covid_quantification/historic_covid_gu/).

The SARS-CoV-2 virus monitoring by the Norder group was done alongside their ongoing monitoring of enteric viruses in wastewater, the data for which are [also shared on this portal](/dashboards/wastewater/enteric_quantification/).

## Wastewater collection sites

Influent wastewater samples were collected from Ryaverket wastewater treatment plant (WWTP) in Gothenburg. Whilst this page includes data collected since 15th May 2023, the group initially began to collect wastewaster samples on 10th February (week 7) 2020. Ryaverket WWTP receives wastewater from the households of more than 790,000 residents of Gothenburg, as well as from industry in the area. Wastewater is also received from residents and industry in surrounding municipalities, including Ale, Härryda, Kungälv, Lerum, Mölndal, and Partille, as well as storm and snow-melt water from older parts of Gothenburg. The amount of wastewater from households remains relatively consistent throughout the year. However, the amount of wastewater overall can be affected by the weather (with higher precipitation resulting in greater amounts). More information about the sample location, sample week, volume, and influent wastewater flow, is available in [Wang _et al._ (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/).

## Visualisation

<div class="alert alert-info">Last updated: <span id="last_modified_gu"></span></div>

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

 <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_gothenburg.json" height="550px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/gothenburg_covid.py).

## Commentary from the research group

<div><b>Date:</b><span id="gu_comment_date"></span><br><b>Commentary:</b><span id="gu_comment"></span></div>

{{< ww_dynamic_content >}}

## Dataset

**Download the data:** [Quantification of SARS-CoV-2 and enteric viruses in wastewater](https://blobserver.dc.scilifelab.se/blob/wastewater_data_gu_allviruses.xlsx). Results are available for SARS-CoV-2 and enteric viruses from week 20 of 2023. Updated weekly.

**Contact:** <helene.norder@gu.se>

**How to cite the dataset:** Norder, H., Nyström, K. Patzi Churqui, M., Tunovic, T., Wang, H., Saguti, F. (2023). Detection of SARS-CoV-2 and other human enteric viruses in wastewater from Gothenburg. [https://doi.org/10.17044/scilifelab.24787353.v1](https://doi.org/10.17044/scilifelab.24787353.v1).

**How to cite method:**

Saguti, F., Magnil, E., Enache, L., Churqui, M.P., Johansson, A., Lumley, D., Davidsson, F., Dotevall, L., Mattsson, A., Trybala, E., Lagging, M., Lindh, M., Gisslen, M., Brezicka, T., Nystrom, K. and Norder, H. (2021). Surveillance of wastewater revealed peaks of SARS-CoV-2 preceding those of hospitalized patients with COVID-19. [https://doi.org/10.1016/j.watres.2020.116620](https://doi.org/10.1016/j.watres.2020.116620).

Wang, H., Churqui, M.P., Tunovic, T., Enache, L., Johansson, A., Karmander, A., Nilsson, S., Lagging, M., Andersson, M., Dotevall, L., Brezicka, T., Nystrom, K. and Norder, H. (2022). The amount of SARS-CoV-2 RNA in wastewater relates to the development of the pandemic and its burden on the health system. [https://doi.org/10.1016/j.isci.2022.105000](https://doi.org/10.1016/j.isci.2022.105000).

## Methods

Samples of wastewater were collected using a fixed-site sampler that collected 30ml per 10,000m<sup>3</sup> of the incoming wastewater. For the purposes of analysis, seven samples (each representing a 24 hour period) were pooled to create a weekly sample. The weekly sample, which consisted of 1.5-15l of wastewater (depending on the flow) was sent to the Clinical Microbiology Laboratory at Sahlgrenska University Hospital for analysis. Analyses were conducted on the Monday after the sample was collected.

At the Clinical Microbiology Laboratory, two methods developed in-house were used to concentrate viruses. The current method uses ultrafiltration as the primary method of concentration. Our previous method instead used an electropositive filter ([Saguti _et al._, 2021](https://pubmed.ncbi.nlm.nih.gov/33212338/)). The two techniques were used in parallel between weeks 20 and 43 in 2023. All information related to the data collected using the previous method can be found on the page related to [historic SARS-CoV-2 data from Gothenburg](/dashboards/wastewater/covid_quantification/historic_covid_gu/).

Nucleic acids were extracted from 1ml of the concentrated sample using the QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Real-time quantitative PCR (RT-qPCR) was performed to detect the RNA-dependent RNA polymerase (RdRP) region of SARS-CoV-2. In all runs, a 10-fold serial diluted plasmid (Eurofins Genomics, Ebersberg, Germany) that contained the target SARS-CoV-2 region was used as a positive control. Nuclease-free water was used as a negative control. Details about the method of calculation are provided in [Hellmér _et al._ (2014)](https://doi.org/10.1128/AEM.01981-14), [Saguti _et al._ (2021)](https://pubmed.ncbi.nlm.nih.gov/33212338/), [Wang _et al._ (2022)](https://doi.org/10.1016/j.isci.2022.105000), and [Wang _et al._ (2023)](https://doi.org/10.1016/j.scitotenv.2023.165012). For the previous method, which was used until week 43 in 2023, the relative amount of viral genome in the wastewater was calculated by dividing the amount of viral genome in the sample by the amount of SARS-CoV-2 genome in the incoming wastewater during week 11 (mid-March) of 2020. Samples from all subsequent weeks contained detectable SARS-CoV-2 genome (see the [historic SARS-CoV-2 data from Gothenburg page to view this data](/dashboards/wastewater/covid_quantification/historic_covid_gu/)). With the new technique, the data for which is shown above, the amount of virus genomes is given as daily average amounts, as is based on one week of wastewater sampling.

## Archived data

- [Historic SARS-CoV-2 data from Gothenburg collected between week 7 of 2020 and week 43 of 2023](/dashboards/wastewater/covid_quantification/historic_covid_gu/).

<br>
<div class="mt-3">
  <a href="/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Go back to SARS-CoV-2 quantification within the wastewater epidemiology dashboard</a>
</div>
