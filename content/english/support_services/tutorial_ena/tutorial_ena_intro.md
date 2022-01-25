---
title: Tutorial for SARS-CoV-2 genome data submission to ENA
menu:
    main:
        identifier: tutorial_ena_intro
        parent: support_services
        weight: 20
        pre: <i class="fas fa-share-alt"></i>
toc : true
---

<ul class="nav nav-tabs nav-justified">
  <li class="nav-item">
    <a class="nav-link active" href="#"><b>Introduction</b></a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_terminology">Terminology<br>and Metadata</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_subprep">Preparation for<br>Submissions</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_selectsub">Select<br>Submission Route</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_subroute1">Submission<br>Route 1</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_subroute2">Submission<br>Route 2</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_contact">Get Help</a>
  </li>
  <li class="nav-item">
  <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_faqs">FAQs</a>
  </li>
</ul>

<br>

## About this tutorial

The research community has put considerable effort into research on the SARS-CoV-2 virus and COVID-19. Fast and open access to different data types (societal, molecular, epidemiological, among others) has been key to the swift development and deployment of, for example, preventative measures, tests, vaccines, and treatments for COVID-19. The pandemic has thus further highlighted how important making data open and [FAIR (Findable, Accessible, Interoperable, Reusable)](https://www.go-fair.org/fair-principles/) is in facilitating research efforts.

Thanks to efforts globally, many SARS-CoV-2 genome sequences have been made openly available in international databases, such as the Global Initiative on Sharing Avian Influenza Data ([GISAID](https://www.gisaid.org)), and the European Nucleotide Archive ([ENA](https://www.ebi.ac.uk/ena/browser/home)). The ENA is part of the International Nucleotide Sequence Database Collaboration ([INSDC](https://www.insdc.org)), and also indexes data from the National Centre for the Biotechnology Information ([NCBI](https://www.ncbi.nlm.nih.gov/)) and [DDBJ](https://www.ddbj.nig.ac.jp). 

Both GISAID and ENA constitute valuable resources, each with distinct relative advantages for those performing research. For example, as of 11th January 2022, GISAID contains considerably more SARS-CoV-2 data from all around the world. Specifically, GISAID contained almost 7 million SARS-CoV-2 sequences, ~250k of which were from the Omicron variant, whereas ENA contained less than 3 million sequences, only 500 of which were from the Omicron variant. The data in GISAID thus enables more reliable insights to be made into the situation globally. However, GISAID only accepts the consensus sequences of assembled genomes, whilst ENA accepts both consensus sequences and 'raw' sequence data. Further, although the data in GISAID is considered open, access is restricted to individuals with verified accounts, whilst there are no restrictions on who can access the data in ENA. This means that using data from ENA simplifies sharing the data (e.g. between members of your group) and access to the data is less likely to become compromised during a project.

The aim of this tutorial is to assist researchers in submitting SARS-CoV-2 sequence data to ENA. This should ultimately lead to an increased availability of open data, including ‘raw’ sequence data. This would not only facilitate greater reproducibility, but also provide more opportunity for reusing the data to address new scientific questions.

<div class="text-center">
  <img src="/img/ena_tutorial/ENA_logo_2021.png" width="350" class="rounded">
</div>

## Learning outcomes

By the end of this tutorial you will:

* Understand the terminology used by ENA (and other similar databases).

* Know how to properly describe and format SARS-CoV-2 data for submission into ENA.

* Know how to complete a submission into ENA.

* Know where to get help for future submissions (whether for SARS-CoV-2, or something else) to ENA.

## Prerequisites

No specific knowledge is needed before starting this tutorial.

## Overview

This tutorial is separated into tabs to aid users in moving through the tutorial. If you are unfamiliar with ENA, we recommend reading the [Terminology and Metadata tab](/support_services/tutorial_ena/tutorial_ena_terminology) before commencing with the tutorial.

Multiple routes of submission are possible with ENA. We describe two complete routes that can be used for submission. Some preparatory steps are common to both routes. These steps are described in the [Preparations for Submissions tab](/support_services/tutorial_ena/tutorial_ena_subprep). We explain how to determine which of the routes is most likely to work best for you in the [Select Submission Route tab](/support_services/tutorial_ena/tutorial_ena_selectsub). The [Submission Route 1](/support_services/tutorial_ena/tutorial_ena_subroute1) and [Submission Route 2](/support_services/tutorial_ena/tutorial_ena_subroute2) tabs explain different routes to completing submissions to ENA.

Information about where to get further guidance is given in the [Get Help tab](/support_services/tutorial_ena/tutorial_ena_contact). For answers to frequently asked questions (FAQs) regarding submissions, please see the [FAQs tab](/support_services/tutorial_ena/tutorial_ena_faqs).

## References used for this tutorial

Multiple sources of information were used to build this tutorial. Links to the reference material are listed below:

* [Teaching module on submission to data repositories, by NBIS Sweden.](https://nbisweden.github.io/module-repository-submission-dm-practices/)

* [SARS-CoV-2 submission workshop, by ENA.](https://ena-covid19-docs.readthedocs.io/en/latest/submission_workshop/getting_started.html)

* [Additional documentation about submission of SARS-CoV-2 data to ENA, by ENA.](https://ena-covid19-docs.readthedocs.io/en/latest/index.html)

* [SARS-CoV-2 ENA submission workflow and guidance for structuring and releasing metadata V.2., by Alikhan, N. -F., Timme, R. E., and Griffiths, E.](https://www.protocols.io/view/sars-cov-2-ena-submission-workflow-guidance-for-st-buqnnvve)

* [General guide on ENA data submission, by ENA.](https://ena-docs.readthedocs.io/en/latest/submit/general-guide.html)

* [Research Data Management (RDM) Guide, by ELIXIR-Belgium.](https://rdm.elixir-belgium.org/covid-19/index.html)

* [GitHub repository for ELIXIR-Belgium ENA upload container.](https://github.com/ELIXIR-Belgium/ena-upload-container)

* [GitHub repository for MultiSub command line submission tool.](https://github.com/maximilianh/multiSub)
