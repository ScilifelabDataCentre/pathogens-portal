---
title: "Post COVID-19 condition in Sweden: statistics, research projects, available data"
toc: true
plotly: true
---

Since the beginning of 2020, the COVID-19 pandemic has challenged healthcare and changed everyday life in societies across the world. The severity of symptoms experienced by patients during the acute infection is known to vary from mild to severe. Most patients show no evidence of long-term effects following this phase, regardless of the severity of the symptoms experienced. However, research has found that some patients exhibit multiple symptoms for long periods following acute infection, for example, deep fatigue, joint pain, ‘brain fog’(difficulty concentrating on certain tasks for longer periods of time, heart palpitations ([Brodin 2021](https://doi.org/10.1038/s41591-020-01202-8); [Marx 2021](https://doi.org/10.1038/s41592-021-01145-z)). The condition has been referred to by a number of names, including *Post COVID-19 condition*, *Post-COVID*, and *Long COVID* (in Swedish it has been called *långtidscovid* or *postcovid*). On this page, we use the term *Post COVID-19 condition* when referring to the condition. See the *[Background](#background)* information below for more detail about the classification of the condition and the research being conducted into it.

On this page, you can find visualisations of statistics related to *Post COVID-19 condition* in Sweden from the The National Board of Health and Welfare (Socialstyrelsen), an overview of research projects on *Post COVID-19 condition* currently carried out in Sweden, and scientific publications by researchers affiliated with Swedish universities or research institutes.

For more information on *Post COVID-19 condition* in Sweden, please see [this section of the The National Board of Health and Welfare (Socialstyrelsen) website](https://www.socialstyrelsen.se/coronavirus-covid-19/socialstyrelsens-roll-och-uppdrag/postcovid/
) and their [report on *Post-COVID condition* (published April 2021)](https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/artikelkatalog/ovrigt/2021-4-7351.pdf).

## Statistics on Post COVID-19 condition in Sweden

<div class="alert alert-info">All data last updated: 08.06.2021</div>

Here, we visualize statistics on Post COVID-19 condition in Sweden collected and shared by The National Board of Health and Welfare (Socialstyrelsen). The majority of the statistics produced by The National Board of Health and Welfare is based on administrative registers. The central sources for statistics regarding COVID-19 is primarily the Patient Register and the Cause of Death Register. The data is updated once a month, on the second Wednesday of the month. All data presented here is [available for download here](https://www.socialstyrelsen.se/statistik-och-data/statistik/statistik-om-covid-19/). Additional data can be requested from the corresponding registers by researchers fulfilling the requirements for access, [the guidelines are available here](https://bestalladata.socialstyrelsen.se/data-for-forskning/).

Since Post COVID-19 condition is not a clearly defined disease, over time various diagnoses were given to it. After the first cases of prolonged disease followed by COVID-19 infection in spring 2020, The National Board of Health and Welfare initiated the diagnosis *Z86.1A - COVID-19 in own medical history* (Covid-19 i den egna sjukhistorien) which started being used from June 1 2020. From January 1 2021, this diagnosis was replaced by *U08.9 (ICD-10-SE) - COVID-19 in own medical history, unspecified* in accordance with the new WHO (World Health Organization) guidelines. This diagnosis is recommended to be given for a person who is receiving healthcare of a different disease or damage but where it is considered to be relevant (of some importance) that this person has previously had COVID-19. This diagnosis should only be given after the person is considered to no longer have COVID-19. The current health condition should not be considered to be caused by COVID-19. This diagnosis is only an additional diagnosis (bidiagnos) and should only be assigned alongside a main diagnosis, it cannot be the main diagnosis itself.

From October 16 2020, the National Board of Health and Welfare initiated a new diagnosis *U09.9 (ICD-10-SE) - Postinfectious state associated with covid-19, unspecified* (Postinfektiöst tillstånd efter covid-19, ospecificerat), in accordance with new WHO guidelines. This new diagnosis supplemented and partially replaced the diagnoses Z86.1A. This diagnosis should only be given after the person is considered to no longer have COVID-19. The code is used for conditions that persist or occur after the acute infection has passsed. This is also an additional diagnosis (bidiagnos) and should be assigned alogside a main diagnosis.

For more information and current guidelines regarding diagnoses used for conditions related to COVID-19, see [this page on the website of the  The National Board of Health and Welfare](https://www.socialstyrelsen.se/utveckla-verksamhet/e-halsa/klassificering-och-koder/icd-10/).

### Age and sex distribution of diagnosed cases

This plot displays the number of times patients diagnosed with the diagnoses of interest since the introduction of these diagnoses codes, divided by age and sex.

#### Diagnosis U09.9

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="diagnosed_age_sex_u09_9"></div>
</div>

#### Diagnosis Z86.1A/U08.9

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="diagnosed_age_sex_u08_9"></div>
</div>

### Geographic distribution of diagnosed cases relative to population size

The maps below show the number of people who received the diagnoses of interest in each county as a percentage of the total population of the county. The total population of the county and the number of people who received the diagnosis can be seen by hovering the mouse above a particular county. Note that the range of values on the two maps is not identical.

#### Diagnosis U09.9

{{< postcovid_map_u09_9_relative_to_population >}}

#### Diagnosis Z86.1A/U08.9

{{< postcovid_map_u08_9_relative_to_population >}}

### Geographic distribution of diagnosed cases relative to confirmed COVID-19 cases

The maps below show the number of people who received the diagnoses of interest in each county as a percentage of the total number of confirmed COVID-19 cases in that county (based on [data from the Public Health Agency, Folkhälsomyndigheten](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/statistik-och-analyser/bekraftade-fall-i-sverige/)). Specifically, the total cumulative number of positive COVID-19 tests in the particular region at the date given for the last update of the number of diagnoses of interest. Both the total number of confirmed COVID-19 cases and the number of people who received the diagnoses of interest can be seen by hovering the mouse above a particular county. Please note that the data visualised on this map should be interpreted with considerable caution for a few reasons. Firstly, the number of COVID-19 cases is likely an underestimate, both due to asymptomatic cases and the fact that not all symptomatic cases will have been confirmed and reported. Secondly, the diagnoses related to post COVID-19 condition were introduced much later, and not all cases are likely to have received a formal diagnosis. Further, more cases may be developing, as the case number reflects present cases and Post COVID-19 condition may not be diagnosed for several weeks or months following acute infection with the virus.

#### Diagnosis U09.9

{{< postcovid_map_u09_9_relative_to_cases >}}

#### Diagnosis Z86.1A/U08.9

{{< postcovid_map_u08_9_relative_to_cases >}}

### Most common accompanying diagnoses

#### Diagnosis U09.9

This table displays the most common diagnoses types (diagnosis groups) which have been reported together with diagnosis *U09.9 (ICD-10-SE) - Postinfectious state associated with covid-19, unspecified*. In other words, the numbers and percentages below show the amount of people who received the diagnosis *U09.9* and simultaneously have a diagnoses from the types below. The data below reflects the period starting from October 16 2020 and until the most recent update of the dataset (see above).

{{< postcovid_accompanying_diagnoses >}}

<span class="text-muted">*Note that a single person may have more than one accompanying diagnoses. However, if I person has the same issue on multiple doctor visits/healthcare contacts, the diagnosis is counted only once.*</span>

### Contacts with healthcare

This plot displays the number of times patients diagnosed with the diagnoses of interest have sought healthcare. Note that while the data below starts from week 22 of 2020, some diagnosis codes started being used at a later point in time (see information above). Every time such a patient sought healthcare after receiving the diagnosis is counted here. Numbers are displayed per week. Note that the data below is not full as information about the the number of contacts from some of the weeks is not available publicly due to privacy restrictions.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot-wrapper">
  <div class="table-responsive" id="healthcare_contacts_all"></div>
</div>

### Contacts with healthcare divided by patients' sex

Thes plots display the number of times patients diagnosed with with diagnoses of interest have sought healthcare. Every time such a patient sought healthcare after receiving the diagnosis is counted here. Numbers are displayed per week and split by sex. Note that the data below is not full as information about the the number of healthcare contacts from some of the weeks is not available publicly due to privacy restrictions.

#### Diagnosis U09.9

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="healthcare_contacts_u09_9"></div>
</div>

#### Diagnosis Z86.1A/U08.9

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="healthcare_contacts_u08_9"></div>
</div>

## Ongoing research projects

This is a manually curated overview of research projects on Post COVID-19 condition which are funded by major funding agencies in Sweden. New projects are added on an ongoing basis. If you would like your project to be listed here, please [get in touch with us](/contact/). For a list of all research projects funded by major funding agencies in Sweden [see this section of the portal](/projects/ongoing/).

{{< postcovid_projects >}}

<!-- ## Available data -->

## Publications

This section presents a list of published scientific journal articles and preprints on Post COVID-19 condition where at least one author has an affiliation with a Swedish research institute. Note that this is a manually curated database and as such may not be exhaustive. If you would like your publication to be added here or information about your publication to be corrected, please [get in touch with us](/contact/). For a list of all publications on COVID-19 and SARS-CoV-2 where at least one author has an affiliation with a Swedish research institute [see this section of the portal](/publications/)

{{< postcovid_publications >}}

## Background: Post COVID-19 condition

Individuals with *Post COVID-19 condition* exhibit symptoms lasting at least two months after the acute phase of COVID-19 infection ([Brodin, 2021](https://doi.org/10.1038/s41591-020-01202-8)). The particular symptoms exhibited varies between patients, as does their duration and severity (though the symptoms are often debilitating), but may include persistent fatigue, myalgia (muscle aches and pains), and autonomic dysregulation that can manifest in a variety of ways, for example , as postural orthostatic tachycardia syndrome (a condition affecting blood flow), abnormal thermoregulation (changes in body temperature), or intestinal disturbances. Some individuals with *Post COVID-19 condition* exhibit the same symptoms as they did during the initial acute infection stage, while others with *Post COVID-19 condition* exhibit new symptoms after the initial acute infection phase ([Brodin 2021](https://www.nature.com/articles/s41591-020-01202-8), [Dennis et al. 2021](http://dx.doi.org/10.1136/bmjopen-2020-048391), [Davido et al. 2020](https://doi.org/10.1016/j.cmi.2020.07.028).

### No agreed upon definition

In September 2020, WHO [established](https://www.who.int/standards/classifications/classification-of-diseases/emergency-use-icd-codes-for-covid-19-disease-outbreak) the ICD10 code for *Post COVID-19 condition* - *U09.9 -  Post COVID-19 condition, unspecified*.  A [WHO report from April 2021](https://www.who.int/publications/i/item/9789240025035) states that there is a real need to characterise and formerly define *Post COVID-19 condition* in order to increase understanding of the condition and facilitate diganosis. However, to date, *Post COVID-19 condition* still does not have a universal definition with regard to the symptoms and disease duration neccessary for diagnosis, and governmental agencies and institutes in different countries use their own definition and terms. Related diagnoses established by WHO are *U08.9 - Personal history of COVID-19, unspecified* and *U10.9 -  Multisystem inflammatory syndrome associated with COVID-19, unspecified*. The code *U08.9* is used to describe an earlier episode of COVID-19 (either confirmed or probable) that influenced the individual's health status, though they no longer have COVID-19. The code *U10.9* is used to describe a temporal association with COVID-19: Cytokine storm; Kawasaki-like syndrome; Multisystem Inflammatory Syndrome in Children (MIS-C); Paediatric Inflammatory Multisystem Syndrome (PIMS).

In England, the [National Institute for Health and Care Excellence](https://en.wikipedia.org/wiki/National_Institute_for_Health_and_Care_Excellence) (NICE) has [defined](https://www.nice.org.uk/guidance/ng188/chapter/context) *Post-COVID-19 syndrome* as "Signs and symptoms that develop during or after an infection consistent with COVID‑19, continue for more than 12 weeks and are not explained by an alternative diagnosis. It usually presents with clusters of symptoms, often overlapping, which can fluctuate and change over time and can affect any system in the body". NICE states that *Post‑COVID‑19 syndrome* can be considered as a dignosis during the first three months after acute infection, while the healthcare system assesses whether the patient may have an alternative underlying disease that could explain the symptoms. Further, NICE [defines](https://www.nice.org.uk/guidance/ng188/chapter/context) the term *Long COVID* as "...signs and symptoms that continue or develop after acute COVID‑19. It includes both ongoing symptomatic COVID‑19 (from 4 to 12 weeks) and post‑COVID‑19 syndrome (12 weeks or more)”. In December 2020, NICE, in partnership with the Scottish Intercollegiate Guidelines Network and the Royal College of General Practitioners, published a [guideline for health and care practitioners](https://www.nice.org.uk/guidance/NG188) (NG188) on identifying, assessing, and managing the long-term effects of COVID-19.

In the USA, The [Centers for Disease Control and Prevention](https://en.wikipedia.org/wiki/Centers_for_Disease_Control_and_Prevention) (CDC) defines *Post-COVID conditions* as "a wide range of new, returning, or ongoing health problems people can experience more than four weeks after first being infected with the virus that causes COVID-19". The CDC distinguishes between *Long COVID*, *Multiorgan Effects of COVID-19*, and *Effects of COVID-19 Treatment or Hospitalisation*. *Long COVID* is defined as "a range of symptoms that can last weeks or months after first being infected with the virus that causes COVID-19 or can appear weeks after infection." People with long COVID are described as experiencing different combinations of the following symptoms; tiredness or fatigue, difficulty thinking or concentrating (sometimes referred to as “brain fog”),
headache, loss of smell or taste, dizziness on standing, fast-beating or pounding heart (also known as heart palpitations), chest pain, difficulty breathing or shortness of breath, cough, joint or muscle pain, depression or anxiety, and fever. For information on *Post-COVID conditions* from The CDC, [see this page](https://www.cdc.gov/coronavirus/2019-ncov/long-term-effects.html). The [National Institutes of Health](https://en.wikipedia.org/wiki/National_Institutes_of_Health) (NIH) in the USA uses the term *Post-Acute Sequelae of SARS-CoV-2 infection* (PASC) to refer to the effects of COVID-19 after the initial stages of infection. In February 2021, the NIH [launched a research initiative](https://www.nih.gov/about-nih/who-we-are/nih-director/statements/nih-launches-new-initiative-study-long-covid) to identify the causes of PASC and, ultimately, to find methods for prevention and treatments for individuals that don’t recover fully over a period of a few weeks following the acute infection phase of COVID-19.

In Sweden, the [Swedish Board of Health and Welfare](https://www.socialstyrelsen.se/) (Socialstyrelsen) [describes](https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/artikelkatalog/ovrigt/2021-4-7351.pdf) patients with *Postcovid* as individuals exhibiting symptoms or experiencing new symtoms after the acute COVID-19 infection. While the severity of symptoms will diminish with time for most individuals (these individuals do not need assistance from healthcare during the recovery), some individuals experience symptoms that are debilitating and need treatment, rehabilitation, and follow-up medical care. In April 2021, Socialstyrelsen [published a report dedicated to Postcovid](https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/artikelkatalog/ovrigt/2021-4-7351.pdf) that defines the condition and provides recommendations.

Adding to the most common terms *Post-COVID-19 condition* and *Long COVID* used globally, a recent commentary in the Journal of Medical Virology ([Mannan Baig 2020](https://doi.org/10.1002/jmv.26624)) proposed that, since COVID-19 is a zoonotic infection, the term chronic covid syndrome (CCS) should be used for the condition, in line with more traditional terminology used for infections.

In summary, *post COVID-19 condition* currently lacks a clear, global definition upon which to base diagnosis. This makes treatment and management of the condition more difficult, as it hinders knowledge sharing.

### Research efforts

A large number of research articles, case reports, and reviews focused on *post COVID-19 condition* have been published over the last year (e.g. [Tarybagil et al. 2020](https://doi.org/10.1136/bcr-2020-241485), [Nabavi 2020](https://doi.org/10.1136/bmj.m3489), [Yelin et al. 2020](https://doi.org/10.1016/j.cmi.2020.12.001), [Dani et al. 2020](https://doi.org/10.7861/clinmed.2020-0896), [Sudre et al. 2021](https://doi.org/10.1038/s41591-021-01292-y)). The primary aims of these studies are to identify the predictors for when *post COVID-19 condition* would develop, the underlying causes of the condition, and potential treatments. A recently published study by [Sudre and colleagues](https://doi.org/10.1038/s41591-021-01292-y) proposed a prediction model to identify individuals at risk of *post COVID-19 condition* using data from the [COVID Symptom Study](/data_types/health_data/symptom_study_sweden/), where participants self-reported their symptoms in an app on their mobile devices. The results indicated that individuals experiencing more than five symptoms during the first week of illness were more likely to develop *post COVID-19 condition* (odds ratio = 3.53 (2.76–4.50)). In addition, the study showed that the development of *post COVID-19 condition* was more likely in females and that the risk also rose with increasing age and body mass index. The researchers behind the study propose that their model could be used to identify individuals at risk of *post COVID-19 condition*. This could inform trials of prevention or treatment methods, and aid in the planning of education and rehabilitation services.

<script src="https://cdn.jsdelivr.net/npm/vega@5.19.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.15.1"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/d8ccc0a02ad248c2ae7e5910806c3586.js?id=healthcare_contacts_u09_9"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/47b7d864db0840dab7c2ff6f8fffc011.js?id=healthcare_contacts_u08_9"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/a31cdae8f06a4ac08f8970e6dd750c13.js?id=healthcare_contacts_all"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/a483404a5b5146cfa9eaeef29d326388.js?id=diagnosed_age_sex_u09_9"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/ae0a086410ea489484d33035469c334f.js?id=diagnosed_age_sex_u08_9"></script>
