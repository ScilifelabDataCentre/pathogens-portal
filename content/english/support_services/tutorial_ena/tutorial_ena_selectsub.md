---
title: Tutorial for SARS-CoV-2 genome data submission to ENA
menu:
    main:
        identifier: tutorial_ena_selectsub
        parent: support_services
        weight: 20
        pre: <i class="fas fa-share-alt"></i>
toc : true
---

<ul class="nav nav-tabs nav-justified">
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_intro">Introduction</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_terminology">Terminology<br>and Metadata</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_subprep">Preparation for<br>Submissions</a>
  </li>
  <li class="nav-item">
    <a class="nav-link active" href="#"><b>Select<br>Submission Route</b></a>
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
</ul>

<br>

## Introduction to submission routes and methods

There are multiple possible methods of submission into ENA. All methods require the use of a combination of interactive interfaces provided by ENA, command-line-based software, and APIs for scripts/custom software. In this tutorial, we have instead structured submission instructions in to two 'routes'. The route likely to work best for you will depend on your comfort with using the different tools provided by ENA and the size of your submission (i.e. the number of sequences included).

On this page, we first briefly [summarise the methods as described by ENA](/support_services/tutorial_ena/tutorial_ena_selectsub/#submission-methods-described-by-ena), for reference. Knowing about these methods will be useful when referencing resources by ENA.

Then, we [describe the two routes of submission that we recommend and how to chose between them](/support_services/tutorial_ena/tutorial_ena_selectsub/#submission-routes-recommended-in-this-tutorial).

## Submission methods described by ENA

ENA provides three methods of submission; interactive submissions, command line submissiions, and programmatic submissions. These methods are briefly described below for reference:

* **Interactive Submissions** are completed by filling out web forms directly in the browser and downloading template spreadsheets that can be completed off-line and later uploaded to ENA. This is the easiest method to use when getting started, but quickly becomes time consuming with bulk submission (> 50 records).

* **Command Line Submissions** use ENA’s **Webin-CLI program**. This validates elements of the submission before submissions are completed.

* **Programmatic Submissions** require that aspects of the submissions are prepared as XML documents that are sent to ENA using cURL or the Webin Portal of ENA.

## Submission routes devised for this tutorial

No single one of the above methods from ENA enables a complete submission. Users must therefore neccessarily use a combination of methods to complete their submission(s). The different methods can be combined in multiple ways, but certain combinations will work better in particular situations. We have developed two 'routes' of submission using combinations best suited to the needs/experience of users. This section will help you to choose the route of submission best suited for your needs:

Choose **Route 1** if:

* You have little to no knowledge of using command line.
* You are submitting a small number of sequences (typically one to ten, but could be used for more).

Choose **Route 2** if:

* You have advanced knowledge of using command line.
* You are doing a bulk submission of sequences (typically more than 100).

When you decide on the most appropriate route, progress to the [Submission Route 1 tab](/support_services/tutorial_ena/tutorial_ena_subroute1) or [Submission Route 2 tab](/support_services/tutorial_ena/tutorial_ena_subroute2) to learn how to complete the submission.

We have restructured the example data originally provided by ENA for use with the two submission routes. This data can be [downloaded here](/ENA_tutorial_data/example_data.zip). The example data is useful for familiarising yourself with how to structure your data for submission, and with completing a submission. However, you're welcome to move through the steps of this tutorial using your own data instead.
