---
title: The Administration and Study of Vaccines in Sweden
toc: false
plotly: true
---

<div class="alert alert-info">
  <i class="fas fa-exclamation-triangle"></i>
  <span>En svensk översättning av denna sida kommer inom kort.</span>
</div>

## General information on vaccine research

Over the last two years, the COVID-19 pandemic has challenged societies and healthcare systems worldwide, and vaccines and therapeautic treatments have been rapidly developed in response. To date, the [European Medicines Agency (EMA)](https://www.ema.europa.eu/en) has approved four vaccines against COVID-19:

* **Comirnaty** - produced by Pfizer/BioNTech, approved on 21st December 2020. 
* **Spikevax** - produced by Moderna, approved on 6th January 2021. 
* **Vaxzevria** - produced by AstraZeneca, approved on 29th January 2021. 
* **Covid-19 Vaccine** - produced by Janssen, approved on 11th March 2021. 

All except Covid-19 Vaccine (by Janssen) have been used in Sweden, though only **Comirnaty** (Pfizer/BioNTech) and **Spikevax** (Moderna) are currently available. **Vaxzevria** (AstraZeneca) ceased to be provided after 1st September 2021.

This page is focussed on vaccine research. On it, we [visualise](/data_types/health_data/vaccines/#visualisations-related-to-vaccination-coverage) information about the amount of people (across different regions, different age groups, or in Sweden generally) that have received one, two, or three doses of vaccination. We also provide links to the publicly available data underlying those visualisations. The visualisations do not include information about the type of vaccine used.

The section also displays a subset of ongoing [Swedish research projects](/data_types/health_data/vaccines/#ongoing-research-projects) related to vaccine research. These projects are focussed broadly on vaccines and, as such, they include life science projects, registery-based projects, and public health projects. We also [show a subset of publications](/data_types/health_data/vaccines/#publications) related to vaccine research by researchers affiliated with a Swedish University or Research Institute. Lastly, we provide more [detailed information on some projects](/data_types/health_data/vaccines/#vaccine-research-projects) on vaccine research that are sharing data.

### Additional resources on COVID-19 vaccines

The **Swedish Health Agency** provides general information about COVID-19 [here](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/).

The **Swedish Medical Products Agency** provides information about COVID-19 vaccines [here](https://www.lakemedelsverket.se/en/coronavirus/covid-19-vaccine).

For health information connected to vaccination and tests by different **Swedish Regions**, see [Regional information on 1177](https://www.1177.se/).

The **European Centre for Disease Prevention and Control** (ECDC) shows information about the vaccines [here](https://www.ecdc.europa.eu/en/covid-19/prevention-and-control/vaccines).

Information about the vaccines is available from the **Centre for disease Control** [here](https://www.cdc.gov/coronavirus/2019-ncov/vaccines/index.html).

## Visualisations related to vaccination coverage

The visualisations in this section are based on publicly available data from the [Swedish Health Agency (Folkhälsomyndigheten, FoHM)](www.folkhalsomyndigheten.se). Follow [this link](https://www.folkhalsomyndigheten.se/folkhalsorapportering-statistik/statistikdatabaser-och-visualisering/vaccinationsstatistik/statistik-for-vaccination-mot-covid-19/) to view their summary of statistics related to vaccination against COVID-19 in Sweden (only available in Swedish). The data used to produce the visualations can be downloaded [here](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data). For each visualisation, we describe which part of the dataset was used and how the calculations were done. The data is updated weekly (on Thursdays).

### General summary statistics

In this section, we examine the overall levels of vaccination in Sweden, as well as the recent rate of vaccination. 

Here, we compare two methods of vaccination; one used by FoHM and one based on the whole population. FoHM have calculated vaccination rates for Sweden by taking the number of vaccinated individuals that are at least 16 years of age as a percentage of the size of the population born since 2005. This method thus essentially approximates the vaccination rate of the population above 16 years of age. The 'FoHM method' differs from that used by other countries, which consider the percentage of the entire population vaccinated. We display the results of both calculations for each vaccine dose (first, second, and third) on the chart below to highlight how the method of calculation used influences the data.

For calculations produced using the 'FoHM method', we use data from the Vaccinerade tidsserie tab of the [FoHM data](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data), specifically the percentage calculation. For the 'whole population method', we instead take the total number of vaccines and use the latest count of the population size of Sweden (available from from [Statistics Sweden (SCB)](https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/population-composition/population-statistics/pong/tables-and-graphs/monthly-statistics--the-whole-country/population-statistics-2021/)) to calculate it as a percentage.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/Total_vaccinated_barchart.json" height="500px" >}}</div>
</div>

<!-- THE BELOW PARAGRAPH CONTAINS MULTIPLE PLACEHOLDERS FOR LIVE TEXT -->
<!-- All the placeholders are calculated in vaccine_indicator_panel_content -->

To summarise, in total, {placeholder: one_dose_swe}% of the population above around 16 years of age have received one dose of vaccination against COVID-19, which represents {placeholder: one_dose_pop}% of the whole population. The values indicate that {placeholder: rate_onedose_lastwk}% of the population over 16 were vaccinated over the last week (a change in rate of {placeholder: onedose_ratechange}% compared to the previous week), or {placeholder: one_dose_pop_lastweek}% of the whole population (a change of {placeholder: onedose_ratechange_pop}% compared to the previous week). By contrast, {placeholder: least_two_dose_swe}% of those over 16, and {placeholder: least_two_dose_pop}%, of the whole population have received two doses in total. Further, {placeholder: rate_leasttwodose_lastwk}% of those over 16 and {placeholder: least_two_dose_pop_lastweek}% of the whole population received their second dose last week (a change in rate of {placeholder: twodose_ratechange}% and {placeholder: twodose_ratechange_pop}% compared to the previous week, respectively). Lastly, {placeholder: third_vacc_dose_tot}% of the population above 16 has received a third 'booster' dose, representing {placeholder: third_vacc_dose_pop}% of the whole population. Since no time series data is available for the third dose yet, it is not possible to calculate data related to rates at this stage.

Reuters COVID-19 Tracker provides some additional summary information on vaccinations against COVID-19 (as well as information regarding the implementation of lockdown measures and cases) [for Sweden](https://graphics.reuters.com/world-coronavirus-tracker-and-maps/countries-and-territories/sweden/). In particular, the data includes how many doses would be needed to provide 100% of the population with 2 doses, and an estimation of how long (based on the current number of doses administered daily) it might take to vaccinate 10% more of the total population.

### Administration of vaccinations over time

The first vaccine doses were administered in Sweden in early 2021. As with other countries, the vaccine program rollout was such that the vaccine became available to decreasing age groups over time (MAYBE WE SHOULD HAVE THIS INCLUDED AS GENERAL INFORMATION SOMEWHERE ELSE ON THE PAGE?? COULD ALSO EXTEND THE INFO).

As of December 2021, data about the administration of vaccinations over time is only available for the first two doses (in the Vaccinerade tidsserie tab of [FoHM data](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)). We have presented the data for the whole of Sweden as a percentage of the Swedish population in the below graph (using the latest population size data from [Statistics Sweden (SCB)](https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/population-composition/population-statistics/pong/tables-and-graphs/monthly-statistics--the-whole-country/population-statistics-2021/)). In future we hope to also be able to show data for the third dose. 

Please keep in mind that this data differs from the percentages as calculated by FoHM, but is comparable to the calculations used by other countries, see the information in the 'general summary statistics' section for details.

**NOTE ON THE GRAPH:** Click on the coloured squares in the legend of the below graph to toggle which datasets are displayed.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/vaccine_timeseries_pop_barchart.json" height="500px" >}}</div>
</div>

### Administration of vaccinations in each county (lan)

In this section, we explore the levels of vaccination coverage for each of the three doses in each county (lan) of Sweden. We again use the latest data on the population size for each county from [Statistics Sweden (SCB)](https://www.scb.se/en/finding-statistics/statistics-by-subject-area/population/population-composition/population-statistics/pong/tables-and-graphs/monthly-statistics--the-whole-country/population-statistics-2021/) to calculate the number of each type of dose administered as a percentage of the whole population of that county. We take the number of first and second doses administered in that county from the 'Vaccinerade tidsserie' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)). Again, please note that the 'raw numbers' related to these doses represent the vaccinations administered to those aged at least 16. As of December 2021, there is no directly comparable 'raw numbers' data availabble for the third 'booster' dose. However, data is available on the total number of individuals aged 18+ that have received each dose in each county (see 'Totalt' values in the Dos 3 per åldersgrupp tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)). We have therefore made use of these values to calculate the percentage of the population that have received the third dose.

Again, please note that these percentage values will differ from those calculated by FoHM, whose calculations only consider the size of the population born since the start of 2005, rather than the whole population.

#### Administration of one vaccine dose:

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/onedose_pop_map.json" height="500px" >}}</div>
</div>

#### Administration of two vaccine doses:

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/twodose_pop_map.json" height="500px" >}}</div>
</div>

#### Administration of three vaccine doses:

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/threedose_pop_map.json" height="500px" >}}</div>
</div>

### Administration of vaccinations according to age group

We constructed the below heatmap to show how the relative numbers of people vaccinated differs according to age. Unsurprisingly, the more advanced age groups tend to have higher levels of vaccination for each dose, as they are given access at an earlier stage.

As of December 2021, data is available for individuals above the age of 12 for the first and second vaccine doeses (available in the 'Vaccinerade ålder' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)), and for people above the age of 18 for the third dose (available in the 'Dos 3 per åldersgrupp' tab of the [data from FoHM](https://fohm.maps.arcgis.com/sharing/rest/content/items/fc749115877443d29c2a49ea9eca77e9/data)). In this case, we have not performed any recalculation, so the numbers are the same as those provided by FoHM.

**NOTE ABOUT THE HEATMAP:** A white colouration indicates that no data is available for that age group.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/vaccine_heatmap.json" height="750px" >}}</div>
</div>

## Ongoing research projects

Below is a manually curated overview of projects focussed on **vaccine research** that are/were funded by major funding agencies in Sweden. As it is manually curated, the list may not be exhaustive, but new projects will be added as soon as possible. If you are aware of a project that is not listed here but ought to be, please [get in touch with us](/contact/). For a list of all research projects funded by major funding agencies in Sweden, see [this section of the portal](/projects/funding/) instead.

## Publications

Below is a subset of pre-prints and published scientific journal articles on the subject of **vaccine research** involving at least one author affiliated with a Swedish university or research institute. This list is based on a manually curated database and, as such, may not be exhaustive. If you think that a publication should be listed here but isn’t, or feel that information about a publication requires correction, please [get in touch with us](/contact/). For a full list of all publications related to COVID-19 and SARS-CoV-2 that involve at least one author affiliated with a Swedish univerisity or research institute, please see [this section of the portal](/publications/).

## Vaccine research projects

### RECOVAC

The [**RECOVAC project**](https://www.gu.se/en/research/recovac) stands for Register-based large-scale national population study to monitor Covid-19 vaccination effectiveness and safety. It is a subproject to **SCIFI-PEARL**. (for more information about **SciFI-PEARL** se below) The project aim is to continuously follow-up Covid-19 vaccination research effectiveness and safety in Sweden using a linked multi-register observational study, *...deliver continuous Covid-19 vaccination follow-up and research on effectiveness and safety in a nationwide linked  multi-register, regularly updated, observational study for timely response to key scientific questions...* [RECOVAC webpage](https://www.gu.se/en/research/recovac),Gothenburg University.

The **RECOVAC project**, will also address potential vaccine adverse effect related to vaccination status and characteristics of the subjects. Study population and data will be regularly updated every 1-3 months. In summary, this research provides a unique resource of continuous data that can be used for future epidemiological research on Covid-19 vaccination. In addition, the research can be used support public health and safety, as well as for policy-making related to the present-day Covid-19 pandemic. The research group from Gothenburg University has also launched aa web app [*"Symptoms"*](https://www.symptoms.se/recovac/fpi ) that will enable patient self-reporting of symptoms, which will then directly contribute to vaccine monitoring and safety in the research project.

#### Visualisations

To be added from Patricia

#### General information:
EPN Nr xxx

#### Contact information
Prof *Fredrik Nyberg*, Project leader and Guest Professor for Register epidemiology,
Gothenburg University. Email: fredrik.nyberg@gu.se or Email: scifipearl@medicin.gu.se
*Patricia Ernst*, Project coordinator SCIFI-PEARL and RECOVAC. Email: patricia.ernst@gu.se

#### Funders
SciLifeLab / Knut and Alice Wallenbergs Foundation, [Swedish Research Council](www.vr.se)

#### Data availability
In order to get data from the **RECOVAC project** xxx

#### Terms for access for the **RECOVAC project datasets**
The database can only be used for xxx (this section will come from Patricia)

#### Publications and pre-prints
*Publications*
Stridsman C, Vanfleteren LEGW, Konradsen JR, Axelsson Fisk S, Pedroletti C, Sjöö Y, Syk J, Sterner T, Lindberg A, Tunsäter A, Nyberg F, Ekberg-Jansson A, Karlsson Sundbaum J
*Eur Respir J* 58 (5) 2101920 [2021-11-00; online 2021-08-19]

Swedish Covid-19 Investigation for Future Insights - A Population Epidemiology Approach Using Register Linkage (SCIFI-PEARL).
Nyberg F, Franzén S, Lindh M, ..., Björck S, Gisslén M
*CLEP* 13 (-) 649-659 [2021-07-30; online 2021-07-30]

Thirty-Day Outcomes of Children and Adolescents With COVID-19: An International Experience. Duarte-Salles T, Vizcaya D, Pistillo A, Casajust P, Sena AG, Lai LYH, Prats-Uribe A, Ahmed WUR, Alshammari TM, Alghoul H, Alser O, Burn E, You SC, Areia C, Blacketer C, DuVall S, Falconer T, Fernandez-Bertolin S, Fortin S, Golozar A, Gong M, Tan EH, Huser V, Iveli P, Morales DR, Nyberg F et al. *Pediatrics* 148 (3) e2020042929 [2021-09-00; online 2021-05-28]

*Preprints*
Nyberg F, Lindh M, Vanfleteren LEGW, Hammar N, Wettermark B, Sundström J, Santosa A, Kirui BK, Gisslén M.(2021) Adverse events of special interest for COVID-19 vaccines - background incidences vary by sex, age and time period and are affected by the pandemic. [Preprint, online 2021-10-05]

### SCIFI-PEARL

The **SCIFI-PEARL project** [Swedish Covid-19 Investigation for Future Insights – a Population Epidemiology Approach using Register Linkage](https://www.gu.se/en/research/scifi-pearl) is a multi-register observational study using *register-based data* to answer questions related to Covid-19 disease. These questions include, for example; risk factors for unfavorable prognosis, and if aspects of comorbidity, treatments, or anamnesis increase long-term consequences of Covid-19 infections. In addition, the project  also addresses questions related to public health, such as if the present-day pandemics and vaccination program has affected drug use, or healthcare in individuals and society.

The overall project aim is to, using a broad range of National Healthcare Registers and Regional Healthcare data from different registers, capture representative general population cohort of Swedish residents with Covid-19 on ongoing basis. Data linkage, that Data from different health databases are linked via the national personal ID,  (personnummer)and regular updating of data, will provide relevant SARS CoV-2/COVID-19 related data for the cohort and allow a longitudinal view of the COVID-19 pandemic.

The following data from national and regional health registers are collected within the **SCIFI-PEARL project**; COVID-19 test data, Vaccination data from the [National Vaccination Register](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/vaccinationer/nationella-vaccinationsregistret/), data from the [National Patient Register](https://www.socialstyrelsen.se/en/statistics-and-data/registers/register-information/the-national-patient-register), the [Swedish Prescribed Drug Register](https://www.socialstyrelsen.se/en/statistics-and-data/registers/register-information/the-swedish-prescribed-drug-register/), [National Cancer Register](https://www.socialstyrelsen.se/en/statistics-and-data/registers/register-information/swedish-cancer-register/), as well as two regional health databases.
