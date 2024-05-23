---
title: "Historic data for Stockholm"
plotly: true
aliases:
  - /data_types/environment/wastewater/historic_stockholm/
  - /dashboards/wastewater/historic_stockholm/
---

This page displays data on the amount of SARS-CoV-2 in the wastewater in Stockholm between April 2020 and August 2021. The amount of SARS-CoV-2 in wastewater was calculated as the number of gene copies per week (raw wastewater) with bovine + PMMoV factor. From September 2021 onwards, the method was changed. Please [see this page for the most recent data](/dashboards/wastewater/covid_quantification/covid_quant_kth/).

This project was led by associate professor Zeynep Cetecioglu Gurol and colleagues (KTH Royal Institute of Technology: <zeynepcg@kth.se>). The project was a collaboration between the [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19), the [Sustainable Development, Environmental Science and Engineering (SEED)](https://www.kth.se/en/seed) and [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196) departments at the KTH Royal Institute of Technology (KTH), as well as Stockholm Vatten och Avfall and the Käppala Association. The sampling of wastewater began in mid-April 2020, from the Bromma, Henriksdal, and Käppala wastewater treatment plants (WWTP). These treatment plants receive wastewater from a population of approximately 360,000, 860,000, and 500,000 people, respectively. Please see the catchment maps for [Käppala](/wastewater/map_Kappala.pdf) and [Bromma and Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf) to understand where the wastewater originated from in each case.

After concentration, filtering, and preparation, the samples are analysed using qPCR to test for SARS-CoV-2 RNA. Primers of the nucleocapsid (N) gene (previously used and verified by [Medema _et al._ (2020)](https://doi.org/10.1016/j.scitotenv.2020.142939)) were used to detect SARS-COV-2. In some cases, samples of raw wastewater were frozen at –20<sup>o</sup>C, and concentrated wastewater or purified RNA were stored at -80<sup>o</sup>C before the next analysis step was carried out. The concentration method used by prof. Gurol and colleagues was based on their published study ([Jafferali _et al._, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)), in which they compared four different concentration methods. The study concluded that the double ultrafiltration method adapted by KTH was significantly more efficient than single filtration and adsorption methods. Please see [Jafferali _et al._ (2021)](https://doi.org/10.1016/j.scitotenv.2020.142939) for more information on the methods. More information about [data summaries and preliminary conclusions are also available](https://www.kth.se/water/research/covid-1.979048).

**Download the data:** [Gene copy number/week (raw wastewater) with bovine + PMMoV factor; Excel file.](https://blobserver.dc.scilifelab.se/blob/wastewater_data_Stockholm.xlsx). The numbers for Stockholm overall, and for the Henriksdal, Sickla, Hässelby, Järva, Riksby, and Käppala inlets are provided. At least partial data are available between week 16 of 2020 and week 34 of 2021.

**How to cite:**
Cetecioglu, Z. G., Williams, C., Khatami, K., Atasoy, M., Nandy, P., Jafferali, M. H., Birgersson, M. (2021). SARS-CoV-2 Wastewater Data from Stockholm, Sweden. [https://doi.org/10.17044/scilifelab.14315483](https://doi.org/10.17044/scilifelab.14315483).

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_data_stockholm.json" height="550px">}}</div>
</div>

<div class="small text-muted">All samples up until week 21 of 2020 were received by the lab in week 21. Between weeks 21 and 33 of 2020, samples were analysed biweekly. After week 33 of 2020, samples were typically analysed weekly, although measurements were taken fortnightly, rather than weekly, between weeks 24 and 32 of 2021.</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/historic_stockholm_data.py).
