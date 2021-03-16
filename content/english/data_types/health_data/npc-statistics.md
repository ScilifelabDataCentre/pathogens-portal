---
title: National Pandemic Centre SARS-CoV-2 (COVID-19) test statistics
menu:
    main:
        identifier: npc-statistics
        parent: health_data
        weight: 10
toc: false
---

<div class="alert alert-info small">
  <p><i class="fas fa-exclamation-triangle"></i>The National Pandemic Center (NPC) at Karolinska Institute ceased operations of high throughput PCR diagnostics on 2020-12-21.</p>
  <p><span class="font-weight-bold">The data presented here receives no further updates</span> and only remains for historical reference.</p>
  <a href="https://nyheter.ki.se/covid-19-tester-ki-atergar-till-ordinarie-laboratorieverksamhet-men-har-fortsatt-beredskap">KI Press Release</a>
</div>

#### Total NPC test numbers

The total number of SARS-CoV-2 (COVID-19) tests run at NPC since
the start, split up into positive, negative and invalid/inconclusive
results.

<div class="d-lg-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div id="total-numbers-chart"></div>
</div>

#### NPC test numbers

The number of SARS-CoV-2 (COVID-19) tests run daily or weekly, split up into
positive, negative and invalid/inconclusive results.

  <div id="dwbuttons"><button class="btn btn-secondary" type="button" data-toggle="collapse" data-target="#daily_stacked_bar_chart" aria-expanded="true" aria-controls="#daily_stacked_bar_chart">
    Daily
  </button>
  </div>
<div class="collapse show" id="daily_stacked_bar_chart">
  <div class="d-lg-none alert alert-info">
    Scroll the plot sideways to view all data.
  </div>
  <div class="plot_wrapper">
    <div id="stacked-bar-chart"></div>
  </div>
</div>
<div id="dwbuttons">
<button class="btn btn-secondary" type="button" data-toggle="collapse" data-target="#weekly_stacked_bar_chart" aria-expanded="true" aria-controls="weekly_stacked_bar_chart">
  Weekly
</button></div>
<div class="collapse show" id="weekly_stacked_bar_chart">
  <div class="d-lg-none alert alert-info">
    Scroll the plot sideways to view all data.
  </div>
  <div class="plot_wrapper">
    <div id="stacked-bar-chart-weekly"></div>
  </div>
</div>

#### NPC tests positive fraction

The fraction of daily or weekly SARS-CoV-2 (COVID-19) tests that are positive,
as percent of all tests (excluding invalid/inconclusive).

  <div id="dwbuttons"><button class="btn btn-secondary" type="button" data-toggle="collapse" data-target="#daily_positive_bar_chart" aria-expanded="true" aria-controls="#daily_positive_bar_chart">
    Daily
  </button></div>
  <div class="collapse show" id="daily_positive_bar_chart">
      <div class="d-lg-none alert alert-info">
        Scroll the plot sideways to view all data.
      </div>
      <div class="plot_wrapper">
        <div id="positive-bar-chart"></div>
      </div>
      <p class="small"><i>*Note that as the number of reported analyses vary, some days may have a low number of samples, affecting the statistics a lot for that day, e.g. August 24th where only seven samples were reported, all positive.</i></p>
  </div>
  <div id="dwbuttons"><button class="btn btn-secondary" type="button" data-toggle="collapse" data-target="#weekly_positive_bar_chart" aria-expanded="true" aria-controls="weekly_positive_bar_chart">
    Weekly
  </button></div>
  <div class="collapse show" id="weekly_positive_bar_chart">
    <div class="d-lg-none alert alert-info">
      Scroll the plot sideways to view all data.
    </div>
    <div class="plot_wrapper">
      <div id="positive-bar-chart-weekly"></div>
    </div>
  </div>

#### Cumulative NPC test numbers

The sum of all SARS-CoV-2 (COVID-19) virus tests run at NPC since the
start, as a function of date, and split up into positive, negative
and invalid/inconclusive results.

<div class="d-lg-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div id="cumulative-plot"></div>
</div>

NPC was a facility for
[SARS-CoV-2 (COVID-19) testing](https://ki.se/mtc/ctmr-and-covid-19)
set up within the
[Centre for Translational Microbiome Research (CTMR)](https://ki.se/en/research/centre-for-translational-microbiome-research-ctmr)
at
[Karolinska Institutet (KI)](https://ki.se/en)/[SciLifeLab](https://www.scilifelab.se/).
At the end of March 2020 the large-scale microbiome research lab was
quickly converted into a center to assist Sweden in analyzing
SARS-CoV-2 tests. This was made possible through a donation by the
[Knut and Alice Wallenberg Foundation (KAW)](https://kaw.wallenberg.org/en)
in combination with a previously established collaboration with
[MGI Tech](https://en.mgitech.cn/) in Shenzen, China. Initially providing
assistance with RNA-extraction capacity to Karolinska
Universitetslaboratoriet, NPC quickly expanded into providing a
facility providing increased SARS-CoV-2 testing capacity to all
regions of Sweden.

The final capacity of the National Pandemic Center at KI/SciLifeLab
reached approximately 10,000 test per day, with results typically
returned within 24 hours from the sample arriving to the lab. NPC
exclusively performed PCR-based analyses, not serological
(antibody-based) analyses.

These numbers are compiled automatically and might not correspond to
the numbers reported through other sources for different reasons.

The dataset visualized in the graphs is available
[here](https://datagraphics.dckube.scilifelab.se/dataset/bbbaf64a25a1452287a8630503f07418).
The source code for the graphs are
[here](https://datagraphics.dckube.scilifelab.se/graphic/ba0b27320fe74ad0aef59a26be6c37f1),
[here](https://datagraphics.dckube.scilifelab.se/graphic/ddb1119aefce47d58d0b3a49e98b4fcc),
[here](https://datagraphics.dckube.scilifelab.se/graphic/b31c50be59c84c93986c25b052115a65)
and [here](https://datagraphics.dckube.scilifelab.se/graphic/9145856246004419983d39fcf56d9eb6).

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.12.2"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/ba0b27320fe74ad0aef59a26be6c37f1.js?id=total-numbers-chart"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/ddb1119aefce47d58d0b3a49e98b4fcc.js?id=stacked-bar-chart"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/1f2322f4301c4773878c956c578e8caf.js?id=stacked-bar-chart-weekly"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/b31c50be59c84c93986c25b052115a65.js?id=positive-bar-chart"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/9145856246004419983d39fcf56d9eb6.js?id=cumulative-plot"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/7f27ae237b8146a498ab4014aadc35db.js?id=positive-bar-chart-weekly"></script>
