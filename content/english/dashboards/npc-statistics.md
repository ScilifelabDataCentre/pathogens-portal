---
title: National Pandemic Centre SARS-CoV-2 (COVID-19) test statistics
description: The national Pandemic Centre (NPC) conducted testing related to SARS-CoV-2 from the start of the pandemic. They show positive, negative, and inconclusive tests. This dashboard is historic, so no longer updated.
banner: /dashboard_thumbs/NPC_logo.png
banner_border: true
menu:
     dashboard_menu:
        identifier: npc-statistics
        name: "National Pandemic Centre (Historic)"
toc: false
plotly: true
aliases:
    - /data_types/health_data/npc-statistics/
dashboards_topics: [COVID-19, Infectious diseases]
---

<div class="alert alert-info small">
  <p><i class="bi bi-exclamation-triangle-fill"></i>The National Pandemic Centre (NPC) at Karolinska Institute ceased operations of high throughput PCR diagnostics on 2020-12-21.</p>
  <p><span class="font-weight-bold">The data presented here is no longer updated</span> but is kept for historical reference.</p>
  <a class="dark-blue" href="https://nyheter.ki.se/covid-19-tester-ki-atergar-till-ordinarie-laboratorieverksamhet-men-har-fortsatt-beredskap">KI Press Release</a>
</div>

The dataset visualised in the graphs on this page is available [here](https://blobserver.dc.scilifelab.se/blob/NPC-statistics-data-set.csv). The numbers reported here were compiled automatically and, as such, might not correspond to the numbers reported through other sources for different reasons.

#### Total NPC test numbers

The total number of SARS-CoV-2 (COVID-19) tests conducted at the national Pandemic Centre (NPC) since the start of the pandemic, separated according to whether the results were positive, negative, or invalid/inconclusive.

Source code for the below graph is available [here](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_total_tests.py).

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

 <div class="plot_wrapper mb-3">
    <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_total_tests.json" height="200px">}}</div>
</div>

#### NPC test numbers

The number of SARS-CoV-2 (COVID-19) tests ran daily or weekly, divided according to whether results were positive, negative, or invalid/inconclusive.

Source code is available for both the [daily](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_tests_daily.py) and [weekly](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_tests_weekly.py) graphs below.

##### Daily

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_tests_daily.json" height="350px">}}</div>
</div>

##### Weekly

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_tests_weekly.json" height="350px">}}</div>
</div>

#### NPC tests positive fraction

The fraction of daily or weekly SARS-CoV-2 (COVID-19) tests that were positive,
as percentage of all tests conducted **(excluding invalid/inconclusive)**.

Source code is available for both the [daily](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_positiveTests_fraction_daily.py) and [weekly](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_positiveTests_fraction_weekly.py) graphs below.

##### Daily

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_positiveTests_fraction_daily.json" height="350px">}}</div>
</div>

##### Weekly

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_positiveTests_fraction_weekly.json" height="350px">}}</div>
</div>

#### Cumulative NPC test numbers

The sum of all SARS-CoV-2 (COVID-19) virus tests conducted at NPC since the
start of the pandemic, as a function of date, and divided according to whether results were positive, negative, or invalid/inconclusive.

Source code for the below graph is available [here](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_cumulative_tests.py).

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_cumulative_tests.json" height="550px">}}</div>
</div>

The National Pandemic Centre (NPC) was a facility for [SARS-CoV-2 (COVID-19) testing](https://ki.se/mtc/ctmr-and-covid-19) established within the [Centre for Translational Microbiome Research (CTMR)](https://ki.se/en/research/centre-for-translational-microbiome-research-ctmr) at [Karolinska Institutet (KI)](https://ki.se/en)/[SciLifeLab](https://www.scilifelab.se/). At the end of March 2020, the large-scale microbiome research lab was quickly converted into a centre to assist Sweden with analysing SARS-CoV-2 tests. This was made possible by a donation from the [Knut and Alice Wallenberg Foundation (KAW)](https://kaw.wallenberg.org/en) and a previously established collaboration with [MGI Tech](https://en.mgitech.cn/) in Shenzen, China. The NPC initially helped to expand the RNA-extraction capacity at Karolinska Universitets laboratoriet. However, it quickly expanded into a facility that increased the testing capacity across all regions of Sweden.

The final capacity of the National Pandemic Centre at KI/SciLifeLab was approximately 10,000 tests per day. The results were typically returned within 24 hours of the sample arriving to the lab. NPC exclusively performed PCR-based analyses, not serological (antibody-based) analyses.
