---
title: Amount of enteric virus in wastewater (GU)
plotly: true
type: wastewater
menu:
  wastewater:
    name: Enteric virus quantification (GU)
    weight: 30
aliases:
  - /dashboards/wastewater/enteric_quant_gu/
---

## Introduction

Enteric viruses are a large group of viruses including, for example, calicivirus (including norovirus and sapovirus), adenoviruses, and astroviruses. They are transmitted via faecal-oral route, and cause enteric disease (i.e. diseases with symptoms such as nausea, diarrhea, and vomiting).

Wastewater contains many different types of viruses that infect humans because viruses are shed in the faeces and urine of infected individuals. The Norder group at the University of Gothenburg showed that the relative levels of some enteric viruses in wastewater could be used to predict upcoming outbreaks ([Hellmér _et al._, 2014](https://pubmed.ncbi.nlm.nih.gov/25172863/)). Indeed, previous studies by the Norder group have shown that the levels of noroviruses in wastewater increase 1-2 weeks before larger outbreaks in nursing homes and hospital wards.

In 2023, the Norder group at the University of Gothenburg (GU) commenced weekly monitoring of the levels of some enteric viruses in wastewater. Specifically, they began to quantify the relative levels of enteroviruses (including poliiovirus), pepper molt mild virus (PMMoV), adenoviruses, GG2 (a norovirus), astroviruses, and sapoviruses. This page details the [methods used in monitoring](#methods), as well as [brief summary information about the viruses](#basic-virus-information), and [information about the data collected](#dataset).

The enteric virus monitoring by the Norder group was done alongside their ongoing monitoring of SARS-CoV-2 in wastewater, the data for which is [also shared on this portal](/dashboards/wastewater/covid_quantification/covid_quant_gu/).

The project is led by Professor Heléne Norder (University of Gothenburg, GU), and supported by co-workers from the University of Gothenburg and Sahlgrenska University Hospital (Hao Wang, Marianela Patzi Churqui, Timur Tunovic, Fredy Saguti, and Kristina Nyström). The wastewater sample collections are performed by Lucica Enache at Ryaverket, Gryaab AB, Gothenburg.

The data and visualisations on this page will be updated approximately weekly.

## Wastewater collection sites

The wastewater samples for virus analysis are collected at Ryaverket's wastewater treatment plant in Gothenburg (see the methods section below for details). The Ryaverket treatment plant receives wastewater from all of the households in Gothenburg, which includes 790,000 inhabitants, as well as from industry in the area. Wastewater is also received from industry and residents in surrounding municipalities, including Ale, Härryda, Kungälv, Lerum, Mölndal, and Partille, and also from storm and snowmelt water from older parts of Gothenburg.

## Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_enteric"></span></div>

Please see [the section with summary information about the viruses](#basic-virus-information) for more information on each of the viruses for which data is being collected.

 <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/enteric_graph_gu.json" height="550px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/enteric_viruses_gu.py).

## Commentary from the research group

<div><b>Date:</b> <span id="gu_enteric_comment_date"></span><br><b>Commentary:</b> <span id="gu_enteric_comment"></span></div>

{{< ww_dynamic_content >}}
<br>

## Dataset

###### **Download the data:**

[Quantification of SARS-CoV-2 and enteric viruses in wastewater](https://blobserver.dckube.scilifelab.se/blob/wastewater_data_gu_allviruses.xlsx). Results are available for SARS-CoV-2 from week 7 of 2020 (with a small gap over winter 2022-2023), and for enteric viruses from week 2 of 2023. Updated weekly.

**Contact:** <helene.norder@gu.se>

###### **How to cite the dataset:**

Norder, H., Nyström, K. Patzi Churqui, M., Tunovic, T., Wang, H. (2023). Detection of SARS-CoV-2 and other human enteric viruses in wastewater from Gothenburg. [https://doi.org/10.17044/scilifelab.22510501](https://doi.org/10.17044/scilifelab.22510501).

###### **How to cite method:**

Hellmér, M., Paxéus, N., Magnius, L., Enache, L., Arnholm, B., Johansson, A., Bergström, T., and Norder, H. (2014). Detection of pathogenic viruses in sewage provided early warnings of hepatitis A virus and norovirus outbreaks. [https://doi.org/10.1128/AEM.01981-14](https://doi.org/10.1128/AEM.01981-14).

Saguti, F., Magnil, E., Enache, L., Churqui, M.P., Johansson, A., Lumley, D., Davidsson, F., Dotevall, L., Mattsson, A., Trybala, E., Lagging, M., Lindh, M., Gisslen, M., Brezicka, T., Nystrom, K. and Norder, H. (2021). Surveillance of wastewater revealed peaks of SARS-CoV-2 preceding those of hospitalized patients with COVID-19. [https://doi.org/10.1016/j.watres.2020.116620](https://doi.org/10.1016/j.watres.2020.116620).

Wang, H., Churqui, M.P., Tunovic, T., Enache, L., Johansson, A., Karmander, A., Nilsson, S., Lagging, M., Andersson, M., Dotevall, L., Brezicka, T., Nystrom, K. and Norder, H. (2022). The amount of SARS-CoV-2 RNA in wastewater relates to the development of the pandemic and its burden on the health system. [https://doi.org/10.1016/j.isci.2022.105000](https://doi.org/10.1016/j.isci.2022.105000).

## Methods

Samples of wastewater are collected using a fixed-site sampler that collects 30ml per 10,000m<sup>3</sup> of the incoming wastewater. For the purposes of analysis, seven samples (each representing a 24 hour period) were pooled to create a weekly sample. Part of this weekly sample was sent to the Clinical Microbiology Laboratory at Sahlgrenska University Hospital for analysis. The amount of sample sent varies between 1.5-15l of wastewater depending on the flow, which is determined in large part by the weather. Whilst the amount of wastewater from households and industry is generally reasonably constant over time, the overall levels of wastewater are affected by weather conditions. For example, the levels are higher when the levels of rainfall are high. In order to account for this during analysis, the samples to be analysed for viruses are flow-weighted. This means that the amount of wastewater collected and analysed relates to the flow of incoming wastewater. More information on this can be found in [Hellmér _et al._ (2014)](https://pubmed.ncbi.nlm.nih.gov/25172863/) and [Wang _et al._ (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/).

At the Clinical Microbiology Laboratory, viruses are concentrated to a final volume of 2.5ml using a method that was developed in-house. This method uses the NanoCeram electropositive filter (Argonide, Florida, USA) as the primary means of concentration, and then ultracentrifugation as secondary concentration method ([Saguti et al., 2021](https://doi.org/10.1016/j.watres.2020.116620)). Nucleic acids are extracted from 1ml of the concentrated sample using the QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Real-time quantitative PCR (RT-qPCR) is performed to detect and quantify the viral genomes Details about the method of calculation are provided in [Hellmér et al. (2014)](https://doi.org/10.1128/AEM.01981-14), [Saguti et al. (2021)](https://doi.org/10.1016/j.watres.2020.116620), and [Wang et al. (2022)](https://doi.org/10.1016/j.isci.2022.105000).

### Basic virus information

**Enteroviruses** are the largest genus of enteric viruses infecting humans, including 15 species (including enteroviruses (EV) and rhinoviruses (RV), among others) and around 300 types (112 types within EV-A to -D and 169 RV-A to -C types). Immunity to one type does not confer immunity to another (i.e. there is no cross-immunity). RV infections are common, especially in winter. Infections may be asymptomatic, but can instead result in flu-like symptoms, lower respiratory tract illness, and/or exacerbate chronic illnesses e.g. asthma. EV infections are usually seen in children and young adults. Infections can cause flu-like symptoms, conjunctivitis, myocarditis, meningitis, encephalitis, and flaccid paralysis. EVs can cause larger outbreaks. For example, in European countries, outbreaks of meningitis caused by an EV type belonging to EV-A-C occur approximately every 5 to 7 years.

**Pepper mild mottle virus (PMMoV)** is a plant virus infecting pepper species. When people consume pepper, they excrete PMMoV in their stool. PMMoV is therefore commonly used as a highly sensitive indicator of faecal contamination in water (e.g. wastewater). The levels of PMMoV in wastewater can be used to standardise for the number of people contributing to samples (done in e.g. commercial assays used to quantify SARS-CoV-2 in wastewater). This assumes that people shed the same amount of PPMoV throughout the year. However, in the experience of the Norder group at GU, the levels of PPMoV in the wastewater in Gothenburg are higher in summer (suggesting that residents consume more pepper in summer).

**Adenoviruses** are part of the _Adenoviridae family_. There are 88 human adenoviruses types, classified into 7 species (HAdV-A to -G). Different types can target different organs or organ systems (i.e. they have different tissue tropisms). Human adenoviruses typically cause respiratory diseases. Symptoms can include flu-like symptoms, sore throat, acute bronchitis and pneumonia (HAdV-B and C), conjunctivitis (HAdV-B and D), and gastroenteritis (HAdV-F and G). Children under 9 are the most at risk of infection, but adenoviruses can spread between adults in crowded environments e.g. hospitals. Epidemics do not occur in the general population, and serious complications are rare.

**Noroviruses**, including GG2 (more commonly known as the "winter vomiting disease virus"), belong to the _Caliciviruses_ family and have short incubation periods. Cases of noroviruses typically peak in winter, and can cause serious complications among the immunocompromised and elderly (see [Folkhälsomyndigheten](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/calicivirus-noro-och-sapovirus/) for more information). GG2, for example, has an incubation period of 12-48 hours. Whilst GG2 infected individuals recover quickly, they can be infectious for 2 days after recovery. GG2 is very contagious and spreads quickly in environments where individuals are in close contact (e.g. schools). Immunity is short lived and, because there are multiple GG2 genotypes, an individual can get sick multiple times.

**Astroviruses** that infect humans are part of the _Mamastrovirus_ genus within the _Astroviridae family_. There are 8 species of human astroviruses (HAst1 to 8) and an additional 7 unclassified types. The viruses cause illnesses in infants and young childen. Most often, they cause gastroenteritis, but can also cause headaches, malaise, nausea, vomiting, low-grade fever, and (in rare cases) encephalitis. The incubation period is 1-4 days and infections usually resolve in 2-4 days. In temperate climates, astrovirus infections are most common in winter and spring. Most children develop immunity by the age of 10, so infections are uncommon in immunocompetent adults. However, immunity tends to wane over time, so older people can be at risk. Outbreaks are often seen in nurseries and nursing homes.

**Sapoviruses** are one of the most common causes of acute gastroenteritis in humans and animals (alongside noroviruses). Symptoms include diarrhea and vomiting, which are often accompanied by fever, nausea, and stomach cramps. Sapporovirus (SaV) is the only species of sapovirus. It is classified into five genogroups (GI to GV), with genogroups GI, GII, GIV, and GV infecting humans. The incubation period is similar to GG2 (12-48 hours), but symptoms are usually milder and last 2–6 days. SaV used to be considered exclusively a pediatric pathogen, but there is increaing evidence that other age groups can be infected. Outbreaks of SaV are seen e.g. hospitals, schools, and as a result of food contamination.
