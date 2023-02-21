---
title: Visualisation of COVID-19 and SARS-CoV-2 research in Sweden as reflected in publications
description: Översikt över publikationer relaterade till COVID-19 och SARS-CoV-2 där minst en medförfattare är verksam vid ett svenskt lärosäte. Visar publikationer över tid samt nyckelord/nyckelfraser i publikationerna.
toc: false
plotly: true
menu:
    dashboard_menu:
        identifier: covid_19_publications_vis
        name: Översikt över COVID-19 publikationer
aliases:
    - /projects/dashboard/
---
<div class="alert alert-info">
  <i class="bi bi-exclamation-triangle-fill"></i>
  <span>En svensk översättning av denna sida kommer inom kort.</span>
</div>

The visualisations on this page evaluate the development of COVID-19 and SARS-CoV-2 research across Sweden by assessing publication output. Specifically, we consider multiple aspects of journal publications and preprints where at least one author has an affiliation with a Swedish research institute. The database containing the publications themselves [can be found on this page](/publications/). Note that our database is manually curated and, as such, may not be exhaustive. The full database is available for download and use for other purposes, please see [DOI: 10.17044/scilifelab.14124014](https://doi.org/10.17044/scilifelab.14124014) for details.

The code used to produce the visulations on this page can be found on [GitHub](https://github.com/ScilifelabDataCentre/covid-portal-visualisations). Specifically, code related to the number of publications can be found in the ['Count_publications' folder of the repository](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/tree/main/Count_publications), and code used to generated the wordclouds can be found in the ['Wordcloud' folder](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/tree/main/Wordcloud).

## Number of new publications

This graph displays the number of publications (including both journal publications and preprints) published each month, as well as the cumulative daily total of publications contained in the database. The dates reflect either the preprint upload date or the official journal publication date, whichever is the most recent. Where a given day of publication is not specified in the publication/upload date, we assign the date as the first of the month. This causes the appearance of a relatively sharp increase at the start of each month. This chart is updated daily, though the publications database is not.

<div class="table-responsive">
{{< publications_per_month >}}
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Count_publications/count_publications.py).

## Ten most recent publications

This table displays the ten most recent publications in our database (including both journal publications and preprints). The date reflects the preprint upload date or the official journal publication date, whichever is the most recent. Authors are summarised in the same format as expected in 'in text' citations. Clicking on the title for a given publication will take you directly to that publication. Note though, that it will only be possible to read the full text of publication if it is open access or if you are granted access via a subscription (e.g. an institutional subscription, or private journal subscripton). Any additions to the manually curated publications database will become visible on this table within a day.

<div class="table-responsive">
{{< recent_ten >}}
</div>

## Most frequent words or two word phrases in the titles

These wordclouds display the words and two word phrases that appear most frequently in the titles of preprints or journal publications within the database. Note that we have filtered out commonly used words that are uninformative (e.g. 'the', 'a', 'this') as well as the words 'COVID-19' and 'SARS-CoV-2', since these appeared in almost all titles. The wordclouds are updated weekly.

**Code used to produce plot:** [Script to produce wordclouds](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Wordcloud/livewordcloud.py). Note that the script relies on multiple external files that can be found in the [same folder in the GitHub repository](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/tree/main/Wordcloud).

#### All publications

<div class="row my-4"><div class="col-md-8"><img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-titles_all.png"></div></div>

#### Publications attributed to particular research funders

Wordclouds are displayed for each funder that we identified as having been associated with at least 20 publications in the database.

<div class="container"> <div class="row mt-2"> <div class="col-md mr-4"> <div class="row"> <h5>Swedish Research Council:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-titles_vr.png"> </div> </div> <div class="col-md mr-4"> <div class="row"> <h5>SciLifeLab/KAW:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-titles_kaw.png"> </div> </div> <div class="col-md"> <div class="row"> <h5>Horizon 2020:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-titles_h2020.png"> </div> </div> </div> </div>

## Most frequent words or two word phrases in the abstracts

These wordclouds display the words and two word phrases that appear most frequently in the abstracts of preprints or journal publications within the database. Note that we have filtered out commonly used words that are uninformative (e.g. 'the', 'a', 'this') as well as the words 'COVID-19' and 'SARS-CoV-2', since these appeared in almost all abstracts. The wordclouds are updated weekly.

**Code used to produce plot:** [Script to produce wordclouds](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/Wordcloud/livewordcloud.py). Note that the script relies on multiple external files that can be found in the [same folder in the GitHub repository](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/tree/main/Wordcloud).

#### All publications

<div class="row my-4"><div class="col-md-8"><img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-abstracts_all.png"></div></div>

#### Publications attributed to particular research funders

Wordclouds are displayed for each funder that we identified as having been associated with at least 20 publications in the database.

<div class="container"> <div class="row mt-2"> <div class="col-md mr-4"> <div class="row"> <h5>Swedish Research Council:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-abstracts_vr.png"> </div> </div> <div class="col-md mr-4"> <div class="row"> <h5>SciLifeLab/KAW:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-abstracts_kaw.png"> </div> </div> <div class="col-md"> <div class="row"> <h5>Horizon 2020:</h5> </div> <div class="row"> <img src="https://blobserver.dckube.scilifelab.se/blob/covid-portal-abstracts_h2020.png"> </div> </div> </div> </div>
