---
title: Amount of SARS-CoV-2 in wastewater (SEEC-SLU)
plotly: true
---

<div class="mt-3">
  <a href="/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Go back to SARS-CoV-2 quantification within the wastewater epidemiology dashboard</a>
</div>
<br>

## Introduction

The data presented on this page is generated in the SLU (Swedish University of Agricultural Sciences) laboratories of SEEC (Swedish Environmental Epidemiology Center). The project is part of [SciLifeLab's Pandemic Laboratory Preparedness (PLP) Program](/resources/), and is led by associate professor Anna J. Székely (Department of Aquatic Sciences and Assessment, SLU). Wastewater analyses are overseen by Anna J. Székely and associate professor Maja Malmberg (Virology unit of Department of Biomedical Science and Veterinary Public Health, SLU). This page pertains to the quantification of the levels of SARS-CoV-2 virus in multiple cities across Sweden. This project currently has the broadest geographic coverage across Sweden; generating data for an additional 22% of the Swedish population.

The data and visualisation on this page are usually updated weekly, typically on Fridays. Please note that the scores provided in the dataset and depicted in plot below are preliminary, so corrections and changes may occur. Data and information about the group on this dashboard are updated frequently, so please check back regularly to stay up to date.

## Wastewater collection sites

SLU-SEEC collect and analyse samples from multiple areas. The below table shows details about each of these sites. The table lists the towns/cities monitored, wastewater treatment plants (WWTP) that samples were collected from, the number of people in the catchment area (Number of people), and the dates that monitoring by SLU-SEEC started and ended monitoring (Start and End date, respectively). A value of 'null' for the end date indicates that collection is ongoing. An asterisk next to the number of people indicates that the figure is preliminary.  

  <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_slusites.json" height="775px" >}}</div>
</div>

<!-- <p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample1" role="button" aria-expanded="false" aria-controls="collapseExample1">
    Genomics data
  </a>
</p>
<div class="collapse" id="collapseExample1">
  <div class="card card-body">
  <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_slusites.json" height="775px" width="800px" >}}</div>
</div>
  </div>
</div> -->

<!-- <button type="button" class="btn btn-sm btn-outline-secondary mb-2" data-bs-toggle="modal" data-bs-target="#interactiveFeaturesModal">
  How to use the interactive features of the plot
</button> -->

<!-- <div class="modal fade" id="interactiveFeaturesModal" tabindex="-1" aria-labelledby="interactiveFeaturesModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="interactiveFeaturesModalLabel">Information on how to use the interactive features of the plot</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_slusites.json" height="600px" >}}</div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div> -->

## Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_uppsala"></span></div>

<b>Important note:</b> Historical data for Knivsta, Vaxholm, and Österåker are available in the dataset (linked below). However, they are no longer included in the visualisation.

Please note that although the same methods are used for all cities shown on this tab, differences in the wastewater collection systems and populations of different cities might bias direct comparisons between cities.

<button type="button" class="btn btn-sm btn-outline-secondary mb-2" data-bs-toggle="modal" data-bs-target="#interactiveFeaturesModal">
  How to use the interactive features of the plot
</button>

<div class="modal fade" id="interactiveFeaturesModal" tabindex="-1" aria-labelledby="interactiveFeaturesModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="interactiveFeaturesModalLabel">Information on how to use the interactive features of the plot</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>The line plots on this page have multiple interactive features. You can use the features to view the data in them in different ways. For example, you can choose to view data only within a certain time period, or from a given collection site. Below, we explain how to use different interactive features to meet your needs.</p>
        <h6>View data from particular sites</h6>
        <p>To view only data from a single site, double click on the name on that site in the legend to the right. To toggle data from a site on/off, single click on the name in the legend. If the data is 'deselected', the name will appear 'greyed out' in the legend, and it will not be displayed on the graph. Initially, all data will be 'selected'. To 'deselect' all data, use the 'Deselect all areas' button. You can use the 'Reselect all areas' button to 'select' data from every site (i.e. return to the default view).</p>
        <h6>View only certain y- and/or x-axes ranges</h6>
        <p>In the below plots, the y-axis represents the copy number of SARS-CoV-2 relative to PMMoV while the x-axis represents the date. If you would like to view values within a given range of the values on the axes, you can do this by clicking and dragging with your mouse. For example, to view all data within a given timeframe, you can click near the start date on the x-axis and drag to create a rectangle that encompasses the whole y-axis and the range of dates on the x-axis that you want to view. The plot will then zoom into the range that you selected.</p>
        <h6>Accurately read data values</h6>
        <p>It is difficult to accurately read the exact values of data from a graph. In order to view the exact data values, hover over the data point of interest. A box will appear that shows the y-axis values for all sites on that date (i.e. that x-axis value).</p>
        <h6>Other features</h6>
        <p>If you hover your cursor over the plot, you will see some additional options as grey icons in the top right. You can use these features to zoom in/out of the plot (using the + and - icons), and scale the axes so that the data from the 'selected' sites are shown on the most appropriate axes (this can be done using the autoscale or reset axes icons, which look like a box containing arrows and a house, respectively).</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_regular.json" height="550px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/combined_slu_regular.py).

