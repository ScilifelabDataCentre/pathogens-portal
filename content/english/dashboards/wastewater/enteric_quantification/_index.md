---
title: Amount of Enteric in wastewater (GU)
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

Enteric viruses, for example calicivirus norovirus (incl. norovirus and sapovirus), adenoviruses, astroviruses) transmit via fecal-oral and cause enteric disease (eg. nausea, diarrhea, vomiting, and abdominal pain). The noroviruses belong to the Caliciviruses family . These viruses have a short incubation time, infected individuals show symptoms within the first two days. Most individuals have symptoms for less than a week and recover quickly, but in frail and elderly individuals´ noroviruses can cause serious health effects. The norovirus GG2 is commonly called "winter vomiting disease virus" and appears seasonally during winter, it often spreads in hospitals, nurseries, and schools ([more info](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/calicivirus-noro-och-sapovirus/)). Wastewater contains many different human viruses present in feces or urine shed from infected persons. Previous studies from the Norder group (Hellmér et al, 2014) has shown that this could be used as a predictive measure of upcoming outbreaks caused by norovirus GG2. Previous studies from the Norder group have shown that the amounts of noroviruses in wastewater increased 1-2 weeks before larger outbreaks in nursery homes and hospital wards. Other human pathogenic viruses, not routinely investigated for, were also identified in the wastewaters.

At the start of the COVID-19 pandemic in 2020, the Norder group restarted these analyses. Simultaneously with investigating for SARS-CoV-2 the presence of a number of other viruses eg. Pepper molt mild virus (PMMoV), adenovirus, norovirus GG2, sapovirus, astrovirus, and enteroviruses including poliovirus are measured weekly. From the beginning of 2023 results from norovirus will be shared with weekly on the Pandemic Preparedness Portal. Data from other viruses will also be shared later.

The project is led by Professor Heléne Norder (University of Gothenburg, GU), and supported by co-workers from the University of Gothenburg and Sahlgrenska University Hospital (Hao Wang, Marianela Patzi Churqui, Timur Tunovic, Fredy Saguti, and Kristina Nyström). The wastewater sample collections are performed by Lucica Enache at Ryaverket, Gryaab AB, Gothenburg.

The data and visualisation on this page are usually updated weekly.

## Wastewater collection sites

Weekly wastewater samples for virus analysis are collected daily at Ryaverket's wastewater treatment plant in Gothenburg. The Ryaverket treatment plant receives wastewater from all households in Gothenburg, which includes 790,000 inhabitants, as well as from industry in the area. Wastewater is also treated from industry and residents in surrounding municipalities, including Ale, Härryda, Kungälv, Lerum, Mölndal and Partille, as well as storm and snowmelt water from older parts of Gothenburg. The amount of wastewater from households is relatively constant throughout the year, but overall the volume varies significantly depending on the weather as higher rainfall results in larger amounts of wastewater. Therefore, the samples to be analyzed for viruses are flow-weighted, so that the amount of collected and analyzed wastewater relates to the flow of incoming wastewater, which means that the amount of analyzed wastewater collected during a week varies between 1 L -15L. More information on this can be found in Hellmér et al., (2014) and Wang et al. (2022).

## Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_gu"></span></div>

 <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/enteric_graph_gu.json" height="550px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/enteric_viruses_gu.py).

## Commentary from the research group

--- TO BE DECIDED ---
## Dataset

###### **Download the data:**

[Quantification of SARS-CoV-2 and enteric viruses in wastewater](https://blobserver.dckube.scilifelab.se/blob/wastewater_data_gu_allviruses.xlsx). Results are available for SARS-CoV-2 from week 7 of 2020 (with a small gap over winter 2022-2023), and for enteric viruses from week 2 of 2023. Updated weekly.

**Contact:** <helene.norder@gu.se>

###### **How to cite the dataset:**

Norder, H., Nyström, K. Patzi Churqui, M., Tunovic, T., Wang, H. (2023). Detection of SARS-CoV-2 and other human enteric viruses in wastewater from Gothenburg. [https://doi.org/10.17044/scilifelab.22510501](https://doi.org/10.17044/scilifelab.22510501).

###### **How to cite method:**

Hellmér M, Paxéus N, Magnius L, Enache L, Arnholm B, Johansson A, Bergström T, Norder H (2014). Detection of pathogenic viruses in sewage provided early warnings of hepatitis A virus and norovirus outbreaks. Appl Environ Microbiol. 80:6771-81. <https://doi.org/10.1128/AEM.01981-14>.

Saguti, F., Magnil, E., Enache, L., Churqui, M.P., Johansson, A., Lumley, D., Davidsson, F., Dotevall, L., Mattsson, A., Trybala, E., Lagging, M., Lindh, M., Gisslen, M., Brezicka, T., Nystrom, K. and Norder, H. (2021). Surveillance of wastewater revealed peaks of SARS-CoV-2 preceding those of hospitalized patients with COVID-19. <https://doi.org/10.1016/j.watres.2020.116620>.

Wang, H., Churqui, M.P., Tunovic, T., Enache, L., Johansson, A., Karmander, A., Nilsson, S., Lagging, M., Andersson, M., Dotevall, L., Brezicka, T., Nystrom, K. and Norder, H. (2022). The amount of SARS-CoV-2 RNA in wastewater relates to the development of the pandemic and its burden on the health system. <https://doi.org/10.1016/j.isci.2022.105000>.


## Methods

Samples of wastewater are collected using a fixed-site sampler that collected 30ml per 10,000m3 of the incoming wastewater. For the purposes of analysis, seven samples (each representing a 24 hour period) were pooled to create a weekly sample. Part of this weekly sample, consisting of 1.5-15 L of wastewater (depending on the flow) was sent to the Clinical Microbiology Laboratory at Sahlgrenska University Hospital for analysis.

At the Clinical Microbiology Laboratory, viruses are concentrated to a final volume of 2.5ml, using a method that was developed in-house. This method uses the NanoCeram electropositive filter (Argonide, Florida, USA) as the primary means of concentration, and then ultracentrifugation as secondary concentration method ([Saguti et al., 2021](https://doi.org/10.1016/j.watres.2020.116620)). Nucleic acids are extracted from 1ml of the concentrated sample using the QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Real-time quantitative PCR (RT-qPCR) is performed to detect and quantify the viral genomes Details about the method of calculation are provided in [Saguti et al. (2021)](https://doi.org/10.1016/j.watres.2020.116620), [Hellmér et al., (2014)](https://doi.org/10.1128/AEM.01981-14), and [Wang et al., (2022)](https://doi.org/10.1016/j.isci.2022.105000).
