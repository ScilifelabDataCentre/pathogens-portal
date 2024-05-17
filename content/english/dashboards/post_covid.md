---
title: "Post COVID-19 condition in Sweden: statistics, research projects, and available data"
description: "The Swedish Board of Health and Welfare (Socialstyrelsen) shares data on Post COVID-19 condition. Here, we show visualisations of data on symptoms, healthcare contacts, and geographic distribution, among other things."
banner: /dashboard_thumbs/postcovid.jpg
toc: true
plotly: true
menu:
  dashboard_menu:
    identifier: post_covid
    name: Post COVID-19 condition
aliases:
  - /data_types/health_data/post_covid/
dashboards_topics: [COVID-19, Infectious diseases]
---

Since the beginning of 2020, the COVID-19 pandemic has challenged healthcare and dramatically changed daily life for people worldwide. The severity of symptoms experienced by patients during the acute infection phase of COVID-19 disease varies between individuals from mild to severe. After this phase, there are usually no indications that the disease will have any long-term effects on their health, regardless of the severity of symptoms experienced during the acute infection phase. However, some patients continue to exhibit symptoms for prolonged periods after the acute phase. The symptoms experienced by such patients are broad, but can include, for example, deep fatigue, joint pain, ‘brain fog’ (difficulty concentrating on certain tasks for longer periods of time), and heart palpitations ([Brodin, 2021](https://doi.org/10.1038/s41591-020-01202-8), [Marx, 2021](https://doi.org/10.1038/s41592-021-01145-z)). These symptoms can have a significant impact on the patients' quality of life.

Most studies that have explored what causes some patients to experience prolonged symptoms have been descriptive. However, several recent studies have explored potential causes in detail. For example, [Važgėlienė _et al._ (2022)](https://www.mdpi.com/2077-0383/11/21/6278) investigated potential links between prolonged symptoms after COVID-19 infection and other types of chronic disease or daily medication. They found an association between the taking of daily medication and the development of prolonged symptoms after COVID-19 infection. Other studies have found that multiple other factors, including being female, advanced age, and poor general health, are associated with an increased risk of experiencing prolonged symptoms after a COVID-19 infection ([Sudre _et al._, 2021](https://www.nature.com/articles/s41591-021-01292-y)).

This condition (i.e. the presistance of symptoms following the acute phase of COVID-19 infection) has been referred to in multiple ways, including _Post COVID-19 condition_, _Post-COVID_, and _Long COVID_. On this page, we use the term _Post COVID-19 condition_ for consistency. See the _[Background Information](#background)_ section below for more detail about the nomenclature used and relevant research.

On this page, you can find visualisations of data related to _Post COVID-19 condition_ in Sweden from The Swedish Board of Health and Welfare ([Socialstyrelsen](https://www.socialstyrelsen.se)), an overview of ongoing _Post COVID-19 condition_ research projects in Sweden, and scientific publications regarding _Post COVID-19 condition_ by researchers affiliated with Swedish universities or research institutes.

For more information on _Post COVID-19 condition_ in Sweden, please see [this section](https://www.socialstyrelsen.se/coronavirus-covid-19/socialstyrelsens-roll-och-uppdrag/postcovid/) of The Swedish Board of Health and Welfare (Socialstyrelsen)’s website and their [report on _Post-COVID condition_ (published April 2021)](https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/artikelkatalog/ovrigt/2021-4-7351.pdf). More [general information](https://www.cdc.gov/coronavirus/2019-ncov/long-term-effects/index.html) is also available from the Centers for Disease Control and Prevention (CDC).

## Availability of data and code

### Data

<div class="alert alert-info">All data last updated: {{% postcovid_date_modified %}}</div>

The data underlying the visualisations on this page are from [The Swedish Board of Health and Welfare](https://www.socialstyrelsen.se/statistik-och-data/statistik/statistik-om-covid-19/) and comprise of data from both the [Patient Register](https://www.socialstyrelsen.se/statistik-och-data/register/alla-register/patientregistret/) and the [‘Cause of Death’ Register](https://www.socialstyrelsen.se/statistik-och-data/register/alla-register/dodsorsaksregistret/). The data are updated monthly, on the second Wednesday of the month, and are available for download [here](https://www.socialstyrelsen.se/statistik-och-data/statistik/statistik-om-covid-19/). Additional data about COVID-19 can be requested from the corresponding registers by any researchers fulfilling the requirements for access, the guidelines for access via the RUT (Register Utiliser Tool) are available [here](https://bestalladata.socialstyrelsen.se/data-for-forskning/).

### Code

All code used to produce the visualisations on this page is available on [GitHub](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/tree/main/postCOVID). The particular scripts used in each case are linked below the individual visualisations.

## Statistics on Post COVID-19 condition in Sweden

Since Post COVID-19 condition is not clearly defined, over time, it has been assigned multiple diagnosis codes for use by medical professionals/researchers. After the first cases of prolonged disease following COVID-19 infection were detected in spring 2020, The Swedish Board of Health and Welfare initiated the diagnosis _Z86.1A - COVID-19 in own medical history_ (Covid-19 i den egna sjukhistorien). This diagnosis code has been used since 1st June 2020. From 1st January 2021, this diagnosis code was replaced by _U08.9 (ICD-10-SE) - COVID-19 in own medical history, unspecified_ (Covid-19 i den egna sjukhistorien) in accordance with new [WHO (World Health Organization)](https://www.who.int) guidelines. This diagnosis should be used when an individual is receiving treatment for an illness/physical damage for which the patient’s history of COVID-19 infection is considered relevant (i.e. a contributory factor to the present illness/damage). Importantly, this diagnosis should only be given if the individual is no longer considered to have COVID-19, and if the current health condition is not considered to result from infection with COVID-19. _U08.9_ is an additional diagnosis, as such, it should only be assigned alongside a main diagnosis; it cannot be the main diagnosis.

From 16th October 2020, the Swedish Board of Health and Welfare initiated a new diagnosis, _U09.9 (ICD-10-SE) - Postinfectious state associated with COVID-19, unspecified_ (Postinfektiöst tillstånd efter covid-19, ospecificerat), in accordance with new WHO guidelines. This new diagnosis supplemented and partially replaced the _Z86.1A_ diagnosis. As with _U08.9_, the _U09.9_ diagnosis should only be given after the person is no longer considered to have COVID-19. This diagnosis code should be used for conditions that persist or begin after the acute infection stage has passed. _U09.9_ is also an additional diagnosis, and should only be assigned alongside a separate main diagnosis.

For more information and current guidelines regarding diagnoses used for conditions related to a history of COVID-19, see [this webpage](https://www.socialstyrelsen.se/utveckla-verksamhet/e-halsa/klassificering-och-koder/icd-10/) from The Swedish Board of Health and Welfare.

### Age and sex distribution of diagnosed cases

These plots display the number of times that patients were assigned the diagnoses of interest in Sweden since the introduction of the relevant codes, divided by patient age and sex.

#### Diagnosis U09.9

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/U099_agesex_casedist.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/create_agesex_distcases.py).

#### Diagnosis Z86.1A/U08.9

<div class="plot_wrapper mb-3">
    <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/U089_agesex_casedist.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/create_agesex_distcases.py).

### Geographic distribution of diagnosed cases relative to population size

The maps below show the number of people that received the diagnoses of interest in each county as a percentage of the total population of that county. The total population of the county and the number of people who received the diagnosis can be seen by hovering the mouse above a particular county.

#### Diagnosis U09.9

<div class="plot_wrapper mb-3">
    <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/map_postcovid_percent_of_population_U099.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Data preparation script](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/postcovid_dataprep.py), [Script to produce map](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/postcovid_mapfig_population_U099.py).

#### Diagnosis Z86.1A/U08.9

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/map_postcovid_percent_of_population_U089.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Data preparation script](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/postcovid_dataprep.py), [Script to produce map](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/postcovid_mapfig_population_U089.py).

<!--

{{/* The data used for this is not available anymore, this section should be removed if no alternatives found */}}

### Geographic distribution of diagnosed cases relative to confirmed COVID-19 cases

The maps below show the number of people that received the diagnoses of interest in each county as a percentage of the total number of confirmed COVID-19 cases in that county (based on [data from the Public Health Agency (Folkhälsomyndigheten)](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/statistik-och-analyser/bekraftade-fall-i-sverige/)). Specifically, the cumulative number of COVID-19 cases in the county at the date given for the last update of the number of diagnoses of interest. Both the total number of confirmed COVID-19 cases and the number of people who received the diagnoses of interest can be seen by hovering the mouse above a particular county. Please note that the data visualised on this map should be interpreted with considerable caution for a few reasons. One reason for this is that the number of COVID-19 cases is likely underestimated; some cases of COVID-19 are asymptomatic, and not all symptomatic cases will have been confirmed and reported. The diagnoses related to *Post COVID-19 condition* were also introduced later than COVID-19, so not all cases of *Post COVID-19 condition* are likely to have received a formal diagnosis. Further, since *Post COVID-19 condition* may not be diagnosed for months following acute COVID-19 infection, some cases of *Post COVID-19 condition* may develop from the COVID-19 cases already reported.

#### Diagnosis U09.9

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/map_postcovid_percent_of_covidcases_U099.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Data preparation script](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/postcovid_dataprep.py), [Script to produce map](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/postcovid_mapfig_cases_U099.py).

#### Diagnosis Z86.1A/U08.9

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/map_postcovid_percent_of_covidcases_U089.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Data preparation script](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/postcovid_dataprep.py), [Script to produce map](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/postcovid_mapfig_cases_U089.py).

-->

### Most common accompanying diagnoses

#### Diagnosis U09.9

The below table displays the most common types of diagnosis (diagnosis groups) that have been reported together with the _U09.9 (ICD-10-SE) - Postinfectious state associated with COVID-19, unspecified_ diagnosis. In particular, the values in the table represent the amount of individuals that received the _U09.9_ diagnosis alongside one of the diagnoses below. The data was recorded between 16th October 2020 and the most recent data update (see above).

<div class="plot_wrapper mb-3">
    <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/accompdiag_table.json" height="527px" >}}</div>
</div>

<span class="text-muted">_Note that an individual may have more than one of the accompanying diagnoses. However, if an individual has the same issue on multiple doctor visits/healthcare contacts, the diagnosis will only be counted once_</span>

**Code used to produce table:** [Script to produce table (English)](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/create_accomp_diagnoses.py), [Script to produce table (Swedish)](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/create_accomp_diagnoses_swe.py).

### Contacts with healthcare

The below plot shows the number of times that patients given the diagnoses of interest have sought healthcare. Note that while the weekly data below starts from week 21 of 2020, some diagnosis codes (_U08.9_ and _U09.9_) were not used until after this date (see information above). It is important to note that the data is not complete, given that data from some healthcare providers (e.g. general practitioners) are not reported to the Patient Registry due to privacy concerns. Where data is reported to registers, data from the most recent weeks should be considered preliminary, as the registers are not instantaneously updated. A delay in reporting data to registers may be particularly evident during traditional holiday periods, including over the summer months.

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/weeklycontacts_healthcare.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/weeklycontacts_healthcare.py).

### Contacts with healthcare, divided by patient sex

The below plots show the number of times that patients given one of the diagnoses of interest have sought healthcare. The weekly number of healthcare visits is shown, divided by patient sex. As in the above section, it is important to note that the data is not complete, given that data from some healthcare providers (e.g. general practitioners) are not reported to the Patient Registry due to privacy concerns. Where data is reported to registers, data from the most recent weeks should be considered preliminary, as the registers are not instantaneously updated. A delay in reporting data to registers may be particularly evident during traditional holiday periods, including over the summer months.

#### Diagnosis U09.9

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/U099_healthcare_divsex.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/weeklycontacts_healthcare_divsex.py).

#### Diagnosis Z86.1A/U08.9

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/U089_healthcare_divsex.json" height="500px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/postCOVID/weeklycontacts_healthcare_divsex.py).

## Ongoing research projects

Below is a manually curated overview of research projects on _Post COVID-19 condition_ that are funded by major funding agencies in Sweden. As it is manually curated, the list may not be exhaustive and new projects will be added as soon as possible. If you think that your project should be listed here but isn’t, please [get in touch with us](/contact/). For a list of all research projects funded by major funding agencies in Sweden [see this section of the portal](/projects/ongoing/).

{{< display_funded_projects filter_variable="post_covid" >}}

<!-- ## Available data -->

## Publications

Below is a list of pre-prints and published scientific journal articles on _Post COVID-19 condition_ involving at least one author affiliated with a Swedish university or research institute. Note that this list is based on a manually curated database and, as such, may not be exhaustive. If you think that a publication should be listed here but isn’t, or feel that information about a publication needs correction, please [get in touch with us](/contact/). For a list of all publications on COVID-19 and SARS-CoV-2 involving at least one author affiliated with a Swedish univerisity or research institute [see this section of the portal](/publications/).

{{< postcovid_publications >}}

<a id="background"></a>

## Background Information

### Post COVID-19 condition

Individuals with _Post COVID-19 condition_ exhibit symptoms lasting at least two months after the acute phase of COVID-19 infection ([Brodin, 2021](https://doi.org/10.1038/s41591-020-01202-8)). The particular symptoms exhibited vary between patients, as does the duration and severity of symptoms. In general though, symptoms are usually debilitating and may include persistent fatigue, myalgia (muscle aches and pains), and autonomic dysregulation, among others. Some individuals with _Post COVID-19 condition_ exhibit the same symptoms as they did during the acute infection stage of COVID-19, while others with _Post COVID-19 condition_ exhibit new symptoms following the acute infection phase ([Brodin 2021](https://www.nature.com/articles/s41591-020-01202-8), [Dennis _et al._, 2021](http://dx.doi.org/10.1136/bmjopen-2020-048391), [Davido _et al._, 2020](https://doi.org/10.1016/j.cmi.2020.07.028).

### No consensus on definition

In September 2020, WHO established the [ICD10](https://www.who.int/standards/classifications/classification-of-diseases/emergency-use-icd-codes-for-covid-19-disease-outbreak) code for _Post COVID-19 condition_ _U09.9 - Post COVID-19 condition, unspecified_. A [WHO report from April 2021](https://www.who.int/publications/i/item/9789240025035) stated that there is a real need to characterise and formally define _Post COVID-19 condition_ in order to increase understanding about the condition and facilitate diagnosis. However, to date, _Post COVID-19 condition_ still lacks a universal definition with regard to the symptoms and disease duration necessary for diagnosis. Consequently, governmental agencies and research institutes in different countries use their own definitions and terms. Related diagnoses established by WHO are _U08.9 - Personal history of COVID-19, unspecified_ and _U10.9 - Multisystem inflammatory syndrome associated with COVID-19, unspecified_. The _U08.9_ diagnosis is used to describe an earlier episode of COVID-19 (either confirmed or probable) that influenced the individual's health status, though they no longer have COVID-19. The code _U10.9_ is used to describe a temporal association with COVID-19: cytokine storm, Kawasaki-like syndrome, multisystem inflammatory syndrome in children (MIS-C), and paediatric inflammatory multisystem syndrome (PIMS).

In England, the [National Institute for Health and Care Excellence (NICE)](https://www.nice.org.uk) has [defined](https://www.nice.org.uk/guidance/ng188/chapter/context) _Post-COVID-19 syndrome_ as "...signs and symptoms that develop during or after an infection consistent with COVID‑19, continue for more than 12 weeks, and are not explained by an alternative diagnosis. It usually presents with clusters of symptoms, often overlapping, which can fluctuate and change over time and can affect any system in the body...". NICE states that _Post‑COVID‑19 syndrome_ can be considered as a diagnosis during the first three months after the acute infection phase of COVID-19 while healthcare assessments are completed to determine whether the symptoms could be explained by an alternative disease. Further, NICE [defines](https://www.nice.org.uk/guidance/ng188/chapter/context) the term _Long COVID_ as "...signs and symptoms that continue or develop after acute COVID‑19. It includes both ongoing symptomatic COVID‑19 (from 4 to 12 weeks) and post‑COVID‑19 syndrome (12 weeks or more)...”. In December 2020, NICE, in partnership with the Scottish Intercollegiate Guidelines Network and the Royal College of General Practitioners, published a [guideline for health and care practitioners](https://www.nice.org.uk/guidance/NG188) (NG188) on identifying, assessing, and managing the long-term effects of COVID-19.

In the USA, The [Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov) defines _Post-COVID conditions_ as "...a wide range of new, returning, or ongoing health problems people can experience more than four weeks after first being infected with the virus that causes COVID-19...". The CDC distinguishes between _Long COVID_, _Multiorgan Effects of COVID-19_, and _Effects of COVID-19 Treatment or Hospitalisation_. For example, they define _Long COVID_ as "a range of symptoms that can last weeks or months after first being infected with the virus that causes COVID-19 or can appear weeks after infection.". For information on _Post-COVID conditions_ from the CDC, [see this page](https://www.cdc.gov/coronavirus/2019-ncov/long-term-effects.html). The [National Institutes of Health (NIH)](https://www.nih.gov) in the USA uses the term _Post-Acute Sequelae of SARS-CoV-2 infection_ (PASC) to refer to the effects of COVID-19 after the initial stages of infection. In February 2021, The NIH [launched a research initiative](https://www.nih.gov/about-nih/who-we-are/nih-director/statements/nih-launches-new-initiative-study-long-covid) to identify the causes of PASC and, ultimately, to find methods for prevention and treatments for individuals that don’t recover fully over a period of a few weeks following the acute infection phase of COVID-19.

The [Swedish Board of Health and Welfare (Socialstyrelsen)](https://www.socialstyrelsen.se/) describes patients with _Postcovid_ as individuals exhibiting prolonged symptoms, or experiencing new relevant symptoms after the acute phase of COVID-19 infection. While the severity of symptoms will diminish over time for most individuals (such individuals do not need assistance from healthcare during the recovery), some individuals experience symptoms that are debilitating and need treatment, rehabilitation, and other follow-up medical care. In April 2021, Socialstyrelsen [published a report dedicated to Postcovid](https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/artikelkatalog/ovrigt/2021-4-7351.pdf) that defines the condition and provides recommendations.

### Research efforts

A large number of research articles, case reports, and reviews focused on _Post COVID-19 condition_ have been published over the last year (e.g. [Dani _et al._ (2020)](https://doi.org/10.7861/clinmed.2020-0896), [Nabavi (2020)](https://doi.org/10.1136/bmj.m3489), [Sudre _et al._ (2021)](https://doi.org/10.1038/s41591-021-01292-y), [Tarybagil _et al._ (2020)](https://doi.org/10.1136/bcr-2020-241485), [Yelin _et al._ (2020)](https://doi.org/10.1016/j.cmi.2020.12.001)). The primary aims of these studies are to identify factors that could be used to predict when _Post COVID-19 condition_ is more likely to develop, the underlying causes of the condition, and potential treatments. A recently published study by [Sudre and colleagues](https://doi.org/10.1038/s41591-021-01292-y) proposed a prediction model to identify individuals at risk of _Post COVID-19 condition_ using data from the [COVID Symptom Study](/data_types/health_data/symptom_study_sweden/), where participants self-reported their symptoms in an app on their mobile devices. The results indicated that individuals experiencing more than five symptoms during the first week of illness were more likely to develop _Post COVID-19 condition_ (odds ratio = 3.53 (2.76–4.50)). In addition, the study showed that the development of _Post COVID-19 condition_ was more likely in females, and that the risk also rose with increasing age and body mass index. The researchers behind the study propose that their model could be used to identify individuals at risk of developing _Post COVID-19 condition_. This could inform trials of preventative or treatment methods, and aid in the planning of education and rehabilitation services.
