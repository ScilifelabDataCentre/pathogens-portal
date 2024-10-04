---
title: Historiska data om influensavirus i avloppsvatten (SLU)
plotly: true
---

## Introduktion

Influensavirus är enkelsträngade, segmenterade RNA-virus inom familjen Orthomyxoviridae. Influensa A- och influensa B-virus orsakar säsongsbetonade epidemier av influensa, en mycket smittsam luftvägssjukdom som kännetecknas av symptom som feber, hosta, halsont, värk i kroppen och trötthet, men diarré och Data som presenteras på denna sida genererades i SLU:s (Sveriges lantbruksuniversitet) laboratorier av SEEC (Swedish Environmental Epidemiology Center). Projektet var en del av SciLifeLabs Pandemic Laboratory Preparedness (PLP) Program, ledd av Anna J. Székely (Institutionen för vatten och miljö, SLU). Avloppsvattenanalyser övervakades av Anna J. Székely, Javier Vargas och Maja Malmberg (Virologienheten vid Institutionen för biomedicinsk vetenskap och veterinär folkhälsovetenskap, SLU). Denna sida handlar om den historiska kvantifieringen av nivåerna av influensa A och B-virus i flera städer över hela Sverige. Projektet hade den bredaste geografiska täckningen över Sverige och genererade data för 43% av den svenska befolkningen.

Observera att data och visualiseringar på denna sida inte längre uppdateras. Poängen i datasetet och som avbildas i diagrammen är slutgiltiga, även om mindre korrigeringar kan ha tillämpats i efterhand. Denna instrumentpanel fungerar som en post över projektets resultat under den aktiva övervakningsperioden.

## Insamlingsplatser för avloppsvatten

SLU-SEEC samlar in och analyserar prover för kvantifiering av nivåerna av influensa A- och influensa B-virus från ett flertal orter. Nedan visas en tabell med detaljerad information om alla insamlingsplatser. Tabellen listar orter som övervakas, avloppsreningsverk (WWTP) där proverna samlas in, antal personer i upptagningsområdet (Number of people), mellan vilka datum SLU-SEEC mätningarna skett (Start date och End date). Notera att 'Start date' avser det datum då övervakning av influensa A startade, men att startdatumet för influensa B alltid är senare. Ett värde ’null’ istället för slutdatum innebär att insamlingen fortfarande pågår. En asterisk (\*) bredvid antal invånare innebär att värdet är uppskattat baserat på hur många invånare som reningsverket betjänar (BOD-7). Två asterisker (\*\*) bredvid staden/staden indikerar att data endast är tillgänglig för influensa A, och inte influensa B. Informationen i tabellen nedan är [tillgänglig för nedladdning som en excel-fil](https://blobserver.dc.scilifelab.se/blob/SLU_INF_collection_sites.xlsx).

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_sluINFsites.json" height="750px" >}}</div>
</div>

## Visualiseringar

<div class="alert alert-info">Last updated: 2024-09-30</div>

**Notera** att även om samma metoder används för alla städer som visas på den här fliken, kan skillnader i befolkningen och hur avloppsvatten samlas in i olika städer påverka jämförelser dem emellan.

### Influensa A

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/historic_wastewater_slu_infA.json" height="600px" >}}</div>
</div>

**Källkod som används för att skapa grafen:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/archive/historic_combined_slu_influenza_a.py).

### Influensa B

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/historic_wastewater_slu_infB.json" height="600px" >}}</div>
</div>

**Källkod som används för att skapa grafen:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/archive/historic_combined_slu_influenza_b.py).

## Kommentarer från forskargruppen

<div><b>Date:</b> 2023-08-30<br><b>Commentary:</b> The data presented for influenza A and B is preliminary. Minor changes to the data are expected in the near future due to ongoing adjustments to the data analyses methods.</div>

## Rapporter från forskargruppen

Forskargruppen tillhandahåller en rapport som sammanfattar information från deras avloppsvattenmätningar. Den senaste rapporten finns tillgänglig som pdf [här](https://blobserver.dc.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU.pdf) (endast tillgänglig på svenska).

## Dataset

**Kontakt:** <anna.szekely@slu.se> and <javier.vargas@slu.se>

**Ladda ner data:** [Genkopieantal för luftvägsvirus normaliserat mot PMMoV-genkopieantal.CSV fil](https://blobserver.dc.scilifelab.se/blob/historic_SLU_wastewater_data.csv). Data finns tillgänglig för influensa A-virus från vecka 42 2022 och för influensa B-virus från vecka 12 2023, uppdateras veckovis.

**Citera data:**

Székely, A. J., Malmberg, M., Vargas, J., Mohamed, N., Dafalla, I., Petrini, F., Davies, L. (2023). Dataset of SARS-CoV-2, influenza A and influenza B virus content in wastewater samples from wastewater treatment plants in Sweden. <https://doi.org/10.17044/scilifelab.14256317>.

## Metoder

För de flesta städer som representeras på den här sidan används flödeskompenserade provtagare vid avloppsreningsverken (WWTP) för att samla in råa, obehandlade avloppsprover representativa för en enskild dag. Uppsala är undantaget, där prover samlas in dagligen och sedan kombineras flödesproportionellt till ett sammansatt veckoprov som används för analyserna.

Det virala genomiska materialet från de insamlade proverna extraheras med en metod som använder Maxwell RSC Enviro TNA-kitet (Promega).

Absolut kvantifiering av antalet kopior av influensa A- och B-virusgenom görs med metoden One-Step RT-qPCR och Flu SC2 Multiplex-testet från Centers for Disease Control and Prevention (CDC). För att korrigera för variation i population och avloppsvattenflöde kvantifieras förekomsten av viruset pepper mild mottle virus (PMMoV), ett växtvirus från peppar som människor får i sig via maten. PMMoV kvantifieras med hjälp av en modifierad version av testet i [Zhang et al. (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV är det vanligaste RNA-viruset i avföring från människa och används för att uppskatta mängden avföring från människa i avloppsvattenprover [Symonds et al., (2019)](https://doi.org/10.1371/journal.ppat.1007639).

Data som presenteras i grafen visar förhållandet mellan det kopieantal som uppmätts med Flu SC2 Multiplex-testet och PMMoV-testet, multiplicerat med 1000. Resultat från Flu SC2 Multiplex-testet är en proxy för mängden influensa A- och B-virus i avloppsvattnet och PMMoV är en proxy för mängden avföring från människa i avloppsvattnet. Detta förhållande kan i sin tur anses vara en proxy för andelen influensa A- och B-infektioner i populationen i avloppsvattnets upptagningsområde.
