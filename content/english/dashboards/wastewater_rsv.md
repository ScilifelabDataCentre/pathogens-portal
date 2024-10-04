---
title: "Amount of Respiratory Syncytial Virus (RSV) in wastewater (SEEC-SLU)"
description: "Explore Respiratory Syncytial Virus (RSV) levels in wastewater across Sweden. Weekly data from SLU-SEEC tracks RSV trends, covering a significant portion of the population, and assists in predicting potential outbreaks."
plotly: true
banner: /dashboard_thumbs/wastewater_rsv.png
menu:
  dashboard_menu:
    identifier: rsv_quant
    name: "Wastewater: RSV Quantification (SLU)"
dashboards_topics: [Wastewater Surveillance, RSV, Epidemiology]
data_status: "updating"
---

## Introduction

Respiratory Syncytial Virus (RSV) is a negative-sense, single-stranded RNA virus that causes infections of the lungs and respiratory tract. Most people only have mild, cold-like symptoms and recover quickly, but infants and older adults can develop severe RSV and need hospitalization. RSV is one of the major reasons of hospitalization for respiratory illnesses in infants < 1 year old. For more information about symptoms, risks and vaccination against RSV, visit the corresponding site of the [Swedish Public Health Agency](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/rs-virusinfektion/).

The data presented on this page is generated in the SLU (Swedish University of Agricultural Sciences) laboratories of SEEC (Swedish Environmental Epidemiology Center). The data and visualisation on this page are usually updated weekly, typically on Mondays. Please refer to the [Methods](#methods) for details on measurements and calculations. All related dashboards can be found on the [Wastewater Surveillance](/dashboards/topics/wastewater-surveillance/) page, and sampling sites and project details are available in the [Wastewater Monitoring Background](/dashboards/wastewater_background/).

<div class="alert alert-info">
<b>Important Note:</b></br>
The scores provided in the dataset and depicted in the plot below are preliminary, so corrections and changes may occur. Data and information about the group on this dashboard are updated frequently, so please check back regularly to stay up to date. </br>Please note that although the same methods are used for all cities shown on this tab, differences in the wastewater collection systems and populations of different cities might bias direct comparisons between cities.
</div>

## Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_slu_rsv"></span></div>

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 1200px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_slu_rsv_v1.0.json" height="800px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/combined_slu_rsv.py).

## Commentary from the research group

<div><b>Date:</b> <span id="slu_rsv_comment_date"></span><br><b>Commentary:</b> <span id="slu_rsv_comment"></span></div>

{{< ww_dynamic_content >}}

## Reports from the research group

The group provide reports to summarise their latest findings. The latest report is available <a target="_blank" href="https://blobserver.dc.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU.pdf">here</a> (only available in Swedish).

## Dataset

**Contact:** <anna.szekely@slu.se> and <javier.vargas@slu.se>

**Download the data:** [Respiratory virus gene copy numbers normalised per PMMoV gene copy number.CSV file](https://blobserver.dc.scilifelab.se/blob/SLU_wastewater_data_v1.0.csv). Data are available for RSV from week 32 of 2023; updated weekly.

**How to cite the dataset:**

Székely, A. J., Malmberg, M., Vargas, J., Mohamed, N., Dafalla, I., Petrini, F., Davies, L. (2023). Dataset of SARS-CoV-2, influenza A and influenza B virus content in wastewater samples from wastewater treatment plants in Sweden. <https://doi.org/10.17044/scilifelab.14256317>.

## Methods

Wastewater is collected from several different treatment plants around the country. For more information about the treatment plants, visit the page about [the background of wastewater surveillance](/dashboards/wastewater_background/). For most cities represented on this page, raw, untreated wastewater samples that are representative of a single day are collected by flow compensated samplers at the wastewater treatment plants (WWTP). Uppsala is the exception, where samples are collected daily, and then combined flow-proportionally into one composite weekly sample for the purpose of analyses.

The viral genomic material from the freshly collected samples is extracted by the direct capture method, using the Maxwell RSC Enviro TNA kit (Promega).

Absolute quantification of the copy numbers of the genome of RSV virus is performed by One-Step RT-qPCR using the assay of <a target="_blank" href="https://doi.org/10.1021/acs.estlett.1c00963">Hughes et al. (2022)</a>. To correct for variations in population size and wastewater flow, pepper mild mottle virus (PMMoV) is quantified using a modified version of the assay of <a target="_blank" href="https://doi.org/10.1371/journal.pbio.0040003">Zhang et al. (2006)</a>. PMMoV is an abundant RNA virus in human faeces and serves as an estimator of human faecal content (<a target="_blank" href="https://doi.org/10.1371/journal.ppat.1007639">Symonds et al., 2019</a>).

The data in the graphs and datafile is presented in three different formats:

- **PMMoV normalised RSV content** represents the ratio of the copy numbers of RSV and PMMoV measured by the RSV assay and PMMoV-assays, respectively, multiplied by 1000. As the RSV assay provides proxies for RSV virus content in the wastewater and PMMoV is a proxy of the faecal content (which is related to the contributing population), the ratio of the two can be considered to be a proxy for the prevalence of RSV infections in the population of the wastewater catchment area.
- **RSV genome copies concentration** presents the RSV copy number concentration measured in the wastewater. These data is influenced by the setup of the different wastewater collection nsystems and is therefore not suitable for comparison betwwen sites. The virus concentrations in the wastewater are also influenced by the weather events that impact wastewater flow (e.g., heavy rain or snow melt).
- **RSV genome copies/day/inhabitant** represents the daily virus amount estimated in the wastewater normalized for the number of inhabitants connected to the system. These data allows for comparison of different sites but some delays in the presentation of these data may occur compared to the other.

**How to cite the method:**

Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. _Environments_, _9_, 39. <https://doi.org/10.3390/environments9030039>.

