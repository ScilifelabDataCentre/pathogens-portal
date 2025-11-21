---
title: Swedish COVID-19 publications May 2020 - May 2025
description: A summary of the COVID-19 and SARS-CoV-2 publications produced involving at least one contributor from a Swedish university or research institute. Shows publications over time and key words/phrases within them.
banner: /dashboard_thumbs/publications.jpg
toc: false
plotly: true
menu:
  dashboard_menu:
    identifier: covid_19_publications_vis
    name: "Swedish COVID-19 publications over 5 years"
aliases:
  - /projects/dashboard/
dashboards_topics: [COVID-19, Infectious diseases]
data_status: "historic"
---

This page explores Swedish research related to COVID-19 over 5 years (May 2020 - May 2025). The manually curated dataset (which is openly available on the [SciLifeLab Data Repository](https://doi.org/10.17044/scilifelab.14124014)) comprises publications about SARS-CoV-2/COVID-19 involving at least one author affiliated with a Swedish research institute/organisation. Each publication was tagged according to multiple factors, including subject (e.g. post-covid condition, vaccine research), type of publication (e.g. preprint, review, article), and the involvement of particular funders (e.g. the Swedish Research Council (Vetenskapsrådet)). Between May 2020 and May 2023, the list was compiled entirely manually by searching all publications databases. From May 2023, the Europe PMC REST API was used to identify publications. The scripts used to do this are [openly available on GitHub](https://github.com/ScilifelabDataCentre/pathogens-portal-scripts/tree/main/All_publications) and can be reused for work with other pathogens.

To see recent Swedish publications on multiple topics, please refer to the [publications page](/publications/).

## Number of publications

This graph displays the number of peer-reviewed articles and preprints published each month, as well as the cumulative daily total of publications. Publication date reflects either the date that the articles were uploaded to preprint servers or the date that the article was published in a journal. Where only a month of publication is provided, rather than a specific date, the date is assigned as the first day of the month. This can cause the appearance of a relatively sharp increase at the start of each month.

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/COVID_publication_count.json" height="600px" >}}</div>
</div>

**Code used to produce plot:** [Script to produce plot](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Count_publications/count_publications.py).

## Most frequent phrases in article titles

The wordclouds display the words and two word phrases that appear most frequently in the titles of preprints or peer-reviewed articles within the dataset. Commonly used, uninformative words (e.g. 'the', 'a', 'this') and the words 'COVID-19' and 'SARS-CoV-2' were excluded, as these appeared in almost all titles.

**Code used to produce plot:** [Script to produce wordclouds](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Wordcloud/livewordcloud.py). Note that the script relies on multiple external files that can be found in the [same folder in the GitHub repository](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/tree/main/Wordcloud).

#### All publications

The most common phrases when considering all publications in the dataset.

<div class="row my-4">
  <div class="col-md-8">
    <img alt="Wordcloud image from all titles" src="https://blobserver.dc.scilifelab.se/blob/covid-portal-titles_all.png">
  </div>
</div>

#### Subdivided by funder

The most common phrases when considering publications funded by the Swedish Research Council, the SciLifeLab and Knut and Alice Wallenberg's COVID-19 research program (SciLifeLab/KAW), or Horizon Europe (Horizon 2020).

<div class="container">
  <div class="row mt-2">
    <div class="col-md mr-4">
      <div class="row">
        <h5>Swedish Research Council:</h5>
      </div>
      <div class="row">
        <img alt="Wordcloud image from VR publication titles" src="https://blobserver.dc.scilifelab.se/blob/covid-portal-titles_vr.png">
      </div>
    </div>
    <div class="col-md mr-4">
      <div class="row">
        <h5>SciLifeLab/KAW:</h5>
      </div>
      <div class="row">
        <img alt="Wordcloud image from KAW publication titles" src="https://blobserver.dc.scilifelab.se/blob/covid-portal-titles_kaw.png">
      </div>
    </div>
    <div class="col-md">
      <div class="row">
        <h5>Horizon 2020:</h5>
      </div>
      <div class="row">
        <img alt="Wordcloud image from Horizon 2020 publication titles" src="https://blobserver.dc.scilifelab.se/blob/covid-portal-titles_h2020.png">
      </div>
    </div>
  </div>
</div>

## Most frequent phrases in article abstracts

The wordclouds display the words and two word phrases that appear most frequently in the abstracts of preprints or peer-reviewed articles within the dataset. Commonly used, uninformative words (e.g. 'the', 'a', 'this') and the words 'COVID-19' and 'SARS-CoV-2' were excluded, as these appeared in almost all abtracts.

**Code used to produce plot:** [Script to produce wordclouds](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/blob/main/Wordcloud/livewordcloud.py). Note that the script relies on multiple external files that can be found in the [same folder in the GitHub repository](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations/tree/main/Wordcloud).

#### All publications

The most common phrases when considering all publications in the dataset.

<div class="row my-4">
  <div class="col-md-8">
    <img alt="Wordcloud image from all publication abstract" src="https://blobserver.dc.scilifelab.se/blob/covid-portal-abstracts_all.png">
  </div>
</div>

#### Subdivided by funder

The most common phrases when considering publications funded by the Swedish Research Council, the SciLifeLab and Knut and Alice Wallenberg's COVID-19 research program (SciLifeLab/KAW), or Horizon Europe (Horizon 2020).

<div class="container">
  <div class="row mt-2">
    <div class="col-md mr-4">
      <div class="row">
        <h5>Swedish Research Council:</h5>
      </div>
      <div class="row">
        <img alt="Wordcloud image from VR publication abstract" src="https://blobserver.dc.scilifelab.se/blob/covid-portal-abstracts_vr.png">
      </div>
    </div>
    <div class="col-md mr-4">
      <div class="row">
        <h5>SciLifeLab/KAW:</h5>
      </div>
      <div class="row">
        <img alt="Wordcloud image from KAW publication abstract" src="https://blobserver.dc.scilifelab.se/blob/covid-portal-abstracts_kaw.png">
      </div>
    </div>
    <div class="col-md">
      <div class="row">
        <h5>Horizon 2020:</h5>
      </div>
      <div class="row">
        <img alt="Wordcloud image from Horizon 2020 publication abstract" src="https://blobserver.dc.scilifelab.se/blob/covid-portal-abstracts_h2020.png">
      </div>
    </div>
  </div>
</div>
