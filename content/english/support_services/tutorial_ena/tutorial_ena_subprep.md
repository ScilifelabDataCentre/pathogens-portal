---
title: Tutorial for SARS-CoV-2 genome data submission to ENA
menu:
    main:
        identifier: tutorial_ena_subprep
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
    <a class="nav-link active" href="#"><b>Preparation for<br>Submissions</b></a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_selectsub">Select<br>Submission Route</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_subroute2">Submission<br>Route 1</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_subroute2">Submission<br>Route 2</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_contact">Get Help</a>
  </li>
</ul>

<br>

It is necessary to do some preparation of files before submission, regardless of the eventual [route that you select](/support_services/tutorial_ena/tutorial_ena_selectsub)). This page explains how to complete these initial steps, so that you can sucessfully complete your submission.

## Required file formats

All the files that are submitted to ENA need to be in the appropriate format to be accepted. Details of the formats are listed in the [Terminology and Metadata tab](/support_services/tutorial_ena/tutorial_ena_terminology). Once all the files are in order you can start the submission process.

## Obtaining an ENA Webin Account

In order to do a submission, you need an account in ENA. To create an account, go to [ENA submission homepage](https://www.ebi.ac.uk/ena/submit/webin/), click on **Register**, and fill in the required details.

*Log in page on the ENA submission homepage:*

<div class="text-center">
  <img src="/img/ena_tutorial/ENA_login_startpage.png" height="350" class="rounded">
</div>

*Enter account details to obtain an account in ENA:*

<div class="text-center">
  <img src="/img/ena_tutorial/ENA_login_detailspage.png" height="500" class="rounded">
</div>

Once you have filled in all the required fields, you can log in to the submission service. If you want to add more contacts for data submissions, you can do this by logging into your account then selecting *Home > Manage account*. You may wish to add contacts if you are working with others to complete your submission. Any contacts that you add will be notified if there are any major changes to data submissions and they will be listed as contacts on public data.

## Obtaining example data

For this tutorial, you are welcome to make use of your own data. However, you may also download the [example data](/ENA_tutorial_data/example_data.zip), as well as some other associated files, to use while you learn how to complete submissions. By using the example data, you will be able to submit 3 samples to an example project, along with raw read data and sequences associated with each sample.

Whether you use your own data or the example data, we recommend that you use the following code in a terminal window to create a path variable called WORKSHOP (this will save you from typing the filepath repeatedly):

>export WORKSHOP="/path/to/example_data/"<br>cd $WORKSHOP/<br>ls

## Preparing the metadata

To ensure that sample data is registered with at least a minimum amount of metadata, ENA provides “Sample Checklists” which are used during registration to tailor these samples to fit minimum standards. The most appropriate checklist for SARS-CoV-2 viral submissions is the *[ENA virus pathogen reporting standard checklist, or ERC000033](https://www.ebi.ac.uk/ena/browser/view/ERC000033)*. This includes 9 mandatory, 15 recommended, and 11 optional fields (along with any additional user-defined fields). Please note that some fields are free text, while others have controlled vocabulary.

In order to ensure that your SARS-CoV-2 data is properly described, we recommend downloading and filling in [this metadata template](/ENA_tutorial_data/metadata_template_ERC000033.xlsx). This template not only contains the ENA checklist for the sample data, but also describes all levels of metadata required for a submission. The template is divided into five sheets, namely; **study**, **sample**, **experiment**, **run** and **analysis**. The experiment and run sheets are used for describing the raw reads, and the analysis sheet is used for describing the sequence assembly.

In each sheet, the first row is the **ENA virus sample checklist field**, the second row is the **ENA definition** (provides a description of the field), and the third row is **ENA requirement status** (whether the field is mandatory, recommended or optional). When you populate the sheets with your metadata, you can delete the second and third row. The default values for SARS-CoV2 submissions are pre-filled (in red) for relevant fields.

For your convenience, we also provide [this pre-filled version of the metadata template](/ENA_tutorial_data/metadata_template_ERC000033_filled.xlsx), so that you can see how the templat should be populated for use with the example data.

**Note**: It is *strongly* recommended that you provide as much information as possible in the metadata sheets. This will increase the [FAIRness](https://www.go-fair.org/fair-principles/) of your data, and thus the probability that it will be useful in future research efforts.

To submit the metadata sheets to ENA, they must be in .tsv file format. The downloads on this page are provided as .xlsx, commonly known as Microsoft Excel, format for ease. It is therefore necessary for you to convert the file format. If you are using Microsoft Excel to edit the metadata templates, click *File (or the Office Button) > Save As* and change 'save as file type' to 'Text (Tab delimited) (\*. tsv)'. Enter a file name and save the file. If you are using a Mac, you can change the file type by right-clicking on the .xlsx file in Finder, selecting *rename* and typing '.tsv' at the end of your file name.
