---
title: SARS-CoV-2 variants detected in Region Uppsala
description: Surveillance of viral genome sequences is crucial in tracking the spread of viral variants. This dashboard shows whole-genome sequencing data generated by Uppsala University Hospital.
toc: true
plotly: true
banner: /dashboard_thumbs/nanopore_seq_cropped.jpg
menu:
  dashboard_menu:
    identifier: clinmicro_uppsala
    name: SARS-CoV-2 whole genome sequencing (Region Uppsala)
dashboards_topics: [COVID-19, Infectious diseases]
---

## Introduction

Surveillance of a viral pathogen is essential for minimising the impacts of that pathogen on society. Without surveillance, it is difficult to understand whether a given pathogen occurs in the area, whether new strains have appeared, or if an outbreak may be likely.

Throughout the pandemic and until present day, the section for [Clinical Microbiology and Hospital Hygiene at Uppsala University Hospital](https://www.akademiska.se/en/departments/departments/klinisk-mikrobiologi-och-vardhygien/) have conducted surveillance for SARS-CoV-2 in Uppsala. To do this, they performed whole genome sequencing on samples from SARS-CoV-2 positive patients in the Uppsala region. Throughout the COVID-19 pandemic, they sequenced over 12,000 samples from Uppsala.

This dashboard includes two visualisations of the data from the section for Clinical Microbiology and Hospital Hygiene at Uppsala University Hospital. It also contains contact information for those behind the work, information about the code used to generate the graphs, and relevant publications. The data on this dashboard will be updated **approximately weekly**.

## SARS-CoV-2 Sequence Visualisations

<div class="alert alert-info">Last updated: <span id="last_modified_uuclinmicro"></span></div>

The sequences are presented according to their [World Health Organisation (WHO) label](https://www.who.int/activities/tracking-SARS-CoV-2-variants) (a greek letter) and/or their Pango lineage. The Pango lineage is determined using [Pangolin](https://cov-lineages.org/resources/pangolin.html), [Nextclade](https://clades.nextstrain.org/), and an in-house annotation-based mutation analysis workflow.

### Recent sequences with Pango lineage

The below plot shows the percentage of sequences that belonged to a given lineage each week. The date is allocated as the Monday of that week. This plot shows data from the start of 2023 in the first instance, but includes multiple dynamic features that can be used to focus on certain subsets of the data.

Use the **‘Last 16 weeks’ button** to see data only from the last 16 weeks, and the **‘Data since Jan 2023’ button** to again show all of the data from the start of 2023. Use the **’Deselect all linages’ button** to clear data from all lineages from the graph. It is possible to then view only certain lineages by clicking on them in the legend. You can use the **’Select all lineages’ button** to show data from all lineages. The graph also has many other interactive features. For example, it is possible to click and drag to focus on a certain part of the graph. When you hover over the graph, options will appear in the top right to e.g. zoom, download as a .png file, or reset the axes to the original view.

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/lineage_four_recent.json" height="600px" >}}</div>
</div>

**Code used to produce plots:** [Graph and data preparation script](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/ClinMicro/lineage_four_recent.py).

### All sequences with WHO label/Pango lineage)

The below plot shows the percentage of sequences from each week belonged to a given lineage. The date is allocated as the Monday of the week that the samples were collected. The plot shows all of the data collected since 2021.

Use the **’Deselect all lineages’ button** to clear data from all lineages from the graph. It is possible to then view only certain lineages by clicking on them in the legend. You can use the **’Select all lineages’ button** to show data from all lineages. The graph also has many other interactive features. For example, it is possible to click and drag to focus on a certain part of the graph. When you hover over the graph, options will appear in the top right to e.g. zoom, download as a .png file, or reset the axes to the original view.

<div class="d-md-none alert alert-info">
  Rotating your phone may improve graph layout
</div>

<div class="plot_wrapper mb-3">
  <div class="table-responsive">{{< plotly json="https://blobserver.dc.scilifelab.se/blob/lineage_one_wholetime.json" height="600px" >}}</div>
</div>

**Code used to produce plots:** [Graph and data preparation script](https://github.com/ScilifelabDataCentre/covid-portal-visualisations/blob/main/ClinMicro/lineage_one_plot.py).

## Commentary from the research group

<div><b>Date:</b> <span id="clinmicro_uu_comment_date"></span><br><b>Commentary:</b> <span id="clinmicro_uu_comment"></span></div>

{{< clinmicro_dynamic_content >}}

## Contact

**Jonathan Haars**, laboratory technician and PhD student at Uppsala University Hospital and Uppsala University. ([jonathan.haars@akademiska.se](mailto:jonathan.haars@akademiska.se))

**René Kaden**, microbiologist and researcher at Uppsala University Hospital and Uppsala University. ([rene.kaden@akademiska.se](mailto:rene.kaden@akademiska.se))

## Publications

Haars, J., Palanisamy, N., Wallin, F., Mölling, P., Lindh, J., Sundqvist, M., Ellström, P., Kaden, R., Lennerstrand, J. (2023). Prevalence of SARS-CoV-2 Omicron Sublineages and Spike Protein Mutations Conferring Resistance against Monoclonal Antibodies in a Swedish Cohort during 2022–2023. _Microorganisms_, **11**, 2417. DOI: [10.3390/microorganisms11102417](https://doi.org/10.3390/microorganisms11102417).

Mannsverk, S., Bergholm, J., Palanisamy, N., Ellström, P., Kaden, R., Lindh, J., Lennerstrand, J. (2022). SARS-CoV-2 variants of concern and spike protein mutational dynamics in a Swedish cohort during 2021, studied by Nanopore sequencing. _Virology Journal_, **19**, 164. DOI: [10.1186/s12985-022-01896-x](https://doi.org/10.1186/s12985-022-01896-x).

Martinell, M., Andersson, T., Mannsverk, S., Bergholm, J., Ellström, P., Hill, A., Lindh, J., Kaden, R. (2022). In-Flight Transmission of a SARS-CoV-2 Lineage B.1.617.2 Harbouring the Rare S:E484Q Immune Escape Mutation. _Viruses_, **14**, 504. DOI: [10.3390/v14030504](https://doi.org/10.3390/v14030504).