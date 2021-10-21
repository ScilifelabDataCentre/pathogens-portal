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

We present wastewater epidemiology data from various Swedish cities which have a total population of over 1.5 million people. Wastewater surveillance could prove an effective system for monitoring COVID-19 prevalence and act as an early warning system for predicting upcoming outbreaks. Note that where data for different cities are presented separately, different sample collection and data analysis methods were used. Thus, it is not necessarily possible to make direct comparisons of viral load between cities. Comparisons can be made for data presented together in plots, as the methodology used was the same (unless specifically noted otherwise). [See below for details](#background) on wastewater epidemiology.

## Map of sample collection sites

<div class="row justify-content-center mb-4"><div class="col">{{< wastewater_map >}}</div></div>

## Uppsala, Umeå, Örebro, Kalmar, and other municipalities

This project is led by associate professor Anna J. Székely (SLU, Swedish University of Agricultural Sciences) and associate professor Maja Malmberg (SLU, Swedish University of Agricultural Sciences). The project is made possible thanks to collaborations with Uppsala Vatten, Roslagsvatten, Enköpings kommun, Gästrike Vatten, TEMAB, and others.

The amount of SARS-CoV-2 virus in the Uppsala wastewater is estimated by analyzing raw wastewater collected at Kungsängsverket, Uppsala Vatten’s main treatment facility. The wastewater treated at the facility is collected by two main wastewater collection channels and covers territory inhabited by approximately 180,000 people. Please [consult this map for the exact catchment area of the two wastewater collection channels in Uppsala](/wastewater/avrinningskarta_inlopp_kungsangsverket.pdf). The amount of SARS-CoV-2 virus in the wastewater from municipalities surrounding municipalities is collected from other wastewater treatment plants. In particular, the amount of SARS-CoV-2 virus in the wastewater of Ekerö is estimated based on samples from Ekebyhov wastewater treatment plant, that of Österåker is based on Margretelund wastewater treatment plant, and that of Vaxholm is based on Blynäs wastewater treatment plant. Please [consult this map for the exact catchment area of the wastewater collection channels in Umeå](/wastewater/map_umeaa.jpg). Please [consult this map for the exact catchment area of the wastewater collection channels in Örebro](/wastewater/map_orebro.pdf).

Measurements are taken weekly, by processing a representative sample collected over 24 hours (i.e. flow compensated sample). The SARS-CoV-2 virus content of the wastewater on the given day is normalized to the fecal matter content to avoid variation from flow differences and population fluctuation. The samples are processed according to standard methods. Briefly, the viral genomic material is concentrated and extracted by the direct capture method using the Maxwell RSC Enviro TNA kit (Promega) and the copy number of SARS-CoV-2 genomes is quantified by RT-qPCR using the CDC RUO nCOV N1 assay (IDT DNA). The virus recovery efficiency of the process and the presence of potential inhibitors is monitored by adding to the samples bovine coronavirus (BCoV) as process surrogate virus. To correct for variations in population size and wastewater flow, we also quantify the pepper mild mottle virus (PMMoV) which is the most abundant RNA virus in human feces and serves as an estimator of human fecal content ([Symonds and colleagues, 2019](https://doi.org/10.1371/journal.ppat.1007639)).

Note that the scores provided in the dataset and depicted in plots below are preliminary. The team is still conducting method efficiency checks that might slightly affect the final results.

**Download the data:** [Relative ratio of copy number of SARS-CoV-2 to PPMoV, CSV file.](https://datagraphics.dckube.scilifelab.se/dataset/0ac8fa02871745048491de74e5689da9.csv) Data available starting from week 38 of 2020; updated weekly.\
**Contact:** anna.szekely@slu.se and maja.malmberg@slu.se\
**How to cite:**
Székely, A. & Mohamed, N. Dataset of SARS-CoV-2 wastewater data from Uppsala, and neighbouring towns Knivsta, Enköping, Östhammar and Älvkarleby, Sweden. [https://doi.org/10.17044/scilifelab.14256317.v1](https://doi.org/10.17044/scilifelab.14256317.v1) (2021).

<div class="alert alert-info">Last updated: <span id="last_modified_uppsala"></span></div>
<div class="alert alert-secondary small">Interacting with the plot: Click on the names of municipalities in the legend in order to select or deselect cities that are displayed. Select a portion of the plot using your cursor in order to zoom in to a particular date range or y axis range. Note that the axes ranges adapt to your selections. Double-click anywhere on the graph in order to return to the default view. It is also possible download the graph as a PNG file, zoom and reset using buttons which appear in the top right corner when you hover over the graph.</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_regular.json" height="550px" >}}</div>
</div>

Please note that the plot below displays the same data, but the y axis is shown as a log scale.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_logyaxis.json" height="550px" >}}</div>
</div>

## Stockholm

This project, led by associate professor Zeynep Cetecioglu Gurol and colleagues (KTH Royal Institute of Technology; zeynepcg@kth.se), is a collaboration between the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) and the [SEED](https://www.kth.se/en/seed) and [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196) departments at KTH, in close collaboration with Stockholm Vatten och Avfall and the Käppala Association. The sampling of wastewater, started in mid-April 2020, from Bromma, Henriksdal, and Käppala wastewater treatment plants (WWTP). These treatment plants receive wastewater from a population of approximately 360,000; 860,000 and 500,000, respectively. Please consult [this map for the exact catchment area of the wastewater collection channels in Käppala](/wastewater/map_Kappala.pdf) and [this map for the exact catchment area of the wastewater collection channels in Bromma and Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf).

After concentration, filtering, and preparation, the samples are analyzed using qPCR technique for SARS CoV-2 RNA. Primers of the nucleocapsid (N) gene were used to detect the SARS-COV-2 gene (previously used and verified by [Medema and colleagues (2020)](https://doi.org/10.1016/j.scitotenv.2020.142939)). In some cases, the raw wastewater has been frozen at –20 degrees, and  concentrated wastewater or purified RNA have been stored at -80 C before the next analysis step was carried out. The concentration method used by prof. Zeynep Cetecioglu Gurol and her colleagues from the beginning of the project until week 35 of 2021 was based on their published study ([Jafferali and colleagues, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)) comparing four different concentration methods. From week 35 of 2021, the group is using [the Promega kit](https://se.promega.com/applications/virus-detection-assay-coronavirus-detection-covid-19-sars-cov-2/wastewater-based-epidemiology-covid19/) for the concentration step.

See also [the page of the research group where summaries of data and preliminary conclusions are presented](https://www.kth.se/water/research/covid-1.979048).

**Download the data:** [Relative N gene normalized by PPMoV; Excel file](https://blobserver.dckube.scilifelab.se/blob/stockholm_wastewater_method_Sep_2021.xlsx). Results are available (partially) starting from week 16 of 2020; updated weekly.

**How to cite:**
Cetecioglu Z G, Williams, C, Khatami, K, Atasoy, M, Nandy, P, Jafferali, M H, Birgersson, M. SARS-CoV-2 Wastewater Data from Stockholm, Sweden. [https://doi.org/10.17044/scilifelab.14315483](https://doi.org/10.17044/scilifelab.14315483) (2021).

<div class="alert alert-info">Last updated: <span id="last_modified_stockholm"></span></div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_stockholm.json" height="550px" >}}</div>
</div>

Please note that the plot below displays the same data, but the y axis is shown as a log scale and only data starting from January 2021 is displayed.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_stockholm_logyaxis.json" height="550px" >}}</div>
</div>

<div class="row ml-0 mt-3"><b>Publications:</b></div><div class="row"><div class="col">
<b><a target="_blank" href="https://doi.org/10.1016/j.scitotenv.2020.142939">Benchmarking virus concentration methods for quantification of SARS-CoV-2 in raw wastewater.</a></b><br>
                    <span class="text-muted">Jafferali MH, Khatami K, Atasoy M, Birgersson M, Williams C, Cetecioglu Z.</span><br>
                    <i>Science of The Total Environment</i> 755. DOI: 10.1016/j.scitotenv.2020.142939
</div></div>

## Archived data

- [Historic data for Örebro and Umeå; amount of SARS-CoV-2 in Umeå and Örebro wastewater between October 2020 and June 2021](historic_orebro_umea).
- [Historic data for Stockholm;  Gene copy number/week (raw wastewater) with bovine + PMMoV factor between April 2020 and August 2021](historic_stockholm)

## Background: Wastewater-based epidemiology

SARS-CoV-2 virus genome can be detected in feces samples from COVID-19 patients using polymerase chain reaction (PCR) (see, for example, [Wu and colleagues, 2020](https://doi.org/10.1016/S2468-1253(20)30083-2)). Monitoring of SARS CoV-2 virus levels in wastewater from communities could therefore provide early surveillance of disease prevalence at a population-wide level, referred to as wastewater-based epidemiology ([Corpuz and colleagues, 2020](https://doi.org/10.1016/j.scitotenv.2020.140910)).

Wastewater-based epidemiology studies the amount of virus genome present in the wastewater, measured using PCR technology. Waste water, also referred too as “sewage,” includes water from households or building, kitchen sinks, toilets, showers. However, it could also include water from non-household sources (for example, rainwater and water from industrial use). Samples are periodically taken at wastewater treatment facilities, allowing to make comparisons of the viral load over time. It has previously been shown that the SARS CoV-2 virus content in wastewater can predict increases in infection in the population and follows the epidemic trend measured by the number of COVID-19 cases and hospitalization rate (see [Peccia and colleagues, 2020](https://doi.org/10.1038/s41587-020-0684-z)). During the COVID-19 pandemic, surveillance of viral RNA levels in waste water has become increasingly used to monitor and predict the spread of the disease.

Please note that the graphs presented on this page are based on preliminary and not yet completely evaluated data. The shared data should therefore be used with caution. Note also that because different sample collection and data analysis methods are used in different research projects below (i.e. for different cities), it is not possible to make comparisons of viral load across these projects (i.e. across cities). Comparisons should be made within each project (i.e. city) since the methodology remains the same for different weeks of measurement. Wastewater monitoring should primarily be seen as a monitoring system. Taken together with data for infection testing, intensive care admissions etc., it may help understanding of the regional dynamics of the COVID-19 pandemic.

{{< ww_dates_modified >}}
