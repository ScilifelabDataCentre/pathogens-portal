---
title: COVID-19 and SARS-CoV-2 publications statistics
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
The visualizations on this page reflect how research on COVID-10 and SARS CoV-2 has been developing in Sweden in terms of the publication output. Specifically, we plot various aspects of journal publications and preprints where at least one author has an affiliation with a Swedish research institute. The full database [can be seen on this page](/publications/). Note that our database is manually curated and as such may not be exhaustive. The full dataset is available for download at X (including titles, abstracts, author lists, and bibliometric information).

## Number of new publications

The graph displays both the number of journal articles or preprints published each month as well as the cumulative total of publications per day. The dates reflect X. There is a bump on the first day of each month which is due to that not every publication is published with a particular day of the month; all publications without a particular day of the month assigned are shown on the 1st day of that month. Any other relevant info goes here.

{{< publications_per_month >}}

## Most frequent words or phrases in the titles

This wordcloud displays 200 most frequent words or phrases (where they make more sense) that appear in the titles of articles or journal publications. Note that we have filtered out functional words (such as 'the', 'a', 'this', etc.).

#### All publications

<div class="row my-4"><div class="col-8"><img src="/temp_pubs_plots/titles_all.png"></div></div>

#### Publications divided by research funders

We display funders for which we identified at least 20 publications.

<div class="container"> <div class="row mt-2"> <div class="col mr-4"> <div class="row"> <h5>Swedish Research Council:</h5> </div> <div class="row"> <img src="/temp_pubs_plots/titles_vr.png"> </div> </div> <div class="col mr-4"> <div class="row"> <h5>SciLifeLab/KAW:</h5> </div> <div class="row"> <img src="/temp_pubs_plots/titles_kaw.png"> </div> </div> <div class="col"> <div class="row"> <h5>Horizon 2020:</h5> </div> <div class="row"> <img src="/temp_pubs_plots/titles_h2020.png"> </div> </div> </div> </div>

## Most frequent words or phrases in the abstracts

The wordclouds display 200 most frequent words or phrases (where they make more sense) that appear in the abstracts of articles or journal publications. Note that we have filtered out functional words (such as 'the', 'a', 'this', etc.).

#### All publications

<div class="row my-4"><div class="col-8"><img src="/temp_pubs_plots/abstracts_all.png"></div></div>

#### Publications divided by research funders

We display funders for which we identified at least 20 publications.

<div class="container"> <div class="row mt-2"> <div class="col mr-4"> <div class="row"> <h5>Swedish Research Council:</h5> </div> <div class="row"> <img src="/temp_pubs_plots/abstracts_vr.png"> </div> </div> <div class="col mr-4"> <div class="row"> <h5>SciLifeLab/KAW:</h5> </div> <div class="row"> <img src="/temp_pubs_plots/abstracts_kaw.png"> </div> </div> <div class="col"> <div class="row"> <h5>Horizon 2020:</h5> </div> <div class="row"> <img src="/temp_pubs_plots/abstracts_h2020.png"> </div> </div> </div> </div>
