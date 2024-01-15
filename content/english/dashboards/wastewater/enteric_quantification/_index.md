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

In 2017, and since 2020, the Norder group at the University of Gothenburg (GU) conducted weekly monitoring of the levels of some enteric viruses in wastewater. They quantify the levels of enteroviruses (including poliovirus), adenoviruses, GG2 (a norovirus causing winter vomiting disease), astroviruses, sapoviruses and also pepper molt mild virus (PMMoV). This page focuses on data produced using an updated method for quantification that was used from week 20 (15th May) of 2023. This method was used in parallel with a previous method until week 43 of 2023. Data produced using that previous method between week 2 and week 43 of 2023 (i.e. 9th January and 23rd October 2023) are available on the page related to [historic enteric virus data from Gothenburg](/dashboards/wastewater/enteric_quantification/historic_enteric_gu/).

This page details the [latest method used in monitoring](#methods), as well as [a brief summary information about the viruses](#basic-virus-information), and [information about the data collected](#dataset).

The enteric virus monitoring by the Norder group was done alongside their ongoing monitoring of SARS-CoV-2 in wastewater, the data for which are [also shared on this portal](/dashboards/wastewater/covid_quantification/covid_quant_gu/).

The data and visualisations on this page will be updated **approximately weekly**.

## Wastewater collection sites

Influent wastewater samples were collected from Ryaverket wastewater treatment plant (WWTP) in Gothenburg by Lucica Enache at Ryaverket, Gryaab AB, Gothenburg (see the methods section below for details). The Ryaverket treatment plant receives wastewater from all of the households in Gothenburg, which includes 790,000 inhabitants, as well as from industry in the area. Wastewater is also received from industry and residents in surrounding municipalities, including Ale, Härryda, Kungälv, Lerum, Mölndal, and Partille, and also from storm and snowmelt water from older parts of Gothenburg.

## Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_enteric"></span></div>

Please see [the section with summary information about the viruses](#basic-virus-information) for more information on each of the viruses for which data is being collected.

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

 <div class="plot_wrapper mb-3">
    <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/enteric_graph_gu_new.json" height="550px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/historic_enteric_viruses_gu.py).

## Commentary from the research group

<!-- <div><b>Date:</b><span id="gu_enteric_comment_date"></span><br><b>Commentary:</b><span id="gu_enteric_comment"></span></div> -->
<div><b>Date:</b> 2023-11-23<br><b>Commentary:</b> From week 20 we have implemented a new concentration method for virus detection. The new technology is ultrafiltration and has been used in parallel with our standard method until now. The new technique has higher sensitivity for the detection and recovery of viruses and has a shorter processing time. The new figure displays the total number of viral genome copies per day instead of the relative amount of viral genomes previously used for SARS-CoV-2. As a result, the baseline for the detection is elevated.

Three weeks after the schools started in Gothenburg, the levels of enterovirus increased in the wastewater and is now decreasing again. Enterovirus often peaks in late summer and early autumn. This virus may cause outbreaks usually among children and adolescents. Rhinoviruses cause common cold and often peaks during early autumn and colder seasons. There were many rhinovirus infections in Gothenburg during late August/early September which may explain some of the increase during weeks 40-43.

No major outbreak caused by the other investigated viruses has been identified until now.

In February we had a minor increase in norovirus GG2 (winter vomiting disease virus) a little earlier than usual and it decreased by week 11. Some minor increases also occurred in late May, but no major outbreak was observed.

For astrovirus, there was a small outbreak in weeks 9 and 10 (end of February and start of March). A slight increase is now observed as expected.

Sapovirus peaked slightly in week 14 (early April).

Adenovirus peaked slightly in week 10, no additional increase has been observed. From week 22 we have improved the technology's sensitivity for adenovirus detection, which means that the baseline for adenovirus detection is elevated. During summer (from June to the beginning of August), Adenovirus showed an increase during weeks 26 to 32.

The amount of pepper mild mottle virus (PMMoV) has varied more than 10-fold during the year. This virus is often used as an indicator of fecal contamination of water. In commercial assays for SARS-CoV-2 detection, quantification of PMMoV is used as an indicator of the number of people contributing to the wastewater, assuming we consume the same amount of peppers and chilies every week. It increased in early June and around midsummer, indicating an increase in our pepper consumption during those weeks rather than an increase in the number of people contributing to the wastewater during those weeks.</div>

{{< ww_dynamic_content >}}
<br>

## Dataset

###### **Download the data:**

[Quantification of SARS-CoV-2 and enteric viruses in wastewater](https://blobserver.dckube.scilifelab.se/blob/wastewater_data_gu_allviruses.xlsx). Results are available for SARS-CoV-2 and enteric viruses from week 20 of 2023. Updated weekly.

**Contact:** <helene.norder@gu.se>

###### **How to cite the dataset:**

Norder, H., Nyström, K. Patzi Churqui, M., Tunovic, T., Wang, H., Saguti, F. (2023). Detection of SARS-CoV-2 and other human enteric viruses in wastewater from Gothenburg. [https://doi.org/10.17044/scilifelab.24787353.v1](https://doi.org/10.17044/scilifelab.24787353.v1).

###### **How to cite method:**

Hellmér, M., Paxéus, N., Magnius, L., Enache, L., Arnholm, B., Johansson, A., Bergström, T., and Norder, H. (2014). Detection of pathogenic viruses in sewage provided early warnings of hepatitis A virus and norovirus outbreaks. [https://doi.org/10.1128/AEM.01981-14](https://doi.org/10.1128/AEM.01981-14).

Saguti, F., Magnil, E., Enache, L., Churqui, M.P., Johansson, A., Lumley, D., Davidsson, F., Dotevall, L., Mattsson, A., Trybala, E., Lagging, M., Lindh, M., Gisslen, M., Brezicka, T., Nystrom, K. and Norder, H. (2021). Surveillance of wastewater revealed peaks of SARS-CoV-2 preceding those of hospitalized patients with COVID-19. [https://doi.org/10.1016/j.watres.2020.116620](https://doi.org/10.1016/j.watres.2020.116620).

Wang, H., Churqui, M.P., Tunovic, T., Enache, L., Johansson, A., Karmander, A., Nilsson, S., Lagging, M., Andersson, M., Dotevall, L., Brezicka, T., Nystrom, K. and Norder, H. (2022). The amount of SARS-CoV-2 RNA in wastewater relates to the development of the pandemic and its burden on the health system. [https://doi.org/10.1016/j.isci.2022.105000](https://doi.org/10.1016/j.isci.2022.105000).

## Methods

Samples of wastewater are collected using a fixed-site sampler that collects 30ml per 10,000m<sup>3</sup> of the incoming wastewater. For the purposes of analysis, seven samples (each representing a 24 hour period) were pooled to create a weekly sample. Part of this weekly sample was sent to the Clinical Microbiology Laboratory at Sahlgrenska University Hospital for analysis. The amount of sample sent varies between 1.5-15l of wastewater, depending on the flow. Whilst the amount of wastewater from households and industry is generally reasonably constant over time, the overall levels of wastewater are affected by weather conditions. For example, the levels are higher when the levels of rainfall are high. In order to account for this during analysis, the samples to be analysed for viruses are flow-weighted. This means that the amount of wastewater collected and analysed relates to the flow of incoming wastewater. More information on this can be found in [Hellmér _et al._ (2014)](https://pubmed.ncbi.nlm.nih.gov/25172863/) and [Wang _et al._ (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/).

At the Clinical Microbiology Laboratory, two methods developed in-house were used to concentrate viruses. The current method used involves ultrafiltration as the main concentration method. Our previous method used an electropositive filter (Argonide, Florida, USA) as the primary means of concentration ([Saguti _et al._, 2021](https://doi.org/10.1016/j.watres.2020.116620)).

Nucleic acids are extracted from 1ml of the concentrated sample using the QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Real-time quantitative PCR (RT-qPCR) is performed to detect and quantify the viral genomes. Details about the method of calculation are provided in [Hellmér et al. (2014)](https://doi.org/10.1128/AEM.01981-14), [Saguti _et al._ (2021)](https://doi.org/10.1016/j.watres.2020.116620), [Wang _et al._ (2022)](https://doi.org/10.1016/j.isci.2022.105000), and [Wang _et al._ (2023)](https://doi.org/10.1016/j.scitotenv.2023.165012). With both techniques, the amounts of the different virus genomes are given as daily average amounts, as they are based on one week of wastewater sampling.

## Archived data

[Historic enteric virus data from Gothenburg collected between week 2 and week 43 of 2023](/dashboards/wastewater/enteric_quantification/historic_enteric_gu/).

### Basic virus information

**Enterovirus** is the largest genus of enteric viruses infecting humans. It includes 15 species with several types classified within each species. In two of these species, enteroviruses (EV) and rhinoviruses (RV), there are around 300 types infecting humans (112 EV-A to -D types (including polioviruses) and 169 RV-A to -C types). Immunity to one type does not confer immunity to another (i.e. there is no cross-immunity). EV infections are usually seen in children and young adults. Infections can cause flu-like symptoms, conjunctivitis, myocarditis, meningitis, encephalitis, and flaccid paralysis. These viruses can cause larger outbreaks. About every 5 to 7 years, there is an outbreak of meningitis among young people in Europe caused by an EV type belonging to EV-A-C. RV infections are common in all ages, especially in winter. Infections are usually mild, but can also cause flu-like symptoms, diseases of the lower respiratory tract, and/or worsen chronic diseases (e.g. asthma).

**Adenoviruses** belong to the _Adenoviridae_ family. There are 88 types of human adenoviruses, classified into 7 species (HAdV-A to -G). Different types infect different organs or organ systems (i.e. they have different tissue tropisms). In humans, adenoviruses often cause respiratory diseases. Symptoms can be flu-like (i.e. sore throat, acute bronchitis, and pneumonia (HAdV-B and C)) but can also include conjunctivitis (HAdV-B and D) and gastroenteritis (HAdV-F and G). Serious complications after an adenovirus infection are rare. Children under the age of 9 are at greatest risk of symptomatic infection, but adults may also be affected (mainly by eye inflammation and gastroenteritis). These viruses do not cause epidemics but can spread between adults in crowded environments such as hospitals and military installations, or in swimming pools.

**Norovirus**, including GG2 (more commonly known as “winter vomiting disease virus”), belong to the _Caliciviridae_ family. The number of norovirus cases usually peaks in the winter (January/February). The infection can cause serious complications among the immunosuppressed and the elderly (see [Folkhälsomyndigheten](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/calicivirus-noro-och-sapovirus/) for more information). GG2 is highly contagious and spreads rapidly in environments where individuals are in close contact. The incubation period is short, between 12 and 48 hours. Although GG2-infected individuals recover quickly, they may be infectious for 2 days after recovery. Immunity is short-lived and because there are several GG2 genotypes, so an individual can get sick multiple times.

**Astroviruses** belong to the _Astroviridae_ family and infect birds and mammals. Those infecting humans (HAst) are part of the _Mamastrovirus_ genus, they form 8 species (HAst1 to 8) and an additional 7 unclassified types. HAst mainly cause illness in children and the elderly. Most often they cause gastroenteritis, but can also cause headache, nausea, vomiting, low-grade fever, and (in rare cases) encephalitis. The incubation period is 1-4 days and infections usually resolve in 2-4 days. In temperate climates, astrovirus infections are most common in winter and spring. Most children have developed immunity by the age of 10, so infections are uncommon in immunocompetent adults. However, immunity tends to wane over time, so older people can be at risk of symptomatic infection. Outbreaks are often seen in daycare centers and nursing homes.

**Sapovirus**, like norovirus, belongs to the _Calicivirdae_ family and infect both humans and animals. Sapporovirus (SaV) is the only species of sapovirus. There are five genogroups of SaV (GI to GV), with GI, GII, GIV, and GV infecting humans and being one of the most common causes of acute gastroenteritis (along with norovirus). Symptoms include diarrhea and vomiting, which are often accompanied by fever, nausea, and stomach cramps. The incubation period is similar to GG2 (12-48 hours), but symptoms are usually milder and last 2-6 days. In the past, SaV was thought to exclusively infect children, but there is increasing evidence that most age groups can be infected. Outbreaks of SaV have been reported from schools, childcare, adult long-term care, and hospitals, often due to contaminated food.

**Pepper mild mottle virus (PMMoV)** is a plant virus infecting plants in the genus _Capsicum_, such as peppers, chili peppers, cayenne peppers, etc. When humans consume any of these plants, which are often infected with PMMoV, the virus is excreted in the faeces. This virus is often used as an indicator of faecal contamination of water (e.g. recreational waters and raw water). In commercial assays for SARS-CoV-2 detection, quantification of PMMoV is used as an indicator of the number of people contributing to the wastewater; inherently assuming that people consume the same amount of peppers and chilies every week. However, according to the experience of the Norder group at GU, the levels of PPMoV in the wastewater in Gothenburg are higher in the summer (indicating that the inhabitants consume more of these plants during this time of year). In their analyses, it is used as a control of the technique.
