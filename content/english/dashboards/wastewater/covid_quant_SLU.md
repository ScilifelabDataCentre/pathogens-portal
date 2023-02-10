---
title: The amount of SARS-CoV-2 virus in wastewater across Sweden
toc: false
type: wastewater
menu:
    wastewater:
        name: COVID quantification at SLU
        weight: 30
plotly: true
---

## Introduction

This page includes information about and data from the wastewater epidemiology project led by associate professor Anna J. Székely (SLU, Swedish University of Agricultural Sciences) and associate professor Maja Malmberg (SLU) at SLU. This page pertains in particular to the quantification of the levels of COVID-19 infections in multiple cities across Sweden. Regular wastewater monitoring by this group started in Uppsala in August 2020, but many other sites have been added since then.

The data and visualisation on this page are usually updated weekly, typically on Fridays. The other information provided here is also regularly updated, so please check back frequently for all of the latest progress on this project.

## Methods

For most cities represented on this page, raw, untreated wastewater samples that are representative of a single day are collected by flow compensated samplers at the wasterwater treatment plants. Uppsala is the exception, with all measurements since week 16 of 2021 instead representing 1 week. In Uppsala, samples are collected daily, and then combined flow-proportionally into one composite weekly sample for the purpose of testing.

The samples are processed according to standard methodologies. Briefly, the viral genomic material is concentrated and extracted by the direct capture method using the Maxwell RSC Enviro TNA kit (Promega). The copy number of SARS-CoV-2 genomes is quantified by RT-qPCR using the CDC RUO nCOV N1 assay (IDT DNA). To correct for variations in population size and wastewater flow, we also quantify the pepper mild mottle virus (PMMoV), which is the most abundant RNA virus in human faeces. This means that the quantification can be used to estimate human faecal content ([Symonds *et al.*, 2019](https://doi.org/10.1371/journal.ppat.1007639)). For more detail about the evaluation of this normalisation method, please refer to the corresponding publication: [Isaksson *et al.* (2022)](https://doi.org/10.3390/environments9030039).

The data in the below graph and datafile represent the ratio of the copy numbers measured by the N1 and PMMoV-assays, multiplied by 10<sup>4</sup>. As N1 copy number is a proxy for SARS-CoV-2 virus content in the wastewater and PMMoV is a proxy of the fecal content (which is related to the contributing population), the ratio of the two can be considered to be a proxy for the prevalence of COVID-19 infections in the population of the wastewater catchment area.

Please note that the scores provided in the dataset and depicted in plot below are preliminary. The team is still conducting method efficiency checks that might slightly affect the final results.

## Dataset

**Contact:** anna.szekely@slu.se and maja.malmberg@slu.se

**Download the data:** [N1-gene copy number per PMMoV gene copy number, CSV file.](https://datagraphics.dckube.scilifelab.se/dataset/0ac8fa02871745048491de74e5689da9.csv). Data are available from week 38 of 2020; updated weekly.

**How to cite the dataset:**

Székely, A. J., Mohamed, N., Dafalla, I., Vargas, J., Malmberg, M. (2021). Dataset of SARS-CoV-2 wastewater data from Uppsala, Umeå, Örebro, Kalmar, and various towns in Uppsala and Stockholm region, Sweden. [https://doi.org/10.17044/scilifelab.14256317](https://doi.org/10.17044/scilifelab.14256317).

**How to cite the method:**

Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. *Environments*, *9*, 39. [https://doi.org/10.3390/environments9030039](https://doi.org/10.3390/environments9030039).

## Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_uppsala"></span></div>

<b>Important note:</b> Historical data for Knivsta, Vaxholm, and Österåker are available in the dataset linked above. However, they are no longer included in the visualisation below.

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

## Commentary from the research group

<div><b>Date:</b> <span id="slu_comment_date"></span><br><b>Commentary:</b> <span id="slu_comment"></span></div>

{{< ww_dynamic_content >}}

<script src="https://cdn.jsdelivr.net/npm/vega@5.19.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.15.1"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/1016b97372e9403da0b8e8e7bb14fa8d.js?id=malmo"></script>
