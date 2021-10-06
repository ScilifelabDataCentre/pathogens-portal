---
title: Mängd SARS-CoV-2 virus i avloppsvatten från svenska städer
toc: true
menu:
other_data:
    name: Samhälle och miljö
    identifier: environment
    weight: 50
    params:
      title_eng: Environment
plotly: true
---

<div class="alert alert-info">
    <i class="fas fa-exclamation-triangle"></i> Svensk översättning för de engelska texterna kommer inom kort.</span>
</div>

Vi presenterar epidemiologiska data av mätningar av SARS-CoV-2 virus i avloppsvatten från olika svenska städer med totalt över 1.5 miljoner invånare. Att mäta virusmängder i avloppsvatten kan var en del av ett system för att detektera och övervaka förekomsten av SARS-CoV-2 i samhället. Notera att direkt jämförelse av virusmängden mellan olika städer inte är möjlig pga olika hantering av insamlade avloppsprov och analys av data.  Jämförelser bör endast göras inom data som samlats in och visualiseras från en och samma stad. [För mer information om epidemiologiska data från mätningar av SARS-CoV-2 i avloppsvatten se nedan](#background).

## Map of sample collection sites

<div class="row justify-content-center mb-4"><div class="col">{{< wastewater_map >}}</div></div>

## Uppsala, Umeå, Örebro, Kalmar, och andra orter

Projektet leds av prof. Anna J. Székely (SLU, Sveriges Lantbruksuniversitet) och prof. Maja Malmberg (SLU, Sveriges Lantbruksuniversitet) i samarbete med Uppsala Vatten, Roslagsvatten, Enköpings kommun, Gästrike Vatten, TEMAB m.m.

Mängden SARS-CoV-2 virus i Uppsala stads avloppsvatten bestäms genom analys av avloppsvatten insamlat vid Kungsängsverket som är Uppsala Vattens största avloppsreningsverk. Avloppsvattnet från avloppsreningsverket samlas in från de två största upptagningsområdena för Uppsalas avloppsvatten med ca. 180.000 invånare. [För kartor som visar respektive upptagningsområde för avloppsvattnet i Uppsala](/wastewater/avrinningskarta_inlopp_kungsangsverket.pdf). Mängden SARS-CoV-2 virus i Ekerös avloppsvatten bestäms genom analys av avloppsvatten insamlat vid Ekebyhov, i Österåkers avloppsvatten bestäms genom analys av avloppsvatten insamlat vid Margretelund, i Vaxholms avloppsvatten bestäms genom analys av avloppsvatten insamlat vid Blynäs. Se [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Umeå](/wastewater/map_umeaa.jpg). Se [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Örebro](/wastewater/map_orebro.pdf).

Mängd SARS-CoV-2 virus i avloppsvatten ett specifik datum har normaliserats jämfört med mängden mänsklig avföring för att undvika variation pga vattenflöde och populationsstorlek. Proverna bearbetas enligt standardmetoder. I korthet koncentreras virusinnehållet i proverna med hjälp av en modifierad elektronegativ filtreringsmetod ([metod C, Ahmed och kollegor, 2020](https://doi.org/10.1016/j.scitotenv.2020.139960)), virus RNA extraheras med hjälp av RNeasy PowerMicrobiome-kit (Qiagen) och mängden SARS-CoV-2 RNA kvantifieras genom RT-qPCR och användning av CDC RUO nCOV N1-analys (IDT DNA). För att studera metodens effektivitet och detektera eventuell närvaro av potentiella virushämmare tillsätts bovint koronavirus (BCoV) ett sk. process-surrogatvirus. För att korrigera för variation i populationen kvantifierar vi också pepper mild mottle virus (PMMoV), som är det vanligaste RNA-viruset i mänsklig avföring ([Symonds et al, 2019](https://doi.org/10.1371/journal.ppat.1007639)).

Notera att resultaten i dataseten och som visas i diagrammen är preliminära data. Forskargruppen genomför fortfarande kontroller av metodens effektivitet vilket kan förändra de slutliga resultaten något.

**Ladda ner data:** [Relativt ratio av viruskopior SARS CoV-2 jämfört med mängd PPMoV, CSV-fil](https://datagraphics.dckube.scilifelab.se/dataset/0ac8fa02871745048491de74e5689da9.csv). Data finns tillgängligt från och med vecka 38 2020; uppdateras varje vecka.\
**Kontakt:** anna.szekely@slu.se and maja.malmberg@slu.se\
**Referera till detta dataset:**
Székely, A. & Mohamed, N. Dataset of SARS-CoV-2 wastewater data from Uppsala, and neighbouring towns Knivsta, Enköping, Östhammar and Älvkarleby, Sweden. [https://doi.org/10.17044/scilifelab.14256317.v1](https://doi.org/10.17044/scilifelab.14256317.v1) (2021).

<div class="alert alert-info">Senast uppdaterad: <span id="last_modified_uppsala"></span></div>
<div class="alert alert-secondary small">Interacting with the plot: Click on the names of municipalities in the legend in order to select or deselect cities that are displayed. Select a portion of the plot using your cursor in order to zoom in to a particular date range or y axis range. Note that the axes ranges adapt to your selections. Double-click anywhere on the graph in order to return to the default view. It is also possible download the graph as a PNG file, zoom and reset using buttons which appear in the top right corner when you hover over the graph.</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_regular.json" height="550px" >}}</div>
</div>

Observera att grafen nedan visar samma data, men y-axeln visas som en logskala

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_slu_logyaxis.json" height="550px" >}}</div>
</div>

## Stockholm

Detta projekt, lett av prof. Zeynep Cetecioglu Gurol och kollegor (KTH) är ett samarbete mellan [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) och avdelningarna [SEED](https://www.kth.se/en/seed) och [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196) vid KTH, i nära samarbete med Stockholm Vatten och Avfall och Käppala Association. Provtagningen av avloppsvatten började i mitten av april 2020 från Bromma, Henriksdal och Käppala reningsverk. Dessa reningsverk får avloppsvatten från en befolkning på cirka 360 000; 860 000 respektive 500 000. Se [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Käppala](/wastewater/map_Kappala.pdf) och [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Bromma och Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf).

Efter koncentrering, filtrering och beredning analyseras proverna med RT-qPCR-teknik för SARS CoV-2 RNA. Primers mot nukleokapsidgenen (N) användes för att detektera SARS-COV-2-genen (tidigare använt och verifierat av [Medema et al (2020)](https://doi.org/10.1016/j.scitotenv.2020.142939). I vissa fall har det råa avloppsvattnet frusits ​​vid –20 °C och koncentrerat avloppsvatten eller renat RNA har lagrats vid -80°C innan nästa analyssteg genomfördes. Koncentrationsmetoden som används av prof. Zeynep Cetecioglu Gurol och hennes kollegor baseras på forskargruppens publicerade artikel ([Jafferali et al, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)) som jämför fyra olika metoder för att koncentrera avloppsvatten.  Studiens slutsats var att den dubbla ultrafiltreringsmetoden som anpassats av KTH gruppen  har betydligt högre effektivitet jämfört med enstaka filtrerings- och adsorptionsmetoder. För detaljerad information om metoden, se publikationen.

Se även [forskargruppens webbsida där sammanfattningar av data och preliminära slutsatser presenteras](https://www.kth.se/water/research/covid-1.979048).

**Ladda ner data:** [Relative N gene normalized by PPMoV; Excel file](https://blobserver.dckube.scilifelab.se/blob/stockholm_wastewater_method_Sep_2021.xlsx). Data tillgänglig (delvis) från och med vecka 16 2020; uppdateras varje vecka. \
**Kontakt:** zeynepcg@kth.se\
**Referera till detta dataset:**
Cetecioglu Z G, Williams, C, Khatami, K, Atasoy, M, Nandy, P, Jafferali, M H, Birgersson, M. SARS-CoV-2 Wastewater Data from Stockholm, Sweden. [https://doi.org/10.17044/scilifelab.14315483](https://doi.org/10.17044/scilifelab.14315483) (2021).

<div class="alert alert-info">Senast uppdaterad: <span id="last_modified_stockholm"></span></div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_combined_stockholm.json" height="550px" >}}</div>
</div>

<div class="row ml-0 mt-3"><b>Publikationer:</b></div><div class="row"><div class="col">
<b><a target="_blank" href="https://doi.org/10.1016/j.scitotenv.2020.142939">Benchmarking virus concentration methods for quantification of SARS-CoV-2 in raw wastewater.</a></b><br>
                    <span class="text-muted">Jafferali MH, Khatami K, Atasoy M, Birgersson M, Williams C, Cetecioglu Z.</span><br>
                    <i>Science of The Total Environment</i> 755. DOI: 10.1016/j.scitotenv.2020.142939
</div></div>

## Archived data

- [Historic data for Örebro and Umeå; amount of SARS-CoV-2 in Umeå and Örebro wastewater between October 2020 and June 2021](historic_orebro_umea).
- [Historic data for Stockholm;  Gene copy number/week (raw wastewater) with bovine + PMMoV factor between April 2020 and August 2021](historic_stockholm)

## Bakgrund

Epidemiologiska undersökningar av avloppsvatten kan användas för att studera SARS-CoV-2-virus i avföringsprover från COVID-19-patienter med RT-qPCR (se till exempel [Wu et al, 2020](https://doi.org/10.1016/S2468-1253(20)30083-2)). Övervakning av virusnivåerna av SARS CoV-2 i avloppsvatten från samhällen kan därför ge en tidig indikation på sjukdomsprevalensen på befolkningsnivå, kallad avloppsvattenbaserad epidemiologi ([Corpuz et al, 2020](https://doi.org/10.1016/j.scitotenv.2020.140910)).

Avloppsvattenbaserad epidemiologi studerar mängden virusgenom i avloppsvattnet, med RT-qPCR. Avloppsvatten av består spillvatten, dagvatten och kylvatten. Dagvatten kommr från hushåll och fastigheter exempelvis kök, toaletter och duschar. Det kan dock också inkludera vatten från exempel regnvatten och vatten från industriellt bruk). Prover tas regelbundet vid avloppsreningsanläggningar, vilket gör det möjligt att jämföra virusbelastningen över tid. Det har tidigare visats att mängden SARS CoV-2-virus i avloppsvatten kan ge en indikation på ökad smittspridning i befolkningen och även att trenden SARS-CoV-2 i avloppsvatten korrelerar med antal fall av COVID-19 och antal patienter som behöver vård (se [Peccia et al, 2020](https://doi.org/10.1038/s41587-020-0684-z)). Under COVID-19-pandemin har övervakning av nivån SARS CoV-2 i avloppsvatten blivit en vanligare metod att övervaka och förutsäga smittspridning.

Observera att graferna som presenteras inom sektionen baseras på preliminära och ännu inte fullständigt utvärderade data. Data som delas ska därför användas med försiktighet. Observera att eftersom olika metoder för insamling av avloppsprover och dataanalys används av olika forskningsprojekten som redovisas nedan(dvs för olika städer) är det inte möjligt jämföra virusmängen mellan projekten (dvs mellan städer). Jämförelser bör göras inom varje projekt (dvs. stad) eftersom metoden är densamma för alla mätningar. Mätningar av SARS CoV-2 i avloppsvatten bör främst ses en indikation på ökande smittspridning, tillsammans med andra datatyper som exempelvis antal positiva SARS CoV-2 test, antal patienter som behöver intensivvård etc och  bidra till kunskap om den regionala dynamiken i COVID-19-pandemi.

{{< ww_dates_modified >}}
