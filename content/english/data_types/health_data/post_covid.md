---
title: "Post-COVID in Sweden: statistics, research projects, available data"
toc: true
plotly: true
---
<!--
- [About Post-COVID](#about-post-covid)
- [Statistics on Post-COVID in Sweden](#statistics-on-post-covid-in-sweden)
- [Ongoing research projects](#ongoing-research-projects)
- [Available data](#available-data)
- [Publications](#publications) -->

## About Post-COVID

Post-COVID or Long COVID is a condition that has not yet been clearly defined. Individuals with typically exhibit variable and debilitating symptoms lasting more than 2 months after COVID-19 infection. The Post-COVID involves a range of symptoms, for example, fatigue, myalgia, and intestinal disturbances. While some individuals are still exhibiting symptoms after the initial infection, others exhibit new symptoms (Brodin, *Nature Medicine* 2021, DOI: [10.1038/s41591-020-01202-8](https://doi.org/10.1038/s41591-020-01202-8)). [More intro on Post-COVID here: some more info about the science behind]

On this page, you can find visualizations of statistics related to Post-COVID in Sweden from the The National Board of Health and Welfare (Socialstyrelsen), overview of research projects on Post-COVID currently carried out in Sweden, publicly available data shared by researchers affiliated with Swedish universities or research institutes.

Please see [this section of the The National Board of Health and Welfare (Socialstyrelsen) website](https://www.socialstyrelsen.se/coronavirus-covid-19/socialstyrelsens-roll-och-uppdrag/postcovid/
) for more information on Post-COVID in Sweden.

## Statistics on Post-COVID in Sweden

Here, we visualize statistics on Post-COVID in Sweden collected and shared by The National Board of Health and Welfare (Socialstyrelsen). The majority of the statistics produced by The National Board of Health and Welfare is based on administrative registers. The central sources for statistics regarding COVID-19 is primarily the Patient Register and the Cause of Death Register.

Since Post-COVID is not a clearly defined disease, over time various diagnoses were used for people with symptoms of Post-COVID. Here, we focus on diagnosis *U09.9 (ICD-10-SE) - Postinfectious state associated with covid-19, unspecified* (Example: Patient who five months ago fell ill with COVID-19; now have residual symptoms in the form of anosmia, lack of smell). Also relevant are the following diagnoses: *U10.9 (ICD-10-SE) - Multisystemic inflammatory syndrome associated with covid-19, unspecified* (Example: Condition temporally associated with covid-19: Cytokinstorm; Kawasaki-like syndrome; Multisystem Inflammatory Syndrome in Children [MIS-C]; Paediatric Inflammatory Multisystem Syndrome [PIMS]); *U08.9 (ICD-10-SE) - COVID-19 in the health history, unspecified* (used for the cases when an earlier confirmed or suspected case of COVID-19 has an effect on the current health status for people who no longer have COVID-19. See [this page for more information](https://www.socialstyrelsen.se/utveckla-verksamhet/e-halsa/klassificering-och-koder/icd-10/)).

[Here some more info about definitions that Socialstyrelsen uses and how they count]

All data presented here is [available for download here](https://www.socialstyrelsen.se/statistik-och-data/statistik/statistik-om-covid-19/). Additional data can be requested from the corresponding registers by researchers fulfilling the requirements for access, [the guidelines are available here](https://bestalladata.socialstyrelsen.se/data-for-forskning/).

### Age distribution of Post-COVID cases

### Sex distribution of Post-COVID cases

### Geographic distribution of Post-COVID cases
<div class="alert alert-info">Last updated: {{% postcovid_map_date_modified %}}.</div>

The map below displays the current geographic distribution of patients given the diagnosis *U09.9 (ICD-10-SE) - Postinfectious state associated with covid-19, unspecified* across different counties in Sweden. Each county is colored according to the proportion of the patients from the total number of people with confirmed COVID-19 infection in that county since XXX (the time point when this diagnosis started being used).

{{< csss_map_large >}}

### Most common diagnoses given together with Post-COVID diagnosis

[Table here: diagnosis, number of people who got this diagnosis together with post covid, proportion of all people who got this diagnosis together with post covid diagnosis]

### Contacts with healthcare of people who have the Post-COVID diagnosis

This plot displays the number of times patients diagnosed with *U09.9 (ICD-10-SE) - Postinfectious state associated with covid-19, unspecified* have sought healthcare, starting from week 22. Every time such a patient sought healthcare after receiving the diagnosis is counted here. Numbers are displayed per week and split by sex.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="healthcare_contacts"></div>
</div>

## Ongoing research projects

This is a manually curated overview of research projects on Post-COVID which are funded by major funding agencies in Sweden. New projects are added on an ongoing basis. If you would like your project to be listed here, please [get in touch with us](/contact/). For a list of all research projects funded by major funding agencies in Sweden [see this section of the portal](/projects/ongoing/).

{{< postcovid_projects >}}

## Available data

[Here will be a list of data related to Post-COVID that can be downloaded: from Socialstyrelsen but also based on our publications database perhaps.]

## Publications

This section presents a list of published scientific journal articles and preprints on Post-COVID where at least one author has an affiliation with a Swedish research institute. Note that this is a manually curated database and as such may not be exhaustive. If you would like your publication to be added here or information about your publication to be corrected, please [get in touch with us](/contact/). For a list of all publications on COVID-19 and SARS-CoV-2 where at least one author has an affiliation with a Swedish research institute [see this section of the portal](/publications/)

{{< postcovid_publications >}}

<script src="https://cdn.jsdelivr.net/npm/vega@5.19.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.15.1"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/3c39867036b645feac689f5816a41024.js?id=healthcare_contacts"></script>
