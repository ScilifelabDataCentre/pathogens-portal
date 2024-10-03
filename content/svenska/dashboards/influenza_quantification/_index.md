---
title: Mängd influensa A- och influensa B-virus i avloppsvatten
plotly: true
banner: /dashboard_thumbs/wastewater_influenza.png
description: Utforska nivåerna av Influenza A och B-virus i avloppsvatten över hela Sverige. Veckodata från SLU-SEEC spårar influensatrender, täcker 43% av den svenska befolkningen, och hjälper till att förutsäga potentiella utbrott.
menu:
 dashboard_menu:
    identifier: wastewater_influenza_quantification
    name: "Avloppsvatten: Kvantifiering av influensa (SLU)"
aliases:
  - /sv/dashboards/wastewater/influenza_quantification/
dashboards_topics: [Wastewater Surveillance, Influenza, Epidemiology]
data_status: "updating"
---

## Introduktion

Influensavirus är enkelsträngade, segmenterade RNA-virus inom familjen Orthomyxoviridae. Influensa A- och influensa B-virus orsakar säsongsbetonade epidemier av influensa, en mycket smittsam luftvägssjukdom som kännetecknas av symptom som feber, hosta, halsont, värk i kroppen och trötthet, men diarré och kräkningar kan också förekomma. Influensa A-virus är utbrett bland sjöfåglar men infekterar också andra fågelarter och olika däggdjur, inklusive människor och grisar, medan influensa B-virus främst infekterar människor. Influensavirus muterar snabbt, vilket leder till olika stammar och säsongsbetonade utbrott. Både influensa A- och B-virus kan orsaka säsongsbetonade utbrott, men endast influensa A är känt för att orsaka pandemier på grund av att viruset kan smitta olika arter och den potentiella möjligheten till genetisk rekombination mellan olika djurarter. För mer information om symtom, risker och vaccination mot influensavirus, besök [Folkhälsomyndighetens motsvarande sida](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/influensa-/).

Data som presenteras på denna sida genereras i Sveriges lantbruksuniversitets (SLU) laboratorier vid Svenskt Miljöepidemiologiskt Centrum (SEEC). Data och visualiseringar på den här sidan uppdateras vanligtvis veckovis, oftast på måndagar. För en omfattande förståelse, vänligen hänvisa till [Metoder](#metoder) avsnittet. För en allmän översikt om avloppsvattenövervakning, vänligen besök [Avloppsbaserad epidemiologi i Sverige](/dashboards/wastewater_background/)

<div class="alert alert-info">
<b>Viktig notering:</b></br>
Notera att de poäng som tillhandahålls i datasetet och som visas i grafen nedan är preliminära, så korrigeringar och ändringar kan förekomma. Data och information om gruppen på den här dashboarden uppdateras kontinuerligt. </br>Notera också att även om samma metoder används för alla städer som visas på den här fliken, kan skillnader i befolkningen och hur avloppsvatten samlas in i olika städer påverka jämförelser dem emellan.
</div>

## Visualiseringar

<div class="alert alert-info">Last updated: <span id="last_modified_slu_flu"></span></div>

### Influensa A

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 1200px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_slu_infA_v1.0.json" height="800px" >}}</div>
</div>

**Källkod som används för att skapa grafen:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/combined_slu_influenza_a.py).

### Influensa B

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 1200px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_slu_infB_v1.0.json" height="800px" >}}</div>
</div>

**Källkod som används för att skapa grafen:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/combined_slu_influenza_b.py).

## Kommentarer från forskargruppen

<div><b>Date:</b> <span id="slu_flu_comment_date"></span><br><b>Commentary:</b> <span id="slu_flu_comment"></span></div>

{{< ww_dynamic_content >}}

## Rapporter från forskargruppen

