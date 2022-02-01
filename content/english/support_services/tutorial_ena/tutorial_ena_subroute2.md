---
title: Tutorial for SARS-CoV-2 genome data submission to ENA
menu:
    main:
        identifier: tutorial_ena_subroute2
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
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_selectsub">Select<br>Submission Route</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_subroute1">Submission<br>Route 1</a>
  </li>
  <li class="nav-item">
    <a class="nav-link active" href="#"><b>Submission<br>Route 2</b></a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_contact">Get Help</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/support_services/tutorial_ena/tutorial_ena_faqs">FAQs</a>
  </li>
</ul>

<br>

## When to use this route

Route 2 is recommended for those with advanced knowledge of using command line, and for those doing bulk submissions. It is the most suitable route for high-throughput, frequent submissions and automated systems. For this route, the metadata is typically provided to ENA in XML documents. This is true in all cases except for sequence assemblies, where the metadata is instead provided in JSON format. In either case, the metadata are submitted using cURL.

## Necessary preparation

Before commencing with the submission, the following things are required:

1. **A text editor and software to read/edit data in .xml format** - The text editor should ideally have the ability to highlight XML formatted files.

2. **cURL** - A command line facility with cURL installed.

**Note:** This submission route works well in a Mac or Linux environment. For Windows users, we recommend downloading a Ubuntu app or a virtual Linux machine for smooth submissions.

### Data required for route 2

All of the data required to complete this submission can be downloaded together in a single zip file by clicking [here](/ENA_tutorial_data/example_data.zip). In this part of the tutorial, we will make use of the information in the '02-route' and 'data' subfolders.

