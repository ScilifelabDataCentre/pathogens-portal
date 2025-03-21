---
title: SciLifeLab Autoimmunity and Serology profiling facility, statistik för SARS-CoV-2 antikroppstester
description: SARS-CoV-2 antikoppstestning utförs av SciLifeLab Autoimmunology and Serology Profiling Facility. Denna dashboard visa totalt antal tester, positiva och negativa, som utförts över tid.
banner: /dashboard_thumbs/auto_sero.jpg
toc: false
menu:
  dashboard_menu:
    identifier: serology
    name: SARS-CoV-2 antikoppstester som utförts av SciLifeLab
aliases:
  - /sv/data_types/health_data/serology-statistics/
dashboards_topics: [COVID-19, Infectious diseases]
plotly: true
data_status: "updating" # or "historic"
---

<div class="alert alert-info">
  <i class="bi bi-exclamation-triangle-fill"></i>
  <span>Denna sida är primärt ett arkiv för tidigare publicerade data, men den kan komma att uppdateras även i framtiden.  Enheten Autoimmunity and Serology Profiling har nu utökat sin pandemiberedskap till att omfatta tester för flera andra virus. Information om detta arbete finns på <a class="dark-blue" href="/dashboards/serology_multidisease/"> 'multi-disease serology dashboard'</a>.</span>
</div>

Serologiska tester innebär att kroppsvätskor testas för förekomst av antikroppar eller andra ämnen. Sedan pandemins början har enheten SciLifeLab Autoimmunity and Serology Profiling genomfört serologiska tester för antikroppar riktade mot SARS-CoV-2-proteiner. Enheten har kontinuerligt tillhandahållit de senaste uppgifterna till Swedish Pathogens Portal. I vart och ett av avsnitten nedan visar vi antalet prover som var **positiva**, **negativa** eller **forskning och utveckling (R&D)**.

- **Positiva tester**: Serologiska tester som indikerar _förekomst_ av immunoglobulin G (IgG)-antikroppar mot SARS-CoV-2-proteiner.
- **Negativa tester**: Serologiska tester som indikerar _frånvaro_ av immunoglobulin G (IgG)-antikroppar mot SARS-CoV-2-proteiner.
- **R&D-tester**: Alla återstående serum-, plasma- och salivprover som kompletterades för att testa nivåerna IgG-, IgM- eller IgA-antikroppar mot SARS-CoV-2-proteiner. Detta omfattar alla positiva och negativa kontroller, alla replikerade och omreplikerade prover och analyser, alla prover som analyserats under den kontinuerliga utvecklingen och optimeringen av testerna, tekniskt misslyckade prover och alla forskningsrelaterade projekt.

<div class="alert alert-info">Senaste uppdatering: {{% serology_date_modified %}}</div>

## Serologiska tester per vecka

Antalet SARS-CoV-2 serologitester som SciLifeLab Autoimmunity and Serology Profiling-enheten genomförde varje vecka, uppdelat efter om testerna var positiva, negativa eller inom forskning och utveckling (R&D).

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 800px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/weekly_serology_tests.json" height="550px" >}}</div>
</div>

<!-- **Ladda ner data:** [Serology-testing-statistics-dataset-20202021.csv](https://blobserver.dc.scilifelab.se/blob/Serology-testing-statistics-dataset-20202021.csv) -->

**Källkod som används för att skapa grafen:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/serology/weekly-serology-tests.py).

## Kumulativa serologiska tester

Det kumulativa antalet positiva, negativa och forsknings- och utvecklingstester (R&D) av SARS-CoV-2-serologi som slutförts över tid vid SciLifeLab Autoimmunity and Serology Profiling-enheten.

<div class="d-md-none alert alert-info">
  Att rotera mobiltelefonen kan förbättra grafens layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive" style="min-width: 800px">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/cumulative_serology_tests.json" height="550px" >}}</div>
</div>

<!-- **Ladda ner data:** [Serology-testing-statistics-dataset-20202021.csv](https://blobserver.dc.scilifelab.se/blob/Serology-testing-statistics-dataset-20202021.csv) -->

**Källkod som används för att skapa grafen:** [Källkod](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/serology/cumulative-serology-tests.py).

#### Om serologisk testning vid enheten för Autoimmunity and Serology Profiling

Tidigt under covid-19-pandemin inleddes arbetet med att [utveckla en serologisk analys](https://www.scilifelab.se/capabilities/pandemic-laboratory-preparedness/pandemic-response/other-scilifelab-efforts/serology/) för storskalig testning av plasma- och serumprover för antikroppar mot SARS-CoV-2. Arbetet utfördes av tre forskargrupper vid [institutionen för proteinvetenskap, Kungliga Tekniska Högskolan (KTH)](https://www.kth.se/sv/pro/protein-science-1.784558) och [enheten för autoimmunitet och serologisk profilering](https://www.scilifelab.se/facilities/autoimmunity-profiling/) vid [SciLifeLab](https://www.scilifelab.se).

Genom att jämföra och kombinera ett stort antal varianter av SARS-CoV-2-proteiner som antigener etablerades en [mycket känslig och specifik så kallad multiplex bead-based assay](https://doi.org/10.1002/cti2.1312). Assayen med hög kapacitet kan användas för att bearbeta upp till 8000 prover per vecka. De allra flesta prover som hittills har analyserats kommer från vårdpersonal, befolkningsbaserade studier, personal inom läkemedels- och bioteknikindustrin samt från flera olika forskningssamarbeten. Samarbetspartners och provleverantörer inkluderar samhällsstudien vid Danderyds universitetssjukhus ([se nyhet om uppföljningsstudie vid Danderyds universitetssjukhus](https://www.scilifelab.se/news/four-out-of-five-still-have-antibodies-against-sars-cov-2)), Karolinska universitetssjukhuset, Akademiska sjukhuset i Uppsala, Skånes universitetssjukhus, Universitetssjukhuset Örebro, Sophiahemmet, Folkhälsomyndigheten, RISE (Research Institutes of Sweden), AstraZeneca, Cytiva, SVPH, Karolinska Institutet, KTH, Uppsala universitet och Lunds universitet.

Kolla in [Autoimmunity and Serology Profiling unit page](https://www.scilifelab.se/units/autoimmunity-profiling/) på SciLifeLabs webbplats för att få reda på mer om själva enheten. Publikationer som producerats av studier som använder enheten finns tillgängliga i databasen [SciLifeLab Infrastructure Publications](https://publications.scilifelab.se/label/Autoimmunity%20and%20Serology%20Profiling).
