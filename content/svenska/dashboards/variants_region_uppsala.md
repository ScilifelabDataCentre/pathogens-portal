---
title: SARS-CoV-2-varianter upptäckta i Region Uppsala
description: Övervakning av virusgenomsekvenser är avgörande för att kunna spåra spridningen av virusvarianter. Denna dashboard visar data från helgenomsekvenseringar som genererats av Akademiska sjukhuset i Uppsala.
banner: /dashboard_thumbs/nanopore_seq_cropped.png
toc: true
plotly: true
menu:
  dashboard_menu:
    identifier: clinmicro_uppsala
    name: SARS-COV-2 helgenomsekvensering (Uppsala)
dashboards_topics: [COVID-19, Infectious diseases]
---

## Introduktion

Att ha en kontinuerlig övervakning av en viral patogen är avgörande för att kunna minimera den specifika patogenens påverkan på samhället. Utan övervakning saknas information om en viss patogen förekommer i ett geografiskt området, om nya stammar har skapats eller om det finns risk för utbrott.

Under hela COVID-19 pandemin och fram till idag har Sektionen för [klinisk mikrobiologi och sjukhushygien vid Akademiska sjukhuset i Uppsala](https://www.akademiska.se/en/departments/departments/klinisk-mikrobiologi-och-vardhygien/) genomfört övervakning av SARS-CoV-2 i Uppsala. De har kört helgenomsekvensering av prover från SARS-CoV-2-positiva patienter i Uppsalaregionen. Under hela covid-19-pandemin sekvenserade de över 12 000 prover från Uppsala. Forskarna är del av nätverket för Pandemisk Laboratorie Beredskap.

Denna dashboard innehåller två visualiseringar av data från Sektionen för klinisk mikrobiologi och sjukhushygien vid Akademiska sjukhuset i Uppsala. Sidan innehåller även kontaktuppgifter till forskarna som delar dessa data samt länkar till relevanta publikationer.

Data på denna dashboard ska uppdateras veckovis.

## SARS-CoV-2 sekvenser Visualiseringar

<div class="alert alert-info">Senaste uppdaterad: <span id="last_modified_uuclinmicro"></span></div>

Sekvenserna presenteras enligt deras [World Health Organisation (WHO) etikett](https://www.who.int/activities/tracking-SARS-CoV-2-variants) (en grekisk bokstav) och/eller deras Pango-linje. Pango-linjen bestäms med hjälp av [Pangolin](https://cov-lineages.org/resources/pangolin.html), [Nextclade](https://clades.nextstrain.org/) och ett internt annotationsbaserat arbetsflöde för mutationsanalys.

### Nya sekvenser med Pango-linje

Diagrammet nedan visar procentandelen sekvenser som tillhörde en viss härstamning varje vecka. Datumet tilldelas som måndagen i den veckan. Diagrammet visar data från början av 2023 i första hand, men innehåller flera dynamiska funktioner som kan användas för att fokusera på vissa delmängder av data.

Använd knappen **'Last 16 weeks'** för att endast se data från de senaste 16 veckorna, och knappen **'Data since jan 2023'** för att återigen visa alla data från början av 2023. Använd knappen **'Deselect all lineages'** för att rensa bort data från alla linjer från grafen. Det är sedan möjligt att visa endast vissa linjer genom att klicka på dem i teckenförklaringen. Du kan använda knappen **’Select all lineages’** för att visa data från alla linjer. Grafen har också många andra interaktiva funktioner. Det är t.ex. möjligt att klicka och dra för att fokusera på en viss del av grafen. När du för muspekaren över diagrammet visas alternativ uppe till höger för att t.ex. zooma, ladda ner som en .png-fil eller återställa axlarna till den ursprungliga vyn.

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/lineage_four_recent.json" height="600px" >}}</div>
</div>

**Källkod som används för att skapa grafen:** [Källkod som används för att skapa grafen](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/ClinMicro/lineage_four_recent.py).

### Alla sekvenser med WHO-märkning/Pango-linje)

Diagrammet nedan visar hur många procent av sekvenserna från varje vecka som tillhörde en viss linje. Datumet anges som måndagen i den vecka då proverna samlades in. Diagrammet visar alla data som samlats in sedan 2021.

Använd knappen **'Deselect all lineages'** för att rensa bort data från alla linjer från diagrammet. Det är sedan möjligt att visa endast vissa linjer genom att klicka på dem i teckenförklaringen. Du kan använda knappen **’Select all lineages’** för att visa data från alla linjer. Grafen har också många andra interaktiva funktioner. Det är t.ex. möjligt att klicka och dra för att fokusera på en viss del av grafen. När du för muspekaren över diagrammet visas alternativ uppe till höger för att t.ex. zooma, ladda ner som en .png-fil eller återställa axlarna till den ursprungliga vyn.

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/lineage_one_wholetime.json" height="600px" >}}</div>
</div>

**Källkod som används för att skapa grafen:** [Källkod som används för att skapa grafen](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/ClinMicro/lineage_one_plot.py).

## Kommentarer från forskargruppen

<div><b>Date:</b> <span id="clinmicro_uu_comment_date"></span><br><b>Kommentarer:</b> <span id="clinmicro_uu_comment"></span></div>

{{< clinmicro_dynamic_content >}}

## Kontaktinformation

**Jonathan Haars**, laboratorieingenjör och doktorand vid Akademiska sjukhuset och Uppsala universitet. ([jonathan.haars@akademiska.se](mailto:jonathan.haars@akademiska.se))

**René Kaden**, mikrobiolog och forskare vid Akademiska sjukhuset och Uppsala universitet. ([rene.kaden@akademiska.se](mailto:rene.kaden@akademiska.se))

## Publikationer

Haars, J., Palanisamy, N., Wallin, F., Mölling, P., Lindh, J., Sundqvist, M., Ellström, P., Kaden, R., Lennerstrand, J. (2023). Prevalence of SARS-CoV-2 Omicron Sublineages and Spike Protein Mutations Conferring Resistance against Monoclonal Antibodies in a Swedish Cohort during 2022–2023. _Microorganisms_, **11**, 2417. DOI: [10.3390/microorganisms11102417](https://doi.org/10.3390/microorganisms11102417).

Mannsverk, S., Bergholm, J., Palanisamy, N., Ellström, P., Kaden, R., Lindh, J., Lennerstrand, J. (2022). SARS-CoV-2 variants of concern and spike protein mutational dynamics in a Swedish cohort during 2021, studied by Nanopore sequencing. _Virology Journal_, **19**, 164. DOI: [10.1186/s12985-022-01896-x](https://doi.org/10.1186/s12985-022-01896-x).

Martinell, M., Andersson, T., Mannsverk, S., Bergholm, J., Ellström, P., Hill, A., Lindh, J., Kaden, R. (2022). In-Flight Transmission of a SARS-CoV-2 Lineage B.1.617.2 Harbouring the Rare S:E484Q Immune Escape Mutation. _Viruses_, **14**, 504. DOI: [10.3390/v14030504](https://doi.org/10.3390/v14030504).
