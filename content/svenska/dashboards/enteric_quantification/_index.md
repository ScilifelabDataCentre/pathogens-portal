---
title: Mängd enteriska virus i avloppsvatten (GU)
banner: /dashboard_thumbs/wastewater_enteric_virus.png
plotly: true
description: Enteriska virusnivåer i Göteborgs avloppsvatten, inklusive norovirus och adenovirus. Data från Norder-gruppens veckoanalys vid Ryaverkets reningsverk hjälper till att förutsäga utbrott och inkluderar prover från omgivande kommuner.
menu:
  dashboard_menu:
    identifier: wastewater_enteric_quantification
    name: "Avloppsvatten: Enteriska virus kvantifiering (GU)"
dashboards_topics: [Wastewater Surveillance, Enteric viruses, Epidemiology]
aliases:
  - /sv/dashboards/wastewater/enteric_quantification/
data_status: "historic"
---

<!-- markdownlint-disable MD051 -->

<div class="alert alert-info">
  <span class="bi bi-exclamation-triangle-fill"> De data som presenteras här uppdateras inte längre utan bevaras för historisk referens.</span>
</div>

## Introduktion

Enteriska virus tillhör en större grupp virus som inkluderar calicivirus (norovirus och sapovirus), adenoviruses, och astroviruses. Dessa virus sprids via fekal-orala smittvägar och orsakar gastroenterit (som kännetecknas av symptom som illamående, diarré och kräkningar).

