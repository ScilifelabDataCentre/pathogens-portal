---
title: Dashboards
toc: false
plotly: true
menu:
    homepage_dashboards:
        name: Dashboards
        identifier: dashboards
        post: Visualisations of datasets as well as an overview of ongoing research on a particular question. <a href="/dashboards/">See all dashboards <i class="bi bi-arrow-right-circle-fill"></i></a>
---

<h4><a href="serology-statistics/">SARS-CoV-2 antibody tests at SciLifeLab <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

The SciLifeLab Autoimmunity and Serology profiling facility has been conducting testing for SARS-CoV-2 antibodies since the start of the COVID-19 pandemic. The vast majority of samples analysed so far have been collected from health care personnel and within population based studies as well as from personnel in the pharmaceutical and biotechnology industry and also within a long range of research collaborations. This dashboard displays the total number of tests conducted, positive and negative test results over time.

<div class="row">
  <div class="container d-md-none"><div class="alert alert-info">Scroll the plot sideways to view all data.</div></div>
  <div class="table-responsive" id="serology"></div>
</div>

<a href="serology-statistics/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<hr>

<h4><a href="wastewater/">The amount of SARS-CoV-2 virus in wastewater in cities across Sweden <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

Wastewater surveillance could prove an effective system for monitoring COVID-19 prevalence and act as an early warning system for predicting upcoming outbreaks. In this dashboard, we present weekly wastewater epidemiology data from various Swedish cities which have a total population of over 2.5 million people (over 25% of the population of Swden). The data presented here originates from analyses conducted by the Swedish Environmental Epidemiology Center (SEEC). Data available from: Stockholm, Malmö, Uppsala, Umeå, Örebro, Kalmar, and other municipalities.

<div class="container d-md-none"><div class="alert alert-info">Scroll the plot sideways to view all data.</div></div>
<div class="table-responsive" id="stockholm_wastewater"></div>

<a href="wastewater/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<hr>

<h4><a href="vaccines/">The administration and study of COVID-19 vaccines in Sweden <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

This dashboard is focussed on vaccine research. We visualise information about the amount of people (across different regions, different age groups, or in Sweden generally) that have received one, two, or three doses of vaccination. The section also displays ongoing Swedish research projects related to vaccine research. These projects are focussed broadly on vaccines and, as such, they include life science projects, registery-based projects, and public health projects. We also show a subset of publications related to vaccine research by researchers affiliated with a Swedish University or Research Institute.

<div class="row">
  <div class="container d-md-none"><div class="alert alert-info">Scroll the plot sideways to view all data.</div></div>
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

<h4><a href="/dashboards/recovac/">RECOVAC <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

This dashboard was produced in collaboration with the group behind register-based large-scale national population study to monitor COVID-19 vaccination effectiveness and safety (RECOVAC). The section contains information about what the RECOVAC project involves, how others may access the data, and initial publications, among other things. Visualisations are available on certain elements of the data collated by the project.

<div class="row">
  <div class="container d-md-none"><div class="alert alert-info">Scroll the plot sideways to view all data.</div></div>
  <div class="table-responsive">
    <div id="https://blobserver.dckube.scilifelab.se/blob/ICUadmiss_small.json" class="plotly"
      style="width:600px;height:300px"></div>
  </div>
  <script>
    Plotly.d3.json('https://blobserver.dckube.scilifelab.se/blob/ICUadmiss_small.json', function (err, fig) {
      Plotly.plot('https://blobserver.dckube.scilifelab.se/blob/ICUadmiss_small.json', fig.data, fig.layout, { responsive: true });
    });
  </script>
</div>

<a href="/dashboards/recovac/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<hr>

<h4><a href="post_covid/">Post COVID-19 condition in Sweden <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

In this dashboard, you can find visualisations of data related to Post COVID-19 condition in Sweden from The Swedish Board of Health and Welfare (Socialstyrelsen), an overview of ongoing Post COVID-19 condition research projects in Sweden, and scientific publications regarding Post COVID-19 condition by researchers affiliated with Swedish universities or research institutes.

<div class="container d-md-none"><div class="alert alert-info">Scroll the plot sideways to view all data.</div></div>
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

In this section of the Portal, we summarise information about publications on COVID-19 and SARS-CoV-2 that involve at least contributor from a Swedish university or research institute. Here, you will see a timeline regarding the number of publications, as well as keywords/phrases from multiple subsets of publications. We also have a <a href="/publications/">dedicated page</a> where we show a database of Swedish COVID-19 and SARS-CoV-2 publications.

<a href="/dashboards/covid_publications/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<hr>

<h4>Partner dashboard: <a href="crush_covid/">CRUSH Covid <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

CRUSH Covid maps outbreaks in Uppsala County by visualizing the number of cases, test positivity, geographic distribution, age distribution, etc. Data on positivity per postal code is available for download and further re-use.

<a href="https://crush-covid.shinyapps.io/crush_covid/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<hr>

<h4>Partner dashboard: <a href="symptom_study_sweden/">COVID Symptom Study Sweden <i class="bi bi-arrow-right-circle-fill"></i></a></h4>

CSSS continuously collects data on COVID-19 prevalence, symptoms, and vaccinations through a smartphone app with over 200.000 users in Sweden. Collected raw data <a href="https://www.covid19app.lu.se/forskare">can be requested for use in research projects</a>.

<a href="https://csss-resultat.shinyapps.io/csss_dashboard/">See the full dashboard <i class="bi bi-arrow-right-circle-fill"></i></a>

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/e4c6a7b8bff648a5adaabbdd3d994bf9.js?id=serology"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/93bad55e86ad4b0f97d4d27c77862bc9.js?id=stockholm_wastewater"></script>
