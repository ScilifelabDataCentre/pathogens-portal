---
title: Mängd SARS-COV-2 i avloppsvatten (SEEC-KTH)
plotly: true
aliases:
    - /sv/dashboards/wastewater/covid_quant_kth/
---

<div class="mt-3">
  <a href="/sv/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Gå tillbaka till SARS-CoV-2-kvantifiering inom avloppsvattenbaserad epidemiologi-dashboarden</a>
</div>
<br>

## Introduktion

Projektet leds av professor Zeynep Cetecioglu Gurol med hjälp av Mariel Perez-Zabaleta and Isaac Owusu-Agyeman verksamna vid Kungliga Tekniska högskolan (KTH). Bioinformatikanalyser av avloppsvattendata sker i samarbete med  professor Luisa Hugerth (Uppsala Universitet). Forskarsamarbetet utgör SEEC-KTH. SEEC-KTH är nu en del av [Institutionen för Industriell bioteknologi](https://www.kth.se/dib/department-of-industrial-biotechnology-1.783103) vid KTH. Projektet finansieras nu som en del av SciLifeLab Pandemic Laboratory Preparedness (PLP) program. Mer information om PLP-programmet finns i [resources section](/resources/).

Data och visualiseringar på den här sidan uppdateras vanligtvis veckovis, oftast på fredagar. Data bakom dashboarden uppdateras kontinuerligt.

## Insamlingsplatser för avloppsvatten

Analysen av avloppsvattenprov från Stockholm av SEEC-KTH görs i nära samarbete med Stockholm Vatten och Avfall och Käppalaförbundet. SEEC-KTH började ta prover på avloppsvatten i mitten av april 2020, och prover samlades då in från avloppsreningsverken i Bromma, Henriksdal och Käppala. Dessa anläggningar tar emot avloppsvatten från en befolkning på cirka 360 000, 860 000 respektive 500 000 personer. Se [den här kartan](/wastewater/map_Kappala.pdf) för det exakta avrinningsområdet för insamlingskanalerna i Käppala och [den här kartan](/wastewater/map_Bromma_Henriksdal.pdf) för det exakta avrinningsområdet för insamlingskanalerna i Bromma och Henriksdal.

SEEC-KTH började samla in prover från avloppsvatten från Sjölunda avloppsreningsverk i Malmö under vecka 39 2021. Detta avloppsreningsverk hanterar större delen av Malmö och Burlövs kommun och delar av kommunerna Lomma, Staffanstorp och Svedala. Ungefär 300 000 personer bor i uppsamlingsområdet. Mer information om området, inklusive en karta, kan [laddas ned direkt](/wastewater/sjolunda.pdf).

SEEC-KTH avloppsvattensanalyser täcker ungefär 20% av Sveriges befolkning.

## Visualiseringar

Vänligen observera att visualiseringarna nedan endast visar data från de senaste 16 veckorna som default. För att se alla tillgängliga data vänligen klicka på knappen ‘Whole timeline’ för att se hela tidslinjen från 2020.

Notera också att även om samma metoder används för alla städer som visas på den här fliken, kan skillnader i befolkningen och hur avloppsvatten samlas in i olika städer påverka jämförelser dem emellan.

### Stockholm

<div class="alert alert-info">Senast uppdaterad: <span id="last_modified_stockholm"></span></div>

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
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_stockholm.json" height="550px" >}}</div>
</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/combined_stockholm_regular.py).

### Malmö

<div class="alert alert-info">Senast uppdaterad: <span id="last_modified_malmo"></span></div>

<div class="d-md-none alert alert-info">
  Skrolla grafen horisontellt för att se alla data.
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_kthmalmo.json" height="550px" >}}</div>
</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/quant_malmo_kthplot.py).

## Kommentarer från forskargruppen

<div><b>Datum:</b> <span id="kth_comment_date"></span><br><b>Kommentar:</b> <span id="kth_comment"></span></div>

{{< ww_dynamic_content >}}

## Dataset

**Kontakt:** <zeynepcg@kth.se>

**Ladda ner data:** [N3-genkopiatal per PMMoV-genkopiatal; Excelfil.](https://blobserver.dckube.scilifelab.se/blob/stockholm_wastewater_method_Sep_2021.xlsx). Data tillgänglig (delvis) från och med vecka 16 2020; uppdateras varje vecka.

**Hur man citerar dataset:**
Cetecioglu, Z. G., Williams, C., Khatami, K., Atasoy, M., Nandy, P., Jafferali, M. H., Birgersson, M. (2021). SARS-CoV-2 Wastewater Data from Stockholm, Sweden. [https://doi.org/10.17044/scilifelab.14315483](https://doi.org/10.17044/scilifelab.14315483).

## Metoder

För att korrigera för variation i population och avloppsvattenflöde kvantifierar gruppen förekomsten av viruset Pepper mild mottle virus (PMMoV), ett växtvirus från peppar som människor får i sig via maten, med hjälp av en modifierad version av testet i [Zhang *et al.* (2006)](https://doi.org/10.1371/journal.pbio.0040003). PMMoV är det vanligaste RNA-viruset i avföring från människa och används för att uppskatta mängden avföring från människa i avloppsvattenproverna ([Symonds *et al.*, 2019](https://doi.org/10.1371/journal.ppat.1007639)). För att kvantifiera mängd SARS-CoV-2 används SARS-specifika N3-primers ([Lu *et al.*, 2020](https://doi.org/10.3201/eid2608.201246)) och mätningen görs med metoden RT-qPCR med SYBR Green-kemi ([Perez-Zabaleta *et al.*, 2023](https://doi.org/10.1016/j.scitotenv.2022.160023)).

Efter koncentration, filtrering och beredning analyseras proverna med RT-qPCR -teknik för att kvantifiera förekomsten av SARS-CoV-2 RNA. För att kvantifiera SARS-CoV-2 användes primers i nukleokapsid-(N)-genen (tidigare använt och verifierat av [Medema *et al.* (2020)](https://doi.org/10.1021/acs.estlett.0c00357)). I vissa fall har det obehandlade avloppsvattnet frusits ​​vid –20 °C och koncentrerat avloppsvatten eller renat RNA har lagrats vid -80°C innan nästa analyssteg genomfördes. Koncentrationsmetoden som initialt användes av SEEC-KTH baseras på en av deras tidigare studier ([Jafferali *et al.*, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)), där fyra olika koncentrationsmetoder jämfördes. Denna metod användes fram till vecka 35, 2021. Efter denna tidpunkt började gruppen istället använda [Promegas kit](https://se.promega.com/applications/virus-detection-assay-coronavirus-detection-covid-19-sars-cov-2/wastewater-based-epidemiology-covid19/) för att koncentrera proverna.

## Arkiverade data

- [Historiska data for Stockholm; genkopieantal per vecka (ofiltrerat avloppsvatten) standardiserat med bovint coronavirus och PMMoV, april 2020 till augusti 2021](/sv/dashboards/wastewater/covid_quantification/historic_stockholm).

<br>
<div class="mt-3">
  <a href="/sv/dashboards/wastewater/covid_quantification/"><i class="bi bi-arrow-left-circle-fill"></i> Gå tillbaka till SARS-CoV-2-kvantifiering inom avloppsvattenbaserad epidemiologi-dashboarden</a>
</div>
