---
title: Wastewater-based epidemiology in Sweden
description: Surveillance of wastewater for pathogens can be an effective means of predicting upcoming outbreaks. This dashboard contains data originating from the multiple research groups across Sweden.
banner: /dashboard_thumbs/wastewater.jpg
toc: false
type: wastewater
menu:
    dashboard_menu:
        identifier: wastewater
        name: Wastewater-based epidemiology in Sweden
    other_data:
        name: Environment
        identifier: environment
        weight: 50
    wastewater:
        name: Introduction
        weight: 10
plotly: true
aliases:
    - /data_types/environment/wastewater/
    - /data_types/environment/
    - /dashboards/wastewater
---

<div class="alert alert-info"><b>Please note:</b> the wastewater dashboard is undergoing expansion over the next few months. We have now separated the data related to the amount of SARS-CoV-2 in wastewater according to the research group that collected and analysed the data (see below for information about the groups involved). In the coming months, more information and data will be added about SARS-CoV-2 and on other infectious diseases. </span></div>

## Introduction

Wastewater surveillance can be used to effectively monitor the levels of pathogens, including SARS-CoV-2, in the population. It can even help to predict upcoming outbreaks, thus acting as an 'early-warning system'. See below for [a general introduction to wastewater epidemiology](#background-wastewater-based-epidemiology).

This dashboard presents wastewater epidemiology data from various Swedish cities. Combined, the cities included here have a total population of over 3.5 million people (or 34% of the Swedish population). The data presented in this dashboard originates from analyses conducted by three laboratories. Two of the laboratories are part of [SEEC (The Swedish Environmental Epidemiology Center)](https://www.scilifelab.se/pandemic-response/pandemic-laboratory-preparedness/swedish-environmental-epidemiology-center-seec/), which was established by researchers at four Swedish universities (Swedish University of Agricultural Sciences, KTH Royal Institute of Technology, Karolinka Institute, and Uppsala University) as a pandemic laboratory preparedness resource project within [SciLifeLab’s Pandemic Preparedness Program](https://www.scilifelab.se/pandemic-response). The two nodes of SEEC involved in wastewater analysis are **SEEC-KTH** (based at KTH Royal Institute of Technology (KTH), led by associate professor Zeynep Cetecioglu Gurol) and **SEEC-SLU** (based at the Department of Aquatic Sciences and Assessment at SLU (Swedish University of Agricultural Sciences), led by associate professor Anna J. Székely and associate professor Maja Malmberg). The third laboratory presenting their work on this dashboard is based at the **University of Gothenburg (GU)** and led by professor Heléne Norder. Please see the ['navigating the dashboard' section](#navigating-the-dashboard) below to understand where to locate work provided from the three laboratories within this dashboard.

Please note that each laboratory processes and analyses their wastewater samples in slightly different ways. Therefore, the absolute values measured by different laboratories are not comparable with each other, and minor differences in trends may occur. This means that you should be cautious when making comparisons. Please consult the 'methods' sections of individual tabs to understand the methodologies used in each case.

## Navigating the dashboard

The work on this dashboard is divided according to different topics explored. See the list below to determine which resources are available:

- [**SARS-CoV-2 quantification**](/dashboards/wastewater/covid_quantification/): Data, visualisations, and information related to the quantification of SARS-CoV-2 in wastewater in differnt areas of Sweden. All three groups share data on this topic, and cover diferent areas of Sweden. It is possible to navigate directly to the group(s) providing data on the area(s) of interest to you.

## Availability of code

All code used to produce the visualisations on the tabs on this dashboard is available on [GitHub](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/tree/main/wastewater). The particular scripts used in each case are linked below the individual visualisations.

## Map of sample collection sites

Below is a map showing the wastewater treatment plants (WWTPs) from which wastewater samples are being collected and analysed by groups sharing data on this dashboard.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_map_test.json" height="600px" >}}</div>
</div>

**Code used to produce map:** [Script to produce map](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/interactive_wastewater_map.py).

## Background: Wastewater-based epidemiology

The genomes of many pathogens, including SARS-CoV-2, can be detected in faecal samples collected from infected individuals (e.g. COVID-19 patients) using polymerase chain reaction (PCR) tests (see, for example, [Wu *et al*. (2020)](https://doi.org/10.1016/S2468-1253(20)30083-2)). Monitoring the levels of pathogens (e.g. SARS-CoV-2) in wastewater from communities can therefore provide an indication of the prevalence of that pathogen at a population-wide level, referred to as wastewater-based epidemiology ([Corpuz *et al.*, 2020](https://doi.org/10.1016/j.scitotenv.2020.140910)).

Wastewater, also referred to as “sewage” includes water from multiple sources in each household, including kitchen sinks, toilets, and showers. However, it could also include water from multiple other sources (for example, rainwater and water from industrial use). Samples used for wastewater epidemiology studies are collected periodically at wastewater treatment facilities; enabling assessments of viral load over time. Wastewater monitoring has been shown to be an effective early-warning system for outbreaks. For example, [Peccia *et al.* (2020)](https://doi.org/10.1038/s41587-020-0684-z) showed early on in the COVID-19 pandemic that SARS CoV-2 virus content in wastewater predicted increases in infection in the population and followed the epidemic trend, as measured by the number of COVID-19 cases and hospitalisation rates. More recently, [Wang *et al.* (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/) showed that the level of SARS-CoV-2 viral genomes in wastewater increased 1-2 weeks before there was an increase in the number of hospitalised COVID-19 patients. During the COVID-19 pandemic, surveillance of viral RNA levels in wastewater has been increasingly used to monitor and predict the spread of the disease.

Wastewater monitoring should primarily be seen as a surveillance system. Taken together with data for infection testing, intensive care admissions etc., it may help in understanding the regional dynamics of disease outbreaks.

{{< ww_dynamic_content >}}
