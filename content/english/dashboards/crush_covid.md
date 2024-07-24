---
title: CRUSH Covid data and dashboard, Region Uppsala
description: CRUSH Covid maps outbreaks in Uppsala County by visualising the number of cases, test positivity, and geographic distribution, among other things. Data for each postal code is available for download and reuse.
banner: /dashboard_thumbs/CRUSH.png
banner_border: true
toc: false
menu:
  dashboard_menu:
    identifier: crush_covid
    name: "CRUSH Covid Uppsala (Partner)"
aliases:
  - /data_types/health_data/crush_covid/
dashboards_topics: [COVID-19, Infectious diseases]
data_status: "historic" # or "updating"
---

<div class="containter">
<div class="row mr-2 mt-2">
<div class="col-lg-9">
<p>CRUSH Covid Uppsala is a research project in which <b>Region Uppsala</b> collaborates with researchers from five different research departments at <b>Uppsala University</b>. The purpose of the project is to map outbreaks of COVID-19 in Uppsala County and to try to mitigate the impact of outbreaks by informing the public.</p>

<p>CRUSH Covid is led by <b>Mats Martinell</b> (senior lecturer at the Department of Public Health and Caring Sciences, General Medicine and Preventive Medicine, Uppsala University) and <b>Tove Fall</b> (professor of Molecular Epidemiology at the Department of Medical Sciences, Molecular Epidemiology, Uppsala University). Sewage analysis is supported by SciLifeLab and Uppsala Vatten. Modelling work is supported by Vinnova.</p>

<p>For questions and feedback, please contact <b>Georgios Varotsis</b> (<a href="mailto:georgios.varotsis@medsci.uu.se">georgios.varotsis@medsci.uu.se</a>).</p>

<p>CRUSH Covid has received ethical approval from the Swedish Ethical Review Authority (ref. no. 2020-04210, 2020-06315 and 2020-06501).</p>

<p>The CRUSH Covid team has released data and information about the project in two places. The primary source of data and information was their <a target="_blank" href="https://crush-covid.shinyapps.io/crush_covid/">custom shiny app, named the CRUSH Covid dashboard</a>, which contained data visualisations as well as reports. As of September 2022, updates to the app ceased. The Portal's dashboard (i.e. this webpage) is the secondary source of data and information for this project. The data generated from CRUSH Covid between 2020-2022 can be downloaded directly below.</p>
</div>
<div class="col-lg-3">
<div class="d-flex justify-content-center mb-3"><img src="/img/logos/crush_covid_logo.png" alt="CRUSH Covid" height="30"></div>
<div class="d-flex justify-content-center mb-3"><img src="/img/logos/uu_logo.png" alt="Uppsala University" height="100"></div>
<div class="d-flex justify-content-center mb-3"><img src="/img/logos/regionuppsala_logo.png" alt="Region Uppsala" height="40"></div>
</div>
</div>
</div>

#### Download CRUSH Covid data

<div class="alert alert-info">Last updated: 2022-09-15</div>

- [Number of tests and % positivity by postal code in Uppsala County, .csv file](https://blobserver.dc.scilifelab.se/blob/CRUSH_Covid_data.csv). For each postal code which is found within the Uppsala län, the dataset contains weekly data on cases per capita, tests per capita and % positivity. The estimates are calculated based on the adult population of each postal code (individuals 15 years of age and older). For reference, both the total population and the adult population are included.

#### Interactive dashboard and reports

<a target="_blank" href="https://crush-covid.shinyapps.io/crush_covid/">Click here</a> to see the dashboard in a new tab/window. NB: The CRUSH Covid dashboard is only available in Swedish.

{{< crush_covid >}}
