---
title: Mängd SARS-CoV-2 virus i avloppsvatten från svenska städer
toc: true
menu:
  swe_menu:
      identifier: wastewater
      name: Mängd SARS-CoV-2 virus i avloppsvatten från svenska städer
      weight: 20
      parent: dashboards
plotly: true
aliases:
    - /sv/data_types/environment/wastewater/
    - /sv/data_types/environment/
---

## Introduktion

Övervakning av SARS-CoV-2 virus i avloppsvatten kan vara effektivt för att kartlägga smittspridning av Covid-19 och även fungera som ett tidigt varningssystem för kommande utbrott. För en allmän introduktion till avloppsvattensepidemiologi, [vänligen se nedan](#bakgrund-avloppsvattenbaserad-epidemiologi).

I vår dashboard presenteras epidemiologiska data från mätningar av SARS-CoV-2 virus i avloppsvatten från ett antal svenska städer, motsvarande över 3 miljoner invånare. Data och resultat som presenteras här kommer från analyser som utförts av två laboratorier vid [Svenskt Miljöepidemiologiskt Centrum (SEEC)](https://www.scilifelab.se/pandemic-response/pandemic-laboratory-preparedness/swedish-environmental-epidemiology-center-seec/). SEEC är ett projekt för att utveckla resurser för pandemisk beredskap inom [SciLifeLabs Pandemic Preparedness Program](https://www.scilifelab.se/pandemic-response). Proverna analyseras av SEECs två noder.

- **SEEC-SLU:** Prover från Uppsala, Örebro, Umeå, bland andra, analyseras vid Sveriges Lantbruksuniversitets (SLUs) nod under ledning av docent Anna J. Székely (anna.szekely@slu.se) och docent Maja Malmberg (maja.malmberg@slu.se).

- **SEEC-KTH:** Prover från Stockholm och Malmö analyseras vid KTH Kungliga Tekniska Högskolans nod som leds av docent Zeynep Cetecioglu Gurol (zeynepcg@kth.se).

Notera att det finns mindre skillnader mellan detektionsmetoderna som de två grupperna använder. Detta måste tas i åtanke vid jämförelser av avloppsvattendata. För att korrigera för variation i population och avloppsvattenflöde använder båda grupperna Pepper mild mottle virus (PMMoV) enligt en modifierad metod av [Zhang *et al.* (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV är det vanligaste RNA-viruset i mänsklig avföring och används för att estimera mängd mänsklig avföring i proverna ([Symonds *et al.*, 2019](https://doi.org/10.1371/journal.ppat.1007639)). För att kvantifiera mängd SARS-CoV-2 virus, använder SEEC-SLU noden en SARS-CoV-2 specifik [N1 assay från Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov/coronavirus/2019-ncov/lab/rt-pcr-panel-primer-probes.html), medan SEEC-KTH noden använder SARS-like virus specifika N3-primers ([Lu *et al.*, 2020](https://doi.org/10.3201/eid2608.201246)) och SYBR Green ([Perez-Zabaleta *et al.*, 2023](https://doi.org/10.1016/j.scitotenv.2022.160023)). Skillnader i insamlingsmetod av avloppsvattenprov och olika befolkningsmängd i olika städer kan ge en bias vilket gör ett svårt att jämföra virusmängd mellan olika städer, även om samma metod använts.

## Karta över platser där prover samlas in

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_map_test.json" height="600px" >}}</div>
</div>

## SEEC-SLU

Detta projekt leds av docent Anna J. Székely (SLU, Sveriges Lantbruksuniversitet) och docent Maja Malmberg (SLU, Sveriges Lantbruksuniversitet).

Forskargruppens övervakning av mängd SARS-CoV-2 i avloppsvatten startade i augusti 2020 i Uppsala, fler orter har därefter lagts till övervakningsprogrammet. Vattenprov av orenat avloppsvatten insamlas en dag per vecka,  provet samlas in över en 24h period för att kompensera för olika vattenflöden, på alla orter, utom Uppsala. I Uppsala baseras mätningarna sedan vecka 16 2021 på ett kombinerat avloppsvattenprov som består av avloppsvattenprover som insamlats över veckan.

Proverna bearbetas enligt standardmetoder. I korthet koncentreras och extraheras det virala genomiska materialet med hjälp av en metod som använder Maxwell RSO Enviro  TNA-kit (Promega) och antal genkopior av SARS-CoV-2 kvantifieras med hjälp av RT-qPCR med CDC RUO  nCOV N1-analys (IT DNA) metoden. För att korrigera för variation i populationsstorlek och vattenflöde kvantifierar gruppen mängd Pepper mild mottlevirus (PMMoV) som är det vanligast förekommande RNA-viruset i mänsklig avföring och fungerar som en uppskattning av mängd mänskliga avföring i provet ([Symonds *et al.*, 2019](https://doi.org/10.1371/journal.ppat.1007639)). För mer information om hur normaliseringsmetoden utvärderats se [Isaksson *et al.* (2022)](https://doi.org/10.3390/environments9030039). Data som presenters in grafen är ett ratio av kopienummer som uppmätts med N1 och PMMpV analyserna multiplicerat med 10^4. N1 kopienummer är en proxy för virusmängd SARS-CoV-2 i avloppsvatten och PMMoV är en proxy för mängd mänsklig avföring, vilket i sin tur är relaterat till befolkning som bidrar till avloppsvattnet. Detta ratio i sin tur kan anses som en proxy for andel infekterade individer i populationen i avloppsvattnets upptagningsområde.

Observera att mängden som tillhandahålls i dataseten och som visas i diagram nedan är preliminära. Forskargruppen genomför fortlöpande kontroller av metodens effektivitet vilket kan påverka de slutliga resultaten något.

### Dataset

**Ladda ner data:** [N1-genkopiatal per PMMoV-genkopiatal, CSV-fil](https://datagraphics.dckube.scilifelab.se/dataset/0ac8fa02871745048491de74e5689da9.csv). Data finns tillgängligt från och med vecka 38 2020; uppdateras varje vecka.\
**Kontakt:** anna.szekely@slu.se and maja.malmberg@slu.se

**Hur man citerar metod:**
Isaksson, F., Lundy, L., Hedström, A., Székely, A. J., Mohamed, N. (2022). Evaluating the Use of Alternative Normalization Approaches on SARS-CoV-2 Concentrations in Wastewater: Experiences from Two Catchments in Northern Sweden. *Environments*, *9*, 39. [https://doi.org/10.3390/environments9030039](https://doi.org/10.3390/environments9030039).

**Hur man citerar dataset:**
Székely, A. J., Mohamed, N., Dafalla, I., Vargas, J., Malmberg, M. (2021). Dataset of SARS-CoV-2 wastewater data from Uppsala, Umeå, Örebro, Kalmar, and various towns in Uppsala and Stockholm region, Sweden. [https://doi.org/10.17044/scilifelab.14256317](https://doi.org/10.17044/scilifelab.14256317).

### Visualiseringar

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
        <p>Linjediagrammen på den här sidan har flera interaktiva funktioner. Du kan använda funktionerna för att visualisera tillgängliga SARS-COV-2 avloppsvattendata  på olika sätt. Du kan till exempel välja att endast se data inom ett visst tidsintervall, eller från en given ort. Nedan förklarar vi hur du själv kan bestämma hur du gör inställningarna med de tillgängliga interaktiva funktionerna.</p>
        <h6>Visa endast en ort</h6>
        <p>För att endast visa data från en ort dubbelklicka på ortsnamnet i baneret till höger. För att avmarkera en ort klicka endast en gång på ortsnamnet. Om en ort avmarkeras kommer denna gråmarkeras och ortens data visas inte i grafen. I inställningar är alla orter markerade i startläget. För att avmarkera alla orter tryck "Deselect all areas" knappen. Du kan markera alla orter igen genom "Reselect all areas" knappen.</p>
        <h6>Visulisera endast vissa intervall på x eller y-axel</h6>
        <p>I diagrammen nedan representerar y-axeln kopiantalet för SARS-CoV-2 i förhållande till PMMoV medan x-axeln representerar datumet. Om du vill se värden inom ett givet värdeintervall på axlarna kan du göra detta genom att klicka och dra med musen. Till exempel, för att se all data inom en given tidsram kan du klicka nära startdatumet på x-axeln och dra för att skapa en rektangel som omfattar hela y-axeln och det datumintervall på x-axeln som du vill ha att se. Grafen kommer sedan att zooma in i intervallet som du valt.</p>
        <h6>Att utläsa exakta mätvärden</h6>
        <p>Det kan vara svårt att exakt läsa de exakta mätvärdena på data från en graf. För att se det exakta datavärdet, håll muspekaren över datapunkten av intresse. En ruta kommer att visas som visar y-axelvärdena för alla mätplatser för ett visst datum (dvs det x-axelvärdet).</p>
        <h6>Andra funktioner</h6>
        <p>Om du håller muspekaren över grafen kommer du att se några ytterligare alternativa funktioner som grå ikoner uppe till höger. Du kan använda dessa funktioner för att zooma in/ut ur  (med hjälp av + och - ikonerna), och för att ändra skalan på axlarna så att data från de "valda" platserna visas på de mest lämpliga axlarna (detta kan göras med hjälp av autoskala eller återställ axlar, som ser ut som en ruta som innehåller pilar respektive ett hus).</p>
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

Observera att grafen nedan visar samma data, men y-axeln visas som en logskala.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_logyaxis.json" height="550px" >}}</div>
</div>

### Kommentar

<div><b>Datum:</b> <span id="slu_comment_date"></span><br><b>Kommentar:</b> <span id="slu_comment"></span></div>

## SEEC-KTH: Prov från Stockholm and Malmö

Detta projekt, lett av prof. Zeynep Cetecioglu Gurol och kollegor (KTH; zeynepcg@kth.se) är ett samarbete mellan [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) och avdelningarna [SEED](https://www.kth.se/en/seed) och [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196) vid KTH, i nära samarbete med Stockholm Vatten och Avfall och Käppala Association. Provtagningen av avloppsvatten började i mitten av april 2020 från Bromma, Henriksdal och Käppala reningsverk. Dessa reningsverk får avloppsvatten från en befolkning på cirka 360 000; 860 000 respektive 500 000. Se [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Käppala](/wastewater/map_Kappala.pdf) och [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Bromma och Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf).

Efter koncentrering, filtrering och beredning analyseras proverna med RT-qPCR-teknik för SARS CoV-2 RNA. Primers mot nukleokapsidgenen (N) användes för att detektera SARS-COV-2-genen (tidigare använt och verifierat av [Medema *et al.* (2020)](https://doi.org/10.1021/acs.estlett.0c00357)). I vissa fall har det råa avloppsvattnet frusits ​​vid –20 °C och koncentrerat avloppsvatten eller renat RNA har lagrats vid -80°C innan nästa analyssteg genomfördes. Den metod för att koncentrera prov som prof. Zeynep Cetecioglu Gurol och hennes grupp har använt från projektets början tom vecka 35 2021 baserades på en av forskargruppens egna artiklar ([Jafferali *et al.*, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)), i artikeln jämfördes gruppens egen metod med fyra andra metoder för att koncentrera prover. Från vecka 35 2021 användes istället [Promegas kit](https://se.promega.com/applications/virus-detection-assay-coronavirus-detection-covid-19-sars-cov-2/wastewater-based-epidemiology-covid19/) för att koncentrera proverna.

Se även [forskargruppens webbsida där sammanfattningar av data och preliminära slutsatser presenteras](https://www.kth.se/water/research/covid-1.979048).

### Dataset

**Ladda ner data:** [N3-genkopiatal per PMMoV-genkopiatal; Excelfil](https://blobserver.dckube.scilifelab.se/blob/stockholm_wastewater_method_Sep_2021.xlsx). Data tillgänglig (delvis) från och med vecka 16 2020; uppdateras varje vecka.\
**Kontakt:** zeynepcg@kth.se

**Hur man citerar dataset:**
Cetecioglu, Z. G., Williams, C., Khatami, K., Atasoy, M., Nandy, P., Jafferali, M. H., Birgersson, M. (2021). SARS-CoV-2 Wastewater Data from Stockholm, Sweden. [https://doi.org/10.17044/scilifelab.14315483](https://doi.org/10.17044/scilifelab.14315483).

### Visualiseringar: Stockholm

<div class="alert alert-info">Senast uppdaterad: <span id="last_modified_stockholm"></span></div>

<button type="button" class="btn btn-sm btn-outline-secondary mb-2" data-bs-toggle="modal" data-bs-target="#interactiveFeaturesModal">
  Hur du kan använda grafens interaktiva funktioner
</button>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_stockholm.json" height="550px" >}}</div>
</div>

Observera att grafen nedan visar samma data, men y-axeln visas som en logskala, och och endast data från januari 2021 visas.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_stockholm_logyaxis.json" height="550px" >}}</div>
</div>

### Visualiseringar: Malmö

<div class="alert alert-info">Senast uppdaterad: <span id="last_modified_malmo"></span></div>

<div class="d-md-none alert alert-info">
  Skrolla grafen horisontellt för att se alla data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive w-100" id="malmo"></div>
</div>

### Kommentar

<div><b>Datum:</b> <span id="kth_comment_date"></span><br><b>Kommentar:</b> <span id="kth_comment"></span></div>

## Arkiverade data

- [Historiska data för Örebro och Umeå, mängd SARS-CoV-2 i avloppsvatten från Umeå respektive Örebro mellan oktober 2020 och juni 2021](historic_orebro_umea).
- [Historiska data för Stockholm, antal genkopior SARS CoV-2 per vecka (raw avloppsvatten) standardiserat med bovint coronavirus och PMMoV, april 2021 till augusti 2021](historic_stockholm).

## Bakgrund: Avloppsvattenbaserad epidemiologi

Epidemiologiska undersökningar av avloppsvatten kan användas för att studera SARS-CoV-2-virus i avföringsprover från COVID-19-patienter med RT-qPCR (se till exempel [Wu *et al.* (2020)](https://doi.org/10.1016/S2468-1253(20)30083-2)). Övervakning av virusnivåerna av SARS CoV-2 i avloppsvatten från samhällen kan därför ge en tidig indikation på sjukdomsprevalensen på befolkningsnivå, kallad avloppsvattenbaserad epidemiologi ([Corpuz *et al.*, 2020](https://doi.org/10.1016/j.scitotenv.2020.140910)).

Avloppsvattenbaserad epidemiologi studerar mängden virusgenom i avloppsvattnet, med RT-qPCR. Avloppsvatten av består spillvatten, dagvatten och kylvatten. Dagvatten kommr från hushåll och fastigheter exempelvis kök, toaletter och duschar. Det kan dock också inkludera vatten från exempel regnvatten och vatten från industriellt bruk). Prover tas regelbundet vid avloppsreningsanläggningar, vilket gör det möjligt att jämföra virusbelastningen över tid. Det har tidigare visats att mängden SARS CoV-2-virus i avloppsvatten kan ge en indikation på ökad smittspridning i befolkningen och även att trenden SARS-CoV-2 i avloppsvatten korrelerar med antal fall av COVID-19 och antal patienter som behöver vård (se [Peccia *et al.* (2020)](https://doi.org/10.1038/s41587-020-0684-z)). Under COVID-19-pandemin har övervakning av nivån SARS CoV-2 i avloppsvatten blivit en vanligare metod att övervaka och förutsäga smittspridning.

Observera att graferna som presenteras inom sektionen baseras på preliminära och ännu inte fullständigt utvärderade data. Data som delas ska därför användas med försiktighet. Observera att eftersom olika metoder för insamling av avloppsprover och dataanalys används av olika forskningsprojekten som redovisas nedan(dvs för olika städer) är det inte möjligt jämföra virusmängen mellan projekten (dvs mellan städer). Jämförelser bör göras inom varje projekt (dvs. stad) eftersom metoden är densamma för alla mätningar. Mätningar av SARS CoV-2 i avloppsvatten bör främst ses en indikation på ökande smittspridning, tillsammans med andra datatyper som exempelvis antal positiva SARS CoV-2 test, antal patienter som behöver intensivvård etc och  bidra till kunskap om den regionala dynamiken i COVID-19-pandemi.

{{< ww_dynamic_content >}}

<script src="https://cdn.jsdelivr.net/npm/vega@5.19.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.15.1"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/1016b97372e9403da0b8e8e7bb14fa8d.js?id=malmo"></script>
