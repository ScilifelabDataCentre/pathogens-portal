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

## Select Submission Route

 ### Introduction to submission routes and methods

There are multiple possible methods of submission into ENA. All methods require the use of a combination of interactive interfaces provided by ENA, command-line-based software, and APIs for scripts/custom software. In this tutorial, we have instead structured submission instructions in to two 'routes'. The route likely to work best for you will depend on your comfort with using the different tools provided by ENA and the size of your submission (i.e. the number of sequences included).

On this page, we first briefly [summarise the methods as described by ENA](/support_services/tutorial_ena/tutorial_ena_selectsub/#submission-methods-described-by-ena), for reference. Knowing about these methods will be useful when referencing resources by ENA.

Then, we [describe the two routes of submission that we recommend and how to chose between them](/support_services/tutorial_ena/tutorial_ena_selectsub/#submission-routes-recommended-in-this-tutorial).

### Submission methods described by ENA

ENA provides three methods of submission; interactive submissions, command line submissiions, and programmatic submissions. Each method is appropriate for a different set of submission types. Users are required to use more than one method when submitting to ENA, as no one method enables a complete submission:

* **Interactive Submissions** are completed by filling out web forms directly in the browser and downloading template spreadsheets that can be completed off-line and later uploaded to ENA. This is the easiest method to use when getting started, but quickly becomes time consuming with bulk submission (> 50 records).

* **Command Line Submissions** use ENA’s **Webin-CLI program**. This validates elements of the submission before submissions are completed.

* **Programmatic Submissions** require that aspects of the submissions are prepared as XML documents that are sent to ENA using cURL or the Webin Portal of ENA.

### Submission routes recommended in this tutorial

As detailed above, all submissions require the use of some combination of the methods described by ENA, and different methods require different levels of expertise with computational tools. We have developed two submission 'routes' that are tailored to the users experience with different tools and the size of their submissions. This section will help you to choose the route of submission best suited to your needs:

1.	Choose **Route 1** if:
  * You have little to no knowledge of using command line.
  * You are submitting a small number of sequences (typically one to ten, but could be used for more).


2.	Choose **Route 2** if:
  * You have advanced knowledge of using command line.
  * You are doing a bulk submission of sequences (typically more than 100).

When you decide on the most appropriate route, progress to the [Submission Route 1 tab](/support_services/tutorial_ena/tutorial_ena_subroute1) or [Submission Route 2 tab](/support_services/tutorial_ena/tutorial_ena_subroute2) to learn how to complete the submission. We provide relevant example data (originally produced by ENA) that can be used with each route.
