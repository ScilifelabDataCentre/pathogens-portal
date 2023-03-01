---
title: Amount of SARS-CoV-2 in wastewater (GU)
toc: false
plotly: true
---

<div class="mt-3">
  <a href="/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Go back to SARS-CoV-2 quantification within the wastewater epidemiology dashboard</a>
</div>
<br>

## Introduction

This project is led by Professor Helene Norder (University of Gothenburg, GU), and supported by co-workers from the University of Gothenburg and Sahlgrenska University Hospital (Hao Wang, Marianela Patzi Churqui, Timur Tunovic, Fredy Saguti, and Kristina Nyström). The wastewater sample collections were performed by Lucica Enache at Ryaverket, Gryaab AB, Gothenburg.

The data and visualisation on this page are usually updated (**insert timeline**), typically on (**day?**).

## Wastewater collection sites

Influent wastewater samples were collected from Ryaverket wastewater treatment plant (WWTP) in Gothenburg. Wastewater sample collection began on February 10th (week 7) of 2020. Ryaverket WWTP receives wastewater from the households of more than 790,000 residents of Gothenburg, as well as from industry in the area. Wastewater is also received from residents and industry in surrounding municipalities, including Ale, Härryda, Kungälv, Lerum, Mölndal, and Partille, as well as storm and snow-melt water from older parts of Gothenburg. The amount of wastewater from households remains relatively consistent throughout the year. However, the amount of wastewater overall can be affected by the weather (with higher precipitation resulting in greater amounts). More information about the sample location, sample week, volume, and influent wastewater flow, is available in [Wang *et al.* (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/).

## Visualisations

<div class="alert alert-info">Last updated: <span id="SET_ME"></span></div>

<!-- <button type="button" class="btn btn-sm btn-outline-secondary mb-2" data-bs-toggle="modal" data-bs-target="#interactiveFeaturesModal">
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
</div> -->

 <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_gothenburg.json" height="550px" >}}</div>
</div>

## Commentary from the research group

## Dataset

**Download the data:** \
**Contact:** helene.norder@gu.se

**How to cite the dataset:**

**How to cite method:**
Saguti, F., Magnil, E., Enache, L., Churqui, M.P., Johansson, A., Lumley, D., Davidsson, F., Dotevall, L., Mattsson, A., Trybala, E., Lagging, M., Lindh, M., Gisslen, M., Brezicka, T., Nystrom, K. and Norder, H. (2021). Surveillance of wastewater revealed peaks of SARS-CoV-2 preceding those of hospitalized patients with COVID-19. [https://doi.org/10.1016/j.watres.2020.116620](https://doi.org/10.1016/j.watres.2020.116620).

Wang, H., Churqui, M.P., Tunovic, T., Enache, L., Johansson, A., Karmander, A., Nilsson, S., Lagging, M., Andersson, M., Dotevall, L., Brezicka, T., Nystrom, K. and Norder, H. (2022). The amount of SARS-CoV-2 RNA in wastewater relates to the development of the pandemic and its burden on the health system. [https://doi.org/10.1016/j.isci.2022.105000](https://doi.org/10.1016/j.isci.2022.105000).

## Methods

Samples of wastewater were collected using a fixed-site sampler that collected 30ml per 10,000m<sup>3</sup> of the incoming wastewater. For the purposes of analysis, seven samples (each representing a 24 hour period) were pooled to create a weekly sample. The weekly sample, which consisted of 1.5-15l of wastewater (depending on the flow) was sent to the Clinical Microbiology Laboratory at Sahlgrenska University Hospital for analysis. Analyses were conducted on the Monday after the sample was collected.

At the Clinical Microbiology Laboratory, viruses were concentrated to a final volume of 2.5ml, using a method that was developed in-house. This method uses the NanoCeram electropositive filter (Argonide, Florida, USA) as the primary means of concentration, and then ultracentrifugation as secondary concentration method ([Saguti *et al.*, 2021](https://pubmed.ncbi.nlm.nih.gov/33212338/)). Nucleic acids were extracted from 1ml of the concentrated sample using the QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Real-time quantitative PCR (RT-qPCR) was performed to detect the RNA-dependent RNA polymerase (RdRP) region of SARS-CoV-2. In all runs, a 10-fold serial diluted plasmid (Eurofins Genomics, Ebersberg, Germany) that contained the target SARS-CoV-2 region was used as a positive control. Nuclease-free water was used as a negative control. The Ct values from the qPCR were used to quantify the amount of SARS-CoV-2 genome in the sample. Details about the method of calculation are provided in [Saguti *et al.* (2021)](https://pubmed.ncbi.nlm.nih.gov/33212338/). The relative amount of viral genome in the wastewater was calculated by dividing the amount of viral genome in the sample by the amount of SARS-CoV-2 genome in the incoming wastewater during week 11 (mid-March) of 2020. Samples from all subsequent weeks contained detectable SARS-CoV-2 genome.
