---
title: The amount of SARS-CoV-2 virus in wastewater across Sweden
toc: true
menu:
  other_data:
      name: Environment
      identifier: environment
      weight: 50
plotly: true
---
Wastewater surveillance could prove to be an effective system for monitoring COVID-19 prevalence and act as an early warning system for predicting upcoming outbreaks.  See below for [general introduction to wastewater epidemiology](#background-wastewater-based-epidemiology).

In this section, we present wastewater epidemiology data from various Swedish cities which have a total population of over 2.5 million people (over 25% of the population of Swden). The data presented here originates from analyses conducted by the [Swedish Environmental Epidemiology Center](https://www.scilifelab.se/pandemic-response/pandemic-laboratory-preparedness/swedish-environmental-epidemiology-center-seec/) (SEEC). Samples are analyzed in two nodes of SEEC:

- **SEEC-SLU:** Samples from Uppsala, Örebro, Umeå, Kalmar, and various municipalities in Uppsala and Stockholm region are analyzed at the Swedish University of Agricultural Sciences node led by associate professor Anna J. Székely (anna.szekely@slu.se) and associate professor Maja Malmberg (maja.malmberg@slu.se).
- **SEEC-KTH:** Samples from Stockholm and Malmö are analyzed at the KTH Royal Institute of Technology node led by associate professor Zeynep Cetecioglu Gurol (zeynepcg@kth.se).

The methods used in each node are somewhat different, see [detailed description of methods below](#methods). Note that the values provided in the datasets and depicted in plots below are preliminary and should not be overinterpreted. The teams are still conducting method efficiency checks that might affect the final results.

## Map of sample collection sites

<div class="row justify-content-center mb-4"><div class="col">{{< wastewater_map >}}</div></div>

## Comments on the recent wastewater measurements

#### SEEC-SLU

<div><b>Date:</b> <span id="slu_comment_date"></span><br><b>Commentary:</b> <span id="slu_comment"></span></div>

#### SEEC-KTH

<div><b>Date:</b> <span id="kth_comment_date"></span><br><b>Commentary:</b> <span id="kth_comment"></span></div>

## Recent wastewater measurements per municipality

### Stockholm

**Last updated:** <span id="last_modified_stockholm"></span> \
**Wastewater treatment plant:** Bromma, Henriksdal, and Käppala ([catchment area of Käppala](/wastewater/map_Kappala.pdf), [catchment area of Bromma and Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf)) \
**Analysis method used:** [SEEC KTH Royal Institute of Technology node method](#seec-kth-1) \
**Download the data:** [Excel file](https://blobserver.dckube.scilifelab.se/blob/stockholm_wastewater_method_Sep_2021.xlsx); results are available starting from week 16 of 2020; updated weekly.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>
<div class="plot_wrapper">
  <div class="table-responsive" id="stockholm_plot"></div>
</div>

### Malmö

**Last updated:** <span id="last_modified_malmo"></span> \
**Wastewater treatment plant:** Sjölunda avloppsreningsverk ([catchment area map](/wastewater/sjolunda.pdf)) \
**Analysis method used:** [SEEC KTH Royal Institute of Technology node method](#seec-kth-1) \
**Download the data:** [Excel file](https://blobserver.dckube.scilifelab.se/blob/stockholm_wastewater_method_Sep_2021.xlsx); results are available starting from week 39 of 2021; updated weekly.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>
<div class="plot_wrapper">
  <div class="table-responsive" id="malmo_plot"></div>
</div>

### Uppsala

**Last updated:** <span id="last_modified_uppsala"></span> \
**Wastewater treatment plant:** Kungsängsverket ([catchment area map](/wastewater/avrinningskarta_inlopp_kungsangsverket.pdf)) \
**Analysis method used:** [SEEC Swedish University of Agricultural Sciences (SLU) node method](#seec-slu-1)\
**Download the data:** [Relative ratio of copy number of SARS-CoV-2 to PPMoV, CSV file](https://datagraphics.dckube.scilifelab.se/api/dataset/0ac8fa02871745048491de74e5689da9.csv); data available starting from week 38 of 2020; updated weekly.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>
<div class="plot_wrapper">
  <div class="table-responsive" id="uppsala_plot"></div>
</div>

### Örebro

**Last updated:** <span id="last_modified_orebro"></span> \
**Wastewater treatment plant:** ([catchment area map](/wastewater/map_orebro.pdf)) \
**Analysis method used:** [SEEC Swedish University of Agricultural Sciences (SLU) node method](#seec-slu-1)\
**Download the data:** [Relative ratio of copy number of SARS-CoV-2 to PPMoV, CSV file](https://datagraphics.dckube.scilifelab.se/api/dataset/0ac8fa02871745048491de74e5689da9.csv); data available starting from week 25 of 2021; updated weekly.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>
<div class="plot_wrapper">
  <div class="table-responsive" id="orebro_plot"></div>
</div>

### Umeå

**Last updated:** <span id="last_modified_umea"></span> \
**Wastewater treatment plant:** ([catchment area map](/wastewater/map_umeaa.jpg)) \
**Analysis method used:** [SEEC Swedish University of Agricultural Sciences (SLU) node method](#seec-slu-1)\
**Download the data:** [Relative ratio of copy number of SARS-CoV-2 to PPMoV, CSV file](https://datagraphics.dckube.scilifelab.se/api/dataset/0ac8fa02871745048491de74e5689da9.csv); data available starting from week 25 of 2021; updated weekly.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>
<div class="plot_wrapper">
  <div class="table-responsive" id="umea_plot"></div>
</div>

### Kalmar

**Last updated:** <span id="last_modified_kalmar"></span> \
**Wastewater treatment plant:**  \
**Analysis method used:** [SEEC Swedish University of Agricultural Sciences (SLU) node method](#seec-slu-1)\
**Download the data:** [Relative ratio of copy number of SARS-CoV-2 to PPMoV, CSV file](https://datagraphics.dckube.scilifelab.se/api/dataset/0ac8fa02871745048491de74e5689da9.csv); data available starting from week 34 of 2021; updated weekly.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>
<div class="plot_wrapper">
  <div class="table-responsive" id="kalmar_plot"></div>
</div>

### Other municipalities in Uppsala and Stockholm regions

**Last updated:** <span id="last_modified_slu_other"></span> \
**Wastewater treatment plant:** The amount of SARS-CoV-2 virus in the wastewater of Ekerö is estimated based on samples from Ekebyhov wastewater treatment plant, that of Österåker is based on Margretelund wastewater treatment plant, and that of Vaxholm is based on Blynäs wastewater treatment plant. \
**Analysis method used:** [SEEC Swedish University of Agricultural Sciences (SLU) node method](#seec-slu-1)\
**Download the data:** [Relative ratio of copy number of SARS-CoV-2 to PPMoV, CSV file](https://datagraphics.dckube.scilifelab.se/api/dataset/0ac8fa02871745048491de74e5689da9.csv); updated weekly.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>
<div class="plot_wrapper">
  <div class="table-responsive" id="various_plot"></div>
</div>

## All wastewater measurements in a single graph

The graph below allows for comparison of SARS-CoV-2 levels in wastewater across wastewater treatment plants. Note that Stockholm and Malmö are not included in the graph below because data from these cities cannot be directly compared to data from the cities included in this graph. That is the case because the method used to analyze samples from these cities is somewhat different from the method used to analyze samples from Stockholm and Malmö. In the future, SEEC hopes to unify the methods in such a way that data from all cities would be comparable to each other.

<div class="alert alert-secondary small">Interacting with the plot: Click on the names of municipalities in the legend in order to select or deselect cities that are displayed. Select a portion of the plot using your cursor in order to zoom in to a particular date range or y axis range. Note that the axes ranges adapt to your selections. Double-click anywhere on the graph in order to return to the default view. It is also possible download the graph as a PNG file, zoom and reset using buttons which appear in the top right corner when you hover over the graph.</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_regular.json" height="550px" >}}</div>
</div>

Please note that the plot below displays the same data, but the y axis is shown as a log scale.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_logyaxis.json" height="550px" >}}</div>
</div>

## Methods

#### SEEC-SLU

The project is made possible thanks to collaborations with Uppsala Vatten, Roslagsvatten, Enköpings kommun, Gästrike Vatten, TEMAB, and others.

Measurements are taken weekly, by processing a representative sample collected over 24 hours (i.e. flow compensated sample). The SARS-CoV-2 virus content of the wastewater on the given day is normalized to the fecal matter content to avoid variation from flow differences and population fluctuation. The samples are processed according to standard methods. Briefly, the viral genomic material is concentrated and extracted by the direct capture method using the Maxwell RSC Enviro TNA kit (Promega) and the copy number of SARS-CoV-2 genomes is quantified by RT-qPCR using the CDC RUO nCOV N1 assay (IDT DNA). The virus recovery efficiency of the process and the presence of potential inhibitors is monitored by adding to the samples bovine coronavirus (BCoV) as process surrogate virus. To correct for variations in population size and wastewater flow, we also quantify the pepper mild mottle virus (PMMoV) which is the most abundant RNA virus in human feces and serves as an estimator of human fecal content ([Symonds and colleagues, 2019](https://doi.org/10.1371/journal.ppat.1007639)).

#### SEEC-KTH

The samples are analyzed at KTH Royal Institute of Technology node as a collaboration between the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) and the [KTH Water Centre](https://www.kth.se/water), [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196), and [Protein Science](https://www.kth.se/pro/protein-science-1.784558) departments at KTH, in close collaboration with Stockholm Vatten och Avfall and the Käppala Association. Three collection channels (Järva, Hässelby and Riksby) are analyzed in Bromma and two (Henriskdal and Sickla) are analyzed in Henriksdal treatment plant.

One-day representative samples (collected over 24 hours) are received every week from the three WWTP. An aliquot of the samples is analyzed weekly and another two aliquots are kept in -20°C (chemical bank) and -80°C (biobank) to have a record of all the samples received and to have the possibility of further investigations. For the weekly measurement, samples are concentrated, and RNA is extracted using Maxwell RSC Enviro TNA kit (Promega). Aliquots of the extracted RNA are stored at -80°C as RNA-biobank and one aliquot is analyzed. The copy number of SARS-CoV-2 is quantified by RT-qPCR, using primers of the nucleocapsid (N) gene detect in the SARS-CoV-2 genome (previously used and verified by [Medema and colleagues (2020)](https://doi.org/10.1016/j.scitotenv.2020.142939)). The SARS-CoV-2 virus content in the wastewater is normalized using Pepper Mild Mottle Virus (PMMoV), which is an indicator of the faecal matter content ([Kitajima and colleagues (2018)](https://doi.org/10.1038/s41545-018-0019-5)). This  normalization corrects the variation of flow rate in the WWTP and population fluctuation. Positive control standards for SARS-CoV-2 and PMMoV are from IDT-DNA are used in the RT-qPCR, while negative controls are tap water (RNA extraction step) and nuclease-free water (RT-qPCR step).

The concentration method used by SEEC-KTH from the beginning of the project until week 35 of 2021 was based on their published study ([Jafferali and colleagues, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)) comparing four different concentration methods. From week 35 of 2021, the group is using [the Promega kit](https://se.promega.com/applications/virus-detection-assay-coronavirus-detection-covid-19-sars-cov-2/wastewater-based-epidemiology-covid19/) for the concentration step.

## Background: Wastewater-based epidemiology

SARS-CoV-2 virus genome can be detected in feces samples from COVID-19 patients using polymerase chain reaction (PCR) (see, for example, [Wu and colleagues, 2020](https://doi.org/10.1016/S2468-1253(20)30083-2)). Monitoring of SARS CoV-2 virus levels in wastewater from communities could therefore provide early surveillance of disease prevalence at a population-wide level, referred to as wastewater-based epidemiology ([Corpuz and colleagues, 2020](https://doi.org/10.1016/j.scitotenv.2020.140910)).

Wastewater-based epidemiology studies the amount of virus genome present in the wastewater, measured using PCR technology. Waste water, also referred too as “sewage,” includes water from households or building, kitchen sinks, toilets, showers. However, it could also include water from non-household sources (for example, rainwater and water from industrial use). Samples are periodically taken at wastewater treatment facilities, allowing to make comparisons of the viral load over time. It has previously been shown that the SARS CoV-2 virus content in wastewater can predict increases in infection in the population and follows the epidemic trend measured by the number of COVID-19 cases and hospitalization rate (see [Peccia and colleagues, 2020](https://doi.org/10.1038/s41587-020-0684-z)). During the COVID-19 pandemic, surveillance of viral RNA levels in waste water has become increasingly used to monitor and predict the spread of the disease.

Please note that the graphs presented on this page are based on preliminary and not yet completely evaluated data. The shared data should therefore be used with caution. Note also that because different sample collection and data analysis methods are used in different research projects below (i.e. for different cities), it is not possible to make comparisons of viral load across these projects (i.e. across cities). Comparisons should be made within each project (i.e. city) since the methodology remains the same for different weeks of measurement. Wastewater monitoring should primarily be seen as a monitoring system. Taken together with data for infection testing, intensive care admissions etc., it may help understanding of the regional dynamics of the COVID-19 pandemic.

## Archived data

- [Historic data for Örebro and Umeå; amount of SARS-CoV-2 in Umeå and Örebro wastewater between October 2020 and June 2021](historic_orebro_umea).
- [Historic data for Stockholm;  Gene copy number/week (raw wastewater) with bovine + PMMoV factor between April 2020 and August 2021](historic_stockholm)

<!-- <div class="alert alert-info">Date: <span id="stockholm_comment_date"></span><br>Commentary: <span id="stockholm_comment"></span></div> -->

<!-- <div class="alert alert-info">Date: <span id="malmo_comment_date"></span><br>Commentary: <span id="malmo_comment"></span></div> -->

{{< ww_dynamic_content >}}

<script src="https://cdn.jsdelivr.net/npm/vega@5.19.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.15.1"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/a203a12374154d568bf0319980870013.js?id=malmo_plot"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/8ff7c1edf2934a87a45b4db652f5cf2b.js?id=stockholm_plot"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/c07f360fc5684e2683460c0d56da964c.js?id=uppsala_plot"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/c07f360fc5684e2683460c0d56da964c.js?id=orebro_plot"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/bd6bf95d7ae34ed0a9442cfc3408c57f.js?id=umea_plot"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/26cc6ddeaf224e3aa623a67f0a06aed1.js?id=kalmar_plot"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/f0c83b41de5543fab358c60626b2b548.js?id=various_plot"></script>
