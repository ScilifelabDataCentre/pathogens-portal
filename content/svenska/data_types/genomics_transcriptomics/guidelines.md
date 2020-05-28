---
title: Riktlinjer för genomik & transkriptomik data
menu:
    main:
        name: Riktlinjer för dataproduktion
        identifier: genomics_transcriptomics_guidelines
        parent: genomics_transcriptomics
        weight: 20
---

## Riktlinjer för COVID-19-data
Gör dina Covid-19-forskningsdata användbara och tillgängliga för resten av forskarvärlden genom att publicera data och tillhörande metadata i en öppen databas.
 
[SciLifeLab](https://www.scilifelab.se) och [NBIS](http://www.nbis.se/) kan hjälpa dig med att i början av projektet planera datahanteringen för att effektivisera datadelning, både genom [konsultationer](https://nbis.se/support/supportform/index.php?form=consultation) och genom att tillhandahålla ett [verktyg](https://dsw.scilifelab.se/) för att skapa datahanteringsplaner. Vi kan också hjälpa dig att identifiera relevanta repositorier och etablerade internationella standarder för att beskriva och publicera dina data, samt vägleda dig genom publiceringsprocessen.
 
### Repositorier
Vi föreslår att rådata samt assemblerad och annoterad genomdata skickas in till [ENA](https://www.ebi.ac.uk/ena). Se dokumentation om publiceringsprocessen [SARS-CoV-2 submission](https://ena-browser-docs.readthedocs.io/sv/latest/help_and_guides/sars-cov-2-submissions.html). Innan sekvensdata (t.ex. ‘shot gun’-sekvenser) skickas in är det nödvändigt att ta bort humana (kontaminerande) sekvenser.
 
Sekvensdata för värd (human) kräver kontrollerad åtkomst, och NBIS utvecklar för närvarande en lokal version av European Genome-phenome Archive (EGA) i Sverige (EGA-SE), vilket möjliggör publicering av känsliga personuppgifter inom en juridisk ram. Tills dess att EGA-SE är tillgänglig, bör datamaterialet förbli i den säkra analysmiljön (t.ex. på Bianca på Uppmax). Vi föreslår att man i [SciLifeLab Data Repository](https://scilifelab.figshare.com/) skapar ett metadatainlägg med kontaktinformation om hur man får åtkomst, och för vilken en DOI (dvs. en beständig identifierare) kan bli utfärdad. DOI:n kan sedan användas i artikeln för att hänvisa till datamaterialet. När svenska EGA är i drift, och datamaterialet skickats in där, kan åtkomstinformationen ändras till att hänvisa dit istället. Se till exempel [https://doi.org/10.17044/NBIS/G000014](https://doi.org/10.17044/NBIS/G000014).
 
### Metadata
Metadata innebär 'data om data' och kan innehålla information om metod som används för att samla in data, analytisk och procedurell information, definitioner av variabler, mätenheter, eventuella antaganden, format och filtyp för datamaterialet och programvara som används för att samla in och / eller bearbeta data. Forskare rekommenderas starkt att använda etablerade metadatastandarder där dessa finns. 

[MINSEQE](https://doi.org/10.25504/FAIRsharing.a55z32) (Minimal Information about a high throughput SEQuencing Experiment) är den föredragna minimala metadatastandarden för transkriptomikdata. För virusdata kan du överväga att använda [ENA virus pathogen reporting standard checklist](https://www.ebi.ac.uk/ena/data/view/ERC000033). 

Det rekommenderas starkt att redan från början av projektet strukturera t.ex. metadata på ett sätt som möjliggör publicering av sekvensdata utan att behöva strukturera om metadata.
 
* [Mer information om repositorier, dataformat och metadatastandarder](https://scilifelab-data-guidelines.readthedocs.io/en/latest/docs/covid-19/index.html#guidelines-about-repositories-data-formats-and-metadata-standards) (engelska)
