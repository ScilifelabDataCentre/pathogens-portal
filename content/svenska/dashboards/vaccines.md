---
title: Administrering av covid-19 vaccin och vaccinforskning i Sverige
description: Folkhälsomyndigheten tillhandahåller data och information om covid-19 i Sverige. Visualiseringar visas på flera aspekter av vaccinationstäckningen, som täckning i olika län.
banner: /dashboard_thumbs/vaccines.jpg
toc: true
plotly: true
menu:
  dashboard_menu:
    identifier: vaccines
    name: Administrering av covid-19 vaccin
aliases:
  - /sv/data_types/health_data/vaccines/
---

<div class="alert alert-info">
  <i class="bi bi-exclamation-triangle-fill"></i>
  <span>Uppgifterna på den här sidan uppdateras inte längre vid datakällan. Vi utvärderar för närvarande användningen av andra datakällor för vaccindata. Se vår <a href="/dashboards/recovac/">RECOVAC dashboard</a> för mer information om vaccin effektivitet och säkerhet (denna dashboard är endast tillgänglig på engelska).</span>
</div>

## General information on COVID-19 vaccines

Over the last two years, the COVID-19 pandemic has challenged societies and healthcare systems worldwide. In response, vaccines and therapeautic treatments have been rapidly developed. To date (October 2022), the [European Medicines Agency (EMA)](https://www.ema.europa.eu/en) has approved six vaccines against COVID-19:

- **Comirnaty** - produced by Pfizer/BioNTech, approved on 21st December 2020. New updates variants for boosters are available (Oct 2022), for example, Comirnaty Original/Omicron BA.1 and Comirnaty Original/Omicron BA.4-5
- **Spikevax** - produced by Moderna, approved on 6th January 2021. New updated variant for boosters is available (Oct 2022), Spikevax bivalent Original/Omicron BA.1.
- **Vaxzevria (previously called COVID-19 Vaccine AstraZeneca)** - produced by AstraZeneca, approved on 29th January 2021.
- **Jcovden (previously COVID-19 Vaccine Janssen)** - produced by Janssen, approved on 11th March 2021.
- **Nuvaxovid** - produced by Novavax, approved on 20th December 2021.
- **COVID-19 Vaccine Valneva** - produced by Valneva Austria GmbH, approved on 24th June 2022.

New vaccines are developed regularly, and are reviewed by EMA. Please refer to EMA's page on [COVID-19 vaccines](https://www.ema.europa.eu/en/human-regulatory/overview/public-health-threats/coronavirus-disease-covid-19/treatments-vaccines/covid-19-vaccines) to see the latest information on which vaccine are approved, which have submitted marketing authorisation, and which are under rolling review. New vaccines remain under rolling review until EMA have reviewed clinical trial data and determined that there is sufficient evidence to enable developers to apply for marketing authorisation.

As of October 2022, only **Comirnaty** (Pfizer/BioNTech), **Spikevax** (Moderna), and **Nuvaxovid** (Novavax) are available in Sweden. **Vaxzevria** (AstraZeneca) was used in past, but ceased to be used after 1st September 2021. The latest information on which vaccines are currently in use in Sweden can be found in [emergency information from Swedish authorities](https://www.krisinformation.se/en/hazards-and-risks/disasters-and-incidents/2020/official-information-on-the-new-coronavirus/vaccination-against-covid-19/about-the-vaccines).

### COVID-19 vaccination in Sweden

On this page, we explore publicly available data for COVID-19 vaccination in Sweden. We [visualise](/dashboards/vaccines/#visualisations-related-to-vaccination-coverage) multiple different aspects of vaccine coverage (i.e. the amount of people that have received a vaccination). Specifically, we consider coverage on different spatial scales (including Sweden in general, as well as specific counties), in different age groups, and for different dose levels. We provide links to the data underlying the visualisations and the scripts used to produce them. The visualisations do not include information about the type of vaccine used.

This page also displays information about [ongoing research projects](/dashboards/vaccines/#ongoing-research-projects) across Sweden related to COVID-19 vaccines. The list includes different kinds of projects, including life science projects, registry-based projects, and public health projects. We also [display a subset of publications](/dashboards/vaccines/#publications) related to vaccine research by researchers affiliated with a Swedish university or research institute.

<div class="alert alert-info">
    <i class="bi bi-info-circle-fill"></i> We invite researchers affiliated with a Swedish research institute to <a href="https://www.covid19dataportal.se/contact/">contact us</a> about adding information, data, and/or visualisations related to their own vaccine research to this Portal.
</div>

For more information on vaccination in Sweden, please also see the [RECOVAC dashboard on this portal](/dashboards/recovac/). The dashboard contains information and data visualisations related to the register-based large-scale national population study to monitor COVID-19 vaccination effectiveness and safety [(RECOVAC)](https://www.gu.se/en/research/recovac).

## Visualisations related to vaccination coverage

<div class="alert alert-info">The visualisations on this page were last updated: <span id="visualisations_date_modified">2023-03-24</span>.</div>

The [Swedish Health Agency (Folkhälsomyndigheten, FoHM)](https://folkhalsomyndigheten.se) provide information, summary statistics, and data related to COVID-19 vaccination in Sweden [(only available in Swedish)](https://www.folkhalsomyndigheten.se/folkhalsorapportering-statistik/statistikdatabaser-och-visualisering/vaccinationsstatistik/statistik-for-vaccination-mot-covid-19/). The visualisations below are based on the publicly available COVID-19 vaccination data from FoHM, which can be [downloaded directly](https://blobserver.dc.scilifelab.se/blob/Folkhalsomyndigheten_Covid19_Vaccine-93.xlsx). For each visualisation, we describe which data in the dataset were used, how calculations were completed, and provide a link to the script(s) used to produce it.

 All of our code related to this page is available on [GitHub](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/tree/main/Vaccine_page). All of the vaccine data is processed using a single [data preparation script](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Vaccine_page/vaccine_dataprep_Swedentots.py). The code required to generate each visualisation/number set is linked close to the corresponding plot/text.

### General summary statistics

In this section, we examine the overall levels of vaccination in Sweden, as well as the recent rate of vaccination.

Vaccine coverage can be calculated in multiple ways. Below, we compare two methods used to determine the percentage of the Swedish population, in total, that have received at least X doses. One method, which we refer to as the 'eligible population method', involves calculating the percentage of 'eligible' individuals that have received at least a given number of doses. In Sweden, as in many countries, different age groups are eligible for different doses. As of October 2022, individuals born in or before 2010 (around 12 years old) are considered eligible for the first two doses, individuals born in or before 2004 (around 18 years old) are considered eligible for a booster, a third dose. The second booster, a fourth dose, is recommended for individuals over 65 years and risk groups over 18 years old, but also available for all individuals over 18 that wish to be vaccinated. Individuals born in or before 1957 (around 65 years old) are considered eligible for the fifth dose if at least four months has passed since the last dose. The other method of calculation for vaccine coverage, which we refer to as the 'whole population method', instead involves calculating the number of people vaccinated as a percentage of the entire population, regardless of how much of the population is eligible.

Please note, because not everyone is eligible for all doses, it would not be appropriate to compare values between the different dose levels for the purposes of asssessing e.g. vaccine coverage or uptake.

In the chart below, we show vaccine coverage as calculated using the 'whole population' and 'eligible population' methods. The calculations consider the number of individuals in Sweden that have received at least 1, 2, 3, 4, or 5 doses. This is intended to highlight how the method of calculation used can influence reported measurements. As different methods are sometimes used by different countries, and by different organisations within a country, it is important to consider the method used before comparing data.

Please note, we refer to the number of doses administered (at least) for simplicity. However, other sources may use specific names/classifications to refer to different doses. For example, individuals given at least 2 doses may be considered 'fully vaccinated'. The third dose is also sometimes referred to as a 'booster dose'. Individuals with at least 3 doses are thus sometimes said to be 'fully vaccinated with a booster dose'. Other variations also exist, and other terms may arise as subsequent doses becomes more widely available.

Vaccination data is spread between multiple tabs of the [FoHM data file](https://blobserver.dc.scilifelab.se/blob/Folkhalsomyndigheten_Covid19_Vaccine-93.xlsx). For calculations done using the 'eligible population method', we used percentage data from the 'Vaccinerade tidsserie', 'Vaccinerade tidsserie dos 3', 'Vaccinerade tidsserie dos 4', and 'Vaccinerade tidsserie dos 5' tabs of the [FoHM data file](https://blobserver.dc.scilifelab.se/blob/Folkhalsomyndigheten_Covid19_Vaccine-93.xlsx). These tabs contained data about the amount of individuals that received at least one or two doses, at least 3 doses, at least 4 doses, and at least 5 doses, respectively. For the 'whole population method', we use the latest population data from [Statistics Sweden (SCB)](https://www.scb.se/) and the most recent 'raw number' of the doses administered from same tabs in the [FoHM data file](https://blobserver.dc.scilifelab.se/blob/Folkhalsomyndigheten_Covid19_Vaccine-93.xlsx).

**Note on the graph:** Click on the coloured squares in the legend of the below graph to toggle which datasets are displayed. A single click will toggle just that dataset on/off. It is possible to display only one of the datasets by double-clicking on the desired dataset.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/Total_vaccinated_barchart.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Vaccine_page/vaccine_indicator_barchart.py).

**Code used to generate the 'live text' in the summary paragraph below:** ['Live text' script](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Vaccine_page/vaccine_livetext.py).

To summarise, in total, <span id="eligible_one_dose"></span>% of the population that are eligible for the first dose have received at least one dose of vaccination against COVID-19, which represents <span id="population_one_dose"></span>% of the whole population. The values indicate that <span id="eligible_one_dose_lastweek"></span>% of the eligible population were vaccinated last week (a change in rate of <span id="eligible_one_dose_rate_change"></span>% compared to the previous week), or <span id="population_one_dose_lastweek"></span>% of the whole population (a change of <span id="population_one_dose_rate_change"></span>% compared to the previous week). By contrast, <span id="eligible_two_doses"></span>% of those eligible, and <span id="population_two_doses"></span>% of the whole population have received at least two doses in total. The values indicate that <span id="eligible_two_doses_lastweek"></span>% of those eligible and <span id="population_two_doses_lastweek"></span>% of the whole population received their second dose last week (a change in rate of <span id="eligible_two_doses_rate_change"></span>% and <span id="population_two_doses_rate_change"></span>% compared to the previous week, respectively). In total, <span id="eligible_three_doses"></span>% of the eligible population received the third dose, representing <span id="population_three_doses"></span>% of the whole population. This means that <span id="eligible_three_doses_lastweek"></span>% of the eligible population received their third dose last week (a change in rate of <span id="eligible_three_doses_rate_change"></span>% compared to the previous week), or <span id="population_three_doses_lastweek"></span>% of the whole population (a change of <span id="population_three_doses_rate_change"></span>% compared to the previous week). To date, <span id="population_four_doses"></span>% of the whole population has received a fourth dose, and <span id="eligible_four_doses"></span>% of those eligible. In the last week, <span id="population_four_doses_lastweek"></span>% of the whole population were vaccinated with a fourth dose, a change in rate of <span id="population_four_doses_rate_change"></span>% compared to the previous week. By contast, <span id="eligible_four_doses_lastweek"></span>% of the eligible population were vaccinated with a fourth dose, a relative change in rate of <span id="eligible_four_doses_rate_change"></span>% compared to the previous week. A fifth dose was added in September 2022, <span id="population_five_doses"></span>% of the Swedish population have received that dose to date, which amounts to <span id="eligible_five_doses"></span>% of those eligible. A total of <span id="population_five_doses_lastweek"></span>% of the whole population were vaccinated with a fifth dose in the last week, a change of <span id="population_five_doses_rate_change"></span>% compared to the week before. When considering only the eligible population, <span id="eligible_five_doses_lastweek"></span>% were given a fifth dose last week, which constitutes a relative change in rate of <span id="eligible_five_doses_rate_change"></span>% compared to the previous week.

### Administration of vaccinations over time

In Sweden, the first vaccine doses were administered in early 2021. As in other countries, the first two doses were made available to progressively younger age groups over time. The third dose of the vaccine was first offered in autumn of 2021, and was offered to individuals in particular ages groups at a given interval after their second dose. The age group and interval length differed over time, with age groups generally getting younger and the interval becoming shorter. A third dose is not offered to those under 18 years of age, unless there are additional considerations e.g. the individual is immunocompromised. In early 2022, a fourth dose was made available to those aged over 80, those receiving care, those living in housing facilities for the elderly, and those with severe immunodeficiency. This was extended to include those over 65 in April 2022. As of September 2022, it was made largely available to those over 18, though the availability varied between counties. At each stage of the rollout of the fourth dose, exceptions were made so that others could get the fourth dose under specific circumstances, for example, where an individual is immunocompromised or taking care of a vulnerable individual. A fifth dose was made available to those over 65 in September 2022 and, as with the other doses, it is likely to be made available to more of the population over time and other groups are able to access it under certain conditions.

Time series data is available in different tabs of the [FoHM data file](https://blobserver.dc.scilifelab.se/blob/Folkhalsomyndigheten_Covid19_Vaccine-93.xlsx). We therefore took data from different places to produce the below time series. Time series data related to the amount of individuals that have received at least one or two doses is available in the 'Vaccinerade tidsserie' tab. Time series data about the amount of individuals that have at least 3, 4, or 5 doses is available in the 'Vaccinerade tidsserie dos 3', 'Vaccinerade tidsserie dos 4', and 'Vaccinerade tidsserie dos 5' tabs, respectively. Again, please note that it would not be appropriate to compare across all of the dose levels, both because the vaccines are not similarly available and because FoHM do not include all of the doses administered in their data. Firstly, a dose is only 'counted' in the FoHM data if it is administered to an individual within a specific age range. Data on the first on second doses is only included for individuals born in or before 2010 (around 12 years old). Data on the third and fourth doses is only included for individuals born in or before 2004 (around 18 years old). Data on the fifth dose is only included if it was given to an individual born in or before 1957 (around 65 years old). There are also some other caveats about whether a dose is 'counted' in the data file. In particular, data on the third dose is only included if it was registered after 1st September 2021 and at least 8 weeks after the individual received their second dose. Similarly, data on the fourth dose is only included if it was registered after 21st January 2022 and at least 8 weeks after the individual received their third dose. Lastly, data on dose 5 is only included if the dose was registerd after 15th August 2022 and was received at least 80 days after the individual received dose 4.

The below graph shows vaccine coverage across the whole of Sweden. We use the 'whole population' method for calculation, as this is more often used by other countries. Our calculations will therefore differ from the percentage values provided by FoHM as part of their summary statistics, because they use the 'eligible population' method of calculation. For more details on the two methods, see the [general summary statistics](/dashboards/vaccines/#general-summary-statistics) section.

**Note on the graph:** Click on the coloured squares in the legend of the below graph to toggle which datasets are displayed. A single click will toggle just that dataset on/off. It is possible to display only one of the datasets by double-clicking on the desired dataset.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/vaccine_timeseries_pop_barchart.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Vaccine_page/vaccine_timeseries_barchart.py).

### Administration of vaccinations in each Swedish county (län)

In this section, we explore how many individuals in a given Swedish county (län) had at least X vaccine doses. Here, we again use the 'whole population' method of calculation (see the [general summary statistics](/dashboards/vaccines/#general-summary-statistics) section for details). Data on the total number of people in each county was taken from [Statistics Sweden (SCB)](https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/population-composition/population-statistics/). Data on the amount of individuals given at least one or two doses in each county was taken from the 'Vaccinerade tidsserie' tab of the [data from FoHM](https://blobserver.dc.scilifelab.se/blob/Folkhalsomyndigheten_Covid19_Vaccine-93.xlsx). As mentioned in previous sections, only doses given to individuals born in or before 2010 (around 12 years old) are counted. Data on the amount of individuals given at least 3 or 4 doses (available in the 'Vaccinerade tidsserie dos 3' and 'Vaccinerade tidsserie dos 4' tabs of the [FoHM data](https://blobserver.dc.scilifelab.se/blob/Folkhalsomyndigheten_Covid19_Vaccine-93.xlsx), respectively) is only given for those born before 2004 (around 18 years old) and in accordance with specific timeframes and registration timepoints. Data on the fifth dose (available in the 'Vaccinerade tidsserie dos 5' tab of the [FoHM data](https://blobserver.dc.scilifelab.se/blob/Folkhalsomyndigheten_Covid19_Vaccine-93.xlsx)) is only available for those born before 1957 (around 65 years old), and in accordance with certain timeframes. Given the differences in which data is 'counted' for each dose, it is clear that data should not be compared across doses.

As data for the fifth dose is available to such a small amount of the population, we have decided to analyse the data using both the 'whole population' and 'eligible population' methods. We feel that this will allow a clearer understanding of the differences between län in terms of the coverage for the fourth dose.

Again, please note that percentage values calculated using the 'whole population method' will differ from those calculated by FoHM, whose calculations do not consider the whole population, but rather the population eligible for the dose (from 12 years for the first and second doses, from 18 years for the third and fourth doses, and from 65 years for the fifth dose).

#### Received at least one vaccine dose

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/onedose_pop_map.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce maps](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Vaccine_page/vaccine_maps_population.py).

#### Received at least two vaccine doses

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/twodoses_pop_map.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce maps](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Vaccine_page/vaccine_maps_population.py).

#### Received at least three vaccine doses

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/threedoses_pop_map.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce maps](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Vaccine_page/vaccine_maps_population.py).

#### Received at least four vaccine doses

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/fourdoses_pop_map.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce maps](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Vaccine_page/vaccine_maps_population.py).

#### Received at least five vaccine doses

Please note the differences between the two below maps. Coverage appears to be very low when considering the whole population (left). However, coverage is higher when considering only the population eligible to receive the fifth dose (right). This difference occurs because, whilst a relatively small portion of the entire population is eligible to receive this dose, most of those eligible have received it.

<div class="row">
<div class="col-md"><div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/fivedoses_pop_map.json" height="500px" >}}</div>
</div></div>
<div class="col-md"><div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/fivedoses_elig_map.json" height="500px" >}}</div>
</div></div>
</div>

**Code used to produce plot:** [Script to produce maps](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Vaccine_page/vaccine_maps_population.py).

### Administration of vaccinations according to age group

The below heatmap provides some indication of the vaccine coverage across different age groups. The data for this **heatmap differs from that in the previous visualisations**. Specifically, instead of showing the number of people with 'at least X doses', the heatmap shows the number of people in Sweden in each age group that have been given **that specific number of doses**. For example, rather than showing the amount of people with 'at least one dose', we show the number that have had 'only one dose'. Understandably, the number that have received ONLY one dose is relatively low across all age groups; individuals that have taken one dose are naturally more likely to take subsequent doses when they become eligible to do so. Given that individuals in more advanced age categories are eligible to take more doses, coverage is likely to be higher at a greater dose level. Age groups that have only recently become eligible for a given dose level are likely to initially show low coverage.

The fact that data is not available for each age category for every dose is reflected in the graph (a white colouration is used to indicate where data is not available/included). Data on the first three doses are available in the 'Dos 1 till 3 per åldersgrupp' tab of the [FoHM dataset](https://blobserver.dc.scilifelab.se/blob/Folkhalsomyndigheten_Covid19_Vaccine-93.xlsx). Data on the fourth and fifth doses are instead available in the 'Dos 4 18+' and 'Dos 5 per åldersgrupp' tabs, respectively.

The 'eligible population method' was used in this case, as it would not be appropriate to consider the whole population when considering vaccination coverage within specific age groups.

Data is available on the number of individuals aged 65-69 that have received the fifth dose. We have not included it in the heatmap because data is not available across the 60-69 age category used in the heatmap.

**Note about the heatmap:** A white colouration indicates that no data is available for that age group.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/vaccine_heatmap.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce heatmap](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Vaccine_page/vaccine_heatmaps.py).

## Ongoing research projects

Below is a manually curated overview of projects focussed on **vaccine research** that are/were supported by major funding agencies in Sweden. As it is manually curated, the list may not be exhaustive. If you are aware of a project that is not listed here but ought to be, please [get in touch with us](/contact/). For a list of all research projects funded by major funding agencies in Sweden, see [this section of the portal](/projects/funding/) instead.

{{< display_funded_projects filter_variable="vaccine" >}}

## Publications

Below is a subset of preprints and published scientific journal articles related to **vaccine research** that involve at least one author affiliated with a Swedish university or research institute. If you would like for your publication to be displayed here, or feel that information about a publication requires correction, please [get in touch with us](/contact/). For a fuller list of all publications related to COVID-19 and SARS-CoV-2 that involve at least one author affiliated with a Swedish university or research institute, please see [this section of the portal](/publications/).

{{< vaccines_publications >}}

{{< vaccines_dynamic_content >}}

### Other sources of information about COVID-19 vaccines

- General information about COVID-19 is available from [The Swedish Health Agency](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/).
- Information about COVID-19 vaccines is available from [The Swedish Medical Products Agency](https://www.lakemedelsverket.se/en/coronavirus/covid-19-vaccine).
- For health information connected to vaccination and tests by different Swedish regions, see [regional information on 1177](https://www.1177.se/).
- Information about COVID-19 vaccine approval, rollout, and safety is available from [The European Centre for Disease Prevention and Control (ECDC)](https://www.ecdc.europa.eu/en/covid-19/prevention-and-control/vaccines).
- Additional information about COVID-19 vaccines is available from [the Centre for disease Control (CDC)](https://www.cdc.gov/coronavirus/2019-ncov/vaccines/index.html).
- Information and data visualisations related to the register-based large-scale national population study to monitor COVID-19 vaccination effectiveness and safety ([RECOVAC](https://www.gu.se/en/research/recovac)) are presented in a [separate dashboard on this Portal](/dashboards/recovac/).
