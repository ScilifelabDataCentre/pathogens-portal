---
title: Avloppsvattensepidemiologiska analyser i Sverige
description: Monitorering av olika patogener i avloppsvatten kan vara ett effektivt sätt att förutse framtida virusutbrott. Denna dashboard innehåller data som ursprungligen samlats in av ett flertal olika forskargrupper runt om i Sverige.
banner: /dashboard_thumbs/wastewater.jpg
inline_toc: true
type: wastewater
menu:
    dashboard_menu:
        identifier: wastewater
        name: Avloppsvattensepidemiologiska analyser i Sverige
    other_data:
        name: Environment
        identifier: environment
        weight: 50
    wastewater:
        name: Introduktion
        weight: 10
plotly: true
aliases:
    - /sv/data_types/environment/wastewater/
    - /sv/data_types/environment/
    - /sv/dashboards/wastewater/introduction/
---

<div class="alert alert-info"><b>Notera:</b> Dashboarden för avloppsvatten kommer att utökas framöver. Vi har nu grupperat mätningarna för mängden av SARS-CoV-2 i avloppsvatten enligt den forskargrupp som samlade in och analyserade respektive data (se nedan för information om de deltagande grupperna). Under kommande månader kommer mer data och information om SARS-CoV-2 och andra infektionssjukdomar att läggas till. </span></div>

## Introduktion

Avloppsvattenövervakning kan fungera som en effektiv metod för att kartlägga förekomsten av patogener, inklusive SARS-CoV-2, i befolkningen. Metoden kan också fungera som ett 'tidigt varningssystem' som förutsäger kommande utbrott. Se nedan för [en allmän introduktion till avloppsvattenbaserad epidemiologi](#bakgrund-avloppsvattenbaserad-epidemiologi).

I den här dashboarden presenteras data från avloppsvattenbaserad epidemiologi från olika svenska städer. Sammanlagt har städerna som ingår här en befolkning på över 3,5 miljoner invånare (eller 34% av Sveriges befolkning). Data och resultat som presenteras här kommer från analyser som utförts av tre laboratorier. Två av laboratorierna ingår i [Svenskt Miljöepidemiologiskt Centrum (SEEC)](https://www.scilifelab.se/pandemic-response/pandemic-laboratory-preparedness/swedish-environmental-epidemiology-center-seec/), etablerat av forskare vid fyra svenska universitet (Sveriges lantbruksuniversitet, Kungliga Tekniska högskolan, Karolinska institutet och Uppsala universitet) som ett projekt för att utveckla resurser för pandemiberedskap inom [SciLifeLab's Pandemic Preparedness Program](https://www.scilifelab.se/pandemic-response). De två noderna i SEEC som är involverade i avloppsvattenanalyser är **SEEC-KTH** baserat vid Kungliga Tekniska högskolan (KTH), under ledning av docent Zeynep Cetecioglu Gurol och **SEEC-SLU** baserat vid Institutionen för vatten och miljö, Sveriges lantbruksuniversitet (SLU), under ledning av docent Anna J. Székely och docent Maja Malmberg. Det tredje laboratoriet som presenterar sina analyser på denna dashboard är baserat vid **Göteborgs universitet (GU)** och leds av professor Heléne Norder. Se ['Navigering på dashboarden'](#navigering-på-dashboarden) nedan för mer information kring var arbetet från de tre respektive laboratorierna återfinns på denna dashboard.

Notera att det förekommer mindre skillnader mellan detektionsmetoderna som grupperna använder. Därför är de absoluta värden som mäts av olika laboratorier inte jämförbara med varandra, och små skillnader i trender kan förekomma. Detta innebär att du bör vara försiktig när du gör jämförelser. Titta på avsnitten "Metoder" under gruppernas flikar för att få information om metoderna som används av de olika laboratorierna.

## Navigering på dashboarden

Forskningen som visas på den här dashboarden är uppdelat efter de olika pathogener som presenteras. Se listan nedan för en överblick av vilka resurser som finns tillgängliga:

- [**SARS-CoV-2 kvantifiering**](/sv/dashboards/wastewater/covid_quantification): Data, visualiseringar och information kopplad till kvantifiering av SARS-CoV-2 i avloppsvatten från olika delar av Sverige. Alla tre forskargrupperna delar data relaterat till SARS-CoV-2 I avloppsvatten, deras mätningar täcker olika områden i Sverige. Det går att navigera direkt till den grupp(er) som tillhandahåller data för ett geografiskt områden som är av intresse.

## Tillgänglighet av källkod

All källkod som skapats för visualiseringarna under de olika  flikarna på denna dashboard finns öppet tillgänglig på [GitHub](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/tree/main/wastewater). Skript som används för respektive visualisering finns tillgängligt under respektive visualisering.

## Karta över platser där prover samlas in

Nedan finns en karta som visar de avloppsreningsverk (på engelska wastewater treatment plants, WWTP) från vilka avloppsprover samlas in och analyseras av de grupper som delar data på den här dashboarden.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dckube.scilifelab.se/blob/wastewater_map_test.json" height="600px" >}}</div>
</div>

**Källkod som använts för att skapa kartan:** [Script to produce map](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/interactive_wastewater_map.py).

## Bakgrund: Avloppsvattenbaserad epidemiologi

Många genom från patogener, inklusive SARS-CoV-2, kan med hjälp av metoden polymeraskedjereaktion (PCR) detekteras i avföringsprov som har samlats in från infekterade individer (t.ex. COVID-19-patienter) [Wu *et al*. (2020)](https://doi.org/10.1016/S2468-1253(20)30083-2). Övervakning av nivåerna av patogener (t.ex. SARS CoV-2) i avloppsvatten från samhällen kan därför ge en tidig indikation på sjukdomsprevalensen på befolkningsnivå, så kallad avloppsvattenbaserad epidemiologi ([Corpuz *et al.*, 2020](https://doi.org/10.1016/j.scitotenv.2020.140910)).

Avloppsvatten av består spillvatten, dagvatten och kylvatten. Dagvatten kommer från hushåll och fastigheter, exempelvis från kök, toaletter och duschar. Det kan också inkludera vatten från regn och från industriellt bruk. Prover tas regelbundet vid avloppsreningsanläggningar, vilket gör det möjligt att jämföra virusbelastningen över tid. Det har tidigare visats att mängden SARS-CoV-2-virus i avloppsvatten kan ge en indikation på ökad smittspridning bland befolkningen och även att mängden SARS-CoV-2 i avloppsvatten korrelerar med antal fall av COVID-19 och antal patienter som behöver sjukhusvård, se [Peccia *et al.* (2020)](https://doi.org/10.1038/s41587-020-0684-z). Nyligen visade också [Wang *et al.* (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/) att nivån av SARS-CoV-2 i avloppsvatten ökade 1-2 veckor innan det fanns en ökning av antalet COVID-19-patienter i behov av sjukhusvård. Under COVID-19-pandemin har övervakning av nivån av SARS-CoV-2 i avloppsvatten blivit en vanlig metod för att följa och förutsäga smittspridning.

Analyser av avloppsvatten ska i första hand ses som ett övervakningssystem. Tillsammans med annan data, t.ex. infektionstestning, intensivvårdsinläggningar etc. kan analyser av avloppsvatten hjälpa till att förstå den regionala dynamiken i sjukdomsutbrott.

{{< ww_dynamic_content >}}
