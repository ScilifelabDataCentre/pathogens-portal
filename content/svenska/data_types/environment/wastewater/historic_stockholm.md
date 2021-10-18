---
title: "Historiska data för Stockholm"
toc: false
---

Den här sidan visar data om mängden SARS-CoV-2 i Stockholm mellan april 2020 och augusti 2021 beräknat som genkopienummer/vecka (från avloppsvatten) standardiserat med bovint coronavirus+ PMMoV.  Från september 2021 ändrades metoden. Se [den här sidan för de senaste uppgifterna](../).

Data som visas här samlades in inom ett forskningsprojekt lett av prof. Zeynep Cetecioglu Gurol och kollegor (KTH) är ett samarbete mellan [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) och avdelningarna [SEED](https://www.kth.se/en/seed) och [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196) vid KTH, i nära samarbete med Stockholm Vatten och Avfall och Käppala Association. Provtagningen av avloppsvatten började i mitten av april 2020 från Bromma, Henriksdal och Käppala reningsverk. Dessa reningsverk får avloppsvatten från en befolkning på cirka 360 000; 860 000 respektive 500 000. Se [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Käppala](/wastewater/map_Kappala.pdf) och [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Bromma och Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf).

Efter koncentrering, filtrering och beredning analyserades proverna med RT-qPCR-teknik för SARS CoV-2 RNA. Primers mot nukleokapsidgenen (N) användes för att detektera SARS-COV-2-genen (tidigare använt och verifierat av [Medema et al (2020)](https://doi.org/10.1016/j.scitotenv.2020.142939). I vissa fall har det råa avloppsvattnet frusits ​​vid –20 °C och koncentrerat avloppsvatten eller renat RNA har lagrats vid -80°C innan nästa analyssteg genomfördes. Koncentrationsmetoden som använddes av prof. Zeynep Cetecioglu Gurol och hennes kollegor baseras på forskargruppens publicerade artikel ([Jafferali et al, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)) som jämför fyra olika metoder för att koncentrera avloppsvatten.  Studiens slutsats var att den dubbla ultrafiltreringsmetoden som anpassats av KTH gruppen  har betydligt högre effektivitet jämfört med enstaka filtrerings- och adsorptionsmetoder. För detaljerad information om metoden, se publikationen.

**Ladda ner data:** [Mängd SARS CoV-2 RNA per vecka i råavloppsvatten, med bovin faktor och PPMoV faktor, Excel-fil](https://blobserver.dckube.scilifelab.se/blob/wastewater_data_Stockholm.xlsx). Uppgifterna delas av Inlet Henriksdal, Sickla, Hässelby, Järva, Riksby och Käppala. Data tillgänglig (delvis) från och med vecka 16 2020; uppdateras varje vecka.

**Referera till detta dataset:**
Cetecioglu Z G, Williams, C, Khatami, K, Atasoy, M, Nandy, P, Jafferali, M H, Birgersson, M. SARS-CoV-2 Wastewater Data from Stockholm, Sweden. [https://doi.org/10.17044/scilifelab.14315483](https://doi.org/10.17044/scilifelab.14315483) (2021).

<div class="d-lg-none alert alert-info">
  Skrolla grafen horisontellt för att se alla data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="stockholm_combined"></div>
</div>

<div class="small text-muted">*NB: Alla prover innan vecka 21 har kommit till labbet vecka 21. Mellan vecka 21 och 33 har prover analyserats varannan vecka. Efter vecka 33 har proverna analyserats varje vecka.</div>

<div class="small text-muted">**NB: Avloppsvattenmätningarna har utförts varannan vecka, inte veckovis, mellan vecka 24 och vecka 32 2021.</div>

<div class="row ml-0 mt-3"><b>Publikationer:</b></div><div class="row"><div class="col">
<b><a target="_blank" href="https://doi.org/10.1016/j.scitotenv.2020.142939">Benchmarking virus concentration methods for quantification of SARS-CoV-2 in raw wastewater.</a></b><br>
                    <span class="text-muted">Jafferali MH, Khatami K, Atasoy M, Birgersson M, Williams C, Cetecioglu Z.</span><br>
                    <i>Science of The Total Environment</i> 755. DOI: 10.1016/j.scitotenv.2020.142939

<script src="https://cdn.jsdelivr.net/npm/vega@5.12.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.1.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.8.0"></script>

<script src="https://datagraphics.dckube.scilifelab.se/graphic/956f9390690043b8ae5f62b90d22f84f.js?id=stockholm_combined"></script>
