---
title: Dashboards
toc: false
plotly: true
menu:
    swe_menu:
        identifier: dashboards
        name: Dashboards
        weight: 20
    homepage_dashboards:
        name: Dashboards
        identifier: dashboards
        post: Visualiseringar av datasets samt en översikt över pågående forskning kring en viss fråga. <a href="/sv/dashboards/">Se alla dashboards <i class="bi bi-arrow-right-circle-fill"></i></a>
---

<div class="alert alert-info">
  <i class="bi bi-exclamation-triangle-fill"></i>
  <span>En svensk översättning av denna sida kommer inom kort.</span>
</div>

<h4><a href="serology-statistics/">SARS-CoV-2 antibody tests at SciLifeLab <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

The SciLifeLab Autoimmunity and Serology profiling facility has been conducting testing for SARS-CoV-2 antibodies since the start of the COVID-19 pandemic. The vast majority of samples analysed so far have been collected from health care personnel and within population based studies as well as from personnel in the pharmaceutical and biotechnology industry and also within a long range of research collaborations. This dashboard displays the total number of tests conducted, positive and negative test results over time.

<div class="row">
  <div class="container d-md-none"><div class="alert alert-info">Skrolla grafen horisontellt för att se alla data.</div></div>
  <div class="table-responsive" id="serology"></div>
</div>

<a href="serology-statistics/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<hr>

<h4><a href="wastewater/">The amount of SARS-CoV-2 virus in wastewater in cities across Sweden <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

Wastewater surveillance could prove an effective system for monitoring COVID-19 prevalence and act as an early warning system for predicting upcoming outbreaks. In this dashboard, we present weekly wastewater epidemiology data from various Swedish cities which have a total population of over 2.5 million people (over 25% of the population of Swden). The data presented here originates from analyses conducted by the Swedish Environmental Epidemiology Center (SEEC). Data available from: Stockholm, Malmö, Uppsala, Umeå, Örebro, Kalmar, and other municipalities.

<div class="container d-md-none"><div class="alert alert-info">Skrolla grafen horisontellt för att se alla data.</div></div>
<div class="table-responsive" id="stockholm_wastewater"></div>

<a href="wastewater/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<hr>

<h4><a href="vaccines/">The administration and study of COVID-19 vaccines in Sweden <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

This dashboard is focussed on vaccine research. We visualise information about the amount of people (across different regions, different age groups, or in Sweden generally) that have received one, two, or three doses of vaccination. The section also displays ongoing Swedish research projects related to vaccine research. These projects are focussed broadly on vaccines and, as such, they include life science projects, registery-based projects, and public health projects. We also show a subset of publications related to vaccine research by researchers affiliated with a Swedish University or Research Institute.

<div class="row">
  <div class="container d-md-none"><div class="alert alert-info">Skrolla grafen horisontellt för att se alla data.</div></div>
  <div class="table-responsive">
    <div id="https://blobserver.dckube.scilifelab.se/blob/vaccine_heatmap_small.json" class="plotly"
      style="width:600px;height:300px"></div>
  </div>
  <script>
    Plotly.d3.json('https://blobserver.dckube.scilifelab.se/blob/vaccine_heatmap_small.json', function (err, fig) {
      Plotly.plot('https://blobserver.dckube.scilifelab.se/blob/vaccine_heatmap_small.json', fig.data, fig.layout, { responsive: true });
    });
  </script>
</div>

<a href="vaccines/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<hr>

<h4><a href="post_covid/">Post COVID-19 condition in Sweden <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

In this dashboard, you can find visualisations of data related to Post COVID-19 condition in Sweden from The Swedish Board of Health and Welfare (Socialstyrelsen), an overview of ongoing Post COVID-19 condition research projects in Sweden, and scientific publications regarding Post COVID-19 condition by researchers affiliated with Swedish universities or research institutes.

<div class="container d-md-none"><div class="alert alert-info">Skrolla grafen horisontellt för att se alla data.</div></div>
<div class="table-responsive">
              <div id="https://blobserver.dckube.scilifelab.se/blob/weeklycontacts_healthcare_small.json" class="plotly"
                style="width:600px;height:300px"></div>
            </div>
            <script>
              Plotly.d3.json('https://blobserver.dckube.scilifelab.se/blob/weeklycontacts_healthcare_small.json', function (err, fig) {
                Plotly.plot('https://blobserver.dckube.scilifelab.se/blob/weeklycontacts_healthcare_small.json', fig.data, fig.layout, { responsive: true });
              });
            </script>

<a href="post_covid/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<hr>

<h4><a href="/dashboards/covid_publications/">Overview of Swedish COVID-19 publications<i class="bi bi-arrow-right-circle-fill"></i></a></h4>

I denna sektion visas information om Covid-19/SARS-CoV-2 publikationer med minst en medförfattare affilierad till ett svenskt lärosäte. Här visas tidslinjer både för antal publikationer och sökord. För att söka artiklar i COVID-19 publikationsdatabasen se <a href="/publications/">här</a>.

<a href="/dashboards/covid_publications/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<hr>

<h4>Partner dashboard: <a href="crush_covid/">CRUSH Covid <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

CRUSH Covid kartlägger SARS-COV-2 utbrott i Region Uppsala genom att visualisera antal prover som tagits, antal positiva prover, geografisk distribution, åldersfördelning mm. Data över antal positiva fall i ett visst postnummerområde finns tillgängligt för datadelning och återanvändning av data.

<a href="https://crush-covid.shinyapps.io/crush_covid/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<hr>

<h4>Partner dashboard: <a href="symptom_study_sweden/">COVID Symptom Study Sweden <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

CSSS samlar kontinuerligt in data om Covid-19 förekomste, symptom, och vaccinationer med hjälp av en smartphone app med över 200.000 användare i Sverige. Insamlade rådata <a href="https://www.covid19app.lu.se/forskare">kan görs tillgängliga för forskningsprojekt</a>.

<a href="https://csss-resultat.shinyapps.io/csss_dashboard/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/e4c6a7b8bff648a5adaabbdd3d994bf9.js?id=serology"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/93bad55e86ad4b0f97d4d27c77862bc9.js?id=stockholm_wastewater"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/530ca62cc6f7449680793a252155fee3.js?id=postcovid_halthcare_contacts"></script>
