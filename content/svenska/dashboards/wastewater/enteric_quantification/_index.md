---
title: Mängd enteriska virus i avloppsvatten (GU)
plotly: true
type: wastewater
menu:
  wastewater:
    name: Enteriska virus kvantifiering
    weight: 30
---

## Introduktion

Enteriska virus tillhör en större grupp virus som inkluderar calicivirus (norovirus och sapovirus), adenoviruses, och astroviruses. Dessa virus sprids via fekal-orala smittvägar och orsakar gastroenterit (som känneteckas av symptom som illamående, diarré och kräkningar).

Avloppsvatten innehåller många olika typer av virus som infekterar människor eftersom infekterade individer utsöndrar viruspartiklar i avföring och urin. Nordergruppen vid Göteborgs universitet har genom sin forsknings påvisat att relativa nivåer av vissa enteriska virus i avloppsvatten kan förutsäga kommande virusutbrott ([Hellmér _et al._, 2014](https://pubmed.ncbi.nlm.nih.gov/25172863/)). Tidigare studier av forskargruppen har även visat att nivåerna av norovirus i avloppsvatten ökar 1-2 veckor innan större utbrott på äldreboenden och sjukhusavdelningar.

År 2023 påbörjade Nordergruppen vid Göteborgs universitet (GU) veckovis övervakning av ett antal enteriska virus i avloppsvatten. Gruppen kvantifiera relativa nivåer av enterovirus (inklusive poliovirus), Pepper Mild Mottle virus (PMMoV), adenovirus, GG2 (ett norovirus), astrovirus och sapovirus. För mer information om [metoderna som används vid övervakning](#metoder),[kort sammanfattande information om virusen](#basic-virus-information), och [information om insamlad data](#dataset).

Den enteriska virusövervakningen av Norder-gruppen sker parallellet med gruppens pågående övervakning av SARS-CoV-2 nivåer i avloppsvatten. SARS-CoV-2 data delas [på denna sida](/dashboards/wastewater/covid_quantification/covid_quant_gu/).

Projektet leds av professor Heléne Norder (Göteborgs universitet, GU), och stöds av medarbetare från Göteborgs universitet och Sahlgrenska Universitetssjukhuset (Hao Wang, Marianela Patzi Churqui, Timur Tunovic, Fredy Saguti, och Kristina Nyström). Provtagningarna av avloppsvatten utförs av Lucica Enache på Ryaverket, Gryaab AB, Göteborg.

Data och visualiseringar på denna sida kommer att uppdateras ungefär en gång i veckan.

## Insamlingsplatser för avloppsvattenprov

Avloppsvattenprover för virusanalys samlas in vid Ryaverkets avloppsreningsverk i Göteborg (se metodavsnittet nedan för detaljer). Ryaverkets reningsverk tar emot avloppsvatten från samtliga hushåll i Göteborg, vilket omfattar 790 000 invånare, samt industrin i området. Avloppsvatten tas även emot från industri och boende i kringliggande kommuner, bland annat Ale, Härryda, Kungälv, Lerum, Mölndal och Partille, samt från storm- och snösmältvatten från äldre delar av Göteborg.

<div class="alert alert-info">Last updated: <span id="last_modified_enteric"></span></div>

Vänligen se [avsnittet med sammanfattande information om virusen](#basic-virus-information) för mer information om vart och ett av de virus som data samlas in för.

 <div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/enteric_graph_gu.json" height="550px" >}}</div>
</div>

**Källkod som avvänts för att generera visualiseringar:** [Källskod](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/wastewater/enteric_viruses_gu.py).

## Kommentarer från forsksargruppen

<div><b>Date:</b> <span id="gu_enteric_comment_date"></span><br><b>Commentary:</b> <span id="gu_enteric_comment"></span></div>

{{< ww_dynamic_content >}}
<br>

## Dataset

###### **Nedladdning av data:**

[Kvantifiering av mängd SARS-CoV-2 och enteriska virus i avloppsvatten](https://blobserver.dckube.scilifelab.se/blob/wastewater_data_gu_allviruses.xlsx). Results för SARS-CoV-2 mätningar är tillgängliga från vecka 7 2020 (med ett avbrott vintern 2022-2023), och för enteriska virus från vecka 2 2023. Uppdatering sker varje vecka.

**Kontakt:** <helene.norder@gu.se>

###### **För att citera datasetet:**

Norder, H., Nyström, K. Patzi Churqui, M., Tunovic, T., Wang, H. (2023). Detection of SARS-CoV-2 and other human enteric viruses in wastewater from Gothenburg. [https://doi.org/10.17044/scilifelab.22510501](https://doi.org/10.17044/scilifelab.22510501).

###### **För att citera metoden som används:**

Hellmér, M., Paxéus, N., Magnius, L., Enache, L., Arnholm, B., Johansson, A., Bergström, T., and Norder, H. (2014). Detection of pathogenic viruses in sewage provided early warnings of hepatitis A virus and norovirus outbreaks. [https://doi.org/10.1128/AEM.01981-14](https://doi.org/10.1128/AEM.01981-14).

Saguti, F., Magnil, E., Enache, L., Churqui, M.P., Johansson, A., Lumley, D., Davidsson, F., Dotevall, L., Mattsson, A., Trybala, E., Lagging, M., Lindh, M., Gisslen, M., Brezicka, T., Nystrom, K. and Norder, H. (2021). Surveillance of wastewater revealed peaks of SARS-CoV-2 preceding those of hospitalized patients with COVID-19. [https://doi.org/10.1016/j.watres.2020.116620](https://doi.org/10.1016/j.watres.2020.116620).

Wang, H., Churqui, M.P., Tunovic, T., Enache, L., Johansson, A., Karmander, A., Nilsson, S., Lagging, M., Andersson, M., Dotevall, L., Brezicka, T., Nystrom, K. and Norder, H. (2022). The amount of SARS-CoV-2 RNA in wastewater relates to the development of the pandemic and its burden on the health system. [https://doi.org/10.1016/j.isci.2022.105000](https://doi.org/10.1016/j.isci.2022.105000).

## Metoder

Insamling av avloppsvatten sker genom en fast insamlare som samlar in 30ml avloppsvatten per 10,000m<sup>3</sup> av inkommande avloppsvatten. För analys veckovis poolas sju prover, varje avloppsvattenprov representerar insamling under ett dygn). En del av detta prov skickas till Klinisk Mikrobiologi på Sahlgrenska Universitetssjukhuset för analys. Mängd prov som skickas varje vecka varierar mellan 1.5-15l beroende på vattenflödet, vilket till stor del beror på väderleken. Mängd avloppsvatten från hushåll och industri är relativt konstant över tid, men mängd avloppsvatten beror även på väderleksförhållandena, exempelvis ökar mängd avloppsvatten vid regnväder. För att ta hänsyn till detta under analysen är proverna som ska analyseras för virus flödesviktade. Det betyder att mängd avloppsvatten som samlas in och analyseras relaterar till flödet av inkommande avloppsvatten. Mer information om detta finns i [Hellmér _et al._ (2014)](https://pubmed.ncbi.nlm.nih.gov/25172863/) och [Wang _et al._ (2022)](https://pubmed.ncbi.nlm.nih.gov/36035197/).

På Klinisk Mikrobiologi på Sahlgrenska Universitetssjukhuset koncentreras proverna till en volym av 2.5ml med hjälp av en metod som utvecklas inom forskargruppen. Denna metod använder NanoCeram electropositive filter (Argonide, Florida, USA) för att koncentrera proverna, följt av ultracentrifugering som sekundär metod ([Saguti et al., 2021](https://doi.org/10.1016/j.watres.2020.116620)). Nukleinsyror extraheras från ett koncentrerat prov på 1 ml med hjälp av QIAamp Circulating Nucleic Acid Kit (Qiagen, Hilden, Germany). Realtids- PCR (RT-qPCR) användes för att detekter och kvantifiera mängd virusgenom. Mer information om metoden som används för att beräkna virusmängd finns i [Hellmér et al. (2014)](https://doi.org/10.1128/AEM.01981-14), [Saguti et al. (2021)](https://doi.org/10.1016/j.watres.2020.116620), and [Wang et al. (2022)](https://doi.org/10.1016/j.isci.2022.105000).

### Grundläggande virusinformation

**Enterovirus** är det största släktet av enterovirus som infekterar människor, inklusive 15 arter (inklusive enterovirus (EV) och rhinovirus (RV), bland annat) och cirka 300 typer (112 typer inom EV-A till -D och 169 RV) -A till -C typer). Immunitet mot en typ ger inte immunitet till en annan (dvs. det finns ingen korsimmunitet). RV-infektioner är vanliga, särskilt på vintern. Infektioner kan vara asymtomatiska, men kan istället resultera i influensaliknande symtom, sjukdomar i nedre luftvägarna och/eller förvärra kroniska sjukdomar t.ex. astma. EV-infektioner ses vanligtvis hos barn och unga vuxna. Infektioner kan orsaka influensaliknande symtom, konjunktivit, myokardit, meningit, encefalit och slapp förlamning. EV-virus kan orsaka större utbrott. Till exempel inträffar utbrott av hjärnhinneinflammation orsakade av en EV-typ som tillhör EV-A-C ungefär vart 5:e till 7:e år i europeiska städer.¨

**Pepper mild mottle virus (PMMoV)** är ett växtvirus som infekterar peppararter. När människor konsumerar peppar utsöndrar de PMMoV i avföringen. PMMoV används därför ofta som en mycket känslig indikator på fekal kontaminering i vatten (t.ex. avloppsvatten). Nivåerna av PMMoV i avloppsvatten kan användas för att standardisera för antalet personer som bidrar till prover (gjorda i t.ex. kommersiella analyser som används för att kvantifiera SARS-CoV-2 i avloppsvatten). Detta förutsätter att människor utsöndrar samma mängd PMMoV under hela året. Men enligt erfarenheten från Norder-gruppen vid GU är halterna av PPMoV i avloppsvattnet i Göteborg högre på sommaren (vilket tyder på att invånarna konsumerar mer peppar på sommaren).

**Adenovirus** är en del av _adenoviridae-familjen_. Det finns 88 typer av humana adenovirus, klassificerade i 7 arter (HAdV-A till -G). Olika typer kan rikta in sig på olika organ eller organsystem (dvs de har olika vävnadstropismer). Humana adenovirus orsakar vanligtvis luftvägssjukdomar. Symtom kan vara influensaliknande symtom, halsont, akut bronkit och lunginflammation (HAdV-B och C), konjunktivit (HAdV-B och D) och gastroenterit (HAdV-F och G). Barn under 9 år löper störst risk för infektion, men adenovirus kan spridas mellan vuxna i trånga miljöer som sjukhus. Epidemier förekommer inte i den allmänna befolkningen och allvarliga komplikationer är sällsynta.

**Norovirus**, inklusive GG2 (mer allmänt känt som "vinterkräksjukevirus"), tillhör familjen _Calicivirus_ och har korta inkubationsperioder. Fall av norovirus når vanligtvis sin topp på vintern och kan orsaka allvarliga komplikationer bland immunosupprimerade och äldre (se [Folkhälsomyndigheten](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/smittsamma-sjukdomar/calicivirus-noro-och-sapovirus/) för mer information). GG2 har till exempel en inkubationstid på 12-48 timmar. Medan GG2-infekterade individer återhämtar sig snabbt, kan de vara smittsamma i 2 dagar efter tillfrisknandet. GG2 är mycket smittsamt och sprider sig snabbt i miljöer där individer är i nära kontakt som skolor. Immuniteten är kortlivad och eftersom det finns flera GG2-genotyper kan en individ bli sjuk flera gånger.

**Astrovirus** som infekterar människor är en del av _Mamastrovirus_-släktet inom _Astroviridae-familjen_. Det finns 8 arter av humana astrovirus (HAst1 till 8) och ytterligare 7 oklassificerade typer. Virusen orsakar sjukdomar hos spädbarn och småbarn. Oftast orsakar de gastroenterit, men kan också orsaka huvudvärk, sjukdomskänsla, illamående, kräkningar, låggradig feber och (i sällsynta fall) hjärninflammation. Inkubationstiden är 1-4 dagar och infektioner brukar gå över på 2-4 dagar. I tempererade klimat är astrovirusinfektioner vanligast på vintern och våren. De flesta barn utvecklar immunitet vid 10 års ålder, så infektioner är ovanliga hos immunkompetenta vuxna. Men immuniteten tenderar att avta med tiden, så äldre människor kan vara i riskzonen. Utbrott ses ofta på daghem och äldreboenden.

**Sapovirus** är en av de vanligaste orsakerna till akut gastroenterit hos människor och djur (vid sidan av norovirus). Symtom inkluderar diarré och kräkningar, som ofta åtföljs av feber, illamående och magkramper. Sapporovirus (SaV) är den enda arten av sapovirus. Det är klassificerat i fem genogrupper (GI till GV), med GI, GII, GIV och GV som infekterar människor. Inkubationstiden liknar GG2 (12-48 timmar), men symtomen är vanligtvis lindrigare och varar 2-6 dagar. Förr ansågs SaV uteslutande vara en pediatrisk patogen, men det finns allt fler bevis för att andra åldersgrupper kan vara infekterade. Utbrott av SaV ses exempelvis på sjukhus, skolor och som ett resultat av livsmedelsförorening.
