---
title: COVID Symptom Study Sweden
toc: false
plotly: true
---

**COVID Symptom Study Sweden** is a national research initiative for large-scale data collection and analysis of symptoms, exposure, and risk factors associated with the COVID-19 infection. The project is run by Lund University and Uppsala University in collaboration with King’s College London and Zoe Global Ltd. COVID Symptom Study Sweden is led by prof. Paul Franks and prof. Maria Gomez (Lund University) as well as prof. Tove Fall (Uppsala University).

[COVID Symptom Study Sweden](https://www.covid19app.lu.se/) uses a non-commercial app for data collection from volunteer study participants. Anyone 18 years or older living in Sweden can participate in the study. As of March 2021, COVID Symptom Study Sweden has over 206,000 participants and accumulated over 12 million data points.

COVID Symptom Study Sweden has two main objectives. The first objective is to investigate temporal and geographical trends in SARS-CoV-2 spread as well as how changes in the regional/national strategies affect the spread. The second objective of the project is to increase understanding of which groups are most likely to be affected by COVID-19, how the disease manifests in terms of symptoms, and the relationship between risk factors and (combinations of) symptoms. The researchers also plan to investigate whether risk factors vary in different stages of infection (early vs. late) as well as the effect of vaccination.

#### Estimated prevalence of symptomatic cases (updated daily)

<div class="alert alert-info">Last updated: {{% csss_date_modified %}}.</div>

Below are estimates of the prevalence of symptomatic COVID-19 cases in various counties in Sweden. The estimates are made based on the app users' data using the prediction model developed by the team of researchers behind the COVID Symptoms Study Sweden; see [this page](https://www.covid19app.lu.se/artikel/uppdatering-av-prediktionsmodell-0) for more information about the prediction model (only available in Swedish). More detailed prevalence estimates and other results can be explored [on the official dashboard of the project results](https://csss-resultat.shinyapps.io/csss_dashboard/).

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/symptoms_map_english.json" height="500px" >}}</div>
</div>

#### Access to the collected data for use in other research projects

While estimates of symptomatic COVID-19 prevalence and basic demographic information about study participants are available through the project results dashboard and an R package, sharing of raw data with external researchers requires a corresponding ethical permit and a data transfer agreement. The researchers behind COVID Symptom Study Sweden welcome applications for data access. Please [see this page for more information on how to apply](https://www.covid19app.lu.se/forskare) (only available in Swedish).

For more information, please visit [covid19app.lu.se](https://www.covid19app.lu.se/).  
For questions about the study, please contact [covid-symptom-study@med.lu.se](mailto:covid-symptom-study@med.lu.se).

#### Publications

* Kennedy, B., Fitipaldi, H., Hammar, U., Maziarz, M., Tsereteli, N., Oskolkov, N., Varotsis, G., Franks, C. A., Spiliopoulos, L., Adami, H-.O., Björk, J., Engblom, S., Fall, K., Grimby-Ekman, A., Litton, J-.E., Martinell, M., Oudin, A., Sjöström, T., Timpka, T., Sudre, C. H., Graham, M. S., du Cadet, J. L, Chan, A. T., Davies, R., Ganesh, S., May, A., Ourselin, S., Pujol, J. C., Selvachandran, S., Wolf, J., Spector, T. D., Steves, C. J., Gomez, M. F., Franks, P. W., Fall T. App-based COVID-19 surveillance and prediction: The COVID Symptom Study Sweden. *MedRxiv* (2021). [https://doi.org/10.1101/2021.06.16.21258691](https://doi.org/10.1101/2021.06.16.21258691)

* Sudre, C. H., Murray, B., Varsavsky, T., Graham, M. S., Penfold, R. S., Bowyer, R. C., Capdevila Pujol, J., Klaser, K., Antonelli, M., Canas, L. S., Molteni, E., Modat, M., Cardoso, M. J., May, A., Ganesh, S.,Davies, R., Nguyen, L. H., Drew, D. A., Astley, C. M., Joshi, A. D., Merino, J., Tsereteli, N., Fall, T., Gomez, M. F., Duncan, E. L., Menni, C., Williams, F. M. K., Franks, P. W., Chan, A. T., Wolf, J., Ourselin, S., Spector, T., Steves, C. J. Attributes and predictors of long COVID. *Nature Medicine* **27**, 626-631 (2021). [https://doi.org/10.1038/s41591-021-01292-y](https://doi.org/10.1038/s41591-021-01292-y)
