---
title: Wastewater-based epidemiology in Sweden
plotly: true
---

## Introduction

Wastewater surveillance can be used to effectively monitor the levels of pathogens, including SARS-CoV-2, in the population. It can even help to predict upcoming outbreaks, thus acting as an ’early-warning system’. See below for [a general introduction to wastewater epidemiology](#background-wastewater-based-epidemiology).

This dashboard presents wastewater epidemiology data from various Swedish cities. Combined, the cities included here have a total population of over 4 million people (more than 40% of the Swedish population). The data presented in this dashboard originates from analyses conducted by three laboratories. Two of the laboratories are part of [SEEC (The Swedish Environmental Epidemiology Center)](https://www.scilifelab.se/pandemic-response/pandemic-laboratory-preparedness/swedish-environmental-epidemiology-center-seec/), which was established by researchers at four Swedish universities (Swedish University of Agricultural Sciences, KTH Royal Institute of Technology, Karolinka Institute, and Uppsala University) as a pandemic laboratory preparedness resource project within [SciLifeLab’s Pandemic Preparedness Program](https://www.scilifelab.se/pandemic-response). The two nodes of SEEC involved in wastewater analysis are **SEEC-KTH** (based at KTH Royal Institute of Technology (KTH), led by associate professor Zeynep Cetecioglu Gurol) and **SEEC-SLU** (based at the Department of Aquatic Sciences and Assessment at SLU (Swedish University of Agricultural Sciences), led by associate professor Anna J. Székely and associate professor Maja Malmberg). The third laboratory presenting their work on this dashboard is based at the **University of Gothenburg (GU)** and led by professor Heléne Norder. Please see the ['Links to pathogen specific dashboards section'](#Links-to-pathogen-specific-dashboards) below to locate the data provided by the three laboratories.

Please note that each laboratory processes and analyses their wastewater samples in slightly different ways. Therefore, the absolute values measured by different laboratories are not comparable with each other, and minor differences in trends may occur.

## Links to pathogen specific dashboards

- [**SARS-CoV-2 quantification**](/dashboards/covid_quantification/): Data, visualisations, and information related to the quantification of SARS-CoV-2 in wastewater in different areas of Sweden. All three groups share historic data for this pathogen, while ongoing data is provided by SEEC-SLU.

- [**Enteric virus quantification**](/dashboards/enteric_quantification/): Data, visualisations, and information related to the quantification of enteric viruses in wastewater Gothenburg. This data is collected, analysed, and shared by the Norder group at Gothenburg university (GU).

- [**Influenza quantification**](/dashboards/influenza_quantification/): Data, visualisations, and information related to the quantification of Influenza viruses in wastewater in different areas of Sweden. These data are collected, analysed, and shared by the SEEC-SLU.

- [**RSV quantification**](/dashboards/wastewater_rsv/): Data, visualisations, and information related to the quantification of Respiratory Syncytial Virus (RSV) in wastewater in different areas of Sweden. These data are collected, analysed, and shared by the SEEC-SLU.

## Availability of code

All code used to produce the visualisations on the tabs on this dashboard is available on [GitHub](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/tree/main/wastewater). The particular scripts used in each case are linked below the individual visualisations.

## Sample collection sites

Below is a map showing the wastewater treatment plants (WWTPs) from which wastewater samples are being collected and analysed by groups sharing data on this dashboard.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_map_test.json" height="600px" >}}</div>
</div>

**Code used to produce map:** [Script to produce map](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/interactive_wastewater_map.py).

The table below lists; the towns/cities monitored by groups sharing data on this dashboard, wastewater treatment plants (WWTP) that samples were collected from, the number of people in the catchment area (Number of people), whether monitoring is actively ongoing (Active?), the viruses monitored at the site (Viruses monitored), and the group(s) that have monitored/are monitoring the site. An asterisk (*) next to the number of people indicates that the value is an estimate of the people connected based on BOD-7 value, rather than the number of people physically connected to the WWTP. The information in the table below is [available for download as an excel file](https://blobserver.dc.scilifelab.se/blob/overall_ww_collection_sites.xlsx).

  <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_overallsites.json" height="840px" >}}</div>
</div>

## Background: Wastewater-based epidemiology

The genomes of many pathogens, including SARS-CoV-2, can be detected in faecal samples collected from infected individuals (e.g. COVID-19 patients) using polymerase chain reaction (PCR) tests (see, for example, [Wu _et al_. (2020)](<https://doi.org/10.1016/S2468-1253(20)30083-2>)). Monitoring the levels of pathogens (e.g. SARS-CoV-2) in wastewater from communities can therefore provide an indication of the prevalence of that pathogen at a population-wide level, referred to as wastewater-based epidemiology ([Corpuz _et al._, 2020](https://doi.org/10.1016/j.scitotenv.2020.140910)).

Wastewater, also referred to as “sewage” includes water from multiple sources in each household, including kitchen sinks, toilets, and showers. However, it could also include water from multiple other sources (for example, rainwater and water from industrial use). Samples used for wastewater epidemiology studies are collected periodically at wastewater treatment facilities; enabling assessments of viral load over time. Wastewater monitoring has been shown to be an effective early-warning system for outbreaks. For example, [Peccia _et al._ (2020)](https://doi.org/10.1038/s41587-020-0684-z) showed early on in the COVID-19 pandemic that SARS CoV-2 virus content in wastewater predicted increases in infection in the population and followed the epidemic trend, as measured by the number of COVID-19 cases and hospitalisation rates. [Wang _et al._ (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/) even showed that the level of SARS-CoV-2 viral genomes in wastewater increased 1-2 weeks before there was an increase in the number of hospitalised COVID-19 patients. Since the COVID-19 pandemic, surveillance of viral RNA levels in wastewater is used to monitor and predict the spread of the disease.

Wastewater monitoring should primarily be seen as a surveillance system. Taken together with data from other sources such as patient testing, intensive care admissions etc., it may help in understanding the regional dynamics of disease outbreaks.

{{< ww_dynamic_content >}}
