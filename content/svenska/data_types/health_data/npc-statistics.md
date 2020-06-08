---
title: Nationellt Pandemicenter SARS-CoV-2 (Covid-19) virus analysstatistik
menu:
    main:
        identifier: npc-statistics
        parent: health_data
        weight: 10
---

#### Dagligt antal tester vid NPC

Totala antalet SARS-CoV-2 (Covid-19) virus tester analyserade för
varje dag, uppdelade på de med positivt, negativt eller
icke-avgjort/felaktigt resultat.

<div class="d-md-none alert alert-info">
  Skrolla grafen horisontellt för att se all data.
</div>
<div class="plot_wrapper">
  <div id="stacked-bar-chart"></div>
</div>

#### Kumulativt antal tester vid NPC

Summan av alla SARS-CoV-2 (Covid-19) virus tester analyserade vid NPC
sedan start.

<div class="d-md-none alert alert-info">
  Skrolla grafen horisontellt för att se all data.
</div>
<div class="plot_wrapper">
  <div id="cumulative-plot"></div>
</div>

Nationellt Pandemicenter (NPC) är ett lab för
[SARS-CoV-2 (Covid-19) tester](https://ki.se/mtc/ctmr-and-covid-19) som har byggts upp
vid
[Centret för Translationell Mikrobiomforskning (CTMR)](https://ki.se/en/research/news-from-the-centre-for-translational-microbiome-research-ctmr)
på [Karolinska Institutet (KI)](https://ki.se/)/
[SciLifeLab](https://www.scilifelab.se/).
I slutet av mars 2020 ställde man snabbt om sitt laboratorium för storskalig mikrobiomforskning till ett
center för att bistå Sverige med att analysera SARS-CoV-2-prov.
Detta möjliggjordes tack vare en donation från
[Knut och Alice Wallenbergs stiftelse (KAW)](https://kaw.wallenberg.org/),
i kombination med ett tidigare redan etablerat nära samarbete med
[MGI Tech.](https://en.mgitech.cn/) i Shenzen, Kina.
Till en början bistod NPC Karolinska Universitetslaboratoriet med
RNA-extraktionskapacitet, men expanderade på kort tid till en
fullskalig verksamhet för att kunna erbjuda resurser för utökad
SARS-CoV-2-testning i alla Sveriges regioner.

Nationellt Pandemicenter (NPC) vid KI/SciLifeLab har en nuvarande
analyskapacitet på ca 5000 prover per dag, med provsvar normalt inom
24 timmar från provets ankomst till labbet. Notera att endast PCR-baserade
analyser görs vid NPC, inte serologiska (antikroppsbaserade) analyser.

Data som visas på den här sidan är automatiskt sammanställd och stämmer inte
nödvändigtvis överens med data som publicerats via andra kanaler
av olika anledningar. Datan uppdateras dagligen, och ändringar bakåt i
tiden kan förekomma.

Datasetet som visualiseras i graferna finns tillgängligt
[här](https://datagraphics.dckube.scilifelab.se/dataset/bbbaf64a25a1452287a8630503f07418).
Källkoden för graferna finns
[här för stapeldiagrammet](https://datagraphics.dckube.scilifelab.se/graphic/ddb1119aefce47d58d0b3a49e98b4fcc)
och [här för den kumulativa grafen](https://datagraphics.dckube.scilifelab.se/graphic/e823c75ee55849e7999da56c6c869c7a).

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4.12.2"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/ddb1119aefce47d58d0b3a49e98b4fcc.js?id=stacked-bar-chart"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/e823c75ee55849e7999da56c6c869c7a.js?id=cumulative-plot"></script>
