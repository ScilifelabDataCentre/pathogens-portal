---
title: Mängd influensa A- och influensa B-virus i avloppsvatten
plotly: true
banner: /dashboard_thumbs/wastewater_influenza.png
description: Den presenterar data om influensa A- och B-virusnivåer i avloppsvatten över hela Sverige, analyserade av SLU som en del av SciLifeLabs PLP-program. Det är ett nyckelverktyg för att övervaka influensatrender på samhällsnivå genom övervakning av avloppsvatten.
menu:
 dashboard_menu:
    identifier: wastewater_influenza_quantification
    name: "Avloppsvatten: Kvantifiering av influensa (SLU)"
    weight: 30
aliases:
  - /sv/dashboards/wastewater/influenza_quantification/
dashboards_topics: [Wastewater Surveillance, Influenza, Epidemiology]
---

## Introduktion

Influensavirus är enkelsträngade, segmenterade RNA-virus inom familjen Orthomyxoviridae. Influensa A- och influensa B-virus orsakar säsongsbetonade epidemier av influensa, en mycket smittsam luftvägssjukdom som kännetecknas av symptom som feber, hosta, halsont, värk i kroppen och trötthet, men diarré och kräkningar kan också förekomma. Influensa A-virus är utbrett bland sjöfåglar men infekterar också andra fågelarter och olika däggdjur, inklusive människor och grisar, medan influensa B-virus främst infekterar människor. Influensavirus muterar snabbt, vilket leder till olika stammar och säsongsbetonade utbrott. Både influensa A- och B-virus kan orsaka säsongsbetonade utbrott, men endast influensa A är känt för att orsaka pandemier på grund av att viruset kan smitta olika arter och den potentiella möjligheten till genetisk rekombination mellan olika djurarter. Globalt uppskattas säsongsinfluensan orsaka 290 000–645 000 dödsfall per år.

Data som presenteras på denna sida genereras i Sveriges lantbruksuniversitets (SLU) laboratorier vid Svenskt Miljöepidemiologiskt Centrum (SEEC). Projektet ingår i <a target="_blank" href="https://www.pathogens.se/resources/">SciLifeLab’s Pandemic Laboratory Preparedness (PLP) Program</a> och leds av docent Anna J. Székely (Institutionen för vatten och miljö, SLU). Avloppsanalyserna övervakas av Anna J. Székely, Javier Vargas och Maja Malmberg (Institutionen för biomedicin och veterinär folkhälsovetenskap, sektionen för virologi, SLU). Denna sida visar kvantifiering av nivåerna av influensa A- och B-virus i flera orter över hela Sverige. Projektet har för närvarande den bredaste geografiska täckningen i Sverige och genererar data som täcker 43% av den svenska befolkningen.

Data och visualiseringar på den här sidan uppdateras vanligtvis veckovis, oftast på fredagar. Notera att de poäng som tillhandahålls i datasetet och som visas i grafen nedan är preliminära, så korrigeringar och ändringar kan förekomma. Data och information om gruppen på den här dashboarden uppdateras kontinuerligt.

## Insamlingsplatser för avloppsvatten

SLU-SEEC samlar in och analyserar prover för kvantifiering av nivåerna av influensa A- och influensa B-virus från ett flertal orter. Nedan visas en tabell med detaljerad information om alla insamlingsplatser. Tabellen listar orter som övervakas, avloppsreningsverk (WWTP) där proverna samlas in, antal personer i upptagningsområdet (Number of people), mellan vilka datum SLU-SEEC mätningarna skett (Start date och End date). Notera att 'Start date' avser det datum då övervakning av influensa A startade, men att startdatumet för influensa B alltid är senare. Ett värde ’null’ istället för slutdatum innebär att insamlingen fortfarande pågår. En asterisk (\*) bredvid antal invånare innebär att värdet är uppskattat baserat på hur många invånare som reningsverket betjänar (BOD-7). Två asterisker (\*\*) bredvid staden/staden indikerar att data endast är tillgänglig för influensa A, och inte influensa B. Informationen i tabellen nedan är [tillgänglig för nedladdning som en excel-fil](https://blobserver.dc.scilifelab.se/blob/SLU_INF_collection_sites.xlsx).

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_sluINFsites.json" height="750px" >}}</div>
</div>

## Visualiseringar

<div class="alert alert-info">Last updated: <span id="last_modified_slu_flu"></span></div>

**Notera** att även om samma metoder används för alla städer som visas på den här fliken, kan skillnader i befolkningen och hur avloppsvatten samlas in i olika städer påverka jämförelser dem emellan.

### Influensa A

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_slu_infA_v1.0.json" height="800px" >}}</div>
</div>

**Källkod som används för att skapa grafen:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/combined_slu_influenza_a.py).

