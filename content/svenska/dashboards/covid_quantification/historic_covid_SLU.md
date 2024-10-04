---
title: Historiska SARS-CoV-2-data i avloppsvatten från SEEC-SLU
plotly: true
---

## Introduktion

Data som presenteras på denna sida genererades i SLU:s (Sveriges lantbruksuniversitet) laboratorier av SEEC (Swedish Environmental Epidemiology Center). Projektet var en del av [SciLifeLabs Pandemic Laboratory Preparedness (PLP) Program](/resources/), ledd av Anna J. Székely (Institutionen för vatten och miljö, SLU). Avloppsvattenanalyser övervakades av Anna J. Székely och Maja Malmberg (Virologienheten vid Institutionen för biomedicinsk vetenskap och veterinär folkhälsovetenskap, SLU). Denna sida handlar om den historiska kvantifieringen av nivåerna av SARS-CoV-2-virus i flera städer över hela Sverige. Projektet hade den bredaste geografiska täckningen över Sverige och genererade data för 43% av den svenska befolkningen.

Observera att data och visualiseringar på denna sida inte längre uppdateras. Poängen i datasetet och som avbildas i diagrammen är slutgiltiga, även om mindre korrigeringar kan ha tillämpats i efterhand. Denna instrumentpanel fungerar som en post över projektets resultat under den aktiva övervakningsperioden.

## Insamlingsplatser för avloppsvatten

SLU-SEEC samlar in och analyserar prover från ett flertal orter. Nedan visas en tabell med detaljerad information om alla insamlingsplatser. Tabellen listar orter som övervakas, avloppsreningsverk (WWTP) där proverna samlas in, antal personer i upptagningsområdet (antal invånare), mellan vilka datum SLU-SEEC mätningarna skett (startdatum och slutdatum). Ett värde ’null’ istället för slutdatum innebär att insamlingen fortfarande pågår. En asterisk bredvid antal invånare innebär att värdet är uppskattat baserat på hur många invånare som reningsverket betjänar (BOD-7). Informationen i tabellen nedan är [tillgänglig för nedladdning som en excel-fil](https://blobserver.dc.scilifelab.se/blob/SLU_COVID_collection_sites.xlsx).

  <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_sluCOVIDsites.json" height="850px" >}}</div>
</div>

## Visualiseringar

<div class="alert alert-info">Last updated: 2024-09-30</span></div>

<b>Notera:</b> Historisk data för Ekerö, Enköping, Knivsta, Tierp, Vaxholm, Älvkarleby, och Österåker finns tillgänglig i det länkade datasetet ovan och ingår inte längre i visualiseringen nedan.

Notera också att även om samma metoder används för alla städer som visas på den här fliken, kan skillnader i befolkningen och hur avloppsvatten samlas in i olika städer påverka jämförelser dem emellan.

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
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/historic_wastewater_combined_slu_regular.json" height="800px" >}}</div>
</div>

**Källkod som används för att skapa grafen:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/archive/historic_combined_slu_regular.py).

## Kommentarer från forskargruppen

<div><b>Date:</b> 2024-03-20<br><b>Commentary:</b> An error occurred during the processing of the data for week 11-2024, due to a normalization issue. Consequently, the SCV2 data appeared to be 16 times higher and the influenza A data 4 times higher than their actual values. We identified and corrected this error the following day while preparing our official report, and promptly updated the website. We appreciate those who brought this to our attention and apologize to anyone alarmed by the inaccurate results. It's important to note that the data on the website is always preliminary. Please feel free to contact us with any questions or concerns.</div>

## Rapporter från forskargruppen

Forskargruppen tillhandahåller även en rapport som sammanfattar informationen från deras avloppsvattenmätningar. Den senaste rapporten finns tillgänglig som pdf [här](https://blobserver.dc.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU.pdf) (endast tillgänglig på svenska).

## Dataset

**Kontakt:** <anna.szekely@slu.se> och <javier.vargas@slu.se>

**Ladda ner data:** [Genkopieantal av luftvägsvirus normaliserat mot PMMoV-genkopieantal, CSV fil.](https://blobserver.dc.scilifelab.se/blob/historic_SLU_wastewater_data.csv). Data finns tillgängligt från vecka 38 2020 och uppdateras veckovis.

**Citera datasetet:**

Székely, A. J., Malmberg, M., Vargas, J., Mohamed, N., Dafalla, I., Petrini, F., Davies, L. (2023). Dataset of SARS-CoV-2, influenza A and influenza B virus content in wastewater samples from wastewater treatment plants in Sweden. <https://doi.org/10.17044/scilifelab.14256317>.

**Citera metoden:**

Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. _Environments_, _9_, 39. <https://doi.org/10.3390/environments9030039>.

## Metoder

För de flesta städer som representeras på den här sidan används flödeskompenserade provtagare vid avloppsreningsverken (WWTP) för att samla in råa, obehandlade avloppsprover representativa för en enskild dag. Uppsala är undantaget, där prover samlas in dagligen och sedan kombineras flödesproportionellt till ett sammansatt veckoprov som används för analyserna.

Proverna bearbetas enligt standardmetoder. För prover som samlats in fram till och med vecka 18 2021 koncentrerades virala partiklar med hjälp av elektronegativ filtrering ([Ahmed _et al._, 2020](https://www.sciencedirect.com/science/article/pii/S004896972033480X)). Från vecka 19 2021 har det virala genomiska materialet istället koncentrerats och extraherats med hjälp av en metod som använder Maxwell RSC Enviro TNA-kitet (Promega).

Absolut kvantifiering av antalet kopior av SARS-CoV-2-genomet utförs med ett One-Step RT-qPCR. Till och med vecka 31 2023 kvantifierades virusgenom med ett [SARS-CoV-2 specifikt N1-test från Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/coronavirus/2019-ncov/lab/rt-pcr-panel-primer-probes.html). För att korrigera för variation i population och avloppsvattenflöde kvantifieras förekomsten av pepper mild mottle virus (PMMoV), ett växtvirus från peppar som människor får i sig via maten. PMMoV kvantifieras med hjälp av en modifierad version av testet i [Zhang _et al._ (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV är det vanligaste RNA-viruset i avföring från människa och används för att uppskatta mängden avföring från människa i avloppsvattenprover ([Symonds _et al._, 2019](https://doi.org/10.1371/journal.ppat.1007639)). För mer information om hur normaliseringsmetoden utvärderats se [Isaksson _et al._ (2022)](https://www.mdpi.com/2076-3298/9/3/39).

Data som presenteras i grafen visar förhållandet mellan det kopieantal som uppmätts med Flu SC2 Multiplex-testet och PMMoV-testet, multiplicerat med 1000. Resultat från Flu SC2 Multiplex-testet är en proxy för mängden SARS-CoV-2 i avloppsvattnet och PMMoV är en proxy för mängden avföring från människa i avloppsvattnet. Detta förhållande kan i sin tur anses vara en proxy för andelen infekterade individer i populationen i avloppsvattnets upptagningsområde. För att kunna jämföra den data som genereras med den nuvarande metoden med data som genererats med tidigare metoder och kvantifieringsanalyser, har äldre data omvandlats med hjälp av omvandlingsfaktorer. Omvandlingsfaktorerna beräknas baserat på jämförelseperioder när gamla och nya metoder använts parallellt.

