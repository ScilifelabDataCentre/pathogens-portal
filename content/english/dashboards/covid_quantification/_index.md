---
title: SARS-CoV-2 quantification
banner: /dashboard_thumbs/wastewater_sars-cov2.png
description: Explore SARS-CoV-2 levels in wastewater across Sweden. Weekly data from SLU-SEEC tracks COVID-19 trends, covering 43% of the population, and aids in outbreak prediction.
menu:
  dashboard_menu:
    identifier: wastewater_SARS-CoV-2_quantification
    name: "Wastewater: SARS-CoV-2 Quantification"
plotly: true
aliases:
  - /dashboards/wastewater/covid_quant_slu/
  - /dashboards/wastewater/covid_quantification/
  - /dashboards/wastewater/covid_quantification/covid_quant_slu/
dashboards_topics: [Wastewater Surveillance, COVID-19, Infectious diseases, Epidemiology]
data_status: "updating"
---


## Introduction

Severe acute respiratory syndrome coronavirus 2 (SARS CoV 2) is a positive-sense single-stranded RNA virus that causes COVID-19 (coronavirus disease 2019), the respiratory illness responsible for the COVID-19 pandemic. SARS-CoV-2 was first identified in the city of Wuhan, Hubei, China, and the World Health Organization (WHO) declared a public health emergency of international concern from January 30, 2020, to May 5, 2023. For more information about symptoms, risks and vaccination against SARS-CoV-2, visit the corresponding site of the [Swedish Public Health Agency](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/covid-19/).

Beside respiratory droplets and aerosols, SARS-CoV-2 viral particles, like many other human coronaviruses, are also excreted in the stools of infected individuals. This enables the possibility for SARS-CoV-2 virus to be detected in wastewater and population-level infection trends of COVID-19 to be followed by wastewater-based epidemiology (WBE).

The data presented on this page is generated in the SLU (Swedish University of Agricultural Sciences) laboratories of SEEC (Swedish Environmental Epidemiology Center). The data and visualisation on this page are usually updated weekly, typically on Mondays. Please refer to the [Methods](#methods) for details on measurements and calculations. All related dashboards can be found on the [Wastewater Surveillance](/dashboards/topics/wastewater-surveillance/) page, and sampling sites and project details are available in the [Wastewater Monitoring Background](/dashboards/wastewater_background/).

<div class="alert alert-info">
<b>Important Note:</b></br>
The scores provided in the dataset and depicted in the plot below are preliminary, so corrections and changes may occur. Data and information about the group on this dashboard are updated frequently, so please check back regularly to stay up to date. </br>Please note that although the same methods are used for all cities shown on this tab, differences in the wastewater collection systems and populations of different cities might bias direct comparisons between cities.
</div>

## Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_uppsala"></span></div>

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

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 1200px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_combined_slu_regular.json" height="800px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/combined_slu_regular.py).

## Commentary from the research group

<div><b>Date:</b> <span id="slu_comment_date"></span><br><b>Commentary:</b> <span id="slu_comment"></span></div>

{{< ww_dynamic_content >}}

## Reports from the research group

