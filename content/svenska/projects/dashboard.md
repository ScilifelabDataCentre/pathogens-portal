---
title: Visualisering av svensk covid-19 forskning
toc: false
menu:
    projects:
        name: Statistik om forskningsartiklar
        identifier: dashboard
        weight: 15
    footer_sections:
        name: Statistik om forskningsartiklar
        weight: 25
plotly: true
---
Visualiseringarna på denna sida återspeglar hur produktionen av vetenskapliga forskningsartiklar kopplade till covid-19 och SARS-CoV-2 utvecklas över tid. Vi har valt att presentera en sammanställning av publicerade vetenskapliga artiklar och preprint där minst en författare är affilierad till ett svenskt lärosäte. Den svenska covid-19 publikationsdatabasen [nås här](/sv/publications/). Observera att sammanställningen görs manuellt och kan därför inte kan anses komplett. Den fullständiga sammanställningen av publikationer som visas på denna sida finns tillgänglig för nedladdning och användning för andra ändamål, se [DOI: 10.17044/scilifelab.14124014](https://doi.org/10.17044/scilifelab.14124014).

## Antal nya publikationer

Diagrammet visar antal publikationer (vilket inkluderar vetenskapliga artiklar och preprint) som publiceras varje månad samt det sammanlagda antalet publikationer per dag. Datumen återspeglar uppladdningsdatumet för preprint eller officiellt publuceringsdatumet för vetenskapliga artiklar, beroende på vilket som är det senaste. Att antalet publikationer tycks vara högt första dagen i varje månad beror på att inte alla publikationer har ett  publikationsdatum; alla publikationer utan specifikt publikationsdatum har lagts in som att de publicerats den första dagen I månaden.

<div class="table-responsive">
{{< publications_per_month >}}
</div>

## De senast publicerade publikationerna (tio senaste)

Tabellen visar de tio senaste publikationerna (inkluderar både tidskriftsartiklar och preprints). Datumet som anges är antingen det första datumet ett preprint laddades upp på en preprintserver eller publikationsdatumet för vetenskapliga artiklar. Författarlistan anges i samma format som citeringar. Genom att klicka på en specifik publikation länkas du vidare till publikationen. Observera att det endast är möjligt att läsa fulltext versionen av publikationer som publiceras open access eller ifall du har tillgång till en prenumeration via högskola eller universitet samt via en egen tidskriftsprenumeration. Tillägg till den manuellt granskade publikationsdatabasen kommer bli synliga i denna tabell nästa dag.

<div class="table-responsive">
{{< recent_ten_swe >}}
</div>

## Vanligast förekommande ord eller fraser i titlarna

Detta ordmoln visar de vanligaste orden eller fraserna som förekommer i publikationernas titlar. Observera att vi har filtrerat bort funktionella ord (som 'the', 'a', 'this', etc.) samt 'COVID-19' och 'SARS-CoV-2' eftersom alla titlar innehöll dessa ord. Alla ordmoln uppdateras veckovis.

#### Alla publikationer

<div class="row my-4"><div class="col-md-8"><img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-titles_all.png"></div></div>

#### Publikationer uppdelade på forskningsfinansiärer

Vi visar endast anslagsgivare där vi identifierat minst 20 publikationer i publikationsdatabasen.

<div class="container"> <div class="row mt-2"> <div class="col-md mr-4"> <div class="row"> <h5>Vetenskapsrådet:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-titles_vr.png"> </div> </div> <div class="col-md mr-4"> <div class="row"> <h5>SciLifeLab/KAW:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-titles_kaw.png"> </div> </div> <div class="col-md"> <div class="row"> <h5>Horizon 2020:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-titles_h2020.png"> </div> </div> </div> </div>

## Vanligast förkommande ord eller fraser i abstrakt

Ordmolnen visar de vanligaste förekommande orden eller fraserna från abstrakten (inkl. både preprint och vetenskapliga artiklar). Observera att vi har filtrerat bort funktionella ord (som 'the', 'a', 'this', etc.) samt 'COVID-19' och 'SARS-CoV-2' eftersom alla abstrakt innehöll dessa ord. Alla ordmoln uppdateras veckovis.

#### Alla publikationer

<div class="row my-4"><div class="col-md-8"><img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-abstracts_all.png"></div></div>

#### Publikationer uppdelade på forskningsfinansiärer

Vi visar endast anslagsgivare där vi identifierat minst 20 publikationer i publikationsdatabasen.

<div class="container"> <div class="row mt-2"> <div class="col-md mr-4"> <div class="row"> <h5>Vetenskapsrådet:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-abstracts_vr.png"> </div> </div> <div class="col-md mr-4"> <div class="row"> <h5>SciLifeLab/KAW:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-abstracts_kaw.png"> </div> </div> <div class="col-md"> <div class="row"> <h5>Horizon 2020:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-abstracts_h2020.png"> </div> </div> </div> </div>
