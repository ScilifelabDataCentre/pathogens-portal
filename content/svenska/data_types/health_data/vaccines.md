---
title: Administrering av vaccin och vaccinforskning i Sverige
toc: true
plotly: true
---
<div class="alert alert-info">
  <i class="fas fa-exclamation-triangle"></i>
  <span>En svensk översättning av denna sida kommer inom kort.</span>
</div>

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
    <i class="fas fa-info-circle"></i> We invite researchers affiliated to a Swedish research institute to get in touch with us about adding information about their vaccine research data or visualisations on this page; send us an email to datacentre@scilifelab.se.
</div>

### Additional resources on COVID-19 vaccines

- The **Swedish Health Agency** provides general information about COVID-19 [here](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/).
- The **Swedish Medical Products Agency** provides information about COVID-19 vaccines [here](https://www.lakemedelsverket.se/en/coronavirus/covid-19-vaccine).
- For health information connected to vaccination and tests by different **Swedish Regions**, see [Regional information on 1177](https://www.1177.se/).
- The **European Centre for Disease Prevention and Control** (ECDC) shows information about the vaccines [here](https://www.ecdc.europa.eu/en/covid-19/prevention-and-control/vaccines).
- Information about the vaccines is available from the **Centre for disease Control** [here](https://www.cdc.gov/coronavirus/2019-ncov/vaccines/index.html).

## Visualisations related to vaccination coverage

<div class="alert alert-info">Visualisations on this page last updated: <span id="visualisations_date_modified"></span>.</div>

The visualisations in this section are based on publicly available data from the [Swedish Health Agency (Folkhälsomyndigheten, FoHM)](https://folkhalsomyndigheten.se). Follow [this link](https://www.folkhalsomyndigheten.se/folkhalsorapportering-statistik/statistikdatabaser-och-visualisering/vaccinationsstatistik/statistik-for-vaccination-mot-covid-19/) to view their summary of statistics related to vaccination against COVID-19 in Sweden (only available in Swedish). The data used to produce the visualations can be downloaded [here](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data). For each visualisation, we describe which part of the dataset was used and how the calculations were done. The data is updated weekly (on Thursdays).

### General summary statistics

In this section, we examine the overall levels of vaccination in Sweden, as well as the recent rate of vaccination.

Here, we compare two methods of calculation for the percentage of the Swedish population that has been vaccinated. One method considers the number of vaccinations as a percentage of the population eligible to get the vaccination. It is important to consider that individuals born in or before 2009 (at least 12-13 years old) are considered eligible for the first and second doses of the vaccine. However, only individuals born in or before 2003 (at least 18-19 years old) are considered eligible for the third dose. We refer to this method of calculations as the 'eligible individuals method'. The other method instead considers the number of people vaccinated as a percentage of the entire population, regardless of how much of the population is eligible. We refer to this method of calculation as the 'whole population method'.

We display the results of both calculations for each vaccine dose (first, second, and third) on the chart below to highlight how the method of calculation used influences the measurement. *Please note that the doses are sometimes referred to as first dose, fully vaccinated, and booster dose elsewhere, rather than first, second, and third dose.*

For calculations produced using the 'eligible individuals method', we use data from the Vaccinerade tidsserie tab of the [FoHM data](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data), specifically the percentage calculation. For the 'whole population method', we instead take the total number of individuals vaccinated and use the latest count of the population size of Sweden (available from from [Statistics Sweden (SCB)](https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/population-composition/population-statistics/pong/tables-and-graphs/monthly-statistics--the-whole-country/population-statistics-2021/)) to calculate it as a percentage of the population.

**Note on the graph:** Click on the coloured squares in the legend of the below graph to toggle which datasets are displayed. A single click will toggle just the dataset that you clicked on. A double-click on a colour will cause the map to display ONLY the dataset clicked on.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/Total_vaccinated_barchart.json" height="500px" >}}</div>
</div>

To summarise, in total, <span id="eligible_one_dose"></span>% of the population that are eligible for the first dose have received at least one dose of vaccination against COVID-19, which represents <span id="population_one_dose"></span>% of the whole population. The values indicate that <span id="eligible_one_dose_lastweek"></span>% of the eligible population were vaccinated last week (a change in rate of <span id="eligible_one_dose_rate_change"></span>% compared to the previous week), or <span id="population_one_dose_lastweek"></span>% of the whole population (a change of <span id="population_one_dose_rate_change"></span>% compared to the previous week). By contrast, <span id="eligible_two_doses"></span>% of those eligible, and <span id="population_two_doses"></span>% of the whole population have received at least two doses in total. The values indicate that <span id="eligible_two_doses_lastweek"></span>% of those eligible and <span id="population_two_doses_lastweek"></span>% of the whole population received their second dose last week (a change in rate of <span id="eligible_two_doses_rate_change"></span>% and <span id="population_two_doses_rate_change"></span>% compared to the previous week, respectively). Lastly, <span id="eligible_three_doses"></span>% of the population eligible for it has received a third 'booster' dose, representing <span id="population_three_doses"></span>% of the whole population. This means that <span id="eligible_three_doses_lastweek"></span>% of the eligible population received their third dose last week (a change in rate of <span id="eligible_three_doses_rate_change"></span>% compared to the previous week), or <span id="population_three_doses_lastweek"></span>% of the whole population (a change of <span id="population_three_doses_rate_change"></span>% compared to the previous week).

Reuters COVID-19 Tracker provides some additional summary information on vaccinations against COVID-19 (as well as information regarding the implementation of lockdown measures and cases) [for Sweden](https://graphics.reuters.com/world-coronavirus-tracker-and-maps/countries-and-territories/sweden/). In particular, the data includes how many doses would be needed to provide 100% of the population with 2 doses, and an estimation of how long (based on the current number of doses administered daily) it might take to vaccinate 10% more of the total population.

### Administration of vaccinations over time

The first vaccine doses were administered in Sweden in early 2021. As with other countries, the vaccine program for the first and second doses rollout was such that the vaccine became available to decreasing age groups over time. The third dose of the vaccine started to be offered in autumn of 2021.

Data about the administration of the first and second doses is available separately (in the 'Vaccinerade tidsserie' tab of [FoHM data](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)) from data regarding the third dose (in the 'Vaccinerade tidsserie dos 3' tab of [FoHM data](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)). Data on the three doses is not directly comparable as the way in which the number of vaccines administered is counted slightly differently. Specifically, the number of first and second vaccine doses administered is counted for those born in or before 2009 (at least 12-13 years old), but the number of third doses administered is counted for those born in or before 2003 (at least 18-19 years old).

We have presented the data for the whole of Sweden as a percentage of the Swedish population in the below graph (using the latest population size data from [Statistics Sweden (SCB)](https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/population-composition/population-statistics/pong/tables-and-graphs/monthly-statistics--the-whole-country/population-statistics-2021/)).

Please keep in mind that this data differs from the percentages as calculated by FoHM, who use the 'eligible individuals method'. However, the data is comparable to the calculations reported by other countries, see the information in the 'general summary statistics' section for details.

**Note on the graph:** Click on the coloured squares in the legend of the below graph to toggle which datasets are displayed. A single click will toggle just the dataset that you clicked on. A double-click on a colour will cause the map to display ONLY the dataset clicked on.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/vaccine_timeseries_pop_barchart.json" height="500px" >}}</div>
</div>

### Administration of vaccinations in each county (län)

In this section, we explore the levels of vaccination coverage for each of the three doses in each county (län) of Sweden. We again use the latest data on the population size for each county from [Statistics Sweden (SCB)](https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/population-composition/population-statistics/pong/tables-and-graphs/monthly-statistics--the-whole-country/population-statistics-2021/) to calculate the coverage for each dose as a percentage of the whole population of that county. We take the number of first and second doses administered in that county from the 'Vaccinerade tidsserie' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data). Again, please note that the 'raw number' of first and second vaccine doses administered includes only those given to individuals born in or before 2009 (at least 12-13 years old). There is no directly comparable data available for the third 'booster' dose. However, data is available on the total number of individuals born in or before 2003 (at least 18-19 years old) that have received the third dose (see 'Totalt' values in the Dos 3 per åldersgrupp tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)). We have therefore made use of these values to calculate the percentage of the population that have received the third dose.

Again, please note that these percentage values will differ from those calculated by FoHM, whose calculations do not consider the whole population, but rather the population eligible for the dose (from 12-13 years for the first and second doses, and from 18-19 years for the third dose).

#### Administration of one vaccine dose

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/onedose_pop_map.json" height="500px" >}}</div>
</div>

#### Administration of two vaccine doses

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/twodose_pop_map.json" height="500px" >}}</div>
</div>

#### Administration of three vaccine doses

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/threedose_pop_map.json" height="500px" >}}</div>
</div>

### Administration of vaccinations according to age group

We constructed the below heatmap to show how the relative numbers of people vaccinated differs according to age. Unsurprisingly, the more advanced age groups tend to have higher levels of vaccination for each dose, as they are given access at an earlier stage.

Data is available for individuals born in or before 2009 (i.e. at least 12-13 years old) for the first and second vaccine doses (available in the 'Vaccinerade ålder' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)), and for people born in or before 2003 (i.e. at least 18-19 years old) for the third dose (available in the 'Dos 3 per åldersgrupp' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)). In this case, we have not performed any recalculation, so the numbers are the same as those provided by FoHM.

**Note about the heatmap:** A white colouration indicates that no data is available for that age group.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/vaccine_heatmap.json" height="750px" >}}</div>
</div>

## Ongoing research projects

Below is a manually curated overview of projects focussed on **vaccine research** that are/were funded by major funding agencies in Sweden. As it is manually curated, the list may not be exhaustive, but new projects will be added as soon as possible. If you are aware of a project that is not listed here but ought to be, please [get in touch with us](/contact/). For a list of all research projects funded by major funding agencies in Sweden, see [this section of the portal](/projects/funding/) instead.

{{< display_funded_projects filter_variable="vaccine" >}}

## Publications

Below is a subset of preprints and published scientific journal articles on the subject of **vaccine research** involving at least one author affiliated with a Swedish university or research institute. If you would like for your publication to be displayed here, or feel that information about a publication requires correction, please [get in touch with us](/contact/). For a full list of all publications related to COVID-19 and SARS-CoV-2 that involve at least one author affiliated with a Swedish university or research institute, please see [this section of the portal](/publications/).

{{< vaccines_publications >}}

{{< vaccines_dynamic_content >}}
