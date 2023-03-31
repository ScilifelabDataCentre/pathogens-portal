---
title: The amount of SARS-CoV-2 virus in wastewater across the Netherlands
toc: true
menu:
    dashboard_menu:
        identifier: wastewater
        name: Amount of SARS-CoV-2 in wastewater across Sweden
        weight: 20
    other_data:
        name: Environment
        identifier: environment
        weight: 50
plotly: true
aliases:
    - /data_types/environment/wastewater/
    - /data_types/environment/
---

## Introduction

Sewage can serve as an indicator of public health in the Netherlands. Many diseases that occur within a group of people can be detected in sewage. This includes infectious diseases such as COVID-19 (caused by the coronavirus SARS-CoV-2) and non-infectious diseases. By examining sewage samples, we can also identify substances that tell us more about our lifestyle or living environment. Sewage research is useful and important, especially in conjunction with other forms of public health research.


### Dataset

**Download the data:** [National SARS-CoV-2 wastewater surveillance](https://data.rivm.nl/meta/srv/eng/catalog.search;jsessionid=5C4F23F31DC8B4F5CF0DFE1849EA5BB3#/metadata/a2960b68-9d3f-4dc3-9485-600570cd52b9). Results are updated weekly.\
**Contact:** [RIVM/I&V/Z&O](mailto:afvalwatersurveillance@rivm.nl)

## Map of sample collection sites

![image_Netherlands](https://data.rivm.nl/meta/srv/api/records/a2960b68-9d3f-4dc3-9485-600570cd52b9/extents.png?mapsrs=epsg:3857&width=300)

### Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_uppsala"></span></div>

Important note: Historical data for Knivsta, Vaxholm, and Österåker is available in the dataset linked above. However, they are no longer included in the visualisations below.

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

Please note that the plot below displays the same data, but the y axis is shown as a log scale.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_logyaxis.json" height="550px" >}}</div>
</div>

{{< ww_dynamic_content >}}

<script src="https://cdn.jsdelivr.net/npm/vega@5.19.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.15.1"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/1016b97372e9403da0b8e8e7bb14fa8d.js?id=malmo"></script>
