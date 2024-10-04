---
title: Amount of influenza virus in wastewater (SLU)
plotly: true
banner: /dashboard_thumbs/wastewater_influenza.png
description: Explore Influenza A and B virus levels in wastewater across Sweden. Weekly data from SLU-SEEC tracks Influenza trends, covering 43% of the Swedish population, and aids in predicting potential outbreaks.
menu:
 dashboard_menu:
    identifier: wastewater_influenza_quantification
    name: "Wastewater: Influenza Quantification (SLU)"
aliases:
  - /dashboards/wastewater/influenza_quantification/
dashboards_topics: [Wastewater Surveillance, Influenza, Epidemiology]
data_status: "updating"
---

## Introduction

Influenza viruses are negative-sense, single-stranded, segmented RNA viruses within the family Orthomyxoviridae. Influenza A and influenza B viruses cause seasonal epidemics of influenza, commonly known as “the flu”, a highly contagious respiratory disease characterized by symptoms such as fever, cough, sore throat, body aches, and fatigue but diarrhea and vomiting can also occur. Influenza A virus is widespread in water birds but also infects other birds and various mammals, including humans and pigs, while influenza B virus primarily infects humans. Influenza viruses mutate rapidly, leading to different strains and seasonal outbreaks. Both influenza A and influenza B viruses can cause seasonal outbreaks, but only influenza A is known to cause pandemics due to its broad host range and resulting potential for interspecies genetic reassortment. For more information about symptoms, risks and vaccination against influenza viruses, visit the corresponding site of the [Swedish Public Health Agency](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/influensa-/).

The data presented on this page is generated in the SLU (Swedish University of Agricultural Sciences) laboratories of SEEC (Swedish Environmental Epidemiology Center). The data and visualisation on this page are usually updated weekly, typically on Mondays. Please refer to the [Methods](#methods) for details on measurements and calculations. All related dashboards can be found on the [Wastewater Surveillance](/dashboards/topics/wastewater-surveillance/) page, and sampling sites and project details are available in the [Wastewater Monitoring Background](/dashboards/wastewater_background/).

<div class="alert alert-info">
<b>Important Note:</b></br>
The scores provided in the dataset and depicted in the plot below are preliminary, so corrections and changes may occur. Data and information about the group on this dashboard are updated frequently, so please check back regularly to stay up to date. </br>Please note that although the same methods are used for all cities shown on this tab, differences in the wastewater collection systems and populations of different cities might bias direct comparisons between cities.
</div>

## Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_slu_flu"></span></div>

### Influenza A

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 1200px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_slu_infA_v1.0.json" height="800px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/combined_slu_influenza_a.py).

### Influenza B

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 1200px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_slu_infB_v1.0.json" height="800px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/combined_slu_influenza_b.py).

## Commentary from the research group

<div><b>Date:</b> <span id="slu_flu_comment_date"></span><br><b>Commentary:</b> <span id="slu_flu_comment"></span></div>

{{< ww_dynamic_content >}}

## Reports from the research group

The group provide reports to summarise their latest findings. The latest report is available [here](https://blobserver.dc.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU.pdf) (only available in Swedish).

## Dataset

**Contact:** <anna.szekely@slu.se> and <javier.vargas@slu.se>

**Download the data:** [Respiratory virus gene copy numbers normalised per PMMoV gene copy number.CSV file](https://blobserver.dc.scilifelab.se/blob/SLU_wastewater_data_v1.0.csv). Data are available for Influenza A from week 42 of 2022 and for Influenza B from week 12 of 2023; updated weekly.

**How to cite the dataset:**

Székely, A. J., Malmberg, M., Vargas, J., Mohamed, N., Dafalla, I., Petrini, F., Davies, L. (2023). Dataset of SARS-CoV-2, influenza A and influenza B virus content in wastewater samples from wastewater treatment plants in Sweden. <https://doi.org/10.17044/scilifelab.14256317>.

## Methods

Wastewater is collected from several different treatment plants around the country. For more information about the treatment plants, visit the page about [the background of wastewater surveillance](/dashboards/wastewater_background/). For most cities represented on this page, raw, untreated wastewater samples that are representative of a single day are collected by flow compensated samplers at the wastewater treatment plants (WWTP). Uppsala is the exception, where samples are collected daily, and then combined flow-proportionally into one composite weekly sample for the purpose of analyses.

The viral genomic material from the freshly collected samples is extracted by the direct capture method, using the Maxwell RSC Enviro TNA kit (Promega).

Absolute quantification of the copy numbers of the genome of influenza A and B viruses is performed by One-Step RT-qPCR using the Flu SC2 Multiplex Assay from the Centers for Disease Control and Prevention (CDC). To correct for variations in population size and wastewater flow, pepper mild mottle virus (PMMoV) is quantified using a modified version of the assay of [Zhang et al. (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV is an abundant RNA virus in human faeces and serves as an estimator of human faecal content ([Symonds et al., 2019](https://doi.org/10.1371/journal.ppat.1007639)).

The data in the graphs and datafile is presented in three different formats:
- **PMMoV normalised Influenza content** represents the ratio of the copy numbers of influenza and PMMoV measured by the influenza assay and PMMoV-assays, respectively, multiplied by 1000. As the influenza assay provides proxies for influenza virus content in the wastewater and PMMoV is a proxy of the faecal content (which is related to the contributing population), the ratio of the two can be considered to be a proxy for the prevalence of influenza infections in the population of the wastewater catchment area.
- **Influenza genome copies concentration** presents the influenza copy number concentration measured in the wastewater. These data is influenced by the setup of the different wastewater collection nsystems and is therefore not suitable for comparison betwwen sites. The virus concentrations in the wastewater are also influenced by the weather events that impact wastewater flow (e.g., heavy rain or snow melt).
- **Influenza genome copies/day/inhabitant** represents the daily virus amount estimated in the wastewater normalized for the number of inhabitants connected to the system. These data allows for comparison of different sites but some delays in the presentation of these data may occur compared to the other.

**How to cite the method:**

Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. _Environments_, _9_, 39. <https://doi.org/10.3390/environments9030039>.

## Archived data from SLU

- [Historic Influenza data in wastewater from SEEC-SLU](/dashboards/influenza_quantification/historic_influenza_SLU)