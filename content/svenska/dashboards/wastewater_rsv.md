---
title: "Mängd Respiratory Syncytial Virus (RSV eller RS-virus) i avloppsvatten (SEEC-SLU)"
description: "Utforska nivåerna av Respiratory Syncytial Virus (RSV) i avloppsvatten över hela Sverige. Veckodata från SLU-SEEC spårar RSV-trender, täcker en betydande del av befolkningen, och hjälper till att förutsäga potentiella utbrott."
plotly: true
banner: /dashboard_thumbs/wastewater_rsv.png
menu:
  dashboard_menu:
    identifier: rsv_quant
    name: "Avloppsvatten: RSV kvantifiering (SLU)"
dashboards_topics: [Wastewater Surveillance, RSV, Epidemiology]
data_status: "updating"
---
## Introduktion

Respiratory Syncytial Virus (RSV) är ett enkelsträngat RNA-virus som orsakar infektioner i lungor och luftvägar. De flesta människor får bara milda förkylningsliknande symtom och återhämtar sig snabbt, men spädbarn och äldre vuxna kan utveckla allvarligare symptom och behöva sjukhusvård. RSV är en av de främsta orsakerna till sjukhusvård vid luftvägssjukdomar hos spädbarn yngre än 1 år. För mer information om symtom, risker och vaccination mot RS-virus, besök [Folkhälsomyndighetens motsvarande sida](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/rs-virusinfektion/).

Data som presenteras på denna sida genereras i Sveriges lantbruksuniversitets (SLU) laboratorier vid Svenskt Miljöepidemiologiskt Centrum (SEEC). Data och visualiseringar på den här sidan uppdateras vanligtvis veckovis, oftast på måndagar. För en omfattande förståelse, vänligen hänvisa till [Metoder](#metoder) avsnittet. För en allmän översikt om avloppsvattenövervakning, vänligen besök [Avloppsbaserad epidemiologi i Sverige](/dashboards/wastewater_background/)

<div class="alert alert-info">
<b>Viktig notering:</b></br>
Notera att de poäng som tillhandahålls i datasetet och som visas i grafen nedan är preliminära, så korrigeringar och ändringar kan förekomma. Data och information om gruppen på den här dashboarden uppdateras kontinuerligt. </br>Notera också att även om samma metoder används för alla städer som visas på den här fliken, kan skillnader i befolkningen och hur avloppsvatten samlas in i olika städer påverka jämförelser dem emellan.
</div>


## Visualiseringar

<div class="alert alert-info">Last updated: <span id="last_modified_slu_rsv"></span></div>

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 1200px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_slu_rsv_v1.0.json" height="800px" >}}</div>
</div>

**Källkod som används för att skapa grafen:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/combined_slu_rsv.py).

## Kommentarer från forskargruppen

<div><b>Date:</b> <span id="slu_rsv_comment_date"></span><br><b>Commentary:</b> <span id="slu_rsv_comment"></span></div>

{{< ww_dynamic_content >}}

## Rapporter från forskargruppen

Forskargruppen tillhandahåller en rapport som sammanfattar information från deras avloppsvattenmätningar. Den senaste rapporten finns tillgänglig som pdf <a target="_blank" href="https://blobserver.dc.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU.pdf">här</a> (endast tillgänglig på svenska).

## Dataset

**kontakt:** <anna.szekely@slu.se> och <javier.vargas@slu.se>

**Ladda ner data:** RSV-genkopieantal normaliserat mot PMMoV-genkopieantal [CSV-fil](https://blobserver.dc.scilifelab.se/blob/SLU_wastewater_data_v1.0.csv). Data för RSV finns tillgängligt från vecka 32 2023 och uppdateras varje vecka.

**Citera datasetet:**

Székely, A. J., Malmberg, M., Vargas, J., Mohamed, N., Dafalla, I., Petrini, F., Davies, L. (2023). Dataset of SARS-CoV-2, influenza A and influenza B virus content in wastewater samples from wastewater treatment plants in Sweden. <https://doi.org/10.17044/scilifelab.14256317>.

## Metoder

Avloppsvatten samlas in från flera olika reningsverk runt om i landet. För mer information om reningsverken, besök sidan om [bakgrunden till avloppsvattenövervakning](/dashboards/wastewater_background/). För de flesta städer som representeras på den här sidan används flödeskompenserade provtagare vid avloppsreningsverken (WWTP) för att samla in råa, obehandlade avloppsprover representativa för en enskild dag. Uppsala är undantaget, där prover samlas in dagligen och sedan kombineras flödesproportionellt till ett sammansatt veckoprov som används för analyserna.

Det virala genomiska materialet från de insamlade proverna extraheras med en metod som använder Maxwell RSC Enviro TNA-kitet (Promega). För en detaljerad beskrivning av metoden, läs följande protokoll.

Absolut kvantifiering av antalet kopior av RSV-genom görs med metoden One-Step RT-qPCR med testet som används i <a target="_blank" href="https://doi.org/10.1021/acs.estlett.1c00963">Hughes et al. (2022)</a>. För att korrigera för variation i population och avloppsvattenflöde kvantifieras förekomsten av viruset pepper mild mottle virus (PMMoV), ett växtvirus från peppar som människor får i sig via maten. PMMoV kvantifieras med hjälp av en modifierad version av testet i <a target="_blank" href="https://doi.org/10.1371/journal.pbio.0040003">Zhang et al. (2006)</a>. PMMoV är det vanligaste RNA-viruset i avföring från människa och används för att uppskatta mängden avföring från människa i avloppsvattenprover (<a target="_blank" href="https://doi.org/10.1371/journal.ppat.1007639">Symonds et al. 2019</a>).

Data i graferna och datafilen presenteras i tre olika format:

- **PMMoV-normaliserat RSV-innehåll** visar förhållandet mellan det kopieantal som uppmätts med RSV-testet och PMMoV-testet, multiplicerat med 1000. Eftersom RSV-testet ger en proxy för RSV-virusmängd i avloppsvattnet och PMMoV är en proxy för avföringsinnehållet (som är relaterat till den bidragande befolkningen) kan förhållandet mellan de två betraktas som en proxy för förekomsten av RSV-infektioner i befolkningen i avloppsvattnets upptagningsområde.
- **Koncentration av RSV-genomkopior** visar koncentrationen av RSV-kopienummer som uppmäts i avloppsvattnet. Dessa data påverkas av hur de olika avloppsvattensystemen är uppbyggda och lämpar sig därför inte för jämförelse mellan platser. Virushalten i avloppsvattnet påverkas också av väderhändelser som påverkar avloppsflödet (t.ex. kraftigt regn eller snösmältning).
- **RSV-genomkopior/dag/invånare** representerar den uppskattade dagliga virusmängden i avloppsvattnet normaliserad för antalet invånare anslutna till systemet. Dessa data går att jämföra mellan olika platser. Vissa fördröjningar i presentationen av dessa data kan förekomma, jämfört med de andra analyserna.

**Citera metoden:**

Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. _Environments_, _9_, 39. <https://doi.org/10.3390/environments9030039>.

<!-- ## Insamlingsplatser för avloppsvatten

SLU-SEEC samlar in och analyserar prover för kvantifiering av nivåerna av influensa A- och B-virus från ett flertal orter. Nedan visas en tabell med detaljerad information om alla insamlingsplatser. Tabellen listar orter som övervakas, avloppsreningsverk (WWTP) där proverna samlas in, antal personer i upptagningsområdet (antal invånare), mellan vilka datum SLU-SEEC mätningarna skett (startdatum och slutdatum). Ett värde ’null’ istället för slutdatum innebär att insamlingen fortfarande pågår. En asterisk bredvid antal invånare innebär att värdet är uppskattat baserat på hur många invånare som reningsverket betjänar. Informationen i tabellen nedan är [tillgänglig för nedladdning som en excel-fil](https://blobserver.dc.scilifelab.se/blob/SLU_All_sites.xlsx).

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_slu_All_sites.json" height="840px" >}}</div>
</div> -->