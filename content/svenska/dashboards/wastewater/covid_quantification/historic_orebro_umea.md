---
title: "Historiska data för Örebro och Umeå"
plotly: true
aliases:
  - /sv/data_types/environment/wastewater/historic_orebro_umea/
  - /sv/dashboards/wastewater/historic_orebro_umea/
---

Denna sida visar data för mängd SARS-CoV-2 i avloppsvatten från Umeå och Örebro mellan oktober 2020 och juni 2021. Från juni 2021 ändrades metoden. Se [den här sidan](/dashboards/wastewater/covid_quantification/covid_quant_slu/) för de senaste uppgifterna.

Data som visas här samlades in inom ett forskningsprojekt av prof. Maja Malmberg (SLU, Sveriges Lantbruksuniversitet) i samarbete med [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) och Mette Myrmel vid Norwegian University of Life Sciences. Mängden SARS-CoV-2-virus i avloppsvattnet mättes i avloppsreningsanläggningen i Örebro och Umeå. Se [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Örebro](/wastewater/map_orebro.pdf); se [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Umeå](/wastewater/map_umeaa.jpg).

Efter beredning har proverna extraherats och ultrafiltrats samt analyserats för SARS CoV-2 med RT-qPCR analys , proverna har normaliserats med PMMoV. Fram till januari 2021, samlades tre prover in per vecka, dessa prov poolades till ett prov per vecka. Från och med februari 2021 samlades endast prover in vid en tidpunkt per vecka. Primers som används för att detektera förekomsten av SARS-CoV-2 RNA har tidigare används av [Corman _et al._ , 2020](https://doi.org/10.2807/1560-7917.ES.2020.25.3.2000045). Mängd SARS-CoV-2 RNA per vecka jämfört med mängd SARS-CoV-2 som uppmättes on November 6 2020.

### Mängd SARS-CoV-2 i avloppsvatten från Umeå mellan oktober 2020 och juni 2021

**Ladda ner data:** [Förändring i mängd SARS CoV-2 RNA (%) jämfört med Nov 6 2020 och flöde varje dag samt veckonummer, Excel fil](https://blobserver.dc.scilifelab.se/blob/wastewater_data_Umeaa.xlsx). Data är tillgänglig från vecka 44 2020 till vecka 22 2021.

**Referera till detta dataset:**
Malmberg, M., Myrmel, M. & Khatri, M. Dataset of SARS-CoV-2 in wastewater in Umeå, Sweden. [https://doi.org/10.17044/scilifelab.14376881.v1](https://doi.org/10.17044/scilifelab.14376881.v1) (2021).

<div class="d-md-none alert alert-info">
  Skrolla grafen horisontellt för att se alla data.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 600px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_graph_Umea.json" height="550px" >}}</div>
</div>

<div class="small text-muted">*Data från dessa veckor är inte tillgängliga.</div>

<div class="small text-muted">**Proverna från har förvarats i +4 °C under 2-3 veckor innan analys vilket skiljer sig från övriga insamlade prover.</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/umea_covid.py).

### Mängd SARS-CoV-2 i avloppsvatten från Örebro mellan oktober 2020 och juni 2021

**Ladda ner data:** [Förändring i mängd SARS CoV-2 RNA (%) jämfört med Nov 6 2020 och flöde varje dag samt veckonummer, Excel fil](https://blobserver.dc.scilifelab.se/blob/wastewater_data_Orebro.xlsx). Data är tillgänglig från vecka 42 2020 till vecka 22 2021.

**Referera till detta dataset:**
Malmberg, M., Myrmel, M. & Khatri, M. (2021) Dataset of SARS CoV-2 in wastewater in Örebro, Sweden. [https://doi.org/10.17044/scilifelab.14377097.v1](https://doi.org/10.17044/scilifelab.14377097.v1) (2021).

<div class="d-md-none alert alert-info">
  Skrolla grafen horisontellt för att se alla data.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 600px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_graph_Orebro.json" height="550px" >}}</div>
</div>

<div class="small text-muted">*Data från dessa veckor är inte tillgängliga.</div>

<div class="small text-muted">**Proverna fhar förvarats i +4 °C under 2-3 veckor innan analys vilket skiljer sig från övriga insamlade prover.</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/orebro_covid.py).