Avloppsvatten innehåller många olika typer av virus som infekterar allt levande även människor eftersom infekterade individer utsöndrar viruspartiklar i avföring och urin. Nordergruppen vid Göteborgs universitet har genom sin forsknings påvisat att nivåer av vissa enteriska virus i avloppsvatten kan förutsäga kommande virusutbrott, som att nivåerna av norovirus i avloppsvatten ökar 1-2 veckor innan större utbrott sker på äldreboenden och sjukhusavdelningar ([Hellmér _et al._, 2014](https://pubmed.ncbi.nlm.nih.gov/25172863/)).

Under 2017, och sedan 2020 och alltjämt utför Nordergruppen vid Göteborgs universitet (GU) veckovis samtidig övervakning av ett antal enteriska virus i avloppsvattnet. Gruppen kvantifierar nivåerna av virusarvsmassa av enterovirus (inklusive poliovirus), adenovirus, GG2 (ett norovirus som orsakar vinterkräksjuka), astrovirus, sapovirus och som kontroll ett växtvirus, Pepper Mild Mottle virus (PMMoV). Denna sida fokuserar på de data som producerats med hjälp av en metod för kvantifiering från vecka 20 (15t maj) 2023. Den nya metoden har använts parallellt med den tidigare använda metoden tom vecka 43. Data från den tidigare använda metoden från vecka 2 tom vecka 43 2023 (dvs. 9 januari till 23 oktober 2023) finns tillgängliga på den webbsida som visar [historiska nivåer av enteriska virusdata från Göteborg](/sv/dashboards/enteric_quantification/historic_enteric_gu/).

Se nedan för mer om [metoderna som används vid övervakning](#metoder), [kort sammanfattande information om virusen](#grundläggande-virusinformation), och [information om insamlad data](#dataset).

Studierna av enteriska virus i avloppsvatten har inom Nordergruppen skett parallellt med arbetet att studera SARS-CoV-2 i avloppsvatten, dessa data delas också [på portalen](/sv/dashboards/covid_quantification/covid_quant_gu/).

Data och visualisering på den här **sidan uppdateras inte längre**.

## Insamlingsplatser för avloppsvattenprov

Avloppsvattenprover för virusanalys samlas in vid Ryaverkets avloppsreningsverk i Göteborg (se metodavsnittet nedan för detaljer). Ryaverkets reningsverk tar emot avloppsvatten från samtliga hushåll i Göteborg, vilket omfattar 790 000 invånare, samt industrin i området. Avloppsvatten tas även emot från industri och boende i kringliggande kommuner, bland annat Ale, Härryda, Kungälv, Lerum, Mölndal och Partille, samt från storm- och snösmältvatten från äldre delar av Göteborg.

## Visualiseringar

<div class="alert alert-info">Senast uppdaterad: <span id="last_modified_enteric"></span> (uppdateras inte längre)</div>

Vänligen se [avsnittet med sammanfattande information om virusen](#grundläggande-virusinformation) för mer information om vart och ett av de virus som data samlas in för.

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

 <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/enteric_graph_gu.json" height="550px" >}}</div>
</div>

**Källkod som avvänts för att generera visualiseringar:** [Källskod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/wastewater/archive/enteric_viruses_gu.py).

## Kommentarer från forskargruppen

<div><b>Date:</b><span id="gu_enteric_comment_date"></span><br><b>Commentary:</b>
<span id="gu_enteric_comment"></span></div>

{{< ww_dynamic_content >}}
<br>

## Dataset

###### **Nedladdning av data:**

[Kvantifiering av mängd SARS-CoV-2 och enteriska virus i avloppsvatten](https://blobserver.dc.scilifelab.se/blob/wastewater_data_gu_allviruses.xlsx). Results för SARS-CoV-2 mätningar är tillgängliga från vecka 20 2023. Uppdatering sker varje vecka.

**Kontakt:** <helene.norder@gu.se>

###### **För att citera datasetet:**

Norder, H., Nyström, K. Patzi Churqui, M., Tunovic, T., Wang, H., Saguti, F. (2023). Detection of SARS-CoV-2 and other human enteric viruses in wastewater from Gothenburg. [https://doi.org/10.17044/scilifelab.24787353.v1](https://doi.org/10.17044/scilifelab.24787353.v1).

###### **För att citera metoden som används:**

Hellmér, M., Paxéus, N., Magnius, L., Enache, L., Arnholm, B., Johansson, A., Bergström, T., and Norder, H. (2014). Detection of pathogenic viruses in sewage provided early warnings of hepatitis A virus and norovirus outbreaks. [https://doi.org/10.1128/AEM.01981-14](https://doi.org/10.1128/AEM.01981-14).

Saguti, F., Magnil, E., Enache, L., Churqui, M.P., Johansson, A., Lumley, D., Davidsson, F., Dotevall, L., Mattsson, A., Trybala, E., Lagging, M., Lindh, M., Gisslen, M., Brezicka, T., Nystrom, K. and Norder, H. (2021). Surveillance of wastewater revealed peaks of SARS-CoV-2 preceding those of hospitalized patients with COVID-19. [https://doi.org/10.1016/j.watres.2020.116620](https://doi.org/10.1016/j.watres.2020.116620).

Wang, H., Churqui, M.P., Tunovic, T., Enache, L., Johansson, A., Karmander, A., Nilsson, S., Lagging, M., Andersson, M., Dotevall, L., Brezicka, T., Nystrom, K. and Norder, H. (2022). The amount of SARS-CoV-2 RNA in wastewater relates to the development of the pandemic and its burden on the health system. [https://doi.org/10.1016/j.isci.2022.105000](https://doi.org/10.1016/j.isci.2022.105000).

## Metoder

Insamling av avloppsvatten sker genom en fast insamlare som samlar in 30ml avloppsvatten per 10,000m<sup>3</sup> av inkommande avloppsvatten. För analys veckovis poolas sju prover, varje avloppsvattenprov representerar insamling under ett dygn. En del av detta prov skickas till Klinisk Mikrobiologi på Sahlgrenska Universitetssjukhuset för analys. Mängd prov som skickas varje vecka varierar mellan 1.5-15l beroende på vattenflödet, vilket till stor del beror på väderleken. Mängd avloppsvatten från hushåll och industri är relativt konstant över tid, men mängd avloppsvatten beror även på väderleksförhållandena, exempelvis ökar mängd avloppsvatten vid regnväder. För att ta hänsyn till detta under analysen är proverna som ska analyseras för virus flödesviktade. Det betyder att mängd avloppsvatten som samlas in och analyseras relaterar till flödet av inkommande avloppsvatten. Mer information om detta finns i [Hellmér _et al._ (2014)](https://pubmed.ncbi.nlm.nih.gov/25172863/) och [Wang _et al._ (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/).

På Klinisk Mikrobiologi på Sahlgrenska Universitetssjukhuset används två metoder utvecklade inom gruppen för att koncentrera virusmängderna. Den metod som nu används använder sig av ultrafiltrering som primär metod. Den tidigare metoden använde ett elektropositivt filter (Argonide, Florida, USA) för att koncentrera proverna ([Saguti et al., 2021](https://doi.org/10.1016/j.watres.2020.116620)).

Nukleinsyror extraheras från ett koncentrerat prov på 1 ml med hjälp av QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Realtids- PCR (RT-qPCR) användes för att detektera och kvantifiera mängd virusgenom. Mer information om metoden som används för att beräkna virusmängd finns i [Hellmér et al. (2014)](https://doi.org/10.1128/AEM.01981-14), [Saguti _et al._ (2021)](https://doi.org/10.1016/j.watres.2020.116620), [Wang _et al._ (2022)](https://doi.org/10.1016/j.isci.2022.105000), och [Wang _et al._ (2023)](https://doi.org/10.1016/j.scitotenv.2023.165012). Båda metoderna anges virusmängd per dag som ett genomsnitt, eftersom virusmängden baseras på en veckas insamling av avloppsvatten.

## Arkiverade data

[Historisk enteriska virus data från Gothenburg mellan veckorna 2 och 43 2023](/sv/dashboards/enteric_quantification/historic_enteric_gu/).

### Grundläggande virusinformation

**Enterovirus** är det största släktet med flest olika virus som infekterar människor. Det omfattar 15 arter, med flertal typer inom varje art. Totalt är de drygt 300 olika virustyper som infekterar människa. I arterna enterovirus A-D (EV-A-EV-D) återfinns av 112 typer (inklusive poliovirus i EV-C) och arterna rhinovirus A-C (RV-A-RV-C) återfinns 169 typer. Immunitet mot en typ ger inte immunitet mot en annan (dvs. det finns ingen korsimmunitet). Infektioner med enterovirus är ofta asymtomatiska, EV-infektioner är vanliga hos barn och unga vuxna. De kan ge influensaliknande symtom, konjunktivit (ögoninflammation), myokardit (hjärtmuskelinflammation), meningit (hjärnhinneinflammation), encefalit (hjärninflammation) och förlamning. Dessa virus kan orsaka större utbrott. Ungefär vart 5:e till 7:e år inträffar utbrott av hjärnhinneinflammation bland unga i Europa orsakade av en EV-typ som tillhör EV-A-C. RV-infektioner är mycket vanliga i alla åldrar, särskilt på vintern. De är oftast milda, men kan även ge influensaliknande symtom, sjukdomar i nedre luftvägarna och/eller förvärra kroniska sjukdomar t.ex. astma.

**Adenovirus** tillhör _adenoviridae-familjen_. Det finns 88 typer av humana adenovirus, klassificerade i 7 arter (HAdV-A till -G). Olika typer infekterar olika organ eller organsystem (dvs de har olika vävnadstropismer). Hos människa orsakar adenovirus ofta luftvägssjukdomar. Symtomen kan vara influensaliknande, halsont, akut bronkit och lunginflammation (HAdV-B och C), konjunktivit (ögoninflammation orsakad av HAdV-B och D) och gastroenterit (HAdV-F och G).Allvarliga komplikationer efter en adenovirus infektion är sällsynt. Barn under 9 år löper störst risk för symptomatisk infektion, men även vuxna drabbas främst av ögoninflammationer och magsjuka orsakat av adenovirus. Dessa virus orsakar inte epidemier men kan spridas mellan vuxna i trånga miljöer som på sjukhus och militäranläggningar eller i simbassänger.

**Norovirus**, inklusive GG2 (mer allmänt känt som “vinterkräksjukevirus”), tillhör familjen _Calicivirus_. Antalet fall av norovirus når vanligtvis sin topp på vintern ( januari/februari). Infektionen kan orsaka allvarliga komplikationer bland immunosupprimerade och äldre (se [Folkhälsomyndigheten](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/calicivirus-noro-och-sapovirus/) för mer information). GG2 är mycket smittsamt och sprider sig snabbt i miljöer där individer är i nära kontakt som skolor. Inkubationstiden är kort, mellan 12 och 48 timmar. Trots att GG2-infekterade individer återhämtar sig snabbt, kan de vara smittsamma under 2 dagar efter tillfrisknandet. Immuniteten är kortlivad och eftersom det finns flera GG2-genotyper kan en individ bli sjuk flera gånger.

**Astrovirus** som infekterar människor är en del av _Mamastrovirus_-släktet inom _Astroviridae-familjen_. Det finns 8 arter av humana astrovirus (HAst1 till 8) och ytterligare 7 oklassificerade typer. Virusen orsakar sjukdomar främst hos barn och äldre. Oftast orsakar de gastroenterit, men kan också huvudvärk, illamående, kräkningar, låggradig feber och (i sällsynta fall) hjärninflammation. Inkubationstiden är 1-4 dagar och infektioner brukar gå över på 2-4 dagar. I tempererade klimat är astrovirusinfektioner vanligast på vintern och våren. De flesta barn har blvit smittade tidigt och har utvecklar immunitet vid 10 års ålder, så infektioner är ovanliga hos immunkompetenta vuxna. Men immuniteten tenderar att avta med tiden, så äldre människor kan vara i riskzonen. Utbrott ses ofta på daghem och äldreboenden.

**Sapovirus** är en av de vanligaste orsakerna till akut gastroenterit hos människor och djur (vid sidan av norovirus). Symtom inkluderar diarré och kräkningar, som ofta åtföljs av feber, illamående och magkramper. Sapporovirus (SaV) är den enda arten av sapovirus. Den i fem genogrupper av SaV (GI till GV), där GI, GII, GIV och GV infekterar människa. Inkubationstiden liknar GG2 (12-48 timmar), men symtomen är vanligtvis lindrigare och varar 2-6 dagar. Förr ansågs SaV uteslutande smitta barn, men det finns allt fler bevis för att alla åldersgrupper kan bli sjuka. Utbrott av SaV ses exempelvis på sjukhus, skolor, oftast via förorenat livsmedel pga dålig handhygien hos livsmedelsarbetare.

**Pepper mild mottle virus (PMMoV)** är ett växtvirus som infekterar växter inom släktet _Capsicum_, som paprika, chilipeppar, cayennepeppar mfl. När människor konsumerar någon av dessa växter, som ofta är smittade med PMMoV, utsöndras viruset i avföringen. PMMoV används därför ofta som en känslig indikator på fekal kontaminering av vatten (t.ex. råvatten som ska bli dricksvatten). Nivåerna av PMMoV i avloppsvattenprov kan användas för att standardisera för antalet personer som bidrar till provet (detta används i kommersiella analyser för kvantifiering av SARS-CoV-2 i avloppsvatten). En sådan standardisering förutsätter att människor utsöndrar samma mängd PMMoV under hela året. Men enligt erfarenheten från Norder-gruppen vid GU är halterna av PPMoV i avloppsvattnet i Göteborg högre på sommaren (vilket tyder på att invånarna konsumerar mer av dessa växter under denna årstid).
