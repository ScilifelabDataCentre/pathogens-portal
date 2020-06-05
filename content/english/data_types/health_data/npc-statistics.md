---
title: National Pandemic Centre Covid-19 test statistics
menu:
    main:
        identifier: npc-statistics
        parent: health_data
        weight: 10
---

The National Pandemic Centre (NPC) is a lab for
[Covid-19 testing](https://ki.se/mtc/ctmr-and-covid-19) set up within the
[Centre for Translational Microbiome Research (CTMR)](https://ki.se/en/research/centre-for-translational-microbiome-research-ctmr)
at [Karolinska Institutet (KI)](https://ki.se/en) and was financed by the
[Knut and Alice Wallenberg Foundation (KAW)](https://kaw.wallenberg.org/en).

#### Daily NPC test results

<div class="d-md-none alert alert-info">Scroll the plot sideways to view all data</div>

<div class="plot_wrapper"><div id="stacked-bar-chart"></div></div>

#### Cumulative NPC test numbers

<div class="d-md-none alert alert-info">Scroll the plot sideways to view all data</div>

<div class="plot_wrapper"><div id="cumulative-plot"></div></div>

The aggregated statistics for the PCR-based tests are shown in the graphs.
The term "failed" indicates a test that was inconclusive or invalid
for technical reasons.

The dataset visualized in the graphs is available
[here](https://datagraphics.dckube.scilifelab.se/dataset/65c5d7e6b505420c98714a4b348bafbb) and is updated daily.
The source code for the graphs are
[here for the stacked bar chart](https://datagraphics.dckube.scilifelab.se/graphic/85c0a41fb118495e88a1fccad37e821e)
and [here for the cumulative plot](https://datagraphics.dckube.scilifelab.se/graphic/aa9e90ed7a5445a0bf70f0b81da2325e).

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.12.2"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/85c0a41fb118495e88a1fccad37e821e.js?id=stacked-bar-chart"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/aa9e90ed7a5445a0bf70f0b81da2325e.js?id=cumulative-plot"></script>
