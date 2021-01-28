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

European Bioinformatics Institute (EBI) driver många olika internationella databaser som bör användas när så är lämpligt. Se deras [Covid-19 Data Portal data submission sida](https://www.covid19dataportal.org/submit-data). Om ditt datamaterial består av datatyper där ingen annan lämplig databas finns tillgänglig kan det deponeras i [SciLifeLab Data Repository](https://scilifelab.se/data/repository) som drivs av SciLifeLab Data Centre. För känsliga persondata som måste lagras i en säker miljö med kontrollerad åtkomst kan SciLifeLab ge [support för publicering och licensgivning](https://www.scilifelab.se/data/humandata/).

Här kommer våra riktlinjer för publicering av data för varje specifik datatyp:

* ##### Genomik & transkriptomik data

    Vi föreslår att rådata samt assemblerad och annoterad genomdata skickas in till [ENA](https://www.ebi.ac.uk/ena). Se dokumentation om publiceringsprocessen [SARS-CoV-2 submission](https://ena-browser-docs.readthedocs.io/en/latest/help_and_guides/sars-cov-2-submissions.html). Innan sekvensdata (t.ex. ‘shot gun’-sekvenser) skickas in är det nödvändigt att ta bort humana (kontaminerande) sekvenser.

    Sekvensdata för värd (human) kräver kontrollerad åtkomst, och NBIS utvecklar för närvarande en lokal version av European Genome-phenome Archive (EGA) i Sverige (EGA-SE), vilket möjliggör publicering av känsliga personuppgifter inom en juridisk ram. Tills dess att EGA-SE är tillgänglig, bör datamaterialet förbli i den säkra analysmiljön (t.ex. på Bianca på Uppmax). Vi föreslår att man i [SciLifeLab Data Repository](https://scilifelab.figshare.com/) skapar ett metadatainlägg med kontaktinformation om hur man får åtkomst, och för vilken en DOI (dvs. en beständig identifierare) kan bli utfärdad. DOI:n kan sedan användas i artikeln för att hänvisa till datamaterialet. När svenska EGA är i drift, och datamaterialet skickats in där, kan åtkomstinformationen ändras till att hänvisa dit istället. Se till exempel [DOI: 10.17044/NBIS/G000014](https://doi.org/10.17044/NBIS/G000014).

    * [The European Nucleotide Archive (ENA)](https://www.ebi.ac.uk/ena)
    * [Riktlinjer för publicering av data om SARS-CoV-2 i ENA](https://ena-browser-docs.readthedocs.io/en/latest/help_and_guides/sars-cov-2-submissions.html)
    * [SciLifeLab Data Repostory för metadata om sekvensdata med begränsad åtkomst](https://scilifelab.se/data/repository)

    ***

* ##### Proteindata

    [Uniprot](https://www.uniprot.org/) är en av de viktigaste databaserna för proteinsekvenser. Proteinfamiljer lagras i [Pfam](http://pfam.xfam.org/) och strukturer i [PDBe](https://www.ebi.ac.uk/pdbe/).

    Se [FAIRsharing](https://fairsharing.org/) med sökterm ['proteomics'](https://fairsharing.org/search/?q=proteomics&content=biodbcore&name=&taxonomies=&organisations=&shortname=&description=&supportlinks=&licenses=&countries=&maintainers=&expanded_onto_domains=&expanded_onto_disciplines=&user_defined_tags=&record_id=&miriam_id=&search_state=hidden) för en granskad lista över relevanta repositorier för proteomikdata.

    Vi rekommenderar att använda repositoriet [PRIDE](https://www.ebi.ac.uk/pride/), som tillhandahålls av  [ProteomeXchange Consortium](http://www.proteomexchange.org/). Repositoriet tar emot protein- och peptiddata, med tillhörande masspektra och övriga, relaterade, datatyper.

    * [PRIDE repository](https://www.ebi.ac.uk/pride/) and [PX Submission Tool](https://www.ebi.ac.uk/pride/markdownpage/pridesubmissiontool)
    * [SciLifeLab Data Repository för andra typer av proteomikdata](https://scilifelab.se/data/repository)

    ***

* ##### Bilddata

    Beroende på vilken typ av avbildningsdata du har så finns det olika publika repositorer att välja bland, se tabellen [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/).

    * [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/)

    ***

* ##### Kemisk biologi

    Vi föreslår att kemisk biologi data skickas in till [ChEMBL](https://www.ebi.ac.uk/chembl/). ChEMBL är är en manuellt kurerad databas med bioaktiva molekyler med läkemedelsliknande egenskaper som drivs av EMBL-EBI. Den samlar kemisk, bioaktivitets- och genomdata för att underlätta översättningen av genominformation till effektiva nya läkemedel.

    * [ChEMBL](https://www.ebi.ac.uk/chembl/)

    ***

* ##### Hälsodata

    I fall där data inte kan deponeras i en publik databas på grund av sekretessbegränsningar föreslår vi att du skapar en metadata-post i [SciLifeLab Data Repository](https://scilifelab.se/data/repository) med information om vilken data som finns tillgängliga på begäran och hur en sådan begäran kan göras. The SciLifeLab Data Repository hanteras lokalt av SciLifeLab Data Centre, och gör det möjligt att få en DOI som sedan kan hänvisas till i publikationen.

    * [SciLifeLab Data Repository](https://scilifelab.se/data/repository)

### Stöd för datahanteringsplaner

För att effektivisera tillgängliggörande av data kan [SciLifeLab](https://www.scilifelab.se) och [NBIS](http://www.nbis.se/) hjälpa dig med att planera din datahantering i början av projektet, både genom [personliga konsultationer](https://nbis.se/support/supportform/index.php?form=consultation) och genom att tillhandahålla ett [anpassat verktyg](https://dsw.scilifelab.se/) för att skapa datahanteringsplaner.
Vi kan också hjälpa dig att identifiera lämpliga repositorier och gemensamma internationella standarder för att beskriva och publicera dina data, samt vägleda dig genom publiceringsprocessen.

* [Ansök om datahanteringskonsultation från NBIS](https://nbis.se/support/supportform/index.php?form=consultation)

###### Deponera data i en publik databas

Genom att deponera data i en publik databas godkänner du att data publiceras under vissa villkor för användning, som du ibland kan bestämma själv, ibland specificeras av den databas där du väljer att lägga data. En publicering innebär oftast att du får en kod som unikt identifierar ditt dataset, och ofta krävs denna information av olika journaler för att ett manuskript ska accepteras för publicering.

Om så krävs, kan data förses med ett moratorium, dvs det blir inte publikt förrän vid ett visst datum som du bestämmer.

_Observera att humandata kan behöva särskilda överväganden när det gäller publicering._

###### Lagra data hos ditt universitet eller SNIC

I Sverige gäller att rådata eller mätdata som genereras inom ett forskningsprojekt ägs av det lärosäte som har huvudmannaskap för projektet, medan resultat ägs av forskaren - det s.k. lärarundantaget. Råder inte sekretess eller skydd av personlig integritet för känsliga persondata, t.ex. biologiska mätdata från människa, så anses forskningsdata generellt vara allmän handling.

Lärosätet har ett juridiskt ansvar att arkivera data. Den datapublicering som vi stödjer i tjänsterna i denna portal ersätter inte detta ansvar. Därför bör du som forskare försäkra dig om att långtidslagra data genom de lösningar som ditt lärosäte tillhandahåller, och under den tid projektet är aktivt kan du få stöd för lagring och beräkning genom [Swedish National Infrastructure for Computing, SNIC](https://snic.se).

###### Övriga resurser

* [SciLifeLab Data Guidelines](https://scilifelab-data-guidelines.readthedocs.io/en/latest/docs/index.html)
* [European COVID-19 Data Portal deponeringsinformation](https://www.covid19dataportal.org/submit-data)
