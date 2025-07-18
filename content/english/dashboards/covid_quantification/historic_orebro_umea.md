---
title: "Historic data for Örebro and Umeå"
plotly: true
aliases:
  - /data_types/environment/wastewater/historic_orebro_umea/
  - /dashboards/wastewater/historic_orebro_umea/
  - /dashboards/wastewater/covid_quantification/historic_orebro_umea/
---

This page displays data on the amount of SARS-CoV-2 in Umeå and Örebro wastewater between October 2020 and June 2021. A new method was used after June 2021, and [the most recent data can be found here](/dashboards/covid_quantification/).

The data displayed here were collected as part of a research project led by associate professor Maja Malmberg (SLU, Swedish University of Agricultural Sciences: <maja.malmberg@slu.se>), in collaboration with the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/news/scilifelab-launches-national-covid-19-research-program/), and associate professor Mette Myrmel at the Norwegian University of Life Sciences.

Samples of wastewater were taken from the wastewater treatment facilities in Umeå and Örebro to determine the amount of SARS-CoV-2 in wastewater. Consult the catchment area maps for [Umeå](/wastewater/map_umeaa.jpg) and [Örebro](/wastewater/map_orebro.pdf) to see where the wastewater came from in each case. To determine the levels of SARS-CoV-2 in wastewater samples, ultrafiltration and qPCR were used after sample preparation. Primers previously used and verified by [Corman _et al._ (2020)](https://doi.org/10.2807/1560-7917.ES.2020.25.3.2000045) were used to detect SARS-CoV-2, and qPCR samples were normalised against the levels of pepper mild mottle virus (PMMV). Up until January 2021, three samples of wastewater were taken from each wastewater facility each week, and the results were pooled to provide a weekly estimate. After January 2021, samples were instead collected weekly.

In the plots below, the amount of SARS-CoV-2 for each week is shown relative to the amount of SARS-CoV-2 on 6th November 2020.

### Amount of SARS-CoV-2 in Umeå wastewater between between October 2020 and June 2021

**Download the data:** [Gene copy number change (%) relative to 6th Nov 2020 and flow level at each measurement, Excel file](https://blobserver.dc.scilifelab.se/blob/wastewater_data_Umeaa.xlsx). Data are available from week 44 of 2020 until week 22 of 2021.

**How to cite:**
Malmberg, M., Myrmel, M. & Khatri, M. (2021). Dataset of SARS-CoV-2 in wastewater in Umeå, Sweden. [https://doi.org/10.17044/scilifelab.14376881.v1](https://doi.org/10.17044/scilifelab.14376881.v1).

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 600px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_graph_Umea.json" height="550px" >}}</div>
</div>

<div class="small text-muted">*Data for these weeks is not available.</div>

<div class="small text-muted">**Samples were stored at +4 °C for 2-3 weeks, unlike all other samples.</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/archive/umea_covid.py).

### Amount of SARS-CoV-2 in Örebro wastewater between October 2020 and June 2021

**Download the data:** [Gene copy number change (%) relative to 6th Nov 2020 and flow level at each measurement, Excel file](https://blobserver.dc.scilifelab.se/blob/wastewater_data_Orebro.xlsx). Data are available from week 44 of 2020 until week 22 of 2021.

**How to cite:**
Malmberg, M., Myrmel, M. & Khatri, M. (2021). Dataset of SARS CoV-2 in wastewater in Örebro, Sweden. [https://doi.org/10.17044/scilifelab.14377097.v1](https://doi.org/10.17044/scilifelab.14377097.v1).

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 600px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_graph_Orebro.json" height="550px" >}}</div>
</div>

<div class="small text-muted">*Data for these weeks is not available.</div>

<div class="small text-muted">**Samples were stored at +4 °C for 2-3 weeks, unlike all other samples.</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/archive/orebro_covid.py).