Forskargruppen tillhandahåller en rapport som sammanfattar information från deras avloppsvattenmätningar. Den senaste rapporten finns tillgänglig som pdf [här](https://blobserver.dc.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU.pdf) (endast tillgänglig på svenska).

## Dataset

**Kontakt:** <anna.szekely@slu.se> and <javier.vargas@slu.se>

**Ladda ner data:** [Genkopieantal för luftvägsvirus normaliserat mot PMMoV-genkopieantal.CSV fil](https://blobserver.dc.scilifelab.se/blob/SLU_wastewater_data_v1.0.csv). Data finns tillgänglig för influensa A-virus från vecka 42 2022 och för influensa B-virus från vecka 12 2023, uppdateras veckovis.

**Citera data:**

Székely, A. J., Malmberg, M., Vargas, J., Mohamed, N., Dafalla, I., Petrini, F., Davies, L. (2023). Dataset of SARS-CoV-2, influenza A and influenza B virus content in wastewater samples from wastewater treatment plants in Sweden. <https://doi.org/10.17044/scilifelab.14256317>.

## Metoder

För de flesta städer som representeras på den här sidan används flödeskompenserade provtagare vid avloppsreningsverken (WWTP) för att samla in råa, obehandlade avloppsprover representativa för en enskild dag. Uppsala är undantaget, där prover samlas in dagligen och sedan kombineras flödesproportionellt till ett sammansatt veckoprov som används för analyserna.

Det virala genomiska materialet från de insamlade proverna extraheras med en metod som använder Maxwell RSC Enviro TNA-kitet (Promega).

Absolut kvantifiering av antalet kopior av influensa A- och B-virusgenom görs med metoden One-Step RT-qPCR och Flu SC2 Multiplex-testet från Centers for Disease Control and Prevention (CDC). För att korrigera för variation i population och avloppsvattenflöde kvantifieras förekomsten av viruset pepper mild mottle virus (PMMoV), ett växtvirus från peppar som människor får i sig via maten. PMMoV kvantifieras med hjälp av en modifierad version av testet i [Zhang et al. (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV är det vanligaste RNA-viruset i avföring från människa och används för att uppskatta mängden avföring från människa i avloppsvattenprover [Symonds et al., (2019)](https://doi.org/10.1371/journal.ppat.1007639).

Data i graferna och datafilen presenteras i tre olika format:
- **PMMoV-normaliserat Influensa-innehåll** visar förhållandet mellan det kopieantal som uppmätts med influensa-testet och PMMoV-testet, multiplicerat med 1000. Eftersom influensa-testet ger en proxy för influensa-virusmängd i avloppsvattnet och PMMoV är en proxy för avföringsinnehållet (som är relaterat till den bidragande befolkningen) kan förhållandet mellan de två betraktas som en proxy för förekomsten av influensa-infektioner i befolkningen i avloppsvattnets upptagningsområde.
- **Koncentration av Influensa-genomkopior** visar koncentrationen av influensa-kopienummer som uppmäts i avloppsvattnet. Dessa data påverkas av hur de olika avloppsvattensystemen är uppbyggda och lämpar sig därför inte för jämförelse mellan platser. Virushalten i avloppsvattnet påverkas också av väderhändelser som påverkar avloppsflödet (t.ex. kraftigt regn eller snösmältning).
- **Influensa-genomkopior/dag/invånare** representerar den uppskattade dagliga virusmängden i avloppsvattnet normaliserad för antalet invånare anslutna till systemet. Dessa data går att jämföra mellan olika platser. Vissa fördröjningar i presentationen av dessa data kan förekomma, jämfört med de andra analyserna.

**Citera metoden:**

Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. _Environments_, _9_, 39. <https://doi.org/10.3390/environments9030039>.


## Insamlingsplatser för avloppsvatten

SLU-SEEC samlar in och analyserar prover för kvantifiering av nivåerna av influensa A- och influensa B-virus från ett flertal orter. Nedan visas en tabell med detaljerad information om alla insamlingsplatser. Tabellen listar orter som övervakas, avloppsreningsverk (WWTP) där proverna samlas in, antal personer i upptagningsområdet (Number of people), mellan vilka datum SLU-SEEC mätningarna skett (Start date och End date). Notera att 'Start date' avser det datum då övervakning av influensa A startade, men att startdatumet för influensa B alltid är senare. Ett värde ’null’ istället för slutdatum innebär att insamlingen fortfarande pågår. En asterisk (\*) bredvid antal invånare innebär att värdet är uppskattat baserat på hur många invånare som reningsverket betjänar (BOD-7). Två asterisker (\*\*) bredvid staden/staden indikerar att data endast är tillgänglig för influensa A, och inte influensa B. Informationen i tabellen nedan är [tillgänglig för nedladdning som en excel-fil](https://blobserver.dc.scilifelab.se/blob/SLU_INF_collection_sites.xlsx).

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_sluINFsites.json" height="750px" >}}</div>
</div>

## Arkiverade data från SLU

- [Historiska influensadata i avloppsvatten från SEEC-SLU](/dashboards/influenza_quantification/historic_influenza_SLU)