---
title: Register-based COVID-19 vaccination study (RECOVAC)
description: Dedicated to the work of the register-based large-scale national population study to monitor COVID-19 vaccination effectiveness and safety (RECOVAC) project.
banner: /dashboard_thumbs/RECOVAC.png
toc: true
plotly: true
menu:
  dashboard_menu:
    identifier: recovac
    name: Register-based vaccination (RECOVAC)
dashboards_topics: [COVID-19, Infectious diseases]
data_status: "updating" # or "historic"
---

## RECOVAC project overview

The [RECOVAC project](https://www.gu.se/en/research/recovac) (register-based large-scale national population study to monitor COVID-19 vaccination effectiveness and safety) is a register-based national population study focused on monitoring the effectiveness and safety of COVID-19 vaccinations. It is a subproject of SCIFI-PEARL (the Swedish COVID-19 Investigation for Future Insights – a Population Epidemiology Approach using Register Linkage). The **RECOVAC project** uses a multi-register observational research approach to track the effectiveness of COVID-19 vaccination research and vaccine safety in Sweden. The project will also assess how any adverse effects of the vaccine (vaccine AE) co-vary with the characteristics of subjects, such as their vaccination status. The data for the project are updated regularly (every 1-3 months), enabling the development of contemporary conclusions and recommendations.

The study cohort of the **RECOVAC project** was originally developed with a study design to include all Swedish COVID-19 cases, all cases with a range of conditions representing potential vaccine adverse events (AEs), and a 10% comparison sample of the general population, but was extended to a full population study design during 2021 to instead include all individuals in the Swedish population and among them all COVID-19 cases, all vaccinated individuals and possibility to identify any potential AE cases. The study links general health data about the cohort with vaccination data in order to provide a comprehensive longitudinal view of the COVID-19 pandemic and effects of the vaccination program. The project also uses data from the ["Symptoms" web app](https://www.symptoms.se/recovac/fpi) in a collaboration between Symptoms AB and The University of Gothenburg for this project, which enables users to self-report symptoms. The addition of symptom data from this app further supplements register-based information related to vaccine effectiveness and safety.

In summary, this project combines data from multiple sources in order to produce a unique set of data that constitutes a valuable resource for epidemiological research on COVID-19 vaccination. The findings from research performed on this data can be used for the benefit of public health and safety. They can be used to formulate appropriate policies for the present pandemic, and to enable preparedness for future pandemics. Indeed, by combining high quality data from national registers with little delay, the project provides a contemporary and internationally unique data source for epidemiological research on SARS-CoV-2.

For more information on SCIFI-PEARL see [here](https://www.gu.se/en/research/scifi-pearl).

EPN Nr 2020-01800, 2020-05829, 2021-00267, 2021-00829, 2021-02106, 2021-04098, 2022-00500-02, 2022-01207-02.

## Data visualisations

<div class="alert alert-info">All data last updated: {{% RECOVAC_date_modified %}}</div>

_All code used to produce the visualisations on this page is available on [GitHub](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/tree/main/RECOVAC). The particular scripts used in each case are linked below the plots._

The visualisations on this page broadly relate to two types of data; (a) data regarding the Swedish population at large, and (b) data on individuals in the Swedish population with certain comorbidities (at the start of the pandemic, assessed as of 1st Jan 2020, based on information from 2015-2019). More detail about the data used to produce the visualisations is available in the two subsections below. Instructions on how to manipulate the interactive plots are provided above the plots in each subsection.

In each case, the data are subdivided according to the number of doses received by individuals.

### Swedish population in general

#### Information on vaccination coverage

The top graph in this section shows data on vaccine coverage (i.e. the proportion of the population that has received a given number of doses). The data are from the National Vaccination Register at the Public Health Agency of Sweden (PHAS) and population register data from Statistics Sweden (SCB).

COVID-19 vaccinations first became available in Sweden in late December 2020. They were first offered to those most at risk of developing serious symptoms (i.e. the elderly and those with certain comorbidities). For more details on the vaccine rollout in Sweden, please see our [page on vaccines](https://www.pathogens.se/dashboards/vaccines/).

There is a clear trend in the coverage for each dose. Specifically, the levels of coverage initially increase slowly, and then rapidly increase before reaching a plateau. This is in line with the fact that vaccines were made available to more of the population over time; vaccines were initially made available to risk groups and the elderly, and eventually became available to most of the population, including younger age groups.

#### Information on admission to intensive care units (ICU)

The lower graph in this section shows the number of people admitted to intensive care (ICU), and how many vaccine doses they had received upon admission. These data are from the registers already mentioned, as well as the Swedish Intensive Care Register (SIR), a healthcare quality register.

There are three major peaks in admissions to intensive care (ICU). The timing of these peaks corresponds to peaks in COVID-19 cases, specifically in spring 2020, winter 2021, and spring 2021, when the rates of infection were high.

In order to infer the impact of vaccination on ICU admissions, it is best to directly compare the data over the same time period. After aligning the timeframes in the below graphs, it is clear that the number of patients admitted with one or two vaccine doses increases with the coverage of these doses. This is unsurprising, given that the vaccine does not completely protect against serious illness, especially after only a single dose. There is considerable evidence of the protective effect of vaccination, though. Firstly, a majority of admissions in most weeks were related to individuals that had not received any vaccine doses, despite the fact that this represents an increasingly smaller portion of the population over time. Secondly, the number of admissions decreases as vaccine coverage increases, particularly when considering the coverage of multiple doses. The absolute numbers are, of course, also affected by the changes in intensity of the pandemic. This means that they tend to be lower in the summer months and other periods when the spread of the infection was low, and higher over the winter-spring period. There is, however, some evidence of a de-coupling between case number and ICU admissions for the first time in winter 2021. Cases were generally high over this period (see e.g. data from the [Swedish public health agency](https://experience.arcgis.com/experience/09f821667ce64bf7be6f9f87457ed9aa)). This is evidence that vaccines are protective against the onset of serious illness, because it means a smaller proportion of cases led to ICU admission. This de-coupling is also evident through 2022.

##### Visualisations

The graphs below have multiple interactive features. In brief, it is possible to view different parts of the data using the buttons above the graphs. For exmaple, it is possible to look only at data from only those over 60 years of age by clicking '>60'. The 'Align timeline' button will change the timeline of the graphs so that only period for which data is available for both types of data shown is visible. The 'Show all data' button can be used to see all of the available data for both datasets (the timelines of the two are not the same).

<div id="dwbuttonsone"><button class="btn btn-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#vis_instr_one" aria-expanded="False" aria-controls="mandatorycollapse">
    Click here for more detailed instructions on using the features of the graphs
</button>
</div>
<div class="collapse" id="vis_instr_one">
  <div class="card card-body">
        <span>

The two plots in this subsection have multiple interactive features. Some features are common between the two plots, and others are unique. The plots are independent of one another, so changes in one will not affect the other.

##### View data from a given age range

The data are presented for 3 age categories; above 18 years (> 18), between 18-59 years (18-59), and above 60 years of age (> 60). To see data from a given age category, simply click on the appropriate button in the 'Age Range' buttons list. The button will appear slightly more blue when activated.

##### View data on a specific number of doses

The data are categorised according to the number of doses received, and each category is represented by a different colour. Double-click on a dose category in the legend on the right to display only that dose. Another double-click will reset the graph so that all doses are displayed. A single-click on a category will toggle the display of that category on/off.

##### Changing the timeframe displayed

The two graphs are shown on different time scales. This is in part because vaccinations were not made available until early 2021, whilst data on ICU admissions resulting from COVID-19 infection are available from March 2020. Further, the latest date for which data is available can differ between the two datasets. The default view will show all of the data available for both datasets. However, it is useful for align the timeframes, especially when making inferences about the effects of vaccination on ICU admission. Use the 'Align timeframe' button in the 'Timeframe' buttons list to align the timeframes. Click the 'Show all data' button to view all of the available data.

##### Accurately read data values

It is possible to view the underlying data values by hovering the cursor over the graph. All values for a given date are shown together.

##### Other features

When hovering over the plot with the cursor, additional grey icons appear in the top right. The +, -, and magnifying glass icons can be used to zoom in/out of the plot. Alternatively, it is possible to zoom into a given part of the graph by clicking and dragging with the cursor to select that portion. The autoscale and reset axes icons (which look like a box containing arrows and a house, respectively) can be used to scale the axes appropriately for the data selected. The plot can be downloaded in .png format by clicking on the camera icon.
</span>

  </div>
</div>

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/swedishpop_subplot_button.json" height="800px" >}}</div>
</div>

**Code used to produce plots:** [Preparation for vaccine coverage data](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/RECOVAC/Swedishpop_vaccinecov_dataprep.py), [Graph of vaccine coverage](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/RECOVAC/Swedishpop_vaccinecov_plotwbuttons.py), [Graph and data preparation for ICU admissions data](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/RECOVAC/Swedishpop_ICU_plotwbuttons.py).

### Data related to patients with comorbidities

This section considers data on individuals with one of four comorbidities; cardiovascular disease, diabetes, respiratory disease, and cancer. The data were obtained from the registers mentioned in the section above, as well as the National Patient Register (NPR) and SmiNet. The NPR contains specialised outpatient and hospitalised inpatient care, and is held by the National Board of Health and Welfare (Socialstyrelsen). SmiNet is the national register for mandatory registration of notifiable infectious diseases, and is held at the PHAS. Coded diagnoses in 2015-2019 from the NPR are used to classify individuals by comorbidity conditions. Note that individuals may be included in one or more of these comorbidity groups. COVID-19 cases diagnosed among people with comorbidities are determined using a positive SARS-CoV-2 test from SmiNet and/or a diagnosis of COVID-19 in NPR (the overwhelming majority have a positive test).

The buttons in the below plots can be used to display data on a given comorbidity (see the blow subsection for details). All data available on a given comorbidity will be displayed by default, this may mean that different timelines are shown in the two graphs. However, the timelines can be aligned so that more direct comparisons can be made between the data in the two graphs.

There is clear evidence of the benefits of vaccination for patients with each comorbidity considered. When switching between comorbidities, it is evident that they follow the same overall pattern in terms of the number of COVID-19 cases detected, but there are variations in magnitude. Similar to the above data considering the population over 18, it is clear that the proportion of vaccinated individuals diagnosed with COVID-19 increases with vaccine coverage. This is expected because the vaccine is not completely effective at preventing infection (although it does have a higher effectiveness against the development of serious disease, as shown in many studies, see also the [above data on ICU admission rates](#swedish-population-in-general)). Thus, as the proportion of the population that is vaccinated increases, more vaccinated individuals are likely to develop COVID-19. Some evidence of a protective effect can already be inferred from a superficial consideration of the number of cases detected in autumn 2020 compared to autumn 2021. The initial reduction in cases that occurs as vaccination coverage increases could, in part, be attributed to a general reduction in cases over the 2021 summer months. There was a peak in cases during winter 2021, and it is clear that many of the cases occurred in vaccinated individuals, but this is not evidence that vaccines do not have a protective effect. Rather, it reflects that a large part of the population was vaccinated by this time. The peak in winter 2021 can be attributed to the emergence of the new Omicron virus variant that was first detected in November 2021. This variant spreads more easily than earlier variants, even in vaccinated individuals. The number of COVID-19 cases presented in the graph below, and the number of ICU admissions in the graph in the section above, do not consider equivalent populations. However, considering both datasets together does provide some insights into the protective effect of vaccines. Specifically, each peak in COVID-19 cases in patients with each of the comorbidities prior to summer 2021 is clearly reflected in the number of ICU admissions in the adult population of Sweden. By contrast, this Omicron peak in cases is not reflected in a peak in ICU admissions. This is evidence that vaccines were protective against the onset of the more severe symptoms. A protective effect has also been confirmed in many studies. Ideally, studies considering a protective effect should directly compare COVID-19 cases and vaccine coverage in a manner that accounts for age-group and time point.

##### Visualisations

The graphs below have multiple interactive features. It is possible to see all of the data available for a given comorbidity for clicking on the corresponding button. The 'Align timeline' button will change the timeframe shown so that only the time period that is common between the two graphs is shown. The 'Show all data' button can be used to see all of the available data for both datasets (the timelines of the two are not the same).

<div id="dwbuttonstwo"><button class="btn btn-secondary" type="button" data-bs-toggle="collapse" data-bs-target="#vis_instr_two" aria-expanded="False" aria-controls="mandatorycollapse">
    Click here for more detailed instructions on using the features of the graphs
</button>
</div>
<div class="collapse" id="vis_instr_two">
  <div class="card card-body">
        <span>

The two plots in this subsection have multiple interactive features. The buttons associated with these plots affect both plots, but other changes can be made independently.

##### View data for a specific comorbidity

Click on the button corresponding to the cormorbidity of interest to display data about that cormorbidity on both graphs.

##### Changing the timeframe displayed

The two graphs are shown on different time scales. This is partly because vaccinations were not made available until early 2021, whilst data on COVID-19 infection are available from March 2020. Further, the latest data available can differ between data types.

The default view will show all of the data available for both datasets. However, it is useful for align the timeframes, especially when making inferences about the effects of vaccination on COVID-19 cases. Use the 'Align timeframe' button in the 'Timeframe' buttons list to align the timeframes. Click the 'Show all data' button to view all of the available data.

##### Accurately read data values

It is possible to view the underlying data values by hovering the cursor over the graph. All values for a given date are shown together.

##### Other features

When hovering over the plot with the cursor, additional grey icons appear in the top right. The +, -, and magnifying glass icons can be used to zoom in/out of the plot. Alternatively, it is possible to zoom into a given part of the graph by clicking and dragging with the cursor to select that portion. The autoscale and reset axes icons (which look like a box containing arrows and a house, respectively) can be used to scale the axes appropriately for the data selected. The plot can be downloaded in .png format by clicking on the camera icon.
</span>

  </div>
</div>

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
    <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/comorbs_subplot_button.json" height="800px" >}}</div>
</div>

**Code used to produce plots:** [Preparation of COVID-19 case data](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/RECOVAC/comorbidity_cases_dataprep.py), [Preparation of vaccination coverage data](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/RECOVAC/comorbidity_vaccinecov_dataprep.py), [Graph containing subplots](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/RECOVAC/comorbidity_subplots_wbuttons.py).

## Determinants of vaccination

The rapid development of COVID-19 vaccination and high vaccination coverage have been crucial in mitigating the societal effects of the COVID-19 pandemic. Two recently published articles by Spetz and colleagues ([Spetz _et al._ (2022a)](https://www.sciencedirect.com/science/article/pii/S2666776222000242?via%3Dihub) and [Spetz _et al._ (2022b)](https://www.sciencedirect.com/science/article/pii/S0264410X22011860)) at Gothenburg University used registry-based data to examine sociodemographic determinants of vaccination coverage. In brief, although the overall vaccination coverage in Sweden was over 82%, vaccination was lower among certain demographic groups. Specifically, vaccination coverage was lower among younger individuals, those on low incomes, those born outside of Sweden, and males. Individuals born in a low- or middle-income countries were found to be six times less likely to be vaccinated than individuals born in Sweden.  When considering the whole working age population (18-64 years), vaccination coverage varied extensively between different subgroups, as defined by the factors studied, from 32% to 96%. Similar results were seen in the older population (65 years of age and older). These results indicate that taking social factors into consideration is important in future health and vaccination efforts. Read more about these findings in [Spetz _et al._ (2022a)](https://www.sciencedirect.com/science/article/pii/S2666776222000242?via%3Dihub) and [Spetz _et al._ (2022b)](https://www.sciencedirect.com/science/article/pii/S0264410X22011860).

## Vaccine effectiveness

Using long-term data about the Swedish general population from RECOVAC, [Xu _et al._ (2022)](https://doi.org/10.3390/vaccines10122074) provided a more detailed insight into time-varying vaccine effectiveness (VE) against COVID-19 infection, hospitalisation, ICU admission, and death up to 13 months after vaccination. Two vaccine doses offered good, long-lasting protection against infection before the Omicron variant emerged (VE above 85% for all time intervals), but more limited protection against infection with the Omicron variant. For severe COVID-19 outcomes, however, high VE was observed during the entire follow-up period with better protection among individuals above age 65. For more details, see [Xu _et al._ (2022)](https://doi.org/10.3390/vaccines10122074).

## Contact information

Prof Fredrik Nyberg, Project Leader and Professor of Register Epidemiology, School of Public Health and Community Medicine, Institute of Medicine, Gothenburg University. Email: [fredrik.nyberg.2@gu.se](mailto:fredrik.nyberg.2@gu.se).

You are also welcome to use the general email addresses for the projects:
[recovac@gu.se](recovac@gu.se) or [scifipearl@medicin.gu.se](mailto:scifipearl@medicin.gu.se)

## Funders

Funding directly related to RECOVAC and vaccine research from SciLifeLab / Knut and Alice Wallenbergs Foundation,Swedish Research Council. The broader SCIFI-PEARL project also has core and other major COVID-19-related funding from ALF funding, Formas, Swedish Heart-Lung Foundation, Social Insurance Agency (Försäkringskassan).

## Data availability

Researchers interested in collaborating around scientific analyses using data from **the RECOVAC / SCIFI-PEARL project database** should contact the project for a discussion. We are open to broad collaborations, as we are keen to see the data used as much as possible for purposes of scientific and public interest, within the boundaries of ethics approvals. Current ethics approvals cover scientific topics broadly related to healthcare and societal aspects of COVID-19 and/or COVID-19 vaccination, and may be possible to update if required for new topics.

The data in this study are pseudonymized individual-level data from Swedish healthcare registers and have been compiled for the scientific purposes of the RECOVAC and SCIFI-PEARL project, as they are available from the respective Swedish public data holders on the basis of ethics approval for the research in question, subject to relevant legislation, processes and data protection.

We will consider proposals for collaboration in a positive vein, based on an assessment of their interest and importance, fit with the project and realistic possibility of implementing (especially given internal resource within the project). We actively seek and encourage cross-functional collaboration and invite new ideas and expertise. Collaborations will be structured as sub projects under **SCIFI-PEARL/RECOVAC** and the existing PI and leadership, in accordance with existing ethics approvals. Arrangements for data access, cost sharing and collaboration support from core project staff and resource will be discussed on a case by case basis. Data will not be shared outside of our protected data environments.
Before you contact us, think carefully through the aims for the collaboration with **SCIFI-PEARL / RECOVAC** that you wish to initiate. Please attach a project idea / subproject synopsis or preliminary project plan. You can use your own format, or the template available here if you wish. We cannot finance research projects, but are open to collaborate in funding applications.

_For more information, please contact those involved with the project using the contact details [above](/dashboards/recovac/#contact-information)._

## Publications and Preprints

Below is a list of publications and preprints from this group. Please see the [SCIFI-PEARL webpage](https://www.gu.se/forskning/scifi-pearl) for a more comprehensive overview of outputs (e.g. lists of conference abstracts and recently submitted articles). The publication lists on that page are also updated more regularly (weekly) than the list below.

- Xu, Y., Li, H., Kirui, B., Santosa, A., Gisslen, M., Leach, S., Wettermark, B., Vanfleteren, L. E. G. W., Nyberg, F. (2022). Effectiveness of COVID-19 Vaccines Over 13 Months Covering the Period of the Emergence of the Omicron Variant in the Swedish Population. _Available at SSRN as a preprint:_ [https://doi.org/10.3390/vaccines10122074](https://doi.org/10.3390/vaccines10122074)

- Spetz, M., Lundberg, L., Nwaru, C., Li, H., Santosa, A., Ng, N., Leach, S., Gisslén, M., Hammar, N., Nyberg, F., Rosvall, M. (2022) An intersectional analysis of sociodemographic disparities in Covid-19 vaccination: a nationwide register-based study in Sweden. _Vaccine, 40_, 6640-6648. [https://doi.org/10.1016/j.vaccine.2022.09.065](https://doi.org/10.1016/j.vaccine.2022.09.065)

- Mousa, S. I., Nyberg, F., Hajiebrahimi, M., Bertilsson, R., Nåtman, J., Santosa, A., Wettermark, B. (2022). Initiation of antihypertensive drugs to patients with confirmed COVID-19-A population-based cohort study in Sweden. _Basic & Clinical Pharmacology & Toxicology, 131_, 196-204. [https://doi.org/10.1111/bcpt.13766](https://doi.org/10.1111/bcpt.13766)

- Sundh, J., Ekström, M., Palm, A., Ljunggren, M., Emilsson, Ö. I., Grote, L., Cajander, S., Li, H., Nyberg, F. (2022). COVID-19 and Risk of Oxygen-dependent Chronic Respiratory Failure: A National Cohort Study. _American Journal of Respiratory and Critical Care Medicine, 206_ 506-509. [https://doi.org/10.1164/rccm.202202-0323le](https://doi.org/10.1164/rccm.202202-0323le)

- Spetz, M., Lundberg, L., Nwaru, C., Li, H., Santosa, A., Leach, S., Gisslén, M., Hammar, N., Rosvall, M., Nyberg, F. (2022). The social patterning of Covid-19 vaccine uptake in older adults: A register-based cross-sectional study in Sweden. _The Lancet Regional Health - Europe, 15,_ 100331. [https://doi.org/10.1016/j.lanepe.2022.100331](https://doi.org/10.1016/j.lanepe.2022.100331)

- Santosa, A., Franzén, S., Nåtman, J., Wettermark, B., Parmryd, I., Nyberg, F. (2022). Protective effects of statins on COVID-19 risk, severity and fatal outcome – a nationwide Swedish cohort study. _Research Square_ [https://doi.org/10.21203/rs.3.rs-1432508/v1](https://doi.org/10.21203/rs.3.rs-1432508/v1)

- Nwaru, C.A., Santosa, A., Franzén, S., Nyberg, F. (2022). Occupation and COVID-19 diagnosis, hospitalisation and ICU admission among foreign-born and Swedish-born employees: a register-based study. _Journal of Epidemiology and Community Health, 7,_ jech-2021-218278. [https://doi.org/10.1136/jech-2021-218278](https://doi.org/10.1136/jech-2021-218278)

- Nyberg, F., Franzén, S., Lindh, M., Vanfleteren, L., Hammar, N., Wettermark, B., Sundström, J., Santosa, A., Björck, S., Gisslén, M. (2021). Swedish Covid-19 Investigation for Future Insights – A Population Epidemiology Approach Using Register Linkage (SCIFI-PEARL). _Clinical Epidemiology, 13,_ 649-659. [https://doi.org/10.2147/CLEP.S312742](https://doi.org/10.2147/CLEP.S312742)

- Nyberg, F., Lindh, M., Vanfleteren, L., Hammar, N., Wettermark, B., Sundström, J., Santosa, A., Kirui, B. K., Gisslén, M. (2021). Adverse events of special interest for COVID-19 vaccines - background incidences vary by sex, age and time period and are affected by the pandemic. _medRxiv_ [https://doi.org/10.1101/2021.10.04.21263507](https://doi.org/10.1101/2021.10.04.21263507)

## Information about SCIFI-PEARL

The SCIFI-PEARL project ([Swedish COVID-19 Investigation for Future Insights – a Population Epidemiology Approach using Register Linkage](https://www.gu.se/en/research/scifi-pearl)) is a multi-register observational study that uses register-based data to answer questions related to COVID-19. The project will investigate, for example, the risk factors likely to lead to an unfavourable prognosis, and whether aspects of comorbidity, treatments, or medical history can increase the risk of long-term consequences of COVID-19 infection. The project will also address questions related to public health, such as whether the current pandemic and vaccination programs have affected drug use or healthcare in society at large.

The overall aim of the project is to maintain a continuously updated overview of how COVID-19 affects the Swedish population. To do this, the project uses data from a broad range of national and regional healthcare registers to produce a representative sample of the Swedish population, and use that data to make assessments. Data on individuals is linked between registers using the national personal ID number (personnummer), though personal data is pseudonymised following linkage. This, together with regular updates of data related to SARS CoV-2/COVID-19, will enable a longitudinal view of the COVID-19 pandemic.

The SCIFI-PEARL project links multiple different types of data from various sources, including: COVID-19 test data from the national database of notifiable infectious diseases [SmiNet](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/overvakning-och-rapportering/sminet), vaccination data from the [National Vaccination Register](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/vaccinationer/nationella-vaccinationsregistret/), data from the [National Patient Register](https://www.socialstyrelsen.se/en/statistics-and-data/registers/national-patient-register/), the [Swedish Prescribed Drug Register](https://www.socialstyrelsen.se/en/statistics-and-data/registers/national-prescribed-drug-register/), [National Cancer Register](https://www.socialstyrelsen.se/en/statistics-and-data/registers/national-cancer-register/), regional health databases with primary care data from the two largest regions in Sweden, as well as data from a range of quality registers including the Swedish Intensive Care Register and a range of disease-specific registers with disease-specific clinical information.

See also the [project page](https://www.gu.se/en/research/scifi-pearl) for more details.
