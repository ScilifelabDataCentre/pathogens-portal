---
title: Amount of SARS-CoV-2 in wastewater (SEEC-KTH)
plotly: true
---

<div class="mt-3">
  <a href="/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"><font size="+1.75"></i> Go back to SARS-CoV-2 quantification within the wastewater epidemiology dashboard</a></font>
</div>
<br>

## Introduction

This project is led by associate professor Zeynep Cetecioglu Gurol and colleagues at KTH Royal Institute of Technology (KTH). This group of researchers are known as SEEC-KTH. The project was established as a collaboration between the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19), and the [SEED](https://www.kth.se/en/seed) and [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196) departments at KTH. The project is now funded as part of the SciLifeLab Pandemic Laboratory Preparedness (PLP) Program. More information about the PLP program can be found in our [resources section](/resources/).

The data and visualisations on this page are usually updated weekly, typically on Fridays. Data and information about the group on this dashboard are updated frequently, so please check back regularly to stay up to date.

## Wastewater collection sites

The analysis of wastewater samples from Stockholm by SEEC-KTH is done in close collaboration with Stockholm Vatten och Avfall, and the Käppala Association. SEEC-KTH began to sample wastewater in mid-April 2020, and samples were collected from the Bromma, Henriksdal, and Käppala wastewater treatment plants. These plants receive wastewater from a population of approximately 360,000, 860,000, and 500,000 people, respectively. Please consult [this map](/wastewater/map_Kappala.pdf) for the exact catchment area of the wastewater collection channels in Käppala and [this map](/wastewater/map_Bromma_Henriksdal.pdf) for the exact catchment area of the wastewater collection channels in Bromma and Henriksdal.

SEEC-KTH began to collect and wastewater samples from the Sjölunda wastewater treatment plant in Malmö in week 39 of 2021. This wastewater plant services the majority of Malmö, as well as the Burlöv municipality and parts of the municipalities of Lomma, Staffanstorp, and Svedala. Around 300,000 people live in the catchment area of this wastewater treatment plant. More information about the catchment area, including a map, can be [downloaded directly](/wastewater/sjolunda.pdf).

## Visualisations

Please note that the visualisations below show data for the most recent 16 weeks for which data are available. This does not represent all of the data that are available. Please refer to the datasets above to see all of the data available over time.

Please also note that although the same methods are used for all cities shown on this tab, differences in the wastewater collection systems and populations of different cities might bias direct comparisons between cities.

### Stockholm

<div class="alert alert-info">Last updated: <span id="last_modified_stockholm"></span></div>

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
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/test_new_ww_sthlm.json" height="550px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/combined_stockholm_regular.py).

### Malmö

<div class="alert alert-info">Last updated: <span id="last_modified_malmo"></span></div>

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_kthmalmö.json" height="550px" >}}</div>
</div>

**Code used to produce plot:** [ADD PLOT SCRIPT!!](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/combined_slu_regular.py).

## Commentary from the research group

<div><b>Date:</b> <span id="kth_comment_date"></span><br><b>Commentary:</b> <span id="kth_comment"></span></div>

{{< ww_dynamic_content >}}

## Dataset

**Download the data:** [N3-gene copy number per PMMoV gene copy number; Excel file](https://blobserver.dckube.scilifelab.se/blob/stockholm_wastewater_method_Sep_2021.xlsx). Results are available (partially) starting from week 16 of 2020 for Stockholm and starting from week 39 of 2021 for Malmö; updated weekly.\
**Contact:** zeynepcg@kth.se

**How to cite dataset:**
Cetecioglu, Z. G., Williams, C., Khatami, K., Atasoy, M., Nandy, P., Jafferali, M. H., Birgersson, M. (2021). SARS-CoV-2 Wastewater Data from Stockholm, Sweden. [https://doi.org/10.17044/scilifelab.14315483](https://doi.org/10.17044/scilifelab.14315483).

## Methods

 To correct for variations in population size and wastewater flow, the group quantifies the pepper mild mottle virus (PMMoV) using a modified version of the assay of [Zhang *et al.* (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV is an abundant RNA virus in human faeces and serves as an estimator of human faecal content ([Symonds *et al.*, 2019](https://doi.org/10.1371/journal.ppat.1007639)). SARS-like virus specific N3-primers ([Lu *et al.*, 2020](https://doi.org/10.3201/eid2608.201246)) with SYBR Green chemistry ([Perez-Zabaleta *et al.*, 2023](https://doi.org/10.1016/j.scitotenv.2022.160023)) are used to quantify SARS-CoV-2.

After concentration, filtering, and preparation, the samples are analysed using the qPCR technique for SARS CoV-2 RNA. Primers of the nucleocapsid (N) gene were used to detect the SARS-COV-2 gene (previously used and verified by [Medema *et al.* (2020)](https://doi.org/10.1021/acs.estlett.0c00357)). In some cases, raw wastewater samples were frozen at -20℃, and concentrated wastewater or purified RNA samples were sometimes stored at -80℃ before the next analysis step was carried out. The concentration method initially used by SEEC-KTH was based on one of their earlier studies ([Jafferali *et al.*, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)), which compared four different concentration methods. This method was used until week 35 of 2021. After this time, the group began to instead use [the Promega kit](https://se.promega.com/applications/virus-detection-assay-coronavirus-detection-covid-19-sars-cov-2/wastewater-based-epidemiology-covid19/) for the concentration step.

## Archived data

- [Historic data for Stockholm; Gene copy number/week (raw wastewater) with bovine + PMMoV factor between April 2020 and August 2021](/dashboards/wastewater/historic_stockholm).

<br>
<div class="mt-3">
  <a href="/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"><font size="+1.75"></i> Go back to SARS-CoV-2 quantification within the wastewater epidemiology dashboard</a></font>
</div>
