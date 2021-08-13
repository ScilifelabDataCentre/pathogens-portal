---
title: "Post COVID-19 i Sverige, statistik, forskniningsprojekt, tillgängliga data"
toc: true
plotly: true
---

Sedan början av 2020 har covid-19 pandemin utmanat hälso- och sjukvården och förändrat samhällen runt om i världen. Forskning och empiri har visat att covid-19 under den akuta infektionen kan ha olika svårighetgrad, från mild till moderat till svår. De flesta patienter, oavsett vilken svårighetsgrad de har under den akuta infektionsfasen, återhämtar sig och har inga kvarstående symptom efter återhämtningen. Vissa patienter uppvisar dock, efter den akuta infektionsfasen, kvarstående eller sena symptom efter covid-19. Besvär och symtom som rapporterats är svår trötthet, sämre hälsa, ledvärk, hjärntrötthet (svårighet att koncentrera sig på vissa uppgifter under längre tid) och hjärtklappning ([Brodin 2021](https://doi.org/10.1038/s41591-020-01202-8); [Marx 2021](https://doi.org/10.1038/s41592-021-01145-z)).

I vetenskaplig litteratur och media används ett flertal olika begrepp för att beskriva kvarstående eller sena symtom efter en akut covid-19 infektion exempelvis långtidscovid, post-akut covid-19, långtidssjuka vid covid-19 och postcovid. I enlighet med Socialstyrelsen så använder vi på denna sida definitionen *postcovid* för kvarstående eller sena symptom efter covid-19. Se *[bakgrundsinformationen](#background)* nedan för mer information om klassificeringen av tillståndet och den forskning som bedrivs inom ämnet.

På denna sida kan du hitta visualiseringar av statistik relaterade till *postcovid* baserat på data från Socialstyrelsen ([Socialstyrelsen](https://www.socialstyrelsen.se)), en översikt över forskningsprojekt inom området postcovid som för närvarande genomförs i Sverige och vetenskapliga publikationer.

För mer information om postcovid i Sverige, se följande [avsnitt](https://www.socialstyrelsen.se/coronavirus-covid-19/socialstyrelsens-roll-och-uppdrag/postcovid/) på Socialstyrelsens webbplatsoch rapporten Postcovid– kvarstående eller sena symtom efter covid-19. Stöd till [beslutsfattare och personal i hälso- och sjukvården (del 2) (publicerad april 2021)](https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/artikelkatalog/ovrigt/2021-4-7351.pdf).

## Statistik om postcovid i Sverige

<div class="alert alert-info">All data last updated: 12.08.2021</div>

Här visualiserar vi svensk statistik över *postcovid* som insamlats och delats av Socialstyrelsen. Majoriteten av statistiken som Socialstyrelsen samlat in bygger på registerforskning. De centrala källorna för statistik om covid-19 är främst patientregistret och dödsorsaksregistret. Statistiken som visualiseringarna om *postcovid* bygger på uppdateras en gång per månad andra onsdagen i månaden. Alla data som presenteras här finns tillgängliga för nedladdning [här](https://www.socialstyrelsen.se/statistik-och-data/statistik/statistik-om-covid-19/). Forskare kan ansöka om tillgänglighet till ytterligare data via RUT om deras projekt uppfyller kraven för åtkomst. Riktlinjerna finns [här](https://bestalladata.socialstyrelsen.se/data-for-forskning/).

## Diagnoskoder

De första patienterna som uppvisade kvarvstående långvariga symptom efter covid-19-infektion kom i kontakt med sjukvården våren 2020. Flera diagnoser och diagnoskoder har sedan dess använts inom sjukvården. Den 1 juni 2020 började Socialstyrelsen använda diagnosen *Z86.1A (Covid-19 i den egna sjukhistorien)*. *Diagnoskoden U09.9 (ICD-10-SE) Postinfektiöst tillstånd efter covid-19*, infördes 16 oktober 2020 och kompletterade och ersatte delvis koden *Z86.1A*. Från 1 januari 2021 upphörde diagnoskoden *Z86.1A* att gälla och ersattes med diagnoskoden *U08.9*, Covid-19 i den egna sjukhistorien, enligt [WHO (Världshälsoorganisationens)](https://www.who.int) riktlinjer.

Den senare diagnosen *U08.9* rekommenderas för en person som får vård av en annan sjukdom eller skada men där det anses vara relevant (av viss betydelse) att denna person tidigare har haft covid-19. Denna diagnos bör endast ges efter att personen anses inte längre ha covid-19. Det nuvarande hälsotillståndet ska inte anses vara orsakat av covid-19. Denna diagnos är bara en ytterligare diagnos (bidiagnos) och bör endast tilldelas vid sidan av en huvuddiagnos, det kan inte vara själva huvuddiagnosen.

Diagnosen för *postcovid* som Socialstyrelsen rekommenderar är *U09.9 (ICD-10-SE)-Postinfektiöst tillstånd efter covid-19*. Denna diagnos bör endast ges efter att personen anses inte längre har en pågående covid-19 infektion. Koden används för tillstånd som kvarstående eller sena besvär efter den akuta infektionen har gått över. Genom att använda termen *postcovid* skiljer sjukvården på en pågående infektion (covid-19) och ett efterföljande hälsotillstånd utan infektion (*postcovid*).

För mer information och aktuella riktlinjer för diagnoser som används för tillstånd relaterade till covid-19, se [denna sida](https://www.socialstyrelsen.se/utveckla-verksamhet/e-halsa/klassificering-och-koder/icd-10/) på Socialstyrelsens webbplats.

### Ålder och könsfördelning av diagnostiserade fall

Detta diagram visar antalet gånger patienter som diagnostiserats med diagnoser av intresse sedan introduktionen av dessa diagnoskoder, dividerat med ålder och kön.

#### Diagnoskod U09.9

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="diagnosed_age_sex_u09_9"></div>
</div>

#### Diagnoskod Z86.1A/U08.9

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="diagnosed_age_sex_u08_9"></div>
</div>

### Geografisk fördelning av diagnostiserade fall relativt populationens storlek

Geografisk fördelning av diagnostiserade fall i förhållande till befolkningsstorlek. Kartorna nedan visar antal individer som med respektive diagnoskod uppdelat per län i % av den totala befolkningen i länet. Den totala befolkningsmängden per län och antal personer med diagnoskoden visas genom att scrolla över ett visst län. Observera att intervallen som används för de två kartorna inte är detsamma.

#### Diagnoskod U09.9

{{< postcovid_map_u09_9_relative_to_population >}}

#### Diagnoskod Z86.1A/U08.9

{{< postcovid_map_u08_9_relative_to_population >}}

### Geografisk fördelning av diagnostiserade fall relativt antal bekräftade fall

Kartorna nedan visar antal individer som fått diagnoskoderna av intresse per län angivet i % av det totalt antal bekräftade fall av covid-19 i länet (baserat på [data från Folkhälsomyndigheten](https://www.folkhalsomyndigheten.se/smittskydd-beredskap/utbrott/aktuella-utbrott/covid-19/statistik-och-analyser/bekraftade-fall-i-sverige/)). Antal bekräftade fall bygger på et  kumulativa antalet positiva covid-19-test i regionen vid det datum som anges för den senaste uppdateringen av diagnoskoderna av intresse. Både totalt antal bekräftade fall av covid-19 och antal personer med diagnoskod av intresse kan ses genom att scrolla över ett visst län. Observera att de data som visualiseras på kartan bör tolkas med försiktighet. Antal bekräftade fall av covid-19-fall är sannolikt en underskattning. Individer som har covid-19 kan vara asymtomatiska och alla individer med covid-19 symtom testas inte och ingår inte i de rapporterade bekräftade fallen. Diagnoserna relaterade till postcovid introducerades vid olika tillfällen, och alla patienter kanske inte ännu fått en formell diagnos.

#### Diagnoskod U09.9

{{< postcovid_map_u09_9_relative_to_cases >}}

#### Diagnoskod Z86.1A/U08.9

{{< postcovid_map_u08_9_relative_to_cases >}}

### Vanligaste diagnosgrupper som rapporterats tillsammans med U09.9 Postinfektiöst tillstånd efter covid-19 (postcovid)

#### Diagnoskod U09.9

Denna tabell visar de vanligaste diagnosgrupper som har rapporterats tillsammans med diagnoskoden *U09.9 (ICD-10-SE)-Post-infektiöst tillstånd efter covid-19 (Postcovid)*. Siffrorna och procentsatserna nedan visar hur många individer som fått diagnosen U09.9 och samtidigt har diagnoser från nedanstående diagnosgrupper. Data nedan återspeglar perioden från och med den 16 oktober 2020 och fram till den senaste uppdateringen av datamängden (se ovan).

{{< postcovid_accompanying_diagnoses >}}

<span class="text-muted">*Observera att en individ kan ha mer än en diagnosgrupp som rapporteras tillsammans med U09.9 Postinfektiöst tillstånd efter covid-19 (Postcovid).  Om en individ har samma besvär vid flera vårdtillfällen/läkarbesök räknas diagnosen bara en gång.*</span>

### Vårdkontakter

Denna graf visar antal vårdkontakter för patienter med de av de tre diagnoskoderna.  Observera att grafen börjar från vecka 22 2020, men att diagnoskoderna *U08.9* och *U09.9* börjar användas först vid senare tillfälle (se information ovan). Varje vårdkontakt efter det att patienten fått diagnosen räknas in i dessa data. Data visas per vecka. Observera att dessa uppgifter inte är fullständiga eftersom information om antalet vårdkontakter från vissa veckor inte är tillgängliga på grund av patientsekretessen.

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot-wrapper">
  <div class="table-responsive" id="healthcare_contacts_all"></div>
</div>

### Antal vårdkontakter uppdelat på kön

Dessa grafer visar antal vårdkontakter för patienter som diagnostiserats med en av de tre diagnoskoderna. Varje vårdkontakt efter det att patienten fått diagnosen räknas in i dessa data. Data visas per vecka och uppdelat på kön. Observera att dessa uppgifter inte är fullständiga eftersom information om antalet vårdkontakter från vissa veckor inte är offentligt tillgängliga på grund av patientsekretessen.

#### Diagnoskod U09.9

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="healthcare_contacts_u09_9"></div>
</div>

#### Diagnoskod Z86.1A/U08.9

<div class="d-md-none alert alert-info">
  Scroll the plot sideways to view all data.
</div>

<div class="plot_wrapper">
  <div class="table-responsive" id="healthcare_contacts_u08_9"></div>
</div>

## Pågående forskningsprojektFormulärets överkant

Pågående Detta är en manuellt sammanställd översikt över forskningsprojekt med fokus på postcovid som fått forskningsanslag från större svenska anslagsgivare. Detta är inte en fullständig lista. Listan uppdateras kontinuerligt med nya projekt. Om du har ett forskningsprojekt inom området som du vill skall läggas upp här [kontakta oss på](/contact/). En lista över alla Covid-19 relaterade forskningsprojekt med anslag från större svenska anslagsgivare se [detta avsnitt av Covid-19 dataportalen](/projects/ongoing/).

{{< postcovid_projects >}}

<!-- ## Available data -->

## Publikationer

Det här avsnittet presenterar en lista över publicerade vetenskapliga artiklar och preprints om postcovid där minst en författare är anknuten till ett svenskt universitet eller institut. Observera att publikationerna kommer från en manuellt uppbyggd publikationsdatabas och att vissa publikationer därför kan saknas. Om du vill att din publikation ska läggas till här eller att informationen om din publikation ska korrigeras, [vänligen kontakta oss](/contact/). För en lista över alla publikationer relaterade till COVID-19 och SARS-CoV-2 där minst en författare är anknuten till ett svenskt universitet eller forskningsinstitut, se [detta avsnitt av Covid-19 dataportalen](/publications/).

{{< postcovid_publications >}}

<a id="background"><h2> </h2></a>

## Bakgrund

### Postcovid

I enlighet med Socialstyrelsen så använder vi på denna sida definitionen postcovid för kvarstående eller sena symptom efter covid-19. Patienter med postcovid uppvisar kvarvarande eller sena besvär som varar minst två månader efter den akuta fasen av COVID-19-infektion ([Brodin, 2021](https://doi.org/10.1038/s41591-020-01202-8)). Besvären och symptomen om patienterna uppvisar varierar, liksom symtomen varaktighet och svårighetsgrad (även om symtomen ofta ger sämre hälsa): svår trötthet, myalgi (muskelsmärta och smärtor) och autonom dysregulering. Vissa personer med postcovid har kvarvarande symptom från det akuta infektionsstadiet, medan andra med postcovid uppvisar nya symptom efter den inledande akuta infektionsfasen ([Brodin 2021](https://www.nature.com/articles/s41591-020-01202-8), [Dennis et al. 2021](http://dx.doi.org/10.1136/bmjopen-2020-048391), [Davido et al. 2020](https://doi.org/10.1016/j.cmi.2020.07.028).

### Definition saknas

I september 2020, inrättade WHO [ICD10](https://www.who.int/standards/classifications/classification-of-diseases/emergency-use-icd-codes-for-covid-19-disease-outbreak) oden för *Post COVID-19 condition - U09.9 - Post COVID-19 condition, unspecified*. En [WHO rapport från april 2021](https://www.who.int/publications/i/item/9789240025035)  beskriver att det finns ett behov av att karakterisera och tidigare definiera tillståndet efter COVID-19 för att öka förståelsen för tillståndet och underlätta diagnosticering. Idag har postcovid ännu inte en universell definition med avseende symptom och sjukdomsvaraktighet vilket behövs för diagnos. Myndigheter och institut i olika länder använder egna definitioner och termer. Relaterade diagnoskoder som upprättats av WHO är *U08.9 - Personal history of COVID-19, unspecified and U10.9 - Multisystem inflammatory syndrome associated with COVID-19, unspecified*. Diagnoskoden *U08.9* används för att beskriva en tidigare covid-19 infektion (bekräftad eller sannolik) som kan påverka individens hälsostatus, även om den akuta infektionen är över. Diagnoskoden *U10.9* används för att beskriva ”a temporal association with COVID-19: Cytokine storm; Kawasaki-like syndrome; Multisystem Inflammatory Syndrome in Children (MIS-C); Paediatric Inflammatory Multisystem Syndrome (PIMS)”.

I England har [National Institute for Health and Care Excellence (NICE)](https://www.nice.org.uk) has [definierat](https://www.nice.org.uk/guidance/ng188/chapter/context) *Post-COVID-19 syndrom* som ”…Signs and symptoms that develop during or after an infection consistent with COVID-19, continue for more than 12 weeks and are not explained by an alternative diagnosis. It usually presents with clusters of symptoms, often overlapping, which can fluctuate and change over time and can affect any system in the body…”. NICE säger att Post COVID 19 -syndrom kan betraktas som en diagnos under de tre första månaderna efter akut infektion, medan sjukvården bedömer om patienten kan ha en alternativ underliggande sjukdom som kan förklara symptomen.

Vidare [definierar](https://www.nice.org.uk/guidance/ng188/chapter/context) NICE termen Long COVID som "... signs and symptoms that continue or develop after acute COVID-19. It includes both ongoing symptomatic COVID-19 (from 4 to 12 weeks) and post-COVID-19 syndrome (12 weeks or more)…". I december 2020 publicerade NICE, i samarbete med Scottish Intercollegiate Guidelines Network och Royal College of General Practitioners, [riktlinjer för vård- och omsorgspersonal](https://www.nice.org.uk/guidance/ng188/chapter/context) (NG188) för att identifiera, bedöma och hantera de långsiktiga effekterna av COVID-19.

[Centers for Disease Control and Prevention (CDC)](https://www.cdc.gov) beskriver *Post-COVID conditions* som ”…a wide range of new, returning, or ongoing health problems people can experience more than four weeks after first being infected with the virus that causes COVID-19…”. CDC skiljer mellan Long COVID, Multiorgan Effects of COVID-19 och Effects of COVID-19 Treatment or Hospitalization…”. Ett antal olika termer används för att beskriva olika typer av Post-COVID conditions som long COVID, long-haul COVID, post-acute COVID-19, long-term effects of COVID, eller chronic COVID. För mer information om Post-COVID conditions från CDC, se denna [sida](https://www.cdc.gov/coronavirus/2019-ncov/long-term-effects.html). [National Institutes of Health (NIH)](https://www.nih.gov) i USA använder termen Post-Acute Sequelae of SARS-CoV-2-infection (PASC) för att hänvisa till effekterna av COVID-19 efter de första stadierna av infektion. I februari 2021 [lancerade NIH ett forskningsinitiativ](https://www.nih.gov/about-nih/who-we-are/nih-director/statements/nih-launches-new-initiative-study-long-covid) för att identifiera orsakerna till PASC och i identifiera metoder för förebyggande och behandlingar för individer som inte återhämtar sig helt inom några veckor efter den akuta infektionsfasen.

I vetenskapliga publikationer och den medias rapporteringen används flera olika begrepp för att beskriva kvarstående eller sena symtom efter covid-19: långtidscovid, post-akut covid-19, långtidssjuka vid covid-19 och sena effekter av covid-19 är några exempel. Ingen av dessa begrepp har emellertid haft en entydig klinisk definition. I Sverige beskriver Socialstyrelsen postcovid som kvarstående eller sena symptom efter covid-19. Medan besvärens svårighetsgrad oftast minskar över tid för de flesta individer (dessa individer behöver inte hjälp från sjukvården under återhämtningen), upplever vissa individer kvarstående besvär som påverkar deras hälsa och behöver behandling, rehabilitering och uppföljande medicinsk vård. I april 2021 [publicerade Socialstyrelsen en rapport om Postcovid](https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/artikelkatalog/ovrigt/2021-4-7351.pdf) som definierar tillståndet och ger rekommendationer.

### Aktuell forskning

Ett stort antal vetenskapliga artiklar, fallrapporter och reviews med fokus på postcovid har publicerats under det senaste året year (jmfr. [Dani et al. 2020](https://doi.org/10.7861/clinmed.2020-0896); [Nabavi 2020](https://doi.org/10.1136/bmj.m3489); [Sudre et al. 2021](https://doi.org/10.1038/s41591-021-01292-y); [Tarybagil et al. 2020](https://doi.org/10.1136/bcr-2020-241485); [Yelin et al. 2020](https://doi.org/10.1016/j.cmi.2020.12.001)). De flesta  vetenskapliga artiklar har haft som syfte att identifiera riskfaktorer och faktorer som kan användas för att prediktera individer som kan utveckla postcovid efter den akuta covid.19 infektionen. En nyligen publicerad studie av [Sudre och kollegor](https://doi.org/10.1038/s41591-021-01292-y) har lagt fram en modell för att prediktera individer som riskerar utveckla postcovid utifrån data från [COVID Symptom Study](/data_types/health_data/symptom_study_sweden/). I denna studie självrapporterar deltagarna sina symtom i en app på sin mobiltelefon. Resultaten indikerade att individer som upplevde fler än fem symtom under den första sjukdomsveckan hade högre risk att utveckla kvarstående symptom efter covid-19 (oddskvot = 3,53 (2,76–4,50). Dessutom visade studien att postcovid var mer sannolikt hos kvinnor och att risken också ökade med ökande ålder och högre BMI. Forskarna bakom studien föreslår att deras prediktionsmodell kan användas för att identifiera individer som riskerar att utveckla postcovid. Dessa resultat kan användas för förebyggande vård och för att utveckla behandlingsmetoder och stöd vid planering av utbildning och rehabilitering.

<script src="https://cdn.jsdelivr.net/npm/vega@5.19.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.0.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.15.1"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/d8ccc0a02ad248c2ae7e5910806c3586.js?id=healthcare_contacts_u09_9"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/47b7d864db0840dab7c2ff6f8fffc011.js?id=healthcare_contacts_u08_9"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/a31cdae8f06a4ac08f8970e6dd750c13.js?id=healthcare_contacts_all"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/a483404a5b5146cfa9eaeef29d326388.js?id=diagnosed_age_sex_u09_9"></script>
<script src="https://datagraphics.dckube.scilifelab.se/graphic/ae0a086410ea489484d33035469c334f.js?id=diagnosed_age_sex_u08_9"></script>
