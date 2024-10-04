---
title: SARS-CoV-2 kvantifiering
banner: /dashboard_thumbs/wastewater_sars-cov2.png
description: Utforska SARS-CoV-2-nivåer i avloppsvatten över hela Sverige. Veckodata från SLU-SEEC spårar covid-19-trender, som täcker 43 % av befolkningen, och hjälper till att förutsäga utbrott.
menu:
  dashboard_menu:
    identifier: wastewater_SARS-CoV-2_quantification
    name: "Avloppsvatten: SARS-CoV-2 kvantifiering"
plotly: true
aliases:
  - /sv/dashboards/wastewater/covid_quant_slu/
  - /sv/dashboards/wastewater/covid_quantification/
  - /sv/dashboards/wastewater/covid_quantification/covid_quant_slu/
dashboards_topics: [Wastewater Surveillance, COVID-19, Infectious diseases, Epidemiology]
data_status: "updating"
---


## Introduktion

Severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2) är ett enkelsträngat RNA-virus som orsakar COVID-19 (coronavirus disease 2019), den luftvägsinfektion som orsakade COVID-19-pandemin. SARS-CoV-2 identifierades först i staden Wuhan, Hubei, Kina, och Världshälsoorganisationen (WHO) deklarerade att viruset var ett internationellt akut hot mot människors hälsa mellan den 30 januari 2020 och 5 maj 2023. För mer information om symtom, risker och vaccination mot influensavirus, besök [Folkhälsomyndighetens motsvarande sida](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/covid-19/).

SARS-CoV-2-viruspartiklar kan utsöndras via andningsdroppar, aerosoler och kan även förekomma i avföringen hos smittade individer. Detta möjliggör att SARS-CoV-2-viruset kan upptäckas i avloppsvatten och att infektionstrender på populationsnivå av COVID-19 kan följas genom avloppsvattenbaserad epidemiologi (på engelska wastewater-based epidemiology, WBE). 

Data som presenteras på denna sida genereras i Sveriges lantbruksuniversitets (SLU) laboratorier vid Svenskt Miljöepidemiologiskt Centrum (SEEC). Data och visualiseringar på den här sidan uppdateras vanligtvis veckovis, oftast på måndagar. För en omfattande förståelse, vänligen hänvisa till [Metoder](#metoder) avsnittet. För en allmän översikt om avloppsvattenövervakning, vänligen besök [Avloppsbaserad epidemiologi i Sverige](/dashboards/wastewater_background/)

<div class="alert alert-info">
<b>Viktig notering:</b></br>
Notera att de poäng som tillhandahålls i datasetet och som visas i grafen nedan är preliminära, så korrigeringar och ändringar kan förekomma. Data och information om gruppen på den här dashboarden uppdateras kontinuerligt. </br>Notera också att även om samma metoder används för alla städer som visas på den här fliken, kan skillnader i befolkningen och hur avloppsvatten samlas in i olika städer påverka jämförelser dem emellan.
</div>

## Visualiseringar

<div class="alert alert-info">Senast uppdaterad: <span id="last_modified_uppsala"></span></div>

<button type="button" class="btn btn-sm btn-outline-secondary mb-2" data-bs-toggle="modal" data-bs-target="#interactiveFeaturesModal">
  Hur du kan använda grafens interaktiva funktioner
</button>

 <div class="modal fade" id="interactiveFeaturesModal" tabindex="-1" aria-labelledby="interactiveFeaturesModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="interactiveFeaturesModalLabel">Information om hur du kan använda grafens interaktiva funktioner</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>Visualiseringar på den här sidan har flera interaktiva funktioner. Du kan använda funktionerna för att visualisera tillgängliga SARS-COV-2 avloppsvattendata på olika sätt. Du kan till exempel välja att endast se data inom ett visst tidsintervall, eller från en given ort. Nedan förklarar vi hur du själv kan bestämma hur du gör inställningarna med de tillgängliga interaktiva funktionerna.</p><h6>Visa endast en ort</h6>
        <p>För att endast visa data från en ort dubbelklicka på ortsnamnet i baneret till höger. För att avmarkera en ort klicka endast en gång på ortsnamnet. Om en ort avmarkeras kommer denna gråmarkeras och ortens data visas inte i grafen. I inställningar är alla orter markerade i startläget. För att avmarkera alla orter tryck "Deselect all areas" knappen. Du kan markera alla orter igen genom "Reselect all areas" knappen.</p>
        <h6>Visulisera endast vissa intervall på x eller y-axel</h6>
        <p>I diagrammen nedan representerar y-axeln kopiantalet för SARS-CoV-2 i förhållande till PMMoV medan x-axeln representerar datumet. Om du vill se värden inom ett givet värdeintervall på axlarna kan du göra detta genom att klicka och dra med musen. Till exempel, för att se all data inom en given tidsram kan du klicka nära startdatumet på x-axeln och dra för att skapa en rektangel som omfattar hela y-axeln och det datumintervall på x-axeln som du vill ha att se. Grafen kommer sedan att zooma in i intervallet som du valt.</p>
        <h6>Att utläsa exakta mätvärden</h6>
        <p>Det kan vara svårt att exakt läsa de exakta mätvärdena på data från en graf. För att se det exakta datavärdet, håll muspekaren över datapunkten av intresse. En ruta kommer att visas som visar y-axelvärdena för alla mätplatser för ett visst datum (dvs det x-axelvärdet).</p>
        <h6>Andra funktioner</h6>
        <p>Om du håller muspekaren över grafen kommer du att se några ytterligare alternativa funktioner som grå ikoner uppe till höger. Du kan använda dessa funktioner för att zooma in/ut ur (med hjälp av + och - ikonerna), och för att ändra skalan på axlarna så att data från de "valda" platserna visas på de mest lämpliga axlarna (detta kan göras med hjälp av autoskala eller återställ axlar, som ser ut som en ruta som innehåller pilar respektive ett hus).</p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Stäng</button>
      </div>
    </div>
  </div>
</div>

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 1200px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_combined_slu_regular.json" height="800px" >}}</div>
</div>

**Källkod som används för att skapa grafen:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/combined_slu_regular.py).

