---
title: Data from SEEC-KTH
toc: true
plotly: true
---
On this page we present wastewater epidemiology data obtained from analyses conducted by the [Swedish Environmental Epidemiology Center](https://www.scilifelab.se/pandemic-response/pandemic-laboratory-preparedness/swedish-environmental-epidemiology-center-seec/) (SEEC) node at the KTH Royal Institute of Technology. SEEC-KTH is led by associate professor Zeynep Cetecioglu Gurol (zeynepcg@kth.se). SEEC-KTH analyzes wastewater samples from Samples from Stockholm (Bromma, Henriksdal, and Käppala wastewater treatment plants; [see catchment area of Käppala](/wastewater/map_Kappala.pdf), [see catchment area of Bromma and Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf)) and Malmö (Sjölunda wastewater treatment plant; [see catchment area map](/wastewater/sjolunda.pdf)). For data from other Swedish cities [see this page](../).

## Comments on the recent wastewater measurements performed by SEEC-KTH

<div><b>Date:</b> <span id="kth_comment_date"></span><br><b>Commentary:</b> <span id="kth_comment"></span></div>

## Full dataset by SEEC-KTH

### Stockholm

**Last updated:** <span id="last_modified_stockholm"></span> \
**Download the data:** [Excel file](https://blobserver.dckube.scilifelab.se/blob/stockholm_wastewater_method_Sep_2021.xlsx). Results are available (partially) starting from week 16 of 2020; updated weekly.

<div class="alert alert-secondary small">Interacting with the plot: Click on the names of municipalities in the legend in order to select or deselect cities that are displayed. Select a portion of the plot using your cursor in order to zoom in to a particular date range or y axis range. Note that the axes ranges adapt to your selections. Double-click anywhere on the graph in order to return to the default view. It is also possible download the graph as a PNG file, zoom and reset using buttons which appear in the top right corner when you hover over the graph.</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_stockholm.json" height="550px" >}}</div>
</div>

Please note that the plot below displays the same data, but the y axis is shown as a log scale and only data starting from January 2021 is displayed.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_stockholm_logyaxis.json" height="550px" >}}</div>
</div>

### Malmö

**Last updated:** <span id="last_modified_malmo"></span> \
**Download the data:** [Excel file](https://blobserver.dckube.scilifelab.se/blob/stockholm_wastewater_method_Sep_2021.xlsx); results are available starting from week 39 of 2021; updated weekly.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>
<div class="plot_wrapper">
  <div class="table-responsive" id="malmo_plot"></div>
</div>

## Analysis method used by SEEC-KTH

The samples are analyzed at KTH Royal Institute of Technology node as a collaboration between the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) and the [KTH Water Centre](https://www.kth.se/water), [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196), and [Protein Science](https://www.kth.se/pro/protein-science-1.784558) departments at KTH, in close collaboration with Stockholm Vatten och Avfall and the Käppala Association. Three collection channels (Järva, Hässelby and Riksby) are analyzed in Bromma and two (Henriskdal and Sickla) are analyzed in Henriksdal treatment plant.

One-day representative samples (collected over 24 hours) are received every week from the three WWTP. An aliquot of the samples is analyzed weekly and another two aliquots are kept in -20°C (chemical bank) and -80°C (biobank) to have a record of all the samples received and to have the possibility of further investigations. For the weekly measurement, samples are concentrated, and RNA is extracted using Maxwell RSC Enviro TNA kit (Promega). Aliquots of the extracted RNA are stored at -80°C as RNA-biobank and one aliquot is analyzed. The copy number of SARS-CoV-2 is quantified by RT-qPCR, using primers of the nucleocapsid (N) gene detect in the SARS-CoV-2 genome (previously used and verified by [Medema and colleagues (2020)](https://doi.org/10.1016/j.scitotenv.2020.142939)). The SARS-CoV-2 virus content in the wastewater is normalized using Pepper Mild Mottle Virus (PMMoV), which is an indicator of the faecal matter content ([Kitajima and colleagues (2018)](https://doi.org/10.1038/s41545-018-0019-5)). This  normalization corrects the variation of flow rate in the WWTP and population fluctuation. Positive control standards for SARS-CoV-2 and PMMoV are from IDT-DNA are used in the RT-qPCR, while negative controls are tap water (RNA extraction step) and nuclease-free water (RT-qPCR step).

The concentration method used by SEEC-KTH from the beginning of the project until week 35 of 2021 was based on their published study ([Jafferali and colleagues, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)) comparing four different concentration methods. From week 35 of 2021, the group is using [the Promega kit](https://se.promega.com/applications/virus-detection-assay-coronavirus-detection-covid-19-sars-cov-2/wastewater-based-epidemiology-covid19/) for the concentration step.

## Publications

<div class="row"><div class="col">
<b><a target="_blank" href="https://doi.org/10.1016/j.scitotenv.2020.142939">Benchmarking virus concentration methods for quantification of SARS-CoV-2 in raw wastewater.</a></b><br>
                    <span class="text-muted">Jafferali MH, Khatami K, Atasoy M, Birgersson M, Williams C, Cetecioglu Z.</span><br>
                    <i>Science of The Total Environment</i> 755. DOI: 10.1016/j.scitotenv.2020.142939
</div></div>

## Archived data

- [Historic data for Stockholm;  Gene copy number/week (raw wastewater) with bovine + PMMoV factor between April 2020 and August 2021](historic_stockholm)

{{< ww_dynamic_content >}}

<script src="https://cdn.jsdelivr.net/npm/vega@5.19.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.15.1"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/a203a12374154d568bf0319980870013.js?id=malmo_plot"></script>
