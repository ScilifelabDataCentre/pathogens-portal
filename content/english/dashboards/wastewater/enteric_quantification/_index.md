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

In 2017, and since 2020, the Norder group at the University of Gothenburg (GU) conducted weekly monitoring of the levels of some enteric viruses in wastewater. They quantify the levels of enteroviruses (including poliovirus), adenoviruses, GG2 (a norovirus causing winter vomiting disease), astroviruses, sapoviruses and also pepper molt mild virus (PMMoV). This page details the [methods used in monitoring](#methods), as well as [brief summary information about the viruses](#basic-virus-information), and [information about the data collected](#dataset). Only the data collected since 2023 are included on this page.

The enteric virus monitoring by the Norder group was done alongside their ongoing monitoring of SARS-CoV-2 in wastewater, the data for which is [also shared on this portal](/dashboards/wastewater/covid_quantification/covid_quant_gu/).

The project is led by Professor Heléne Norder (University of Gothenburg, GU), and supported by co-workers from the University of Gothenburg and Sahlgrenska University Hospital (Marianela Patzi Churqui, Timur Tunovic, Hao Wang, Fredy Saguti, and Kristina Nyström). The wastewater sample collections are performed by Lucica Enache at Ryaverket, Gryaab AB, Gothenburg.

The data and visualisations on this page will be updated approximately weekly.

## Wastewater collection sites

The wastewater samples for virus analysis are collected at Ryaverket's wastewater treatment plant in Gothenburg (see the methods section below for details). The Ryaverket treatment plant receives wastewater from all of the households in Gothenburg, which includes 790,000 inhabitants, as well as from industry in the area. Wastewater is also received from industry and residents in surrounding municipalities, including Ale, Härryda, Kungälv, Lerum, Mölndal, and Partille, and also from storm and snowmelt water from older parts of Gothenburg.

## Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_enteric"></span></div>

Please see [the section with summary information about the viruses](#basic-virus-information) for more information on each of the viruses for which data is being collected.

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

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

**Enterovirus** is the largest genus of enteric viruses infecting humans. It includes 15 species with several types classified within each species. In two of these species, enteroviruses (EV) and rhinoviruses (RV), there are around 300 types infecting humans (112 EV-A to -D types (including polioviruses) and 169 RV-A to -C types). Immunity to one type does not confer immunity to another (i.e. there is no cross-immunity). EV infections are usually seen in children and young adults. Infections can cause flu-like symptoms, conjunctivitis, myocarditis, meningitis, encephalitis, and flaccid paralysis. These viruses can cause larger outbreaks. About every 5 to 7 years, there is an outbreak of meningitis among young people in Europe caused by an EV type belonging to EV-A-C. RV infections are common in all ages, especially in winter. Infections are usually mild, but can also cause flu-like symptoms, diseases of the lower respiratory tract, and/or worsen chronic diseases (e.g. asthma).

**Adenoviruses** belong to the _Adenoviridae_ family. There are 88 types of human adenoviruses, classified into 7 species (HAdV-A to -G). Different types infect different organs or organ systems (i.e. they have different tissue tropisms). In humans, adenoviruses often cause respiratory diseases. Symptoms can be flu-like (i.e. sore throat, acute bronchitis, and pneumonia (HAdV-B and C)) but can also include conjunctivitis (HAdV-B and D) and gastroenteritis (HAdV-F and G). Serious complications after an adenovirus infection are rare. Children under the age of 9 are at greatest risk of symptomatic infection, but adults may also be affected (mainly by eye inflammation and gastroenteritis). These viruses do not cause epidemics but can spread between adults in crowded environments such as hospitals and military installations, or in swimming pools.

**Norovirus**, including GG2 (more commonly known as “winter vomiting disease virus”), belong to the _Caliciviridae_ family. The number of norovirus cases usually peaks in the winter (January/February). The infection can cause serious complications among the immunosuppressed and the elderly (see [Folkhälsomyndigheten](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/calicivirus-noro-och-sapovirus/) for more information). GG2 is highly contagious and spreads rapidly in environments where individuals are in close contact. The incubation period is short, between 12 and 48 hours. Although GG2-infected individuals recover quickly, they may be infectious for 2 days after recovery. Immunity is short-lived and because there are several GG2 genotypes, so an individual can get sick multiple times.

**Astroviruses** belong to the _Astroviridae_ family and infect birds and mammals. Those infecting humans (HAst) are part of the _Mamastrovirus_ genus, they form 8 species (HAst1 to 8) and an additional 7 unclassified types. HAst mainly cause illness in children and the elderly. Most often they cause gastroenteritis, but can also cause headache, nausea, vomiting, low-grade fever, and (in rare cases) encephalitis. The incubation period is 1-4 days and infections usually resolve in 2-4 days. In temperate climates, astrovirus infections are most common in winter and spring. Most children have developed immunity by the age of 10, so infections are uncommon in immunocompetent adults. However, immunity tends to wane over time, so older people can be at risk of symptomatic infection. Outbreaks are often seen in daycare centers and nursing homes.

**Sapovirus**, like norovirus, belongs to the _Calicivirdae_ family and infect both humans and animals. Sapporovirus (SaV) is the only species of sapovirus. There are five genogroups of SaV (GI to GV), with GI, GII, GIV, and GV infecting humans and being one of the most common causes of acute gastroenteritis (along with norovirus). Symptoms include diarrhea and vomiting, which are often accompanied by fever, nausea, and stomach cramps. The incubation period is similar to GG2 (12-48 hours), but symptoms are usually milder and last 2-6 days. In the past, SaV was thought to exclusively infect children, but there is increasing evidence that most age groups can be infected. Outbreaks of SaV have been reported from schools, childcare, adult long-term care, and hospitals, often due to contaminated food.

**Pepper mild mottle virus (PMMoV)** is a plant virus infecting plants in the genus _Capsicum_, such as peppers, chili peppers, cayenne peppers, etc. When humans consume any of these plants, which are often infected with PMMoV, the virus is excreted in the faeces. This virus is often used as an indicator of faecal contamination of water (e.g. recreational waters and raw water). In commercial assays for SARS-CoV-2 detection, quantification of PMMoV is used as an indicator of the number of people contributing to the wastewater; inherently assuming that people consume the same amount of peppers and chilies every week. However, according to the experience of the Norder group at GU, the levels of PPMoV in the wastewater in Gothenburg are higher in the summer (indicating that the inhabitants consume more of these plants during this time of year). In their analyses, it is used as a control of the technique.
