---
title: Avloppsbaserad epidemiologi i Sverige
plotly: true
---

## Introduktion

Avloppsvattenövervakning kan fungera som en effektiv metod för att kartlägga förekomsten av patogener, inklusive SARS-CoV-2, i befolkningen. Metoden kan också fungera som ett ’tidigt varningssystem’ som förutsäger kommande utbrott. Se nedan för [en allmän introduktion till avloppsvattenbaserad epidemiologi](#bakgrund-avloppsvattenbaserad-epidemiologi).

I den här dashboarden presenteras data från avloppsvattenbaserad epidemiologi från olika svenska städer. Sammanlagt har städerna som ingår här en befolkning på över 4 miljoner invånare (>40% av Sveriges befolkning). Data och resultat som presenteras här kommer från analyser som utförts av tre laboratorier. Två av laboratorierna ingår i [Svenskt Miljöepidemiologiskt Centrum (SEEC)](https://www.scilifelab.se/pandemic-response/pandemic-laboratory-preparedness/swedish-environmental-epidemiology-center-seec/), etablerat av forskare vid fyra svenska universitet (Sveriges lantbruksuniversitet, Kungliga Tekniska högskolan, Karolinska institutet och Uppsala universitet) som ett projekt för att utveckla resurser för pandemiberedskap inom [SciLifeLab’s Pandemic Preparedness Program](https://www.scilifelab.se/pandemic-response). 

De två noderna i SEEC som är involverade i avloppsvattenanalyser är **SEEC-KTH** baserat vid Kungliga Tekniska högskolan (KTH), under ledning av Zeynep Cetecioglu Gurol och **SEEC-SLU** baserat vid Institutionen för vatten och miljö, Sveriges lantbruksuniversitet (SLU), under ledning av docent Anna J. Székely och docent Maja Malmberg. Det tredje laboratoriet som presenterar sina analyser på denna dashboard är baserat vid **Göteborgs universitet (GU)** och leds av professor Heléne Norder. Se [‘Länkar till dashboards’](#länkar-till-dashboards) nedan för mer information om var arbetet från de tre respektive laboratorierna återfinns på dessa dashboards.

Notera att det förekommer mindre skillnader mellan detektionsmetoderna som grupperna använder. Därför är de absoluta värden som mäts av olika laboratorier inte jämförbara med varandra, och små skillnader i trender kan förekomma.

## Länkar till dashboards

- [**Kvantifiering av SARS-CoV-2**](/dashboards/covid_quantification/): Data, visualiseringar och information kopplad till kvantifiering av SARS-CoV-2 i avloppsvatten från olika delar av Sverige. Alla tre forskargrupperna delar historiska data för denna patogen, medan löpande data tillhandahålls av SEEC-SLU.

- [**Enteric virus quantification**](/dashboards/enteric_quantification/): Data, visualiseringar och information kopplad till kvantifiering av enteriska virus i avloppsvatten från Göteborg. Dessa data samlas in, analyseras och delas av Heléne Norders grupp vid Göteborgs universitet (GU).

- [**Influenza quantification**](/dashboards/influenza_quantification/): Data, visualiseringar och information kopplad till kvantifiering av influensavirus i avloppsvatten från olika delar av Sverige. Dessa data samlas in, analyseras och delas av SEEC-noden vid Sveriges lantbruksuniversitet (SLU).

- [**RSV quantification**](/dashboards/wastewater_rsv/): Data, visualiseringar och information relaterad till kvantifiering av respiratoriskt syncytialvirus (RSV) i avloppsvatten i olika delar av Sverige. Dessa data samlas in, analyseras och delas av SEEC-SLU.

## Tillgänglighet av källkod

All källkod som skapats för visualiseringarna under de olika flikarna på denna dashboard finns öppet tillgänglig på [GitHub](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/tree/main/wastewater). Skripten finns tillgängliga under respektive visualisering.

## Insamlingsplatser för avloppsvatten

Nedan finns en karta som visar de avloppsreningsverk (på engelska wastewater treatment plants, WWTP) från vilka avloppsvattenprover har samlats in och analyserats av de grupper som delar data på den här dashboarden.

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_map_test.json" height="600px" >}}</div>
</div>

**Källkod som använts för att skapa kartan:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/interactive_wastewater_map.py).

Tabellen nedan listar; städerna/orterna som monitoreras av de forskargrupper som delar data, vilka avloppsreningsverk (WWTP) som avloppsprover samlats in ifrån, antal personer i upptagningsområdet (Number of people), om övervakningen är pågående eller inte (Active?), vilket virus som övervakas på platsen (Viruses monitored) och forskargrupp(er) som har övervakat/övervakar platsen. En asterisk (*) bredvid antal personer anger att värdet är baserat på BO-7-värde (en uppskattning av de personer som är anslutna till ett avloppsreningsverk), snarare än antalet personer som är fysiskt anslutna. Informationen i tabellen nedan är [tillgänglig för nedladdning som en excel-fil](https://blobserver.dc.scilifelab.se/blob/overall_ww_collection_sites.xlsx).

  <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/wastewater_overallsites.json" height="850px" >}}</div>
</div>

## Bakgrund: Avloppsvattenbaserad epidemiologi

Många patogengenom, inklusive SARS-CoV-2, kan med hjälp av metoden polymeraskedjereaktion (PCR) detekteras i avföringsprov som har samlats in från infekterade individer (t.ex. COVID-19-patienter) [Wu _et al_. (2020)](<https://doi.org/10.1016/S2468-1253(20)30083-2>). Övervakning av nivåerna av patogener (t.ex. SARS CoV-2) i avloppsvatten från samhällen kan därför ge en tidig indikation på sjukdomsprevalensen på befolkningsnivå, så kallad avloppsvattenbaserad epidemiologi ([Corpuz _et al._, 2020](https://doi.org/10.1016/j.scitotenv.2020.140910)).

Avloppsvatten av består spillvatten, dagvatten och kylvatten. Dagvatten kommer från hushåll och fastigheter, exempelvis från kök, toaletter och duschar. Det kan också inkludera vatten från regn och från industriellt bruk. Prover tas regelbundet vid avloppsreningsanläggningar, vilket gör det möjligt att jämföra virusbelastningen över tid. Det har tidigare visats att mängden SARS-CoV-2-virus i avloppsvatten kan ge en indikation på ökad smittspridning bland befolkningen och även att mängden SARS-CoV-2 i avloppsvatten korrelerar med antal fall av COVID-19 och antal patienter som behöver sjukhusvård, se [Peccia _et al._ (2020)](https://doi.org/10.1038/s41587-020-0684-z). Nyligen visade också [Wang _et al._ (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/) att nivån av SARS-CoV-2 i avloppsvatten ökade 1-2 veckor innan det fanns en ökning av antalet COVID-19-patienter i behov av sjukhusvård. Under COVID-19-pandemin har övervakning av nivån av SARS-CoV-2 i avloppsvatten blivit en vanlig metod för att följa och förutsäga smittspridning.

Analyser av avloppsvatten ska i första hand ses som ett övervakningssystem. Tillsammans med annan data, t.ex. infektionstestning, intensivvårdsinläggningar etc. kan analyser av avloppsvatten hjälpa till att förstå den regionala dynamiken i sjukdomsutbrott.

{{< ww_dynamic_content >}}
