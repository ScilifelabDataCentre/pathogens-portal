---
title: Visualisation of COVID-19 and SARS-CoV-2 research in Sweden as reflected in publications
toc: false
menu:
    projects:
        name: Publications statistics
        identifier: dashboard
        weight: 15
    footer_sections:
        name: Publications statistics
        weight: 25
---
The visualisations on this page reflect how research on COVID-19 and SARS-CoV-2 has been developing in Sweden in terms of the publication output. Specifically, we plot various aspects of journal publications and preprints where at least one author has an affiliation with a Swedish research institute. The database of the publications themselves [can be found on this page](/publications/). Note that our database is manually curated and as such may not be exhaustive. The full dataset of publications is available for download and use for other purposes, please see [DOI: 10.17044/scilifelab.14124014](https://doi.org/10.17044/scilifelab.14124014) for details.

## Number of new publications

The graph displays the number of publications (including both journal publications and preprints) published each month as well as the cumulative total of publications per day. The dates reflect the preprint upload date or the official journal publication date, whichever is the most recent. A bump on the first day of each month appears due to that not every publication is published with a particular day of the month; all publications without a particular day of the month assigned are shown on the 1st day of that month.

<div class="table-responsive">
{{< publications_per_month >}}
</div>

## Most frequent words or phrases in the titles

This word cloud display most frequent words or phrases (where they make more sense) that appear in the titles of preprints or journal publications. Note that we have filtered out functional words (such as 'the', 'a', 'this', etc.) as well as words 'COVID-19' and 'SARS-CoV-2' since all publication titles contained those.

#### All publications

<div class="row my-4"><div class="col-md-8"><img src="https://dc-dynamic.dckube.scilifelab.se/covid-portal/titles_all.png"></div></div>

#### Publications divided by research funders

We display funders for which we identified at least 20 publications.

<div class="container"> <div class="row mt-2"> <div class="col-md mr-4"> <div class="row"> <h5>Swedish Research Council:</h5> </div> <div class="row"> <img src="https://dc-dynamic.dckube.scilifelab.se/covid-portal/titles_vr.png"> </div> </div> <div class="col-md mr-4"> <div class="row"> <h5>SciLifeLab/KAW:</h5> </div> <div class="row"> <img src="https://dc-dynamic.dckube.scilifelab.se/covid-portal/titles_kaw.png"> </div> </div> <div class="col-md"> <div class="row"> <h5>Horizon 2020:</h5> </div> <div class="row"> <img src="https://dc-dynamic.dckube.scilifelab.se/covid-portal/titles_h2020.png"> </div> </div> </div> </div>

## Most frequent words or phrases in the abstracts

The word clouds display most frequent words or phrases (where they make more sense) that appear in the abstracts of preprints or journal publications. Note that we have filtered out functional words (such as 'the', 'a', 'this', etc.) as well as words 'COVID-19' and 'SARS-CoV-2' since all publication abstracts contained those.

#### All publications

<div class="row my-4"><div class="col-md-8"><img src="https://dc-dynamic.dckube.scilifelab.se/covid-portal/abstracts_all.png"></div></div>

#### Publications divided by research funders

We display funders for which we identified at least 20 publications.

<div class="container"> <div class="row mt-2"> <div class="col-md mr-4"> <div class="row"> <h5>Swedish Research Council:</h5> </div> <div class="row"> <img src="https://dc-dynamic.dckube.scilifelab.se/covid-portal/abstracts_vr.png"> </div> </div> <div class="col-md mr-4"> <div class="row"> <h5>SciLifeLab/KAW:</h5> </div> <div class="row"> <img src="https://dc-dynamic.dckube.scilifelab.se/covid-portal/abstracts_kaw.png"> </div> </div> <div class="col-md"> <div class="row"> <h5>Horizon 2020:</h5> </div> <div class="row"> <img src="https://dc-dynamic.dckube.scilifelab.se/covid-portal/abstracts_h2020.png"> </div> </div> </div> </div>
