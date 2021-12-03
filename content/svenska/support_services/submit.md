---
title: Publicera data
toc: false
menu:
    top_nav:
        weight: 40
        pre: <i class="fas fa-paper-plane mr-2"></i>
        post: highlight
    main:
        identifier: submit_data
        parent: support_services
        weight: 50
        pre: <i class="fas fa-paper-plane"></i>
---
Publicera dina covid-19-forskningsdata för att göra dem tillgängliga för resten av forskarsamhället. Data bör lagras i en öppen databas tillsammans med beskrivande metadata. För många datatyper finns internationalla databaser som kan anses vara _de facto_ standarder.

### Dela data

[SciLifeLab](https://www.scilifelab.se/) (datacentre@scilifelab.se) eller [NBIS](https://nbis.se/) (support@nbis.se)
kan ge stöd och information för var och hur du kan dela dina data i publika databaser. Tveka inte att kontakta oss om du har några frågor. Din forskargrupp behöver inte vara ansluten till någon speciell institution för att få vår hjälp, vi är tillgängliga för alla forskare anslutna till svenska universitet och högskolor.

European Bioinformatics Institute (EBI) driver många olika internationella databaser som bör användas när så är lämpligt.  Se vidare [Covid-19 Data Portal data submission page](https://www.covid19dataportal.org/submit-data). Om ditt datamaterial består av en datatyp som saknar en de facto databas, kan data istället deponeras i [SciLifeLab Data Repository](https://scilifelab.se/data/repository) som drivs av SciLifeLab Data Centre. För känsliga persondata som måste lagras i en säker miljö med kontrollerad åtkomst kan SciLifeLab [can help with publishing and access control](https://www.scilifelab.se/data/humandata/).

Här följer riktlinjer för publicering av data uppdelat på datatyp:

* ##### Genomik & transkriptomik data

    Vi föreslår att rådata och sammansatta sekvensdata skickas in  till [ENA](https://www.ebi.ac.uk/ena). ENA har skapat dokumentation för att underlätta för forskare att [publicera SARS CoV-2 data via ENA](https://ena-browser-docs.readthedocs.io/en/latest/help_and_guides/sars-cov-2-submissions.html). För att ytterligare underlätta detta arbete har vi skapat en handledning [se här](/support_services/tutorial_ena/tutorial_ena_intro).

    Innan sekvensdata (t.ex. ”shot gun”-sekvenser) skickas in är det nödvändigt att ta bort humana (kontaminerande) sekvenser. Humana värdsekvensdata kräver kontrollerad åtkomst, och NBIS utvecklar för närvarande en lokal version av European Genome-phenome Archive (EGA) i Sverige (EGA-SE) vilket kommer möjliggöra arkivering och delning av känsliga data inom en rättslig ram.  

    Tills dess att EGA-SE är tillgänglig, bör känsliga data fortsätta förvaras i en säker miljön (t.ex. på BIANCA på [Uppmax](https://www.uppmax.uu.se/)).  SciLifeLab kan [hjälpa er med förfrågningar om åtkomst och publicering](https://www.scilifelab.se/data/humandata/). Vi föreslår att ett meta-data post skapas i [SciLifeLab Data Repository](/support_services/general_data_repository/), med kontaktinformation för åtkomst, vilket genererar en permanent identifierare, en doi. DOI:n kan därefter användas i vetenskapliga publikationer för att hänvisa till dataseten. När den svenska EGA tagits i drift, och dataseten skickats in, kan åtkomstinformationen ändras för att hänvisa till EGA. Se till exempel [DOI: 10.17044/NBIS/G000014](https://doi.org/10.17044/NBIS/G000014).

    * [The European Nucleotide Archive (ENA)](https://www.ebi.ac.uk/ena)
    * [ENA SARS-CoV-2 submission guildelines](https://ena-browser-docs.readthedocs.io/en/latest/help_and_guides/sars-cov-2-submissions.html)
    * [SciLifeLab Data Repository for metadata records of sequence data with restricted access](https://scilifelab.se/data/repository)

    ***

* ##### Proteindata

    Se [FAIRsharing](https://fairsharing.org/) med sökterm ‘[proteomics](https://fairsharing.org/search/?q=proteomics&content=biodbcore&name=&taxonomies=&organisations=&shortname=&description=&supportlinks=&licenses=&countries=&maintainers=&expanded_onto_domains=&expanded_onto_disciplines=&user_defined_tags=&record_id=&miriam_id=&search_state=hidden)’ för en granskad lista över relevanta repositorier för proteomikdata. [Uniprot](https://www.uniprot.org/) är en av de viktigaste databaserna för proteinsekvenser. Proteinfamiljer lagras i [Pfam](http://pfam.xfam.org/) och strukturer i [PDBe](https://www.ebi.ac.uk/pdbe/node/1).

    Vi rekommenderar använding av repositoriet [PRIDE](https://www.ebi.ac.uk/pride/), som tillhandahålls av [ProteomeXchange](http://www.proteomexchange.org/) Consortium. Repositoriet tar emot protein- och peptiddata, med tillhörande masspektra och övriga relaterade datatyper. Använd PRIDE repository and [PX Submission Tool](https://www.ebi.ac.uk/pride/markdownpage/pridesubmissiontool).

    Andra typer av proteomikdata bör också göras tillgängliga genom datadelning, för detta rekommenderar vi använding av [SciLifeLab Data Repository](/support_services/general_data_repository/) för andra typer av proteomikdata. För att data skall vara användbar för vidare analys och integrering rekommenderar vi en detaljerad beskrivning av data och variabler inkluderas. Varje protein skall ha en unik indentifierar som ett UniProt ID eller ENGS ID  ( och ange vilken version som länken anges).  

    * [PRIDE repository](https://www.ebi.ac.uk/pride/) och [PX Submission Tool](https://www.ebi.ac.uk/pride/markdownpage/pridesubmissiontool)
    * [SciLifeLab Data Repository for other types of proteomics data](https://scilifelab.se/data/repository)

    ***

* ##### Bilddata

    Beroende på vilken typ av bilddata du har finns olika publika repositorier att välja bland, se [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/).

    * [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/)

    ***

* ##### Kemisk biologi

    Vi föreslår att kemisk biologi data skickas in till [ChEMBL](https://www.ebi.ac.uk/chembl/). ChEMBL är är en manuellt kurerad databas med bioaktiva molekyler med läkemedelsliknande egenskaper som drivs av EMBL-EBI. Databasen samlar kemiska och bioaktiva data samt genomikdata för att bidra till övergången från genomikdata till läkemedelsutveckling.

    * [ChEMBL](https://www.ebi.ac.uk/chembl/)

    ***

* ##### Hälsodata

    Ifråga om hälsodata, där data inte kan deponeras i en publik databas på grund av sekretessbegränsningar, föreslår vi istället att en metadata-post skapas i [SciLifeLab Data Repository](https://scilifelab.se/data/repository). Denna skall innehålla information om vilken data som finns tillgängliga, var ten åtkomstbegäran skall skickas, hur en åtkomstbegäran kan göras och vad som krävs för åtkomst av känsliga hälsodata. The SciLifeLab Data Repository, som kureras och drivs av SciLifeLab Data Centre, gör det möjligt att få en permanent indentifierare för en meta-data post. Den permanenta identifieraren, doi, kan senare användas i exempelvis publikationer för att hänvisa till vart datatillgänglighet.

    * [SciLifeLab Data Repository](https://scilifelab.se/data/repository)

    ***

### Stöd för datahanteringsplaner

För att effektivisera tillgängliggörande av data kan [SciLifeLab](https://www.scilifelab.se) och [NBIS](http://www.nbis.se/) hjälpa dig med att planera din datahantering i början av projektet, både genom [personliga konsultationer](https://nbis.se/support/supportform/index.php?form=consultation) och genom att tillhandahålla ett [anpassat verktyg](https://dsw.scilifelab.se/) för att skapa datahanteringsplaner.
Vi kan också hjälpa dig att identifiera lämpliga repositorier och gemensamma internationella standarder för att beskriva och publicera dina data, samt vägleda dig genom publiceringsprocessen.

* [Ansök om datahanteringskonsultation från NBIS](https://nbis.se/support/supportform/index.php?form=consultation)

##### Deponera data i en publik databas

Genom att deponera data i en publik databas godkänner du att data publiceras under vissa villkor för användning, som du ibland kan bestämma själv, ibland specificeras av den databas där du väljer att lägga data. En publicering innebär oftast att du får en kod som unikt identifierar ditt dataset, och ofta krävs denna information av olika journaler för att ett manuskript ska accepteras för publicering.

Om så krävs, kan data förses med ett moratorium, dvs det blir inte publikt förrän vid ett visst datum som du bestämmer.

_Observera att humandata kan behöva särskilda överväganden när det gäller publicering._

##### Lagra data hos ditt universitet eller SNIC

I Sverige gäller att rådata eller mätdata som genereras inom ett forskningsprojekt ägs av det lärosäte som har huvudmannaskap för projektet, medan resultat ägs av forskaren - det s.k. lärarundantaget. Råder inte sekretess eller skydd av personlig integritet för känsliga persondata, t.ex. biologiska mätdata från människa, så anses forskningsdata generellt vara allmän handling.

Lärosätet har ett juridiskt ansvar att arkivera data. Den datapublicering som vi stödjer i tjänsterna i denna portal ersätter inte detta ansvar. Därför bör du som forskare försäkra dig om att långtidslagra data genom de lösningar som ditt lärosäte tillhandahåller, och under den tid projektet är aktivt kan du få stöd för lagring och beräkning genom [Swedish National Infrastructure for Computing, SNIC](https://snic.se).

#### Övriga resurser

* [SciLifeLab Data Guidelines](https://scilifelab-data-guidelines.readthedocs.io/en/latest/docs/index.html)
* [European COVID-19 Data Portal deponeringsinformation](https://www.covid19dataportal.org/submit-data)