### Influensa B

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_slu_infB_v1.0.json" height="800px" >}}</div>
</div>

**Källkod som används för att skapa grafen:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/combined_slu_influenza_b.py).

## Kommentarer från forskargruppen

<div><b>Date:</b> <span id="slu_flu_comment_date"></span><br><b>Commentary:</b> <span id="slu_flu_comment"></span></div>

{{< ww_dynamic_content >}}

## Rapporter från forskargruppen

Forskargruppen tillhandahåller en rapport som sammanfattar information från deras avloppsvattenmätningar. Den senaste rapporten finns tillgänglig som pdf [här](https://blobserver.dc.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU.pdf) (endast tillgänglig på svenska).

## Dataset

**Kontakt:** <anna.szekely@slu.se> and <javier.vargas@slu.se>

**Ladda ner data:** [Genkopieantal för luftvägsvirus normaliserat mot PMMoV-genkopieantal.CSV fil](https://blobserver.dc.scilifelab.se/blob/SLU_wastewater_data.csv). Data finns tillgänglig för influensa A-virus från vecka 42 2022 och för influensa B-virus från vecka 12 2023, uppdateras veckovis.

**Citera data:**

Székely, A. J., Malmberg, M., Vargas, J., Mohamed, N., Dafalla, I., Petrini, F., Davies, L. (2023). Dataset of SARS-CoV-2, influenza A and influenza B virus content in wastewater samples from wastewater treatment plants in Sweden. <https://doi.org/10.17044/scilifelab.14256317>.

## Metoder

För de flesta städer som representeras på den här sidan används flödeskompenserade provtagare vid avloppsreningsverken (WWTP) för att samla in råa, obehandlade avloppsprover representativa för en enskild dag. Uppsala är undantaget, där prover samlas in dagligen och sedan kombineras flödesproportionellt till ett sammansatt veckoprov som används för analyserna.

Det virala genomiska materialet från de insamlade proverna extraheras med en metod som använder Maxwell RSC Enviro TNA-kitet (Promega).

Absolut kvantifiering av antalet kopior av influensa A- och B-virusgenom görs med metoden One-Step RT-qPCR och Flu SC2 Multiplex-testet från Centers for Disease Control and Prevention (CDC). För att korrigera för variation i population och avloppsvattenflöde kvantifieras förekomsten av viruset pepper mild mottle virus (PMMoV), ett växtvirus från peppar som människor får i sig via maten. PMMoV kvantifieras med hjälp av en modifierad version av testet i [Zhang et al. (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV är det vanligaste RNA-viruset i avföring från människa och används för att uppskatta mängden avföring från människa i avloppsvattenprover [Symonds et al., (2019)](https://doi.org/10.1371/journal.ppat.1007639).

Data som presenteras i grafen visar förhållandet mellan det kopieantal som uppmätts med Flu SC2 Multiplex-testet och PMMoV-testet, multiplicerat med 1000. Resultat från Flu SC2 Multiplex-testet är en proxy för mängden influensa A- och B-virus i avloppsvattnet och PMMoV är en proxy för mängden avföring från människa i avloppsvattnet. Detta förhållande kan i sin tur anses vara en proxy för andelen influensa A- och B-infektioner i populationen i avloppsvattnets upptagningsområde.