## Kommentarer från forskargruppen

<div><b>Datum:</b> <span id="slu_comment_date"></span><br><b>Kommentar:</b> <span id="slu_comment"></span></div>

{{< ww_dynamic_content >}}

## Rapporter från forskargruppen

Forskargruppen tillhandahåller även en rapport som sammanfattar informationen från deras avloppsvattenmätningar. Den senaste rapporten finns tillgänglig som pdf [här](https://blobserver.dc.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU.pdf) (endast tillgänglig på svenska).

## Dataset

**Kontakt:** <anna.szekely@slu.se> och <javier.vargas@slu.se>

**Ladda ner data:** [Genkopieantal av luftvägsvirus normaliserat mot PMMoV-genkopieantal, CSV fil.](https://blobserver.dc.scilifelab.se/blob/SLU_wastewater_data.csv). Data finns tillgängligt från vecka 38 2020 och uppdateras veckovis.

**Citera datasetet:**

Székely, A. J., Malmberg, M., Vargas, J., Mohamed, N., Dafalla, I., Petrini, F., Davies, L. (2023). Dataset of SARS-CoV-2, influenza A and influenza B virus content in wastewater samples from wastewater treatment plants in Sweden. <https://doi.org/10.17044/scilifelab.14256317>.

## Metoder

Avloppsvatten samlas in från flera olika reningsverk runt om i landet. För mer information om reningsverken, besök sidan om [bakgrunden till avloppsvattenövervakning](/dashboards/wastewater_background/). För de flesta städer som representeras på den här sidan används flödeskompenserade provtagare vid avloppsreningsverken (WWTP) för att samla in råa, obehandlade avloppsprover representativa för en enskild dag. Uppsala är undantaget, där prover samlas in dagligen och sedan kombineras flödesproportionellt till ett sammansatt veckoprov som används för analyserna.

Proverna bearbetas enligt standardmetoder. För prover som samlats in fram till och med vecka 18 2021 koncentrerades virala partiklar med hjälp av elektronegativ filtrering ([Ahmed _et al._, 2020](https://www.sciencedirect.com/science/article/pii/S004896972033480X)). Från vecka 19 2021 har det virala genomiska materialet istället koncentrerats och extraherats med hjälp av en metod som använder Maxwell RSC Enviro TNA-kitet (Promega).

Absolut kvantifiering av antalet kopior av SARS-CoV-2-genomet utförs med ett One-Step RT-qPCR. Till och med vecka 31 2023 kvantifierades virusgenom med ett [SARS-CoV-2 specifikt N1-test från Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/coronavirus/2019-ncov/lab/rt-pcr-panel-primer-probes.html). För att korrigera för variation i population och avloppsvattenflöde kvantifieras förekomsten av pepper mild mottle virus (PMMoV), ett växtvirus från peppar som människor får i sig via maten. PMMoV kvantifieras med hjälp av en modifierad version av testet i [Zhang _et al._ (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV är det vanligaste RNA-viruset i avföring från människa och används för att uppskatta mängden avföring från människa i avloppsvattenprover ([Symonds _et al._, 2019](https://doi.org/10.1371/journal.ppat.1007639)). För mer information om hur normaliseringsmetoden utvärderats se [Isaksson _et al._ (2022)](https://www.mdpi.com/2076-3298/9/3/39).

Data i graferna och datafilen presenteras i tre olika format:

- **PMMoV-normaliserat SARS-CoV-2-innehåll** visar förhållandet mellan det kopieantal som uppmätts med SARS-CoV-2-testet och PMMoV-testet, multiplicerat med 1000. Eftersom SARS-CoV-2-testet ger en proxy för SARS-CoV-2-virusmängd i avloppsvattnet och PMMoV är en proxy för avföringsinnehållet (som är relaterat till den bidragande befolkningen) kan förhållandet mellan de två betraktas som en proxy för förekomsten av SARS-CoV-2-infektioner i befolkningen i avloppsvattnets upptagningsområde.
- **Koncentration av SARS-CoV-2-genomkopior** visar koncentrationen av SARS-CoV-2-kopienummer som uppmäts i avloppsvattnet. Dessa data påverkas av hur de olika avloppsvattensystemen är uppbyggda och lämpar sig därför inte för jämförelse mellan platser. Virushalten i avloppsvattnet påverkas också av väderhändelser som påverkar avloppsflödet (t.ex. kraftigt regn eller snösmältning).
- **SARS-CoV-2-genomkopior/dag/invånare** representerar den uppskattade dagliga virusmängden i avloppsvattnet normaliserad för antalet invånare anslutna till systemet. Dessa data går att jämföra mellan olika platser. Vissa fördröjningar i presentationen av dessa data kan förekomma, jämfört med de andra analyserna.

**Citera metoden:**

Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. _Environments_, _9_, 39. <https://doi.org/10.3390/environments9030039>.

## Relaterade dataset

- Genomiska SARS-CoV-2 analyser från avloppsvatten (data tillgängligt på European Nucleotide Archive (ENA) under projektnummer [PRJEB60156](https://www.ebi.ac.uk/ena/browser/view/PRJEB60156)). Forskargruppen från SLU har analyserat avloppsvattenprover från Uppsala, Örebro, Umeå och Kalmar (2021-2022).

## Arkiverade data

- [Historiska data för Örebro och Umeå, mängd SARS-CoV-2 i avloppsvatten från Umeå respektive Örebro mellan oktober 2020 och juni 2021](/sv/dashboards/covid_quantification/historic_orebro_umea).
- [Historiska SARS-CoV-2-data i avloppsvatten från SEEC-SLU](/dashboards/covid_quantification/historic_covid_SLU)

## Kvantifiering av SARS-CoV-2 av andra grupper

Andra grupper kvantifierade också SARS-CoV-2 i avloppsvatten i Sverige. Grupperna använde olika metoder för att kvantifiera SARS-CoV-2 och mätte i vissa fall olika områden av Sverige. All data från grupperna nedan är historisk:

- [**Göteborgs universitet (GU):**](/sv/dashboards/covid_quantification/covid_quant_gu/) Kvantifiering av mängd SARS-CoV-2 i avloppsvatten från Göteborg från Helene Norders forskargrupp vid GU.

- [**SEEC-KTH noden:**](/sv/dashboards/covid_quantification/covid_quant_kth/)Kvantifiering av mängd SARS-CoV-2 i avloppsvatten från Malmö, Stockholm och Göteborg från forskargruppen SEEC-KTH (uppdateras inte efter juni 2023, historiska data finns tillgängliga).