**Note:** If you use your own data, you can fill in the metadata template, for instructions on how to do this please see [this section in the preparation for submissions tab](/support_services/tutorial_ena/tutorial_ena_subprep/#preparing-the-metadata).

### Create checksums (MD5)

The sequence files need to be uploaded to the dropbox on ENA's servers (see below). In order to check for successful file transfers, it is necessary to compute [MD5s](https://en.wikipedia.org/wiki/MD5) for each file prior to upload. Follow the steps below to do this:

1. Open a terminal (command prompt) window and change directory into where the raw sequence files are located, e.g. `cd example_data/data/raw/`.

2. Type a version of the command `md5sum SARS-CoV-2-Sample1_1.fastq.gz > SARS-CoV-2-Sample1_1.fastq.gz.md5`. This command will calculate the checksum for file SARS-CoV-2-Sample1_1.fastq.gz and put the checksum in a file named SARS-CoV-2-Sample1_1.fastq.gz.md5. Modify this command to match your file names and required output name.

It is possible to calculate MD5 on several files at once using a for-loop:

>for s in SARS-CoV-2-Sample*<br>>  do<br>>  md5sum $s > $s.md5<br>>  done

This command calculates checksums for all files with names beginning with `SARS-CoV-2-Sample`.

### Upload data files

Sequence files and the MD5 checksum files must be uploaded before starting the submission. There are multiple ways in which the upload can be done:

#### Using the Webin File Uploader

The most user-friendly approach is to [use the Webin File Uploader](https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html#using-webin-file-uploader). This is a Java web start application that can be downloaded [here](http://www.ebi.ac.uk/ena/upload/WebinUploader.jnlp):

1. Launch the application.
2. Enter your Webin username in the `Username` field and your Webin password in the `Password` field.
3. Browse into the local `Upload Directory`, which contains the data files that you want to upload. You can use the `...` button to do this.
4. Click ‘OK’ to see a list of all files contained in the selected directory displayed in the Webin File Uploader window.
5. Choose the `Overwrite` option if you want to replace any existing files that were previously uploaded.
6. Choose the `Upload Tree` option if you wish to preserve the directory structure when uploading files to the Webin upload area. By default, the files will be uploaded into the root directory of your Webin upload area.
7. Select the files to upload. You can use the `Select All` button to select all of the files for upload.
8. Click on the `Upload` button.

*The above steps are adapted from [ENA](https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html#using-webin-file-uploader)* <!--Parul/yvonne, please check the reference-->

#### Use the command line FTP client

Another option is to use a command line FTP client in Linux or Mac:

1. Open a terminal and type `lftp webin2.ebi.ac.uk -u Webin-xxxxx`. Enter your username at the end in place of xxxxx.
2. Enter your password when prompted.
3. Type `ls` to check the content of your drop box.
4. Use the `mput <filename>` command to upload files.
5. Use the `bye` command to exit the FTP client.

*The above steps are adapted from [ENA](https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html#uploading-files-using-command-line-ftp-client)* <!--Parul/yvonne, please check the reference-->

#### Use the Windows File Explorer

It is also possible to use Windows File Explorer:

1. Launch the Windows File Explorer application.
2. Click on `Add a network location` in the `Computer` tab.
3. Click `Next`.
4. Select `Choose a custom network location` and click `Next`.
5. Type `ftp://webin.ebi.ac.uk` in the `Internet or network address` field and click `Next`.
6. Unselect `Log on anonymously`, type your Webin user name in the `User name` field and click `Next`.
7. Type a network location to show in Windows Explorer e.g. `webin.ebi.ac.uk` then click `Next`.
8. Click `Finish`.
9. When using the new folder you will be prompted for your Webin password. Type your password and click `Log on`.

*The above steps are adapted from [ENA](https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html#using-windows-file-explorer)* <!--Parul/yvonne, please check the reference-->

For other options to upload, more detailed instructions, or troubleshooting, please see [this section of ENA's tutorial](https://ena-docs.readthedocs.io/en/latest/submit/fileprep/upload.html).

**Note**: Always keep a local copy of the uploaded files until the files have been successfully submitted and archived. The ENA dropbox is a temporary transit area and is not backed up.

## How to do a route 2 submission

### Register a study

In this section, we will use the materials in the *02-route/study/* subfolder of the example data that you downloaded earlier. Use the following commands in the command line to navigate to the folder and view its contents:

> cd $WORKSHOP/02-route/study/<br>ls

In the *study* subfolder, you will find two example XML files (the file type required for this kind of submission). For this type of submission, we will need 2 XML files:

* **project.xml** - This XML file contains the metadata for the study, including e.g. title of the study.

* **submission.xml** - This file declares one or more Webin submission service actions. The action can be `<ADD/>`, which is used to submit new objects. The user can decide the study release date, which is the date that the study will become public, along with all data associated with it. By default, the release date will be set as two months after the date of submission, but the submitter can select any date within 2 years of the present date. This can be done using the `<HOLD/>` action, and may look e.g. `<HOLD HoldUntilDate="TODO: release date"/>`. You can modify release date by replacing `<ADD/>` with `<MODIFY/>`. The submission.xml file in the $WORKSHOP folder that you set up, defines the `<ADD/>` action that will allow you to create a new study.

Edit *project.xml* to create a project alias that is unique to you. Once complete, you are ready to send the project.xml and submission.xml files (using the `<ADD/>` action) to the test service using the following cURL command:

`curl -u username:password -F "SUBMISSION=@submission.xml" -F "PROJECT=@project.xml" "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"*`

**Note**: Replace `username` with your Webin username (starting with Webin-), and `password` with your Webin password.

After you run the above command in your command prompt, you will receive a ‘receipt.xml’ file. This file will contain information about the contents and success of your submission, as well as your study accession.

The attribute 'success' in the receipt file will have a value of either true or false. If the value is false, it indicates that submission was unsuccessful. In this case, please check the rest of the receipt file for error messages. When you have resolved the errors indicated, you can try the submission again. If the value is true, then it indicates that the submission was successful. The receipt will contain the accession number of the study metdata object that you submitted. The accession number generated will be the one you will include in a publication. Please take note of your study accession number at this stage, we will use this later to submit other objects to this study.

### Prepare information for samples

In this section, we will use the materials in the *02-route/samples/* subfolder of the example data that you downloaded earlier. This subfolder contains multiple XML files. Use the following commands in the command line prompt to navigate to the folder and view its contents:

>cd $WORKSHOP/02-route/samples/<br>ls

You will see the following files:

* **samples.xml** - This file contains the metadata for the samples.

* **submission.xml** - This file is the same as that used to submit your study. It defines the `<ADD/>` action that will allow us to create new samples.

* **submission_modify.xml** - This file defines the `<MODIFY/>` action, which allows us to update existing samples.

In the *samples.xml* file, we can define many samples inside a `<SAMPLE_SET>` tag. Each sample (enclosed in `<SAMPLE>` tags), must contain:

* `<TITLE>` tags: defining the title of the sample
* `<SAMPLE_NAME>` tags: defining the taxonomic information
* `<DESCRIPTION>` tags: providing a description of what has been sampled
* Multiple `<SAMPLE_ATTRIBUTE>` tags: defining all other metadata fields

To see an example of a `<SAMPLE_SET>` please [see this example from ENA](https://ena-docs.readthedocs.io/en/latest/submit/samples/programmatic.html).

Sample aliases are defined within the `<SAMPLE>` tag, e.g. `<SAMPLE alias='this_alias'>`. In the example data, the alias has been suffixed with the word ‘programmatic’. Aliases must be unique.

### Submit samples

As with study registration (above), we need to use cURL to send the samples.xml and submission.xml files (using the `<ADD/>` action) to the test service:

`curl -u username:password -F "SUBMISSION=@submission.xml" -F "SAMPLE=@samples.xml" "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"`

You should again receive a 'receipt XML' with information regarding submission success and accession numbers. Note that, in this instance, you will also receive a `<SAMPLE>` tag for each submitted sample (when using the sample data for this tutorial, you should see 3). Please take note of each sample alias and accession, as you will need these later when submitting sequence files.

### Modify samples

Sometimes, previously uploaded metadata needs to be updated. You can do this by editing the *sample.xml* file to include the correct values, and resubmitting it with a submission.xml file containing the `<MODIFY/>` action in place of `<ADD/>`:

* First, open the *samples.xml* file and update the metadata fields as required, e.g. with a new, later collection date, and then save the file.

* This time, we will use the `submission_modify.xml` in the submission. This file instructs the service to update an existing sample. The update uses the alias to detect existing samples, so it is important not to change the alias.

`curl -u username:password -F "SUBMISSION=@submission_modify.xml" -F "SAMPLE=@samples.xml" "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"`

Check the receipt file to see whether your update was successful. Note that the receipt file will also report which samples have not been updated.

### Submit raw reads

As in all previous steps, this type of submission is performed using XML files. In the case of raw reads, we must submit two types of object: experiments and runs. Experiments hold information about library preparation and sequencing protocols, and also provide a link to the appropriate study and samples. Runs simply link experiments and data files.

Submissions are defined using different metadata objects. To know more about metadata objects, please [read this section](/support_services/tutorial_ena/tutorial_ena_terminology/) of this tutorial.

Please go to the example data that you downloaded earlier, and locate example XMLs for both experiments and runs in the `02-route/runs` directory. Make the following edits:

* In **experiments.xml**, replace all occurrences of PRJEB#### with your study accession number, and all occurrences of SAME###### with the equivalent sample accessions.

* In **runs.xml**, replace the checksum field in each `<FILE>` tag with those that you computed earlier. These will be used to check for file corruption during upload.

Note that runs reference experiments by their aliases. For example:

* In **experiments.xml** : `<EXPERIMENT alias="SARS-CoV-2 experiment 1">`
* In **runs.xml** : `<EXPERIMENT_REF refname="SARS-CoV-2 experiment 1" />`

**Note**: In all objects that use referencing/linking (with `<*_REF>` tags), we can link by either using the alias (with refname="") or the accession (with accession=""). <!-- checked this with Yvonne - example uses alias and refname - should it be accession, as in this part of the text???-->

We will send these XML files to the test service using cURL with the following command:

`curl -u username:password -F "SUBMISSION=@submission.xml" -F "EXPERIMENT=@experiments.xml" -F "RUN=@runs.xml" "https://wwwdev.ebi.ac.uk/ena/submit/drop-box/submit/"`

For additional information, please see [this section of the documentation from ENA](https://ena-docs.readthedocs.io/en/latest/submit/reads/programmatic.html).

### Validate and submit sequence assemblies

A new JSON-based REST service was introduced by ENA during 2021 specifically for the submission of SARS-CoV-2 sequences. Sequences for submissions made using this service are not held in FASTA files. Rather, they are included directly in the JSON itself, thus greatly simplifying the process of submission. This is only made possible due to the small size and relatively low complexity of the genome. For more information on this system, including useful code snippets, please see [ENA documentation on this topic](https://ena-covid19-docs.readthedocs.io/en/latest/help_and_guides/webin-cli-rest.html).

In this section, we will use the materials in the 02-route/sequences/ subfolder of the example data that you downloaded earlier. Use the following commands in the command line prompt to navigate to the folder and view its contents:

```bash
cd $WORKSHOP/02-route/sequences/
ls
cat hCoV-19_isolate_1.json
```

Note that this JSON object contains exactly the same information as that in its equivalent manifest file. The only difference is that the sequence is embedded directly into the JSON payload. We will send the entire JSON object (via the `POST` protocol) to the Webin-CLI-REST (test) service of ENA using cURL.

This service also provides both validation and submission services, as with the Webin-CLI tool, but here we `POST` to different URLs for each service:

* Validation: [https://wwwdev.ebi.ac.uk/ena/submit/webin-cli/api/v1/genome/covid-19/validate](https://wwwdev.ebi.ac.uk/ena/submit/webin-cli/api/v1/genome/covid-19/validate).

* Submission: [https://wwwdev.ebi.ac.uk/ena/submit/webin-cli/api/v1/genome/covid-19](https://wwwdev.ebi.ac.uk/ena/submit/webin-cli/api/v1/genome/covid-19/validate).

Let's validate the contents of `hCoV-19_isolate_1.json`. Remember to replace `-u user:pass` with your webin credentials, and to substitute in your own accessions into the JSON object:

```bash
curl -X 'POST' -u user:pass
'https://wwwdev.ebi.ac.uk/ena/submit/webin-cli/api/v1/genome/covid-19/validate'
-H 'accept: application/json'
-H 'Content-Type: application/json'
-d '{
  "study": "PRJEB#####",
  "sample": "ERS#######",
  "runRef": "ERR#######",
  "name": "hCov-19_isolate_1",
  "coverage": 100,
  "program": "ARTIC fieldbioinformatics (minimap2/nanopolish) 1.1.3 (nanopolish 0.13.2)",
  "platform": "ILLUMINA",
  "minGapLength": 3,
  "moleculeType": "genomic RNA",
  "description": "example sequence #1 for workshop",
  "sequence": "NNNNNNNNNTTATACCTTCCCAGGTAACAAACCAACCAACTTTCGATCTCTTGTA......."
  }'
  ```

To submit the sequence, simply remove `/validate` from the URL in the above command and run it again.

#### What happens after submission

Once the submitted sequences have been processed, they will be distributed as **EMBL flat files**, see [this example from ENA](https://ena-docs.readthedocs.io/en/latest/submit/fileprep/flat-file-example.html) to understand the format. These files largely comprise of:

1. Metadata, such as author names and addresses (contained in lines beginning with `R`, e.g. `RA`, `RL`, `RG`)
2. Sample information, located inside a `source` block
3. The sequence itself

Upon generation of the EMBL file, sequences also acquire a sequence accession number. This accession number will comprise of 2 upper case letters followed by 6 numbers, e.g. [LR991698](https://www.ebi.ac.uk/ena/browser/api/embl/LR991698.2?lineLimit=1000).

For each assembly submission, Webin will report a unique accession number (starting with ERZ). For most assemblies, this number is only used for internal processing and will not be visible in the browser. However, for SARS-CoV-2 assemblies, the ERZ records will also be available in the browser to provide a point of access for the submitted file(s).