The group provide reports to summarise their latest findings. The latest report is available [here](https://blobserver.dc.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU.pdf) (only available in Swedish).

## Dataset

**Contact:** <anna.szekely@slu.se> and <javier.vargas@slu.se>

**Download the data:** [Respiratory virus gene copy numbers normalised per PMMoV gene copy number.CSV file.](https://blobserver.dc.scilifelab.se/blob/SLU_wastewater_data.csv). Data are available from week 38 of 2020; updated weekly.

**How to cite the dataset:**

Székely, A. J., Malmberg, M., Vargas, J., Mohamed, N., Dafalla, I., Petrini, F., Davies, L. (2023). Dataset of SARS-CoV-2, influenza A and influenza B virus content in wastewater samples from wastewater treatment plants in Sweden. <https://doi.org/10.17044/scilifelab.14256317>.

## Methods

Wastewater is collected from several different treatment plants around the country. For more information about the treatment plants, visit the page about [the background of wastewater surveillance](/dashboards/wastewater_background/). For most cities represented on this page, raw, untreated wastewater samples that are representative of a single day are collected by flow compensated samplers at the wastewater treatment plants (WWTP). Uppsala is the exception, with all measurements since week 16 of 2021 instead representing 1 week. In Uppsala, samples are collected daily, and then combined flow-proportionally into one composite weekly sample for the purpose of analyses.

The freshly collected samples are processed according to standard methodologies. For samples collected up to and including week 18 of 2021, viral particles were concentrated using the electronegative filtration method ([Ahmed _et al._, 2020](https://www.sciencedirect.com/science/article/pii/S004896972033480X)). Since week 19 of 2021, the viral genomic material has instead been concentrated and extracted by the direct capture method, using the Maxwell RSC Enviro TNA kit (Promega).

Absolute quantification of the copy numbers of the SARS-CoV-2 genome is performed using One-Step RT-qPCR. Until week 31 of 2023 the quantification of the viral genomes was performed using the [SARS-CoV-2 specific N1 assay from the Centers for Disease Control and Prevention (CDC)](https://www.fda.gov/media/134922/download). From week 32 of 2023 quantification is performed using the Flu SC2 Multiplex Assay (CDC). To correct for variations in population size and wastewater flow, the pepper mild mottle virus (PMMoV) is quantified using a modified version of the assay of [Zhang _et al._ (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV is an abundant RNA virus in human faeces and serves as an estimator of human faecal content ([Symonds _et al._, 2019](https://doi.org/10.1371/journal.ppat.1007639)). For more details about the sample processing method, and the evaluation of the use of the PMMoV normalisation method for Swedish wastewater, please refer to the corresponding publication: [Isaksson _et al._ (2022)](https://www.mdpi.com/2076-3298/9/3/39).

The data in the graphs and datafile is presented in three different formats:
- **PMMoV normalised SARS-CoV2 content** represents the ratio of the copy numbers of SARS-CoV2 and PMMoV measured by the SARS-CoV2 assay and PMMoV-assays, respectively, multiplied by 1000. As the SARS-CoV2 assay provides proxies for SARS-CoV2 virus content in the wastewater and PMMoV is a proxy of the faecal content (which is related to the contributing population), the ratio of the two can be considered to be a proxy for the prevalence of SARS-CoV2 infections in the population of the wastewater catchment area.
- **SARS-CoV2 genome copies concentration** presents the SARS-CoV2 copy number concentration measured in the wastewater. These data is influenced by the setup of the different wastewater collection nsystems and is therefore not suitable for comparison betwwen sites. The virus concentrations in the wastewater are also influenced by the weather events that impact wastewater flow (e.g., heavy rain or snow melt).
- **SARS-CoV2 genome copies/day/inhabitant** represents the daily virus amount estimated in the wastewater normalized for the number of inhabitants connected to the system. These data allows for comparison of different sites but some delays in the presentation of these data may occur compared to the other.

**How to cite the method:**

Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. _Environments_, _9_, 39. <https://doi.org/10.3390/environments9030039>.

## Related data

- SARS-CoV-2 variant analysis from wastewater (data available in the European Nucleotide Archive (ENA) under project number [PRJEB60156](https://www.ebi.ac.uk/ena/browser/view/PRJEB60156)): The group at SLU analysed samples from Uppsala, Örebro, Umeå, and Kalmar (2021-2022).


## Archived data from SLU

- [Historic data for Örebro and Umeå; amount of SARS-CoV-2 in Umeå and Örebro wastewater between October 2020 and June 2021](/dashboards/covid_quantification/historic_orebro_umea).
- [Historic SARS-CoV-2 data in wastewater from SEEC-SLU](/dashboards/covid_quantification/historic_covid_SLU)

## Quantification of SARS-CoV-2 by other groups

Other groups also quantified SARS-CoV-2 in wastewater in Sweden. The groups used different methods to quantify SARS-CoV-2 and, in some cases, measured different areas of Sweden. All of the data from the groups below is historic:

- [**Gothenburg university (GU):**](/dashboards/covid_quantification/covid_quant_gu/) Quantification of the level of SARS-CoV-2 in wastewater from Gothenburg by the Norder group at GU.

- [**SEEC-KTH node:**](/dashboards/covid_quantification/covid_quant_kth/) Quantification of the levels of SARS-CoV-2 in wastewater from Stockholm and Malmö by the SEEC-KTH node (no longer updated after June 2023, historic data is available).


