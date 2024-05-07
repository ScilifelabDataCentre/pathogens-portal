---
title: "Historic data for Örebro and Umeå"
plotly: true
aliases:
    - /data_types/environment/wastewater/historic_orebro_umea/
    - /dashboards/wastewater/historic_orebro_umea/
---

This page displays data on the amount of SARS-CoV-2 in Umeå and Örebro wastewater between October 2020 and June 2021. After June 2021, a new method is used for analyses of wastewater, and [the most recent data can be found here](../).

The data displayed here were collected as part of a research project led by associate professor Maja Malmberg (SLU, Swedish University of Agricultural Sciences; <maja.malmberg@slu.se>) in collaboration with the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) and associate professor Mette Myrmel at the Norwegian University of Life Sciences. The amount of SARS-CoV-2 virus in the wastewater of Umeå is measured using samples taken from the wastewater treatment facilities in Umeå and Örebro. Please [consult this map for the exact catchment area of the wastewater collection channels in Umeå](/wastewater/map_umeaa.jpg). Please [consult this map for the exact catchment area of the wastewater collection channels in Örebro](/wastewater/map_orebro.pdf).

After preparation, the viruses were extracted using ultra filtration and analyzed using qPCR technique for SARS CoV-2 RNA. Primers were used to detect the SARS-COV-2 gene (previously used and verified by [Corman and colleagues (2020)](https://doi.org/10.2807/1560-7917.ES.2020.25.3.2000045)). qPCR samples were normalized against PMMV. Until January 2021, three samples per week were taken and their results were pooled to provide a weekly estimate. From February 2021, samples were instead collected weekly.

In the plots plots below, the amount of SARS-CoV-2 for each week is measured/depicted compared to the amount of SARS-CoV-2 on 6th November 2020.

### Amount of SARS-CoV-2 in Umeå wastewater between between October 2020 and June 2021

**Download the data:** [Gene copy number change (%) relative to 6th Nov 2020 and flow level at each measurement day and weekly numbers, Excel file](https://blobserver.dc.scilifelab.se/blob/wastewater_data_Umeaa.xlsx). Data is available from week 44 of 2020 until week 22 of 2021.

**How to cite:**
Malmberg, M., Myrmel, M. & Khatri, M. Dataset of SARS-CoV-2 in wastewater in Umeå, Sweden. [https://doi.org/10.17044/scilifelab.14376881.v1](https://doi.org/10.17044/scilifelab.14376881.v1) (2021).

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_graph_Umea.json" height="550px" >}}</div>
</div>

<div class="small text-muted">*Data for these weeks is not available.</div>

<div class="small text-muted">**The samples from weeks 11 and 12 were stored in +4 °C for 2-3 weeks, this is different from what was done for all other samples.</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/umea_covid.py).

### Amount of SARS-CoV-2 in Örebro wastewater between October 2020 and June 2021

**Download the data:** [Gene copy number change (%) relative to 6th Nov 2020 and flow level at each measurement day and weekly numbers, Excel file](https://blobserver.dc.scilifelab.se/blob/wastewater_data_Orebro.xlsx). Data is available from week 42 of 2020 until week 22 of 2021.

**How to cite:**
Malmberg, M., Myrmel, M. & Khatri, M. Dataset of SARS CoV-2 in wastewater in Örebro, Sweden. [https://doi.org/10.17044/scilifelab.14377097.v1](https://doi.org/10.17044/scilifelab.14377097.v1) (2021).

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_graph_Orebro.json" height="550px" >}}</div>
</div>

<div class="small text-muted">*Data for these weeks is not available.</div>

<div class="small text-muted">**The samples from weeks 11 and 12 were stored in +4 °C for 2-3 weeks, this is different from what was done for all other samples.</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/orebro_covid.py).

