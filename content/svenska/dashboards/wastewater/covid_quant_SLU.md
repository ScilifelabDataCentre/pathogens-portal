---
title: Mängd SARS-COV-2 i avloppsvatten (SEEC-SLU)
plotly: true
---

<div class="mt-3">
  <a href="/sv/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Gå tillbaka till SARS-CoV-2-kvantifiering inom avloppsvattenbaserad epidemiologi-dashboarden</a>
</div>
<br>

## Introduktion

Data som presenteras på denna sida genereras i Sveriges lantbruksuniversitets (SLU) laboratorier vid Svenskt Miljöepidemiologiskt Centrum (SEEC). Projektet ingår i [SciLifeLab's Pandemic Laboratory Preparedness (PLP) Program](/resources/) och leds av docent Anna J. Székely (Institutionen för vatten och miljö, SLU). Avloppsanalyserna övervakas av Anna J. Székely och docent Maja Malmberg (Institutionen för biomedicin och veterinär folkhälsovetenskap, sektionen för virologi, SLU). Denna sida visar kvantifiering av nivåerna av SARS-CoV-2-virus i flera orter över hela Sverige. Projektet har för närvarande den bredaste geografiska täckningen i Sverige och genererar data som täcker 22% av den svenska befolkningen.

Data och visualiseringar på den här sidan uppdateras vanligtvis veckovis, oftast på fredagar. Notera att de poäng som tillhandahålls i datasetet och som visas i grafen nedan är preliminära, så korrigeringar och ändringar kan förekomma. Data och information om metod som används uppdateras kontinuerligt.

## Insamlingsplatser för avloppsvatten

SLU-SEEC samlar in och analyserar prover från ett flertal orter/städer. Nedan visas en tabell med detaljerad information om alla insamlingsplatser. Tabellen listar orter/städer som monitoreras, avloppsreningsverk (WWTP) där proverna samlas in, antal personer i upptagningsområdet (antal invånare), mellan vilka datum  SLU-SEEC mätningarna skett  (startdatum och slutdatum).  Ett värde ’null’ istället för slutdatum innebär att insamlingen fortfarande pågår. En asterisk bredvid antal invånare innebär att antal invånare är preliminärt.

  <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_slusites.json" height="775px" >}}</div>
</div>

<!-- <p>
  <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapseExample1" role="button" aria-expanded="false" aria-controls="collapseExample1">
    Genomics data
  </a>
</p>
<div class="collapse" id="collapseExample1">
  <div class="card card-body">
  <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_slusites.json" height="775px" width="800px" >}}</div>
</div>
  </div>
</div> -->

<!-- <button type="button" class="btn btn-sm btn-outline-secondary mb-2" data-bs-toggle="modal" data-bs-target="#interactiveFeaturesModal">
  How to use the interactive features of the plot
</button> -->

<!-- <div class="modal fade" id="interactiveFeaturesModal" tabindex="-1" aria-labelledby="interactiveFeaturesModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="interactiveFeaturesModalLabel">Information on how to use the interactive features of the plot</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_slusites.json" height="600px" >}}</div>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div> -->

## Visualiseringar

<div class="alert alert-info">Senast uppdaterad: <span id="last_modified_uppsala"></span></div>

<b>Notera:</b> Historisk data för Knivsta, Vaxholm och Österåker finns tillgänglig i det länkade datasetet ovan och ingår inte längre i visualiseringen nedan.

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

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_regular.json" height="550px" >}}</div>
</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/combined_slu_regular.py).

## Kommentarer från forskargruppen

<div><b>Datum:</b> <span id="slu_comment_date"></span><br><b>Kommentar:</b> <span id="slu_comment"></span></div>

{{< ww_dynamic_content >}}

## Rapporter från forskargruppen

Forskargruppen delar även en rapport som sammanfattar den senaste informationen från deras avloppsvattenmätningar. Den senaste rapporten finns tillgänglig som pdf [här](https://blobserver.dckube.scilifelab.se/blob/Latest_weekly_report_SEEC-SLU) (endast tillgänglig på svenska).

## Dataset

**Kontakt:** anna.szekely@slu.se and maja.malmberg@slu.se

**Ladda ner data:** [N1-gene copy number per PMMoV gene copy number, CSV file.](https://datagraphics.dckube.scilifelab.se/dataset/0ac8fa02871745048491de74e5689da9.csv). Data are available from week 38 of 2020; updated weekly.

**Hur man citerar dataset:**

Székely, A. J., Vargas, J., Mohamed, N., Dafalla, I., Malmberg, M. (2021). Dataset of SARS-CoV-2 wastewater data from various towns in Sweden. [https://doi.org/10.17044/scilifelab.14256317](https://doi.org/10.17044/scilifelab.14256317).

**Hur man citerar metod:**

Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. *Environments*, *9*, 39. [https://doi.org/10.3390/environments9030039](https://doi.org/10.3390/environments9030039).

## Metoder

För de flesta städer på den här sidan samlas obehandlade avloppsvattenprover, representativa för en enskild dag, in av flödeskompenserade provtagare vid avloppsreningsverken (WWTP). Uppsala är undantaget, där alla mätningar sedan vecka 16 2021 istället representerar en vecka. Där samlas prover in dagligen och kombineras sedan flödesproportionellt till ett sammansatt veckoprov för följande analyser.

Proverna bearbetas enligt standardmetoder. För prover som samlats in fram till och med vecka 18 2021 koncentrerades virala partiklar med hjälp av elektronegativ filtrering ([Ahmed *et al.*, 2020](https://www.sciencedirect.com/science/article/pii/S004896972033480X)). Från vecka 19 2021 har det virala genomiska materialet istället koncentrerats och extraherats med hjälp av en metod som använder Maxwell RSC Enviro TNA-kitet (Promega). Absolut kvantifiering av antalet kopior av SARS-CoV-2-genomet utförs med ett [SARS-CoV-2 specifikt N1-test från Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/coronavirus/2019-ncov/lab/rt-pcr-panel-primer-probes.html). För att korrigera för variation i population och avloppsvattenflöde kvantifierar gruppen förekomsten av viruset Pepper mild mottle virus (PMMoV), ett växtvirus från peppar som människor får i sig via maten, med hjälp av en modifierad version av testet i [Zhang *et al.* (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV är det vanligaste RNA-viruset i avföring från människa och används för att uppskatta mängden avföring från människa i avloppsvattenprover ([Symonds *et al.*, 2019](https://doi.org/10.1371/journal.ppat.1007639)).  För mer information om hur normaliseringsmetoden utvärderats se [Isaksson *et al.* (2022)](https://www.mdpi.com/2076-3298/9/3/39).

Data som presenteras i grafen är ett ratio av kopieantal som uppmätts med N1- och PMMoV-analyserna, multiplicerat med 10^4. N1-kopieantal är en proxy för mängd SARS-CoV-2 i avloppsvatten och PMMoV är en proxy för mängd avföring från människa, vilket i sin tur är relaterat till befolkningen som bidrar till avloppsvattnet. Detta ratio kan i sin tur anses vara en proxy för andelen infekterade individer i populationen i avloppsvattnets upptagningsområde.

## Arkiverade data

- [Historiska data för Örebro och Umeå, mängd SARS-CoV-2 i avloppsvatten från Umeå respektive Örebro mellan oktober 2020 och juni 2021.](/sv/dashboards/wastewater/historic_orebro_umea).

<br>
<div class="mt-3">
  <a href="/sv/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Gå tillbaka till SARS-CoV-2-kvantifiering inom avloppsvattenbaserad epidemiologi-dashboarden</a>
</div>
