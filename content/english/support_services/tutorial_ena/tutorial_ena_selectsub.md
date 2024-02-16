---
title: Tutorial for SARS-CoV-2 genome data submission to ENA
toc : false # in case of the ena tutorial pages the table of contents is inserted inside the template, ena_tutorial
type: ena_tutorial
menu:
    ena_tutorial:
        name: Select Submission Route
        weight: 40
---

## Introduction to submission routes and methods

There are multiple ways to submit data and sequences into ENA. In order to do a submission of of 'raw' sequences and/or assemblies, you need to use a combination of interactive interfaces in ENA, command-line based software, and APIs for scripts/custom software. The prospect of using multiple tools and determining which tools are better to use for a given part of a submission can seem daunting, especially if you are unfamiliar with the tools. In this tutorial, we have devised two submission 'routes' that enable you to do a complete submission, and explained how to use the tools. Which route will work best for you will depend on your comfort with using the different tools provided by ENA and the size of your submission (i.e. the number of sequences included).

On this page, we first briefly summarise how ENA refers to [different submission methods](/support_services/tutorial_ena/tutorial_ena_selectsub/#submission-methods-described-by-ena). Understanding the descriptions of methods used by ENA will be useful when referencing any resources that they have produced.

Then, we describe the [two routes of submission](/support_services/tutorial_ena/tutorial_ena_selectsub/#submission-routes-devised-for-this-tutorial) that we recommend and explain how to choose between them.

## Submission methods described by ENA

ENA described three methods of submission, none of which can be used in isolation to complete all parts of a submission:

* **Interactive Submission Method** - involves filling out web forms directly in the browser and downloading template spreadsheets that can be completed off-line and uploaded later to ENA. This is the easiest method to use when getting started, but quickly becomes time-consuming with bulk submission (> 50 records).

* **Command-Line Submission Method** - uses ENA’s **Webin-CLI program**. Submissions require the preparation of text (manifest) files that are validated before submissions are completed.

* **Programmatic Submission Method** - requires the preparation of XML documents that are sent to ENA using cURL or the Webin Portal of ENA.

## Submission routes devised for this tutorial

As mentioned above, a combination of these methods is needed to complete a submission. The methods can be combined in multiple ways, but certain combinations will work better in particular situations. We have developed two 'routes' of submission that comprise two different combinations of methods. Users can chose the route that is most likely to suit their needs:

Choose [**Route 1**](/support_services/tutorial_ena/tutorial_ena_subroute1) if:

* You have little to no knowledge of using command line tools.
* You are submitting a small number of sequences (typically one to ten, but could be used for more).

Choose [**Route 2**](/support_services/tutorial_ena/tutorial_ena_subroute2) if:

* You have advanced knowledge of using command line tools.
* You are doing a bulk submission of sequences (typically more than 50).