## Commentary from the research group

<div><b>Date:</b> <span id="slu_comment_date"></span><br><b>Commentary:</b> <span id="slu_comment"></span></div>

{{< ww_dynamic_content >}}

## Reports from the research group

The group provide reports to summarise their latest findings. The latest report is available [here](https://blobserver.dckube.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU). 

## Dataset

**Contact:** anna.szekely@slu.se and maja.malmberg@slu.se

**Download the data:** [N1-gene copy number per PMMoV gene copy number, CSV file.](https://datagraphics.dckube.scilifelab.se/dataset/0ac8fa02871745048491de74e5689da9.csv). Data are available from week 38 of 2020; updated weekly.

**How to cite the dataset:**

Székely, A. J., Vargas, J., Mohamed, N., Dafalla, I., Malmberg, M. (2021). Dataset of SARS-CoV-2 wastewater data from various towns in Sweden. [https://doi.org/10.17044/scilifelab.14256317](https://doi.org/10.17044/scilifelab.14256317).

**How to cite the method:**

Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. *Environments*, *9*, 39. [https://doi.org/10.3390/environments9030039](https://doi.org/10.3390/environments9030039).

## Methods

For most cities represented on this page, raw, untreated wastewater samples that are representative of a single day are collected by flow compensated samplers at the wastewater treatment plants (WWTP). Uppsala is the exception, with all measurements since week 16 of 2021 instead representing 1 week. In Uppsala, samples are collected daily, and then combined flow-proportionally into one composite weekly sample for the purpose of analyses.

The freshly collected samples are processed according to standard methodologies. For samples collected up to and including week 18 of 2021, viral particles were concentrated using the electronegative filtration method ([Ahmed *et al.*, 2020](https://www.sciencedirect.com/science/article/pii/S004896972033480X)). Since week 19 of 2021, the viral genomic material has instead been concentrated and extracted by the direct capture method, using the Maxwell RSC Enviro TNA kit (Promega). Absolute quantification of the copy numbers of the SARS-CoV-2 genome is performed using the [SARS-CoV-2 specific N1 assay from the Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/coronavirus/2019-ncov/lab/rt-pcr-panel-primer-probes.html). To correct for variations in population size and wastewater flow, the group quantifies the pepper mild mottle virus (PMMoV) using a modified version of the assay of [Zhang *et al.* (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV is an abundant RNA virus in human faeces and serves as an estimator of human faecal content ([Symonds *et al.*, 2019](https://doi.org/10.1371/journal.ppat.1007639)). For more details about the sample processing method, and the evaluation of the use of the PMMoV normalisation method for Swedish wastewater, please refer to the corresponding publication: [Isaksson *et al.* (2022)](https://www.mdpi.com/2076-3298/9/3/39).

The data in the below graph and datafile represent the ratio of the copy numbers measured by the N1 and PMMoV-assays, multiplied by 10<sup>4</sup>. As N1 copy number is a proxy for SARS-CoV-2 virus content in the wastewater and PMMoV is a proxy of the faecal content (which is related to the contributing population), the ratio of the two can be considered to be a proxy for the prevalence of COVID-19 infections in the population of the wastewater catchment area.

## Archived data

- [Historic data for Örebro and Umeå; amount of SARS-CoV-2 in Umeå and Örebro wastewater between October 2020 and June 2021](/dashboards/wastewater/historic_orebro_umea).

<br>
<div class="mt-3">
  <a href="/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Go back to SARS-CoV-2 quantification within the wastewater epidemiology dashboard</a>
</div>
