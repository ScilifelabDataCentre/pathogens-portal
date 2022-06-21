---
title: The Administration and Study of COVID-19 Vaccines in Sweden
toc: true
plotly: true
menu:
    data_menu:
        identifier: vaccines
        name: Vaccine administration in Sweden
        weight: 30
        parent: dashboards
aliases:
    - /data_types/health_data/vaccines/
---

## General information on vaccine research

Over the last two years, the COVID-19 pandemic has challenged societies and healthcare systems worldwide, and vaccines and therapeautic treatments have been rapidly developed in response. To date, the [European Medicines Agency (EMA)](https://www.ema.europa.eu/en) has approved four vaccines against COVID-19:

- **Comirnaty** - produced by Pfizer/BioNTech, approved on 21st December 2020.
- **Spikevax** - produced by Moderna, approved on 6th January 2021.
- **Vaxzevria** - produced by AstraZeneca, approved on 29th January 2021.
- **Covid-19 Vaccine** - produced by Janssen, approved on 11th March 2021.
- **Nuvaxovid** - produced by Novavax, approved on 20th December 2021.

As of December 2021, only **Comirnaty** (Pfizer/BioNTech) and **Spikevax** (Moderna) are available in Sweden. **Vaxzevria** (AstraZeneca) was used in past but is no longer used after 1st September 2021.

This page is focussed on vaccine research. On it, we [visualise](/data_types/health_data/vaccines/#visualisations-related-to-vaccination-coverage) information about the amount of people (across different regions, different age groups, or in Sweden generally) that have received one, two, or three doses of vaccination. We also provide links to the publicly available data underlying those visualisations. The visualisations do not include information about the type of vaccine used.

The section also displays ongoing [Swedish research projects](/data_types/health_data/vaccines/#ongoing-research-projects) related to vaccine research. These projects are focussed broadly on vaccines and, as such, they include life science projects, registery-based projects, and public health projects. We also [show a subset of publications](/data_types/health_data/vaccines/#publications) related to vaccine research by researchers affiliated with a Swedish University or Research Institute.

<div class="alert alert-info">
    <i class="bi bi-info-circle-fill"></i> We invite researchers affiliated to a Swedish research institute to get in touch with us about adding information about their vaccine research data or visualisations on this page; send us an email to datacentre@scilifelab.se.
</div>

### Additional resources on COVID-19 vaccines

- The **Swedish Health Agency** provides general information about COVID-19 [here](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/).
- The **Swedish Medical Products Agency** provides information about COVID-19 vaccines [here](https://www.lakemedelsverket.se/en/coronavirus/covid-19-vaccine).
- For health information connected to vaccination and tests by different **Swedish Regions**, see [Regional information on 1177](https://www.1177.se/).
- The **European Centre for Disease Prevention and Control** (ECDC) shows information about the vaccines [here](https://www.ecdc.europa.eu/en/covid-19/prevention-and-control/vaccines).
- Information about the vaccines is available from the **Centre for disease Control** [here](https://www.cdc.gov/coronavirus/2019-ncov/vaccines/index.html).
- Information and data visualisations related to the register-based large-scale national population study to monitor COVID-19 vaccination effectiveness and safety ([RECOVAC](https://www.gu.se/en/research/recovac)) are presented in a [separate dashboard](/dashboards/recovac/).

## Visualisations related to vaccination coverage

<div class="alert alert-info">Visualisations on this page last updated: <span id="visualisations_date_modified"></span>.</div>

The visualisations in this section are based on publicly available data from the [Swedish Health Agency (Folkhälsomyndigheten, FoHM)](https://folkhalsomyndigheten.se). Follow [this link](https://www.folkhalsomyndigheten.se/folkhalsorapportering-statistik/statistikdatabaser-och-visualisering/vaccinationsstatistik/statistik-for-vaccination-mot-covid-19/) to view their summary of statistics related to vaccination against COVID-19 in Sweden (only available in Swedish). The data used to produce the visualations can be downloaded [here](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data). For each visualisation, we describe which part of the dataset was used and how the calculations were done. The source data is updated weekly (on Thursdays), and this page will be updated shortly thereafter.

The code used to produce the visulations can be found on [GitHub](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/tree/main/Vaccine_page). All data is processed using a single [data preparation script](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Vaccine_page/vaccine_dataprep_Swedentots.py). The codes required to generate each plot are linked beneath the visualisations. 

### General summary statistics

In this section, we examine the overall levels of vaccination in Sweden, as well as the recent rate of vaccination.

Here, we compare two methods of calculation that can be used to determine the percentage of the Swedish population that have received a given vaccination dose level. One method involves calculating the number of vaccines as a percentage of the number of people in the age categories eligible to get a given dose. Individuals born in or before 2009 (at least 12-13 years old) are considered eligible for the first two doses, individuals born in or before 2003 (at least 18-19 years old) are considered eligible for the third dose, and individuals born in or before 1956 (at least 65-66 years old) are considered eligible for the fourth dose. We refer to this method of calculations as the 'eligible population method'. The other method instead considers the number of people vaccinated as a percentage of the entire population, regardless of how much of the population is eligible. We refer to this method of calculation as the 'whole population method'.

Please note, because not everyone is eligible for all doses, it would not be appropriate to compare values between the doses for the purposes of asssessing e.g. coverage or uptake.

We display the results of both calculations for each vaccine dose (first, second, third, and fourth) on the chart below to highlight how the method of calculation used influences the measurement. *Please note that the doses are sometimes referred to differently elsewhere, with 'fully vaccinated' referring to those given 2 or 3 doses, depending on the source, and 'booster dose' most often referring to the third dose.*

For calculations done using the 'eligible population method', we use data from the 'Vaccinerade tidsserie' (first two doses), 'Vaccinerade tidsserie dos 3' (third dose), and 'Vaccinerade tidsserie dos 4' (fourth dose) tabs of the [FoHM data](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data), specifically the percentage values. For the 'whole population method', we do not take values directly from the data, but instead use the latest data from [Statistics Sweden (SCB)](https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/population-composition/population-statistics/pong/tables-and-graphs/monthly-statistics--the-whole-country/population-statistics-2021/)) and the most recent 'raw number' of the doses administered from the [FoHM data](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data).

**Note on the graph:** Click on the coloured squares in the legend of the below graph to toggle which datasets are displayed. A single click will toggle just the dataset that you clicked on. A double-click on a colour will cause the map to display ONLY the dataset clicked on.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/Total_vaccinated_barchart.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Vaccine_page/vaccine_indicator_barchart.py).

**Code used to generate the 'live text' in the summary paragraph below:** ['Live text' script](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Vaccine_page/vaccine_livetext.py).

To summarise, in total, <span id="eligible_one_dose"></span>% of the population that are eligible for the first dose have received at least one dose of vaccination against COVID-19, which represents <span id="population_one_dose"></span>% of the whole population. The values indicate that <span id="eligible_one_dose_lastweek"></span>% of the eligible population were vaccinated last week (a change in rate of <span id="eligible_one_dose_rate_change"></span>% compared to the previous week), or <span id="population_one_dose_lastweek"></span>% of the whole population (a change of <span id="population_one_dose_rate_change"></span>% compared to the previous week). By contrast, <span id="eligible_two_doses"></span>% of those eligible, and <span id="population_two_doses"></span>% of the whole population have received at least two doses in total. The values indicate that <span id="eligible_two_doses_lastweek"></span>% of those eligible and <span id="population_two_doses_lastweek"></span>% of the whole population received their second dose last week (a change in rate of <span id="eligible_two_doses_rate_change"></span>% and <span id="population_two_doses_rate_change"></span>% compared to the previous week, respectively). In total, <span id="eligible_three_doses"></span>% of the eligible population received the third (or 'booster') dose, representing <span id="population_three_doses"></span>% of the whole population. This means that <span id="eligible_three_doses_lastweek"></span>% of the eligible population received their third dose last week (a change in rate of <span id="eligible_three_doses_rate_change"></span>% compared to the previous week), or <span id="population_three_doses_lastweek"></span>% of the whole population (a change of <span id="population_three_doses_rate_change"></span>% compared to the previous week). To date, <span id="population_four_doses"></span>% of the whole population has received a fourth dose, and <span id="eligible_four_doses"></span>% of those eligible. The relatively greater difference between these two calculations for the fourth dose, occurs because only a very small portion of the population is eligible. In the last week, <span id="population_four_doses_lastweek"></span>% of the whole population were vaccinated with a fourth dose, a change in rate of <span id="population_four_doses_rate_change"></span>% compared to the previous week. By contast, <span id="eligible_four_doses_lastweek"></span>% of the eligible population were vaccinated with a fourth dose, a relative change in rate of <span id="eligible_four_doses_rate_change"></span>% compared to the previous week.

### Administration of vaccinations over time

The first vaccine doses were administered in Sweden in early 2021. As with other countries, the first two doses of the vaccination were made available to progressively younger age groups over time. The third dose of the vaccine was first offered in autumn of 2021, and was offered to individuals a given time period after their second dose. In early 2022, a fourth dose was made available to those aged over 80, those receiving care, those living in housing facilities for the elderly, and those with severe immunodeficiency. This was extended to include those over 65 in April 2022.

Time series data on the first and second doses is held sepately than that for other doses in the [data available from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)). Time series data on the first two doses is available in the 'Vaccinerade tidsserie' tab. Time series data about the third dose is available in the 'Vaccinerade tidsserie dos 3' tab, and time series data about the fourth dose is available in the 'Vaccinerade tidsserie dos 4' tab

Again, please note that it would not be valid to make comparisons across the doses; they are not equally available across all age/risk groups, and FoHM only include doses given to certain age groups in their data. Specifically, only first or second doses administered to those born in or before 2009 (at least 12-13 years old), third doses given to people born in or before 2003 (at least 18-19 years old), and fourth doses given to those born in or before 1956 (at least 65-66 years old) are included.

We have presented the data for the whole of Sweden as a percentage of the Swedish population in the below graph (using the latest population size data from [Statistics Sweden (SCB)](https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/population-composition/population-statistics/pong/tables-and-graphs/monthly-statistics--the-whole-country/population-statistics-2021/)). Please keep in mind that this data differs from the percentages as calculated by FoHM, who use the 'eligible population method'. However, the results are comparable to the calculations reported by other countries, see the information in the 'general summary statistics' section for details.

**Note on the graph:** Click on the coloured squares in the legend of the below graph to toggle which datasets are displayed. A single click will toggle just the dataset that you clicked on. A double-click on a colour will cause the map to display ONLY the dataset clicked on.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/vaccine_timeseries_pop_barchart.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Vaccine_page/vaccine_timeseries_barchart.py).

### Administration of vaccinations in each county (län)

In this section, we explore the levels of vaccination coverage for each of the doses in each county (län) of Sweden. For each dose, we have calculated the percentage of the people in the county that have received that dose (using the lastest [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data) and [Statistics Sweden (SCB)](https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/population-composition/population-statistics/pong/tables-and-graphs/monthly-statistics--the-whole-country/population-statistics-2021/)). Data about the numbers of first and second doses administered in each county is taken from the 'Vaccinerade tidsserie' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data). Again, please note that the 'raw number' of first and second vaccine doses administered includes only those given to individuals born in or before 2009 (at least 12-13 years old). As explained in the sections above, there is no directly comparable data regarding the third dose, as only the doses given to people born in or before 2003 (at least 18-19 years old) are included. We have used the 'Totalt' values in the 'Dos 3 per åldersgrupp' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)) for this calculation. It is exactly equivalent to the number given in the time series data for the third dose. As with the third dose, data for the fourth dose is not directly comparable to that from any other dose. Indeed, the number of 'fourth doses' administered only includes those given to people born in or before 1956 (at least 65-66 years of age). This is obviously a much smaller portion of the population compared to any of the other three doses. As a result, we find it appropriate to consider the data in two ways; one in which the 'whole population method' for calculation is used, and one in which the 'eligible population method' is used. This will allow a clearer understanding of the differences between län in terms of the coverage for this dose. The data were taken from the 'Dos 4 per åldersgrupp' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)). The 'Totalt' value was used for the 'whole population method', and the percantage calculation was used for the 'eligible population method'.

Again, please note that percentage values calculated using the 'whole population method' will differ from those calculated by FoHM, whose calculations do not consider the whole population, but rather the population eligible for the dose (from 12-13 years for the first and second doses, from 18-19 years for the third dose, and from 65-66 years for the fourth dose).

#### Administration of one vaccine dose

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/onedose_pop_map.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce maps](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Vaccine_page/vaccine_maps_population.py).

