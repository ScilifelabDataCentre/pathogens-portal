---
title: Nationellt Pandemicenter SARS-CoV-2 (covid-19)-analysstatistik
menu:
    main:
        identifier: npc-statistics
        parent: health_data
        weight: 10
aliases:
    - /sv/data_types/health_data/npc-statistics/
---

<div class="alert alert-info small">
  <p><i class="fas fa-exclamation-triangle"></i>Nationellt Pandemiskt center på Karolinska Institutet upphörde med högkapacitets PCR diagnostik 2020-12-21.</p>
  <p><span class="font-weight-bold">Den data som visas här har slutat uppdateras</span> och utgör endast historisk dokumentation.</p>
  <a href="https://nyheter.ki.se/covid-19-tester-ki-atergar-till-ordinarie-laboratorieverksamhet-men-har-fortsatt-beredskap">KIs pressmeddelande</a>
</div>

#### Totala antalet tester vid NPC

Det totala antalet SARS-CoV-2 (covid-19)-virustester analyserade vid NPC
uppdelade på de med positivt, negativt eller icke-avgjort/felaktigt
resultat.

<div class="d-lg-none alert alert-info">
  Skrolla grafen horisontellt för att se all data.
</div>

<div class="plot_wrapper">
  <div id="grand-total-chart"></div>
</div>

#### Antal tester vid NPC

Antalet SARS-CoV-2 (covid-19)-virustester analyserade för varje dag eller varje vecka
uppdelade på de med positivt, negativt eller icke-avgjort/felaktigt
resultat.

<div id="dwbuttons"><button class="btn btn-secondary" type="button" data-toggle="collapse" data-target="#daily_stacked_bar_chart" aria-expanded="true" aria-controls="#daily_stacked_bar_chart">
  Per dag
</button>
</div>
<div class="collapse show" id="daily_stacked_bar_chart">
<div class="d-lg-none alert alert-info">
  Skrolla grafen horisontellt för att se all data.
</div>
<div class="plot_wrapper">
  <div id="stacked-bar-chart"></div>
</div>
</div>
<div id="dwbuttons">
<button class="btn btn-secondary" type="button" data-toggle="collapse" data-target="#weekly_stacked_bar_chart" aria-expanded="true" aria-controls="weekly_stacked_bar_chart">
Per vecka
</button></div>
<div class="collapse show" id="weekly_stacked_bar_chart">
<div class="d-lg-none alert alert-info">
  Skrolla grafen horisontellt för att se all data.
</div>
<div class="plot_wrapper">
  <div id="stacked-bar-chart-weekly"></div>
</div>
</div>

#### Fraktion positiva tester vid NPC

Fraktionen SARS-CoV-2 (COVID-19)-virustester för varje dag eller vecka som är positiva,
i procent av alla tester (exkluderande icke-avgjort/felaktiga).

<div id="dwbuttons"><button class="btn btn-secondary" type="button" data-toggle="collapse" data-target="#daily_positive_bar_chart" aria-expanded="true" aria-controls="#daily_positive_bar_chart">
  Per dag
</button></div>
<div class="collapse show" id="daily_positive_bar_chart">
    <div class="d-lg-none alert alert-info">
      Skrolla grafen horisontellt för att se all data.
    </div>
    <div class="plot_wrapper">
      <div id="positive-bar-chart"></div>
    </div>
    <p class="small"><i>*Observera att eftersom antalet rapporterade analyser varierar kan vissa dagar ha ett lågt antal prover, vilket påverkar statistiken mycket för den dagen, t.ex. 24 augusti där endast sju prover rapporterades, alla positiva.</i></p>
</div>
<div id="dwbuttons"><button class="btn btn-secondary" type="button" data-toggle="collapse" data-target="#weekly_positive_bar_chart" aria-expanded="true" aria-controls="weekly_positive_bar_chart">
  Per vecka
</button></div>
<div class="collapse show" id="weekly_positive_bar_chart">
  <div class="d-lg-none alert alert-info">
    Skrolla grafen horisontellt för att se all data.
  </div>
  <div class="plot_wrapper">
    <div id="positive-bar-chart-weekly"></div>
  </div>
</div>

#### Kumulativt antal tester vid NPC

Summan av alla SARS-CoV-2 (covid-19)-virustester analyserade vid NPC
sedan start.

<div class="d-lg-none alert alert-info">
  Skrolla grafen horisontellt för att se all data.
</div>

<div class="plot_wrapper">
  <div id="cumulative-plot"></div>
</div>

Nationellt Pandemicenter (NPC) var en facilitet för
[SARS-CoV-2 (COVID-19)-tester](https://ki.se/mtc/ctmr-and-covid-19)
som byggdes upp vid
[Centre for Translational Microbiome Research (CTMR)](https://ki.se/en/research/centre-for-translational-microbiome-research-ctmr)
vid [Karolinska Institutet (KI)](https://ki.se/)/[SciLifeLab](https://www.scilifelab.se/).
Under slutet av mars 2020 byggdes det storskaliga mikrobiom-forskningslabbet
om till ett center för att bidra till testning av SARS-CoV-2 i Sverige.
Detta möjliggjordes genom en donation från
[Knut and Alice Wallenberg Foundation (KAW)](https://kaw.wallenberg.org/)
tillsammans med ett redan tidigare etablerat samarbete med
[MGI Tech](https://en.mgitech.cn/) i Shenzen, Kina. Efter att först ha
bidragit med kapacitet för RNA-extraktion åt Karolinska
Universitetslaboratoriet, expanderade NPC snabbt till att bli en
facilitet för ökad kapacitet för SARS-CoV-2-tester åt alla regioner i
Sverige.

Kapaciteten vid Nationellt Pandemicenter vid KI/SciLifeLab nådde
till slut ungefär 10.000 tester per dag, och resultaten skickades
i de flesta fall tillbaka inom 24 timmar efter att provet inkommit
till labbet. NPC utförde endast PCR-baserad analys, inte serologisk
(antikropps-baserad) analys.

Data som visas på den här sidan är automatiskt sammanställd och stämmer inte
nödvändigtvis överens med data som publicerats via andra kanaler
av olika anledningar.

Datasetet som visualiseras i graferna finns tillgängligt
[här](https://datagraphics.dckube.scilifelab.se/dataset/bbbaf64a25a1452287a8630503f07418).
Källkoden för graferna finns
[här](https://datagraphics.dckube.scilifelab.se/graphic/ba0b27320fe74ad0aef59a26be6c37f1),
[här](https://datagraphics.dckube.scilifelab.se/graphic/ddb1119aefce47d58d0b3a49e98b4fcc),
[här](https://datagraphics.dckube.scilifelab.se/graphic/b31c50be59c84c93986c25b052115a65)
och [här](https://datagraphics.dckube.scilifelab.se/graphic/9145856246004419983d39fcf56d9eb6).

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.12.2"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/ba0b27320fe74ad0aef59a26be6c37f1.js?id=grand-total-chart"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/ddb1119aefce47d58d0b3a49e98b4fcc.js?id=stacked-bar-chart"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/1f2322f4301c4773878c956c578e8caf.js?id=stacked-bar-chart-weekly"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/b31c50be59c84c93986c25b052115a65.js?id=positive-bar-chart"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/9145856246004419983d39fcf56d9eb6.js?id=cumulative-plot"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/7f27ae237b8146a498ab4014aadc35db.js?id=positive-bar-chart-weekly"></script>
