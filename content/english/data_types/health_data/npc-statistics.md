---
title: National Pandemic Centre Covid-19 test statistics
menu:
    main:
        identifier: npc-statistics
        parent: health_data
        weight: 10
---

#### Daily NPC test results

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div id="stacked-bar-chart"></div>
</div>

#### Cumulative NPC test numbers

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div id="cumulative-plot"></div>
</div>

The National Pandemic Centre (NPC) is a lab for
[Covid-19 testing](https://ki.se/mtc/ctmr-and-covid-19) set up within the
[Centre for Translational Microbiome Research (CTMR)](https://ki.se/en/research/centre-for-translational-microbiome-research-ctmr)
at [Karolinska Institutet (KI)](https://ki.se/en)/
[SciLifeLab](https://www.scilifelab.se/).
At the end of March 202 the large-scale microbiome research lab was
quickly converted into a center that can assist Sweden in
analyzing SARS-CoV-2 tests.
This was made possible through a donation by the
[Knut and Alice Wallenberg Foundation (KAW)](https://kaw.wallenberg.org/en)
in combination with a previously established collaboration with
[MGI Tech.](https://en.mgitech.cn/) in Shenzen, China.
Initially providing assistance with RNA-extraction capacity to
Karolinska Universitetslaboratoriet, the National Pandemic Center
at KI/SciLifeLab quickly expanded into providing a facility providing
increased SARS-CoV-2 testing capacity to all regions of Sweden.

The current capacity of the National Pandemic Center at KI/SciLifeLab is
approximately 5000 test per day, with results typically returned within
24 hours from the sample arriving to the lab.

These numbers are compiled automatically and might not correspond to
the numbers reported through other sources for different reasons.
The data are updated once daily, and backdated changes to numbers might occur.

The dataset visualized in the graphs is available
[here](https://datagraphics.dckube.scilifelab.se/dataset/bbbaf64a25a1452287a8630503f07418) and is updated daily.
The source code for the graphs are
[here for the stacked bar chart](https://datagraphics.dckube.scilifelab.se/graphic/ddb1119aefce47d58d0b3a49e98b4fcc)
and [here for the cumulative plot](https://datagraphics.dckube.scilifelab.se/graphic/e823c75ee55849e7999da56c6c869c7a).

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.12.2"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/ddb1119aefce47d58d0b3a49e98b4fcc.js?id=stacked-bar-chart"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/e823c75ee55849e7999da56c6c869c7a.js?id=cumulative-plot"></script>
