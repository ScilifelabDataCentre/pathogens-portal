---
title: "Historiska data för Stockholm"
plotly: true
aliases:
  - /sv/data_types/environment/wastewater/historic_stockholm/
  - /sv/dashboards/wastewater/historic_stockholm/
  - /sv/dashboards/wastewater/covid_quantification/historic_stockholm/

---

Den här sidan visar data om mängden SARS-CoV-2 i Stockholm mellan april 2020 och augusti 2021 beräknat som genkopienummer/vecka (från avloppsvatten) standardiserat med bovint coronavirus+ PMMoV. Från september 2021 ändrades metoden. Se [den här sidan för de senaste uppgifterna](/dashboards/covid_quantification/covid_quant_kth/).

Data som visas här samlades in inom ett forskningsprojekt lett av prof. Zeynep Cetecioglu Gurol och kollegor (KTH) är ett samarbete mellan [SciLifeLab COVID-19 National Research Program](https://www.scilifelab.se/covid-19) och avdelningarna [SEED](https://www.kth.se/en/seed) och [Chemical Engineering](https://www.kth.se/ket/chemical-engineering-1.784196) vid KTH, i nära samarbete med Stockholm Vatten och Avfall och Käppala Association. Provtagningen av avloppsvatten började i mitten av april 2020 från Bromma, Henriksdal och Käppala reningsverk. Dessa reningsverk får avloppsvatten från en befolkning på cirka 360 000; 860 000 respektive 500 000. Se [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Käppala](/wastewater/map_Kappala.pdf) och [den här kartan för det exakta avrinningsområdet för insamlingskanalerna i Bromma och Henriksdal](/wastewater/map_Bromma_Henriksdal.pdf).

Efter koncentrering, filtrering och beredning analyserades proverna med RT-qPCR-teknik för SARS CoV-2 RNA. Primers mot nukleokapsidgenen (N) användes för att detektera SARS-COV-2-genen (tidigare använt och verifierat av [Medema _et al._ (2020)](https://doi.org/10.1016/j.scitotenv.2020.142939). I vissa fall har det råa avloppsvattnet frusits ​​vid –20 °C och koncentrerat avloppsvatten eller renat RNA har lagrats vid -80°C innan nästa analyssteg genomfördes. Koncentrationsmetoden som använddes av prof. Zeynep Cetecioglu Gurol och hennes kollegor baseras på forskargruppens publicerade artikel ([Jafferali _et al._, 2021](https://doi.org/10.1016/j.scitotenv.2020.142939)) som jämför fyra olika metoder för att koncentrera avloppsvatten. Studiens slutsats var att den dubbla ultrafiltreringsmetoden som anpassats av KTH gruppen har betydligt högre effektivitet jämfört med enstaka filtrerings- och adsorptionsmetoder. För detaljerad information om metoden, se publikationen.

**Ladda ner data:** [Mängd SARS CoV-2 RNA per vecka i råavloppsvatten, med bovin faktor och PPMoV faktor, Excel-fil](https://blobserver.dc.scilifelab.se/blob/wastewater_data_Stockholm.xlsx). Uppgifterna delas av Inlet Henriksdal, Sickla, Hässelby, Järva, Riksby och Käppala. Data tillgänglig (delvis) från och med vecka 16 2020; uppdateras varje vecka.

**Referera till detta dataset:**
Cetecioglu, Z. G., Williams, C., Khatami, K., Atasoy, M., Nandy, P., Jafferali, M. H., Birgersson, M. (2021). SARS-CoV-2 Wastewater Data from Stockholm, Sweden. [https://doi.org/10.17044/scilifelab.14315483](https://doi.org/10.17044/scilifelab.14315483).

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout.
</div>

 <div class="plot_wrapper mb-3">
    <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_data_stockholm.json" height="550px">}}</div>
</div>

<div class="small text-muted">Alla prover innan vecka 21 har kommit till labbet vecka 21. Mellan vecka 21 och 33 har prover analyserats varannan vecka. Efter vecka 33 har proverna analyserats varje vecka. Avloppsvattenmätningarna har utförts varannan vecka, inte veckovis, mellan vecka 24 och vecka 32 2021.</div>

**Källskod som används för att skapa grafen:** [Källskod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/archive/historic_stockholm_data.py).
