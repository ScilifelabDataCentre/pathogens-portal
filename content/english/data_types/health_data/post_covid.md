---
title: "Post COVID-19 condition in Sweden: statistics, research projects, available data"
toc: true
plotly: true
---

Since the beginning of 2020, the COVID-19 pandemic has challenged healthcare and changed everyday life in societies across the world. Research has shown that in those who have the COVID-19 disease several other conditions may occur after the acute infection phase. Most patients that experience mild, moderate, or severe symtoms during the acute COVID-19 infection recover without long-term effects. However, some individuals have been found to exhibit symtoms including: deep fatigue, joint pain, ‘brain fog’, (hard to concentrate on work task for longer periods of time) and heart palpitations for longer periods of time after the acute infection ([Brodin 2021](https://doi.org/10.1038/s41591-020-01202-8); [Marx 2021](https://doi.org/10.1038/s41592-021-01145-z)). The condition is often referred to as *Post COVID-19 condition*, but also referred to as *Post COVID* or *Long COVID* (in Swedish it has been referred to as *långtidscovid* or *postcovid*). On this page, we chose to use *Post COVID-19 condition* but refer to all of the above. See the *[Background](#background)* information below for more information about the classification of the disease and research that is beging conducted.

On this page, you can find visualizations of statistics related to Post COVID-19 condition in Sweden from the The National Board of Health and Welfare (Socialstyrelsen), overview of research projects on Post COVID-19 condition currently carried out in Sweden, publicly available data shared by researchers affiliated with Swedish universities or research institutes.

for more information on Post COVID-19 condition in Sweden, please see [this section of the The National Board of Health and Welfare (Socialstyrelsen) website](https://www.socialstyrelsen.se/coronavirus-covid-19/socialstyrelsens-roll-och-uppdrag/postcovid/
) and their [reporton Post-COVID condition published in April 2021](https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/artikelkatalog/ovrigt/2021-4-7351.pdf).

## Statistics on Post COVID-19 condition in Sweden

Here, we visualize statistics on Post COVID-19 condition in Sweden collected and shared by The National Board of Health and Welfare (Socialstyrelsen). The majority of the statistics produced by The National Board of Health and Welfare is based on administrative registers. The central sources for statistics regarding COVID-19 is primarily the Patient Register and the Cause of Death Register.

Since Post COVID-19 condition is not a clearly defined disease, over time various diagnoses were used for people with symptoms of Post COVID-19 condition. Here, we focus on diagnosis *U09.9 (ICD-10-SE) - Postinfectious state associated with covid-19, unspecified* (Example: Patient who five months ago fell ill with COVID-19; now have residual symptoms in the form of anosmia, lack of smell). Also relevant are the following diagnoses: *U10.9 (ICD-10-SE) - Multisystemic inflammatory syndrome associated with covid-19, unspecified* (Example: Condition temporally associated with covid-19: Cytokinstorm; Kawasaki-like syndrome; Multisystem Inflammatory Syndrome in Children [MIS-C]; Paediatric Inflammatory Multisystem Syndrome [PIMS]); *U08.9 (ICD-10-SE) - COVID-19 in the health history, unspecified* (used for the cases when an earlier confirmed or suspected case of COVID-19 has an effect on the current health status for people who no longer have COVID-19. See [this page for more information](https://www.socialstyrelsen.se/utveckla-verksamhet/e-halsa/klassificering-och-koder/icd-10/)).

[Here some more info about definitions that Socialstyrelsen uses and how they count]

All data presented here is [available for download here](https://www.socialstyrelsen.se/statistik-och-data/statistik/statistik-om-covid-19/). Additional data can be requested from the corresponding registers by researchers fulfilling the requirements for access, [the guidelines are available here](https://bestalladata.socialstyrelsen.se/data-for-forskning/).

### Age distribution of Post COVID-19 condition cases

### Sex distribution of Post COVID-19 condition cases

### Geographic distribution of Post COVID-19 condition cases
<div class="alert alert-info">Last updated: {{% postcovid_map_date_modified %}}.</div>

The map below displays the current geographic distribution of patients given the diagnosis *U09.9 (ICD-10-SE) - Postinfectious state associated with covid-19, unspecified* across different counties in Sweden. Each county is colored according to the proportion of the patients from the total number of people with confirmed COVID-19 infection in that county since XXX (the time point when this diagnosis started being used).

{{< csss_map_large >}}

### Most common diagnoses given together with Post COVID-19 condition diagnosis

[Table here: diagnosis, number of people who got this diagnosis together with post covid, proportion of all people who got this diagnosis together with post covid diagnosis]

### Contacts with healthcare of people who have the Post COVID-19 condition diagnosis

This plot displays the number of times patients diagnosed with *U09.9 (ICD-10-SE) - Postinfectious state associated with covid-19, unspecified* have sought healthcare, starting from week 22. Every time such a patient sought healthcare after receiving the diagnosis is counted here. Numbers are displayed per week and split by sex.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot*wrapper">
  <div class="table-responsive" id="healthcare*contacts"></div>
</div>

## Ongoing research projects

This is a manually curated overview of research projects on Post COVID-19 condition which are funded by major funding agencies in Sweden. New projects are added on an ongoing basis. If you would like your project to be listed here, please [get in touch with us](/contact/). For a list of all research projects funded by major funding agencies in Sweden [see this section of the portal](/projects/ongoing/).

{{< postcovid_projects >}}

## Available data

[Here will be a list of data related to Post COVID-19 condition that can be downloaded: from Socialstyrelsen but also based on our publications database perhaps.]

## Publications

This section presents a list of published scientific journal articles and preprints on Post COVID-19 condition where at least one author has an affiliation with a Swedish research institute. Note that this is a manually curated database and as such may not be exhaustive. If you would like your publication to be added here or information about your publication to be corrected, please [get in touch with us](/contact/). For a list of all publications on COVID-19 and SARS-CoV-2 where at least one author has an affiliation with a Swedish research institute [see this section of the portal](/publications/)

{{< postcovid_publications >}}

<script src="https://cdn.jsdelivr.net/npm/vega@5.19.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.15.1"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/3c39867036b645feac689f5816a41024.js?id=healthcare*contacts"></script>

## Background

Individuals with *Post COVID-19 condition* typically exhibit variable and debilitating symptoms lasting two or more months after an acute COVID-19 infection ([Brodin, 2021](https://www.nature.com/articles/s41591-020-01202-8 )). The Post COVID-19 condition symptoms involve a range of symptoms such as persistent fatigue, and myalgia, as well as autonomic dysregulation that can be manifested as, for example, postural orthostatic tachycardia syndrome, abnormal thermoregulation, or intestinal disturbances. While some individuals with *Post COVID-19 condition* are exhibiting the same symptoms as during the initial acute infection stage for a long time, other patients with *Post COVID-19 condition* exhibit new symptoms after the initial acute infectious phase ([Brodin 2021](https://www.nature.com/articles/s41591-020-01202-8), [Dennis et al. 2021](http://dx.doi.org/10.1136/bmjopen-2020-048391), [Davido et al. 2020](https://doi.org/10.1016/j.cmi.2020.07.028).

### No agreed upon definition

In September 2020, WHO [established]((https://www.who.int/standards/classifications/classification-of-diseases/emergency-use-icd-codes-for-covid-19-disease-outbreak)) the ICD10 code for the Post COVID-19 condition - *U09.9 -  Post COVID-19 condition, unspecified*.  A [WHO report from April 2021](https://www.who.int/publications/i/item/9789240025035) states that the is a need to characterize and define the *Post COVID-19 condition* in order to to increase understanding of the condition. However, *Post-covid* diadnosis to date still does not have one agreed upon definition in terms of the required duration of the disease and symptoms, and governmental agencies and institutes in different countries use their own definition and terms. Related diagnoses established by WHO are *U08.9 - Personal history of COVID-19, unspecified* and *U10.9 -  Multisystem inflammatory syndrome associated with COVID-19, unspecified*. The code *U08.9* is used to describe an earlier episode of COVID-19, confirmed or probable that influences the person’s health status, and the person no longer suffers of COVID-19. The code *U10.9* is used to describe temporarily associated with COVID-19: Cytokine storm; Kawasaki-like syndrome; Multisystem Inflammatory Syndrome in Children (MIS-C); Paediatric Inflammatory Multisystem Syndrome (PIMS).

In the England, the [National Institute for Health and Care Excellence](https://en.wikipedia.org/wiki/National_Institute_for_Health_and_Care_Excellence) (NICE) has [defined]((https://www.nice.org.uk/guidance/ng188/chapter/context)) *Post-COVID-19 syndrome* as "Signs and symptoms that develop during or after an infection consistent with COVID‑19, continue for more than 12 weeks and are not explained by an alternative diagnosis. It usually presents with clusters of symptoms, often overlapping, which can fluctuate and change over time and can affect any system in the body". The NICE states that *Post‑COVID‑19 syndrome* can be considered, for the first three month after acute infection as a diagnosis during the time the healthcare system assess whether the patient may have an alternative underlying disease that can explain the symtoms. Further, NICE [defines]((https://www.nice.org.uk/guidance/ng188/chapter/context)) the term *Long COVID* as "...signs and symptoms that continue or develop after acute COVID‑19. It includes both ongoing symptomatic COVID‑19 (from 4 to 12 weeks) and post‑COVID‑19 syndrome (12 weeks or more)”. In december 2020, NICE, in partnership with the Scottish Intercollegiate Guidelines Network and the Royal College of General Practitioners, published a [guideline for health and care practitioners](https://www.nice.org.uk/guidance/NG188) on identifying, assessing, and managing the long-term effects of COVID-19 (NG188).

In the USA, [Centers for Disease Control and Prevention](https://en.wikipedia.org/wiki/Centers_for_Disease_Control_and_Prevention) (CDC) defines *Post-COVID Conditions* as "a wide range of new, returning, or ongoing health problems people can experience more than four weeks after first being infected with the virus that causes COVID-19". CDC distinguishes between *Long COVID*, *Multiorgan Effects of COVID-19*, and *Effects of COVID-19 Treatment or Hospitalization*. Long COVID is defined as "a range of symptoms that can last weeks or months after first being infected with the virus that causes COVID-19 or can appear weeks after infection." People with long COVID are described as experiencing different combinations of the following symptoms: tiredness or fatigue; difficulty thinking or concentrating (sometimes referred to as “brain fog”)
headache; loss of smell or taste; fizziness on standing; fast-beating or pounding heart (also known as heart palpitations); chest pain; difficulty breathing or shortness of breath; cough; joint or muscle pain; depression or anxiety; fever. For information on Post-COVID conditions from CDC, [see this page](https://www.cdc.gov/coronavirus/2019-ncov/long-term-effects.html). The [National Institutes of Health](https://en.wikipedia.org/wiki/National_Institutes_of_Health) (NIH) in the USA uses the term *Post-Acute Sequelae of SARS-CoV-2 infection* (PASC) to refer to the effects of COVID-19 after the initial stages of infection. In February 2023, the NIH [launched a research initiative](https://www.nih.gov/about-nih/who-we-are/nih-director/statements/nih-launches-new-initiative-study-long-covid) to identify the causes and ultimately the means of prevention and treatment of individuals who have been sickened by COVID-19, but don’t recover fully over a period of a few weeks.

In Sweden, the [Swedish Board of Health and Welfare](https://www.socialstyrelsen.se/) (Socialstyrelsen) [describes](https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/artikelkatalog/ovrigt/2021-4-7351.pdf) patients with Postcovid as individuals exhibiting symptoms or experiencing new symtoms after the acute COVID-19 infection. While for most individuals the symptoms will diminish with time (these individuals do not need assistance from healthcare during the recovery), some individual experience symptoms that are debilitation and need treatment, rehabilitation, and follow-up medical care. In April 2021, Socialstyrelsen [published a report dedicated to Postcovid](https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/artikelkatalog/ovrigt/2021-4-7351.pdf) which defines the condition and provides recommendations.

In summary, the Post COVID-19 condition currently does not have a clear definition which makes diagnosis, treatment, and management of the condition more difficult. Adding to the most common terms Post-COVID-19 condition and Long COVID, a recent commentary in the Journal of Medical Virology ([Mannan Baig 2020](https://doi.org/10.1002/jmv.26624)) proposed that since COVID-19 is a zoonotic infection the term chronic covid syndrome (CCS) should be used for the condition based on a more traditional terminology of infections.

### Ongoing research efforts

A large number of research articles, case reports, and reviews focused on post COVID-19 condition has been published over the last year (for example, [Tarybagil et al. 2020](https://doi.org/10.1136/bcr-2020-241485), [Nabavi 2020](https://doi.org/10.1136/bmj.m3489), [Yelin et al. 2020](https://doi.org/10.1016/j.cmi.2020.12.001), [Dani et al. 2020](https://doi.org/10.7861/clinmed.2020-0896), [Sudre et al. 2021](https://doi.org/10.1038/s41591-021-01292-y)). The goal of these studies is to identify the predictors for when the post COVID-19 condition would develop, underlying causes, and treatments. A recently published research study by [Sudre and colleagues](https://doi.org/10.1038/s41591-021-01292-y) proposed a prediction model to identify individuals at risk of Post COVID-19 condition using data from the [COVID Symptom Study](https://www.covid19dataportal.se/data_types/health_data/symptom_study_sweden/) where participants self-reported their symptoms on an app in their mobile devices. The results indicated that experiencing more than five symptoms during the first week of illness was associated with the later Post COVID-19 condition (odds ratio = 3.53 (2.76–4.50)). In addition, the study showed that having Post COVID-19 condition was more likely with increasing age, body mass index, and female sex. The researchers behind the study propose that their model could be used to identify individuals at risk of long COVID for trials of prevention or treatment and to plan education and rehabilitation services.
