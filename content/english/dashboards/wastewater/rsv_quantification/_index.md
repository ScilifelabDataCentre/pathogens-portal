---
title: Amount of Respiratory Syncytial Virus (RSV) in wastewater (SEEC-SLU)
plotly: true
type: wastewater
menu:
  wastewater:
    name: RSV quantification (SLU)
    weight: 50
---

## Introduction

Respiratory Syncytial Virus (RSV) is a negative-sense, single-stranded RNA virus that causes infections of the lungs and respiratory tract. Most people only have causes mild, cold-like symptoms and recover quickly, but infants and older adults can develop severe RSV and need hospitalization. RSV is one of the major reasons of hospitalization for respiratory illnesses in infants < 1 year old.

The data presented on this page is generated in the SLU (Swedish University of Agricultural Sciences) laboratories of SEEC (Swedish Environmental Epidemiology Center). The project is part of <a target="_blank" href="https://www.pathogens.se/resources/">SciLifeLab’s Pandemic Laboratory Preparedness (PLP) Program</a>, and is led by Anna J. Székely (Dep. of Aquatic Sciences and Assessment, SLU). Wastewater analyses are overseen by Anna J. Székely, Javier Vargas and Maja Malmberg (Virology unit of Department of Biomedical Science and Veterinary Public Health, SLU). This page pertains to the quantification of the levels of SARS-CoV-2 virus in multiple cities across Sweden. This project currently has the broadest geographic coverage across Sweden; generating data for 43% of the Swedish population.

The data and visualisation on this page are usually updated weekly, typically on Fridays. Please note that the scores provided in the dataset and depicted in plot below are preliminary, so corrections and changes may occur. Data and information about the group on this dashboard are updated frequently, so please check back regularly to stay up to date.

## Wastewater collection sites

SLU-SEEC collects and analyses samples for RSV from multiple areas. The below table shows details about each of these sites. The table lists the towns/cities monitored, wastewater treatment plants (WWTP) that samples were collected from, the number of people in the catchment area (Number of people), and the dates that monitoring by SLU-SEEC started and ended monitoring (Start and End date, respectively). A value of ’null’ for the end date indicates that collection is ongoing. An asterisk next to the number of people indicates that the value is estimated based on the population equivalent (p.e.) loading of the treatment plant. The information in the below table is [available for download as an excel file](https://blobserver.dc.scilifelab.se/blob/SLU_RSV_collection_sites.xlsx).

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_sluRSVsites.json" height="350px" >}}</div>
</div>

## Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_slu_rsv"></span></div>

<b>Important note:</b> Please note that although the same methods are used for all cities shown on this tab, differences in the wastewater collection systems and populations of different cities might bias direct comparisons between cities.

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_slu_rsv.json" height="800px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/combined_slu_rsv.py).

## Commentary from the research group

<div><b>Date:</b> <span id="slu_rsv_comment_date"></span><br><b>Commentary:</b> <span id="slu_rsv_comment"></span></div>

{{< ww_dynamic_content >}}

## Reports from the research group

The group provide reports to summarise their latest findings. The latest report is available <a target="_blank" href="https://blobserver.dc.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU.pdf">here</a> (only available in Swedish).

## Dataset

**Contact:** <anna.szekely@slu.se> and <javier.vargas@slu.se>

**Download the data:** [Respiratory virus gene copy numbers normalised per PMMoV gene copy number.CSV file](https://blobserver.dc.scilifelab.se/blob/SLU_wastewater_data.csv). Data are available for RSV from week 32 of 2023; updated weekly.

**How to cite the dataset:**

Székely, A. J., Malmberg, M., Vargas, J., Mohamed, N., Dafalla, I., Petrini, F., Davies, L. (2023). Dataset of SARS-CoV-2, influenza A and influenza B virus content in wastewater samples from wastewater treatment plants in Sweden. <https://doi.org/10.17044/scilifelab.14256317>.

## Methods

For most cities represented on this page, raw, untreated wastewater samples that are representative of a single day are collected by flow compensated samplers at the wastewater treatment plants (WWTP). Uppsala is the exception, where samples are collected daily, and then combined flow-proportionally into one composite weekly sample for the purpose of analyses.

The viral genomic material from the freshly collected samples is extracted by the direct capture method, using the Maxwell RSC Enviro TNA kit (Promega). For detailed description of the method, please consult the following protocol:

Absolute quantification of the copy numbers of the genome of RSV virus is performed by One-Step RT-qPCR using the assay of <a target="_blank" href="https://doi.org/10.1021/acs.estlett.1c00963">Hughes et al. (2022)</a>. To correct for variations in population size and wastewater flow, pepper mild mottle virus (PMMoV) is quantified using a modified version of the assay of <a target="_blank" href="https://doi.org/10.1371/journal.pbio.0040003">Zhang et al. (2006)</a>. PMMoV is an abundant RNA virus in human faeces and serves as an estimator of human faecal content (<a target="_blank" href="https://doi.org/10.1371/journal.ppat.1007639">Symonds et al., 2019</a>).

The data in the graphs and datafile represent the ratio of the copy numbers of RSV measured by the RSV assay and PMMoV-assays, multiplied by 104. As the RSV assay provides proxies for RSV virus content in the wastewater and PMMoV is a proxy of the faecal content (which is related to the contributing population), the ratio of the two can be considered to be a proxy for the prevalence of RSV infections in the population of the wastewater catchment area.

**How to cite the methods:**

Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. Environments, 9, 39. <https://doi.org/10.3390/environments9030039>.
