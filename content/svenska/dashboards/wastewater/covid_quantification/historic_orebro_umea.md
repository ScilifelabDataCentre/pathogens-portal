---
title: "Historiska data för Örebro och Umeå"
aliases:
    - /sv/data_types/environment/wastewater/historic_orebro_umea/
    - /sv/dashboards/wastewater/historic_orebro_umea/
---

Denna sida visar data för mängd SARS-CoV-2 i avloppsvatten från Umeå och Örebro mellan oktober 2020 och juni 2021. Från juni 2021 ändrades metoden. Se [den här sidan](../) för de senaste uppgifterna.

Data som visas här samlades in inom ett forskningsprojekt av prof. Maja Malmberg (SLU, Sveriges Lantbruksuniversitet) i samarbete med [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) och Mette Myrmel vid Norwegian University of Life Sciences. Mängden SARS-CoV-2-virus i avloppsvattnet mättes i avloppsreningsanläggningen i Örebro och Umeå. Se [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Örebro](/wastewater/map_orebro.pdf); se [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Umeå](/wastewater/map_umeaa.jpg).

Efter beredning har proverna extraherats och ultrafiltrats samt analyserats för SARS CoV-2 med RT-qPCR analys , proverna har normaliserats med PMMoV. Fram till januari 2021, samlades tre prover in per vecka, dessa prov poolades till ett prov per vecka. Från och med februari 2021 samlades endast prover in vid en tidpunkt per vecka. Primers som används för att detektera förekomsten av SARS-CoV-2 RNA har tidigare används av [Corman et al , 2020](https://doi.org/10.2807/1560-7917.ES.2020.25.3.2000045). Mängd SARS-CoV-2 RNA per vecka jämfört med mängd SARS-CoV-2 som uppmättes on November 6 2020.

### Mängd SARS-CoV-2 i avloppsvatten från Umeå mellan oktober 2020 och juni 2021

**Ladda ner data:** [Förändring i mängd SARS CoV-2 RNA (%) jämfört med Nov 6 2020 och flöde varje dag samt veckonummer, Excel fil.](https://blobserver.dc.scilifelab.se/blob/wastewater_data_Umeaa.xlsx). Data startar vecka 44 of 2020; uppdateras en gång per månad.

**Referera till detta dataset:**
Malmberg, M., Myrmel, M. & Khatri, M. Dataset of SARS-CoV-2 in wastewater in Umeå, Sweden. [https://doi.org/10.17044/scilifelab.14376881.v1](https://doi.org/10.17044/scilifelab.14376881.v1) (2021).

<div class="d-md-none alert alert-info">
  Skrolla grafen horisontellt för att se alla data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="umea_combined"></div>
</div>

<div class="small text-muted">*Data från dessa veckor är inte tillgängliga.</div>

<div class="small text-muted">**Proverna från vecka 11 och 12 har förvarats i +4 °C under 2-3 veckor innan analys vilket skiljer sig från övriga insamlade prover.</div>

### Mängd SARS-CoV-2 i avloppsvatten från Örebro mellan oktober 2020 och juni 2021

**Ladda ner data:** [Förändring i mängd SARS CoV-2 RNA (%) jämfört med Nov 6 2020 och flöde varje dag samt veckonummer, Excel fil](https://blobserver.dc.scilifelab.se/blob/wastewater_data_Orebro.xlsx). Data startar vecka 44 of 2020; uppdateras en gång per månad.

**Referera till detta dataset:**
Malmberg, M., Myrmel, M. & Khatri, M. Dataset of SARS CoV-2 in wastewater in Örebro, Sweden. [https://doi.org/10.17044/scilifelab.14377097.v1](https://doi.org/10.17044/scilifelab.14377097.v1) (2021).

<div class="d-md-none alert alert-info">
  Skrolla grafen horisontellt för att se alla data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="orebro_combined"></div>
</div>

<div class="small text-muted">*Data från dessa veckor är inte tillgängliga.</div>

<div class="small text-muted">**Proverna från vecka 11 och 12 har förvarats i +4 °C under 2-3 veckor innan analys vilket skiljer sig från övriga insamlade prover.</div>

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.1.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dc.scilifelab.se/graphic/030ac237d44248dda87e2c9277a49cc7.js?id=umea_combined"></script>
<script src="https://datagraphics.dc.scilifelab.se/graphic/fe03ef2220814eeeb3e99eb26a7c46e2.js?id=orebro_combined"></script>
