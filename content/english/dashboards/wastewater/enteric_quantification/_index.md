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

Wastewater contains many different types of viruses that infect humans, as such viruses are shed in the faeces and/or urine of individuals infected with the virus. The Norder group at the University of Gothenburg showed that the relative levels of some enteric viruses could be used to predict upcoming outbreaks ([Hellmér _et al._, 2014](https://pubmed.ncbi.nlm.nih.gov/25172863/)). Indeed. previous studies by the Norder group have shown that the levels of noroviruses in wastewater increase 1-2 weeks before larger outbreaks in nursing homes and hospital wards.

In 2023, the Norder group at the University of Gothenburg (GU) commenced weekly monitoring of the levels of some enteric viruses in wastewater. Specifically, they began to quantify the relative levels of enteroviruses (including poliiovirus), pepper molt mild virus (PMMoV), adenoviruses, GG2 (a norovirus), astroviruses, and sapoviruses. This monitoring was done alongside their ongoing monitoring of SARS-CoV-2 in wastewater, the data for which is [shared on this portal](/dashboards/wastewater/covid_quantification/covid_quant_gu/). The Norder group now also share data from their monitoring of enteric viruses on this portal.

The project is led by Professor Heléne Norder (University of Gothenburg, GU), and supported by co-workers from the University of Gothenburg and Sahlgrenska University Hospital (Hao Wang, Marianela Patzi Churqui, Timur Tunovic, Fredy Saguti, and Kristina Nyström). The wastewater sample collections are performed by Lucica Enache at Ryaverket, Gryaab AB, Gothenburg.

The data and visualisations on this page will be updated approximately weekly.

### Basic virus information

**Enteroviruses** comprise of a group of around one hundred viruses of the _Picornaviridae family_. This group includes, for example, Enterovirus A-D (which includes Poliovirus (type 1-3)), Coxsackievirus (group A and B), Echovirus, and Enterovirus. Non-polio enteroviruses typically cause only mild symptoms akin to those caused by the common cold.

**Adenoviruses** are part of the _Adenoviridae family_. There are seven human adenoviruses (A to G) and >60 (sero)types. They often cause acute viral gastroenteritis (diarrhea and vomiting) in children under 5, but this is rare in adults.

**Noroviruses**, including GG2 (more commonly known as the "winter vomiting disease virus"), belong to the _Caliciviruses_ family of enteric viruses. They have a short incubation time, and infected individuals show symptoms within the first two days. Most patients recover quickly, and experience symptoms for less than a week. However, there can be more serious effects on the health of those in certain groups, including individuals that are immunocompromised. GG2 cases are seasonal, with cases peaking in winter. It often spreads most where individuals come into close contact, such as in hospitals, nurseries, and schools. See [Folkhälsomyndigheten](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/calicivirus-noro-och-sapovirus/) for more information.

**Astroviruses** are part of the _Astroviridae family_, which includes eight serotypes (HAst1-8). Patients infected with astroviruses often experience mild diarrhea for a few days. Other symptoms could include a headache, malaise, nausea, vomiting, and a mild fever. Cases of astrovirus infection are most common in winter and spring. Healthy individuals typically acquire immunity after infection, so reinfections are rare.

## Wastewater collection sites

The wastewater samples for virus analysis are collected at Ryaverket's wastewater treatment plant in Gothenburg (see the methods section below for details). The Ryaverket treatment plant receives wastewater from all of the households in Gothenburg, which includes 790,000 inhabitants, as well as from industry in the area. Wastewater is also received from industry and residents in surrounding municipalities, including Ale, Härryda, Kungälv, Lerum, Mölndal, and Partille, and also from storm and snowmelt water from older parts of Gothenburg.

## Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_enteric"></span></div>

 <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/enteric_graph_gu.json" height="550px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/enteric_viruses_gu.py).

## Commentary from the research group

<div><b>Date:</b> <span id="gu_enteric_comment_date"></span><br><b>Commentary:</b> <span id="gu_enteric_comment"></span></div>

{{< ww_dynamic_content >}}

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

Samples of wastewater are collected using a fixed-site sampler that collects 30ml per 10,000m<sup>3</sup> of the incoming wastewater. For the purposes of analysis, seven samples (each representing a 24 hour period) were pooled to create a weekly sample. Part of this weekly sample, was sent to the Clinical Microbiology Laboratory at Sahlgrenska University Hospital for analysis. The amount of sample sent varies between 1.5-15l of wastewater depending on the flow, which is determined in large part by the weather. Whilst the amount of wastewater from households and industry is generally reasonably constant, the overall level of wastewater received by treatment plants are much greater when the levels of rainfall are high, for example. In order to account for this during analysis, the samples to be analysed for viruses are flow-weighted. This means that the amount of wastewater collected and analysed wastewater relates to the flow of incoming wastewater. More information on this can be found in [Hellmér _et al._ (2014)](https://pubmed.ncbi.nlm.nih.gov/25172863/) and [Wang _et al._ (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/).

At the Clinical Microbiology Laboratory, viruses are concentrated to a final volume of 2.5ml, using a method that was developed in-house. This method uses the NanoCeram electropositive filter (Argonide, Florida, USA) as the primary means of concentration, and then ultracentrifugation as secondary concentration method ([Saguti et al., 2021](https://doi.org/10.1016/j.watres.2020.116620)). Nucleic acids are extracted from 1ml of the concentrated sample using the QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Real-time quantitative PCR (RT-qPCR) is performed to detect and quantify the viral genomes Details about the method of calculation are provided in [Saguti et al. (2021)](https://doi.org/10.1016/j.watres.2020.116620), [Hellmér et al. (2014)](https://doi.org/10.1128/AEM.01981-14), and [Wang et al. (2022)](https://doi.org/10.1016/j.isci.2022.105000).
