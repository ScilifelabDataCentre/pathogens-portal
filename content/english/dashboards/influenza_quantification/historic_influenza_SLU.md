---
title: Historic data of influenza virus in wastewater (SLU)
plotly: true
---

## Introduction

The data presented on this page was generated in the SLU (Swedish University of Agricultural Sciences) laboratories of SEEC (Swedish Environmental Epidemiology Center). The project was part of SciLifeLab’s Pandemic Laboratory Preparedness (PLP) Program, led by Anna J. Székely (Dep. of Aquatic Sciences and Assessment, SLU). Wastewater analyses were overseen by Anna J. Székely, Javier Vargas, and Maja Malmberg (Virology unit of Department of Biomedical Science and Veterinary Public Health, SLU). This page pertains to the historic quantification of the levels of influenza A and B viruses in multiple cities across Sweden. The project had the broadest geographic coverage across Sweden, generating data for 43% of the Swedish population.

Please note that the data and visualizations on this page are no longer updated. The scores in the dataset and depicted in the plots are final, though minor corrections may have been applied retrospectively. This dashboard serves as a record of the project's results during the active monitoring period.

## Wastewater collection sites

SLU-SEEC collects and analyses samples for influenza A and B viruses from multiple areas. The below table shows details about each of these sites. The table lists the towns/cities monitored, wastewater treatment plants (WWTP) that samples were collected from, the number of people in the catchment area (Number of people), and the dates that monitoring by SLU-SEEC started and ended monitoring (Start and End date, respectively). Please note that 'Start date' refers to the first date of monitoring for influenza A, but that the start date for influenza B is always later. A value of ’null’ for the end date indicates that collection is ongoing. An asterisk (\*) next to the number of people indicates that the value is a BOD-7 value (an estimate of the people connected), rather than the number of people physically connected to each WWTP. Two asterisks (\*\*) next to the Town/City indicates that data is only available for influenza A, not influenza B. The information in the below table is [available for download as an excel file](https://blobserver.dc.scilifelab.se/blob/SLU_INF_collection_sites.xlsx).

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_sluINFsites.json" height="750px" >}}</div>
</div>

## Visualisations

<div class="alert alert-info">Last updated: 2024-09-30</div>


<b>Important note:</b> Please note that although the same methods are used for all cities shown on this tab, differences in the wastewater collection systems and populations of different cities might bias direct comparisons between cities.

### Influenza A

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/historic_wastewater_slu_infA.json" height="600px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/archive/historic_combined_slu_influenza_a.py).

### Influenza B

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/historic_wastewater_slu_infB.json" height="600px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/archive/historic_combined_slu_influenza_b.py).

## Commentary from the research group

<div><b>Date:</b> 2023-08-30<br><b>Commentary:</b> The data presented for influenza A and B is preliminary. Minor changes to the data are expected in the near future due to ongoing adjustments to the data analyses methods.</div>

## Reports from the research group

The group provide reports to summarise their latest findings. The latest report is available [here](https://blobserver.dc.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU.pdf) (only available in Swedish).

## Dataset

**Contact:** <anna.szekely@slu.se> and <javier.vargas@slu.se>

**Download the data:** [Respiratory virus gene copy numbers normalised per PMMoV gene copy number.CSV file](https://blobserver.dc.scilifelab.se/blob/historic_SLU_wastewater_data.csv). Data are available for Influenza A from week 42 of 2022 and for Influenza B from week 12 of 2023; updated weekly.

**How to cite the dataset:**

Székely, A. J., Malmberg, M., Vargas, J., Mohamed, N., Dafalla, I., Petrini, F., Davies, L. (2023). Dataset of SARS-CoV-2, influenza A and influenza B virus content in wastewater samples from wastewater treatment plants in Sweden. <https://doi.org/10.17044/scilifelab.14256317>.

## Methods

For most cities represented on this page, raw, untreated wastewater samples that are representative of a single day are collected by flow compensated samplers at the wastewater treatment plants (WWTP). Uppsala is the exception, where samples are collected daily, and then combined flow-proportionally into one composite weekly sample for the purpose of analyses.

The viral genomic material from the freshly collected samples is extracted by the direct capture method, using the Maxwell RSC Enviro TNA kit (Promega).

Absolute quantification of the copy numbers of the genome of influenza A and B viruses is performed by One-Step RT-qPCR using the Flu SC2 Multiplex Assay from the Centers for Disease Control and Prevention (CDC). To correct for variations in population size and wastewater flow, pepper mild mottle virus (PMMoV) is quantified using a modified version of the assay of [Zhang et al. (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV is an abundant RNA virus in human faeces and serves as an estimator of human faecal content ([Symonds et al., 2019](https://doi.org/10.1371/journal.ppat.1007639)).

The data in the graphs and datafile represent the ratio of the copy numbers measured by the Flu SC2 Multiplex Assay and PMMoV-assays, multiplied by 1000. As the Flu SC2 Multiplex Assay provides proxies for both influenza A and B viruses content in the wastewater and PMMoV is a proxy of the faecal content (which is related to the contributing population), their ratio can be considered as a proxy for the prevalence of influenza A and influenza B infections in the population of the wastewater catchment area.
