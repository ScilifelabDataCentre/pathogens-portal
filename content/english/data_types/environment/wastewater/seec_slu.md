---
title: Data from SEEC-SLU
toc: true
plotly: true
---
On this page we present wastewater epidemiology data obtained from analyses conducted by the [Swedish Environmental Epidemiology Center](https://www.scilifelab.se/pandemic-response/pandemic-laboratory-preparedness/swedish-environmental-epidemiology-center-seec/) (SEEC) node at the Swedish University of Agricultural Sciences. SEEC-SLU is led by associate professor Anna J. Székely (anna.szekely@slu.se) and associate professor Maja Malmberg (maja.malmberg@slu.se). SEEC-SLU analyzes wastewater samples from Samples from Uppsala, Örebro, Umeå, Kalmar, Ekerö, Enköping, Knivsta, Tierp, Vaxholm, Älvkarleby, and Österåker, Östhammar. For data from other Swedish cities [see this page](../).

The amount of SARS-CoV-2 virus in the Uppsala wastewater is estimated by analyzing raw wastewater collected at Kungsängsverket, Uppsala Vatten’s main treatment facility. The wastewater treated at the facility is collected by two main wastewater collection channels and covers territory inhabited by approximately 180,000 people. Please [consult this map for the exact catchment area of the two wastewater collection channels in Uppsala](/wastewater/avrinningskarta_inlopp_kungsangsverket.pdf). The amount of SARS-CoV-2 virus in the wastewater from municipalities surrounding municipalities is collected from other wastewater treatment plants. In particular, the amount of SARS-CoV-2 virus in the wastewater of Ekerö is estimated based on samples from Ekebyhov wastewater treatment plant, that of Österåker is based on Margretelund wastewater treatment plant, and that of Vaxholm is based on Blynäs wastewater treatment plant. Please [consult this map for the exact catchment area of the wastewater collection channels in Umeå](/wastewater/map_umeaa.jpg). Please [consult this map for the exact catchment area of the wastewater collection channels in Örebro](/wastewater/map_orebro.pdf).

## Commentary on the recent wastewater measurements performed by SEEC-SLU

<div><b>Date:</b> <span id="slu_comment_date"></span><br><b>Commentary:</b> <span id="slu_comment"></span></div>

## Full dataset by SEEC-SLU

**Last updated:** <span id="last_modified_uppsala"></span> \
**Download the data:** [Relative ratio of copy number of SARS-CoV-2 to PPMoV, CSV file](https://datagraphics.dckube.scilifelab.se/api/dataset/0ac8fa02871745048491de74e5689da9.csv); data available starting from week 38 of 2020; updated weekly.

The graph below allows for comparison of SARS-CoV-2 levels in wastewater across wastewater treatment plants.

<div class="alert alert-secondary small">Interacting with the plot: Click on the names of municipalities in the legend in order to select or deselect cities that are displayed. Select a portion of the plot using your cursor in order to zoom in to a particular date range or y axis range. Note that the axes ranges adapt to your selections. Double-click anywhere on the graph in order to return to the default view. It is also possible download the graph as a PNG file, zoom and reset using buttons which appear in the top right corner when you hover over the graph.</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_regular.json" height="550px" >}}</div>
</div>

Please note that the plot below displays the same data, but the y axis is shown as a log scale.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_logyaxis.json" height="550px" >}}</div>
</div>

## Analysis method used by SEEC-SLU

The project is made possible thanks to collaborations with Uppsala Vatten, Roslagsvatten, Enköpings kommun, Gästrike Vatten, TEMAB, and others.

Measurements are taken weekly, by processing a representative sample collected over 24 hours (i.e. flow compensated sample). The SARS-CoV-2 virus content of the wastewater on the given day is normalized to the fecal matter content to avoid variation from flow differences and population fluctuation. The samples are processed according to standard methods. Briefly, the viral genomic material is concentrated and extracted by the direct capture method using the Maxwell RSC Enviro TNA kit (Promega) and the copy number of SARS-CoV-2 genomes is quantified by RT-qPCR using the CDC RUO nCOV N1 assay (IDT DNA). The virus recovery efficiency of the process and the presence of potential inhibitors is monitored by adding to the samples bovine coronavirus (BCoV) as process surrogate virus. To correct for variations in population size and wastewater flow, we also quantify the pepper mild mottle virus (PMMoV) which is the most abundant RNA virus in human feces and serves as an estimator of human fecal content ([Symonds and colleagues, 2019](https://doi.org/10.1371/journal.ppat.1007639)).

## Archived data

- [Historic data for Örebro and Umeå; amount of SARS-CoV-2 in Umeå and Örebro wastewater between October 2020 and June 2021](historic_orebro_umea).

{{< ww_dynamic_content >}}
