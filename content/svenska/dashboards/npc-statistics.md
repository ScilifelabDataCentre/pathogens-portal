---
title: Nationellt Pandemicenter SARS-CoV-2 (covid-19)-analysstatistik
aliases:
  - /sv/data_types/health_data/npc-statistics/
description: Nationellt Pandemiskt Center (NPC) genomförde testning för SARS-CoV-2 från pandemins början. Data som visas inkluderar antal positiva och negativa test samt antal test med oklart testresultat. Denna dashboard visar endast historiska data och uppdateras inte längre.
banner: /dashboard_thumbs/NPC_logo.png
banner_border: true
plotly: true
menu:
  dashboard_menu:
    identifier: npc-statistics
    name: "SARS-CoV-2-tester vid National Pandemic Centre"
---

<div class="alert alert-info small">
  <p><i class="bi bi-exclamation-triangle-fill"></i>Nationellt Pandemiskt center på Karolinska Institutet upphörde med högkapacitets PCR diagnostik 2020-12-21.</p>
  <p><span class="font-weight-bold">Den data som visas här har slutat uppdateras</span> och utgör endast historisk dokumentation.</p>
  <a href="https://nyheter.ki.se/covid-19-tester-ki-atergar-till-ordinarie-laboratorieverksamhet-men-har-fortsatt-beredskap">KIs pressmeddelande</a>
</div>

Datauppsättningen som visualiseras i graferna på denna sida är tillgänglig [på SciLifeLab Blobserver](https://blobserver.dc.scilifelab.se/blob/NPC-statistics-data-set.csv). De siffror som redovisas här har sammanställts automatiskt och kan av olika anledningar inte motsvara siffror som rapporterats via andra källor.

#### Totala antalet tester vid NPC

Det totala antalet SARS-CoV-2 (covid-19)-virustester analyserade vid NPC
uppdelade på de med positivt, negativt eller icke-avgjort/felaktigt
resultat.

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout.
</div>

 <div class="plot_wrapper mb-3">
    <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_total_tests.json" height="200px">}}</div>
</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_total_tests.py)

#### Antal tester vid NPC

Antalet SARS-CoV-2 (covid-19)-virustester analyserade för varje dag eller varje vecka uppdelade på de med positivt, negativt eller icke-avgjort/felaktigt resultat.

##### Per dag

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_tests_daily.json" height="350px">}}</div>
</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_tests_daily.py)

##### Per vecka

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_tests_weekly.json" height="350px">}}</div>
</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_tests_weekly.py)

#### Fraktion positiva tester vid NPC

Fraktionen SARS-CoV-2 (COVID-19)-virustester för varje dag eller vecka som är positiva, i procent av alla tester **(exkluderande icke-avgjort/felaktiga)**.

##### Per dag

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_positiveTests_fraction_daily.json" height="350px">}}</div>
</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_positiveTests_fraction_daily.py)

##### Per vecka

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_positiveTests_fraction_weekly.json" height="350px">}}</div>
</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_positiveTests_fraction_weekly.py)

#### Kumulativt antal tester vid NPC

Summan av alla SARS-CoV-2 (covid-19)-virustester analyserade vid NPC sedan start.

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/npc_cumulative_tests.json" height="550px">}}</div>
</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/npctests/npc_cumulative_tests.py)

Nationellt Pandemicenter (NPC) var en facilitet för [SARS-CoV-2 (COVID-19)-tester](https://ki.se/mtc/ctmr-and-covid-19) som byggdes upp vid [Centre for Translational Microbiome Research (CTMR)](https://ki.se/en/research/centre-for-translational-microbiome-research-ctmr) vid [Karolinska Institutet (KI)](https://ki.se/)/[SciLifeLab](https://www.scilifelab.se/). Under slutet av mars 2020 byggdes det storskaliga mikrobiom-forskningslabbet om till ett center för att bidra till testning av SARS-CoV-2 i Sverige. Detta möjliggjordes genom en donation från [Knut and Alice Wallenberg Foundation (KAW)](https://kaw.wallenberg.org/) tillsammans med ett redan tidigare etablerat samarbete med [MGI Tech](https://en.mgitech.cn/) i Shenzen, Kina. Efter att först ha bidragit med kapacitet för RNA-extraktion åt Karolinska Universitetslaboratoriet, expanderade NPC snabbt till att bli en facilitet för ökad kapacitet för SARS-CoV-2-tester åt alla regioner i Sverige.

Kapaciteten vid Nationellt Pandemicenter vid KI/SciLifeLab nådde till slut ungefär 10.000 tester per dag, och resultaten skickades i de flesta fall tillbaka inom 24 timmar efter att provet inkommit till labbet. NPC utförde endast PCR-baserad analys, inte serologisk (antikropps-baserad) analys.