#### Administration of two vaccine doses

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/twodoses_pop_map.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce maps](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Vaccine_page/vaccine_maps_population.py).

#### Administration of three vaccine doses

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/threedoses_pop_map.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce maps](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Vaccine_page/vaccine_maps_population.py).

#### Administration of four vaccine doses

<div class="row">
<div class="col-md"><div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/fourdoses_pop_map.json" height="500px" >}}</div>
</div></div>
<div class="col-md"><div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/fourdoses_elig_map.json" height="500px" >}}</div>
</div></div>
</div>

**Code used to produce plot:** [Script to produce maps](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Vaccine_page/vaccine_maps_population.py).

### Administration of vaccinations according to age group

We constructed the below heatmap to show how the relative numbers of people vaccinated differs according to age. Unsurprisingly, the more advanced age groups tend to have higher levels of vaccination for each dose, as they are typically given access at an earlier date.

Data is available for individuals born in or before 2009 (i.e. at least 12-13 years old) for the first and second vaccine doses (available in the 'Vaccinerade ålder' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)), and for people born in or before 2003 (i.e. at least 18-19 years old) for the third dose (available in the 'Dos 3 per åldersgrupp' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)). For the fourth dose, data is only available for those born in or before 1956 (i.e. at least 65-66 years old) available in the 'Dos 4 per åldersgrupp' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)). This means that data is not available for all age groups for each dose, and this is reflected in the plot. In this case, we have not performed any recalculation of the data, so the numbers are the same as those provided by FoHM (i.e. all values were calculated using the 'eligible population method').

Please note, data has not been added for 65-69 year olds for the fourth dose because data is not available in equivalent categories.

**Note about the heatmap:** A white colouration indicates that no data is available for that age group.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/vaccine_heatmap.json" height="750px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce heatmap](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Vaccine_page/vaccine_heatmaps.py).

## Ongoing research projects

Below is a manually curated overview of projects focussed on **vaccine research** that are/were funded by major funding agencies in Sweden. As it is manually curated, the list may not be exhaustive, but new projects will be added as soon as possible. If you are aware of a project that is not listed here but ought to be, please [get in touch with us](/contact/). For a list of all research projects funded by major funding agencies in Sweden, see [this section of the portal](/projects/funding/) instead.

{{< display_funded_projects filter_variable="vaccine" >}}

## Publications

Below is a subset of preprints and published scientific journal articles on the subject of **vaccine research** involving at least one author affiliated with a Swedish university or research institute. If you would like for your publication to be displayed here, or feel that information about a publication requires correction, please [get in touch with us](/contact/). For a full list of all publications related to COVID-19 and SARS-CoV-2 that involve at least one author affiliated with a Swedish university or research institute, please see [this section of the portal](/publications/).

{{< vaccines_publications >}}

{{< vaccines_dynamic_content >}}
