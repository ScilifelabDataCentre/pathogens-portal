# Instructions on adding and editing information displayed on the portal

Contributions are welcomed for all sections of the portal. This page describes how to make contributions to multiple different types of pages via GitHub. Contributions can be made either in the GitHub web interface (usually used for small additions to existing pages), or by editing a local copy of the portal on your computer and pushing that to GitHub (typically used for larger contributions and new pages). If you would prefer to contribute using a different route, for example, by sending text documents, please email us at [pathogens@scilifelab.se](mailto:pathogens@scilifelab.se).

**Table of contents:**

- [Making contributions via GitHub](#making-contributions-via-github)
- [Available datasets](#available-datasets)
- [Funding opportunities](#funding-opportunities)
- [Ongoing research projects](#ongoing-research-projects)
- [Data highlights](#data-highlights)
- [News about the Portal](#news-about-the-portal)
- [Resources](#resources)

## Making contributions via GitHub

All of the information displayed on the portal is contained within [this GitHub repository](https://github.com/ScilifelabDataCentre/pathogens-portal). When you enter that repository, you will see multiple folders. The majority of the content can be found within the `content` folder (where there is one folder for each language used on the portal). Some sections also use information that is ncluded within the `data` or `static` folders. Please see the sections further down on this page for information on how to locate different types of pages. It is also possible to use the URL to gain some idea of where a page is located within the folders. For example, all dashboard pages are within the `dashboards` folder, and their URLs are in the structure http://pathogens.se/dashboards/page_name/.

Please note that we require that all commits are verified, so you must sign your commits. For information on how to set this up, see the [GitHub documentation](https://docs.github.com/en/authentication/managing-commit-signature-verification/signing-commits).

### Using the web interface

This route is typically used for making relatively small additions/updates to the content. For example, adding an entry to a database or modifying/adding some text to an existing page.

- Navigate to the folder that contains your file (typically the `content` folder), and then to the file within that folder that represents the page/section that you want to modify.
- Click on the pencil on the top right hand corner of the page (when you hover, it will show "fork this repository and edit this file"/"edit this file"). This will create a fork of the portal code in your own GitHub account. You should then be able to directly edit the content of the page.
- Make all of the changes that you would like to make. Remember that if the page appears in both Swedish and English, it is necessary to update both versions of the page.
- Click on "Commit changes". Write a description of what you have done in the "Propose changes" pop-up screen. Press the "Propose changes" button when you are done.
- You should now be taken to a page that allows you to create a pull request. Ensure that the request is being made to the `develop` branch of the base repository `SciLifeLabDataCentre/pathogens-portal`.
- You can see the files that you have changed at the bottom of the page, and can double-check that everything looks as intended. If it does, click "Create pull request".
- A member of the portal team will review the pull request as quickly as possible regarding the pull request. Once approved, the changes will show on the portal.

### Using a local copy

It can sometimes be preferable to make changes to files directly on your computer in your favourite text editor and then push those to GitHub. This can be particularly true, for example, when adding files or making larger changes. To do this, you can fork this repository to your account and then clone the forked repository to your machine:

```bash
git clone git@github.com:[YOUR-USERNAME]/pathogens-portal.git
cd pathogens-portal
```

To make it easier to pull in changes made by others, you can add the main repository as a remote:

```bash
git remote add upstream https://github.com/ScilifelabDataCentre/pathogens-portal.git
```

Then you can fetch changes at any time from this remote:

```bash
git pull upstream develop
```

You can now edit/add files with the text editor on your computer. You can test your changes locally, so you can see how it will look on the site. This is good for ensuring that your changes appear as intended. See [this page](https://github.com/ScilifelabDataCentre/pathogens-portal/blob/develop/CONTRIBUTING/running_a_local_copy.md) for information on how to see the effect of changes that you're making locally.

When you have finished editing, commit and push to your fork:

```bash
git add .
git commit -m "My changes"
git push
```

Once you're finished with your edits and they are committed and pushed to your forked repository, it's time to open a pull request. In short:

- Go to your repository on GitHub and click "New Pull Request".
- Alternatively, go to the main repository on GitHub ([https://github.com/ScilifelabDataCentre/pathogens-portal](https://github.com/ScilifelabDataCentre/pathogens-portal)) and click "New Pull Request", then click the text link near the top that says "compare across forks".
- At the top of the page, you should see a pale grey box under the 'Comparing changes' text. The right-hand "head repository" drop down should show your username/fork and the branch that you worked on. Under 'base repository' you should see "ScilifelabDataCentre/pathogens-portal" and the 'base' should read 'develop'.
- If you're happy with the list of commits and file changes shown towards the bottom of the page, click "Create pull request".
- Write a title and description for your pull request, and then click 'Create pull request'.
- A member of the portal team will review the pull request as quickly as possible regarding the pull request. Once approved, the changes will show on the portal.

## How to add a new page

The easiest way to add a new page to the portal is to [make a local copy](#using-the-web-interface). You can then navigate to the folder to which you would like to add a page (see below to gain an idea of where this might be, or check the URL of pages in the same section, as that will indicate the file structure). Create a new markdown (.md) file. We recommend copying the metadata from an existing page from the same section to initiate your page. The metadata is the piece at the top of the file that is between two lines of 3 dashes (i.e. '---'). You will have to change the metadata to reflect information about your new page, but this will ensure that your page is correctly initiated.

## Adding available data

We have a table of available data/code from Sweden that can be found [in the available data section of the portal ](http://pathogens.se/datasets/all/). Multiple different types of data can be added to this database. Please note that this database is also updated approximtely monthly by the portal team.

In order to add entries in the database, you should edit the `available_datasets.json` within the `data`folder. You need to update the date at the top of the file to the date that you are making the update. Then you can add your entry/entries. Please note that entries must include one author affiliated with a Swedish university, should pertain to COVID-19, and the data/code should be openly available or have clear instructions for how access can be made (in the event thatthe data could not be shared openly). Each entry should be in the format:

```bash
    {
      "doi": "DOI of the paper",
      "available_items": [
        {
          "type": "data",
          "repo_name": "",
          "accession_number": "",
          "description": "Information that is sufficient for anyone hoping to assess whether they can reuse the data.",
          "data_type": ["Biochemistry data", "Protein data", "Serology data", "Public health data", "Health data", "Genomics & transcriptomics data", "Drug discovery data", "Imaging data", "Social science and humanities data", "Other data" (delete as appropriate)],
          "data_url": "URL to data"
        },
        {
          "type": "code",
          "repo_name": "",
          "accession_number": "",
          "description": "Information that is sufficient for anyone hoping to assess whether they can reuse the data.",
          "data_type": [see above - different data/code instances within one entry should be the same],
          "data_url": ""
        }
      ],
      "title": "title of paper",
      "issue": "",
      "volume": "",
      "publisher": "",
      "published": "yyyy-mm-dd",
      "author": [
        "List O. A.", "Author T."
      ]
    },
```

## Dashboard pages

**Data dashboards** are pages that include data from either research groups or public data sources. They include custom, dynamic visualisations of the data alongside relevant information about the background of the study, the methods used to collect data, and the research groups involved, among other things.

### Data visualisations

The portal team are happy to create code for custom, dyanmic visualisations for your data. We work with those involved in data collection to create these, so that they show the data in the most appropriate way. The visualisation codes that we have written to date can be found in [our visualisations GitHub repository](https://github.com/ScilifelabDataCentre/pathogens-portal-visualisations). Our visualisation are typically writtten in Plotly in Python. To get a visualisation produced for your data, please email us at [pathogens@scilifelab.se](mailto:pathogens@scilifelab.se).

### Dashboard files

There are multiple dashboard pages. They are located within the `dashboards` folders of the `english` and `svenska` folders of the `content` folder. Some dashboards (e.g. the wastewater dashboard) contain multiple pages. In such cases, the pages are included within the same subfolder.

The file for each page is in markdown format. The top of the file is considered metadata, and it sets up your page. It looks as follows:

```Markdown
---
title: Title of your page
description: A short (around 100 chracters) description of your dashboard
banner: /dashboard_thumbs/picture.jpg (see information on 'illustrations' below)
toc: false (false means that no table of contents will be show, on the page)
plotly: true (trues means that plotly will be used on the page, this is needed for the visualisations)
menu:
  dashboard_menu:
    identifier: set_name_id
    name: "name as it should appear in the dashboard menu in the header"
dashboards_topics: [COVID-19, Infectious diseases] (add the names of the topics that are appropriate - see below for topics)
---
```

Under the metadata, you can write information about the research and the data. The portal team can help with adding code related to plots within the page.

### Illustrations

Links to dashboard pages are typically shown in cards e.g. in <https://pathogens.se/dashboards/>. These cards show a small image that is representative of that dashboard. The size of the image should be 250 px high and 500 px wide. The portal team can help with resizing/editing images. Images should be placed in the `/static/dashboard_thumbs` folder.

## Data highlights

**Data highlights** are short, data-centric articles focusing on recent research that openly shares data, code, or other research outputs

### Illustrations

Each highlight can have two illustrations. One is used as a thumbnail image on the pages showing multiple highlights e.g. <https://pathogens.se/highlights/>. The other can be shown on the page. Only the first is required, and should be 250 px high and 500 px wide. The portal team can help with resizing/editing images. The illustrations should be placed in the `/static/highlights/banners` folder.

### Data highlight files

The data highlights are generated from Markdown formatted files contained in the `/content/english/highlights/` folder. The file name used here will also be the URL of the data highlight (e.g., `test-highlight.md` will become `https://pathogens.se/highlights/test-highlight/`). The images can be in .png or .jpg format.

### Content of the data highlight files

Below is an example of a data highlight file content. You can copy this text into your markdown file and edit it to write your own data highlight, or you can copy an existing highlight and edit the copy. As with the dashboard files, and most other pages in the site, the file comprises of page metadata and then the content shown on the page itself.

```Markdown
---
title: Title of page
date: yyyy-mm-dd
summary: A summary of around 100 characters in length
banner: /highlights/banners/picture.png (thumbnail image, see above for details)
banner_large: /highlights/banners/picture.png (larger images shown on the page)
banner_caption: "caption for the image shown on the page"
highlights_topics: [COVID-19, Infectious diseases] (include the names of any topics that apply - see topics section for details)
tags: [keyword 1, keyword 2,...]
images: [/highlights/banners/picture.png]
---

This is the text of the highlight. This is the first paragraph. Introduce why this is an important topic.

This is the second paragraph of the text of the highlight. Markdown formatting should be used in the text. For example, you can make a piece of text italic by placing an asterisk at the beginning and end, *like this*. You can make a piece of text bold by placing two asterisks at the beginning and end, **like this**. You can also add a link with square brackets following round round brackets, [like this](https://example.com/data/).

We typically describe exactly what data has been shared, how it can be re-used, and give links to where it can be downloaded.

#### Data and code availability

* [Shared dataset 1](https://example.com/data1/): description of shared dataset 1
* [Shared dataset 2](https://example.com/data2/): description of shared dataset 2
* [Shared dataset 3](https://example.com/data3/): description of shared dataset 3

#### Article

DOI: [_put_DOI_here](https://doi.org/_put_DOI_here)

Authors. A..... (20XX) Title of the journal publication. In: Journal Title (Vol. XX, Issue XX, XXXX).

#### Funding

We typically put funder information near the end, here.

#### Infrastructure

Information about any infrastruture used to complete the study.
```

## Editorials

**Editorials** are short, opinion articles that describe the current state of an area of research. They are contributed by those working in that area. They are similar in format to data highlights.

### Illustrations

Each editorial has an illustation that should be 250 px high and 500 px wide. The portal team can help with resizing/editing images. The illustrations should be placed in the `/static/editorials` folder.

### Editorial files

The editorials are generated from Markdown formatted files contained in the `/content/english/editorials/` folder. The file name used here will also be the URL of the editorial (e.g., `test-editorial.md` will become `https://pathogens.se/editorials/test-editorial/`). The images can be in .png or .jpg format.

### Content of the editorial files

Below is an example of a editorial file content. You can copy this text into your markdown file and edit it to write your own editorial, or you can copy an existing editorial and edit the copy. As with the dashboard files, and most other pages in the site, the file comprises of page metadata and then the content shown on the page itself.

```Markdown
---
title: "title of editorial"
date: yyyy-mm-dd
summary: a short summary of the editorial (less than 100 characters)
banner: /editorials/image_names.jpg
banner_caption: 'caption of image'
tags: [keyword 1, keyword 2...]
editorials_topics: [Infectious diseases] (any topics that apply, see below for information on topics)
editorials_authors: [Your Name]
images: [/editorials/image_name.jpg]
---

This is the text of the editorial. This is the first paragraph.

This is the second paragraph of the textt. Markdown formatting should be used in the text. For example, you can make a piece of text italic by placing an asterisk at the beginning and end, *like this*. You can make a piece of text bold by placing two asterisks at the beginning and end, **like this**. You can also add a link with square brackets following round round brackets, [like this](https://example.com/data/).

#### Cite this editorial

The portal team can help to upload the editorial on the [SciLifeLab Data Repository](https://figshare.scilifelab.se). Please email us at [pathogens@scilifelab.se](mailto:pathogens@scilifelab.se) to discuss this.
```

## Emerging pathogens

The **emerging pathogens** pages are intended to show the latest information in the event of a new outbreak. The pages are found in the [emerging pathogens section](https://pathogens.se/pathogens/), located in the `/content/english/pathogens/`. It is the first type of page that we put up about an emerging disease, and do so as soon as possible. We include any information and all resources that are currently available. The structure of the pages vary, but only requires a title in the metadata section (see e.g. editorials and highlights above for more information.) and some text in markdown format below this.

## Events

The **events** page shows events related to topics around pandemic preparedness, e.g. antibiotic resistance. Users should go to the [events page](https://pathogens.se/events/) on the portal itself and fill in the form to suggest an event. The portal team will typically add the suggestion within one working day.

## Funding opportunities

We collect funding opportunities relevant for topics related to pandemic preparedness, e.g. COVID-19, infectious diseases, and antibiotic resistance research. Users should go to the [funding page](https://pathogens.se/funding/) on the portal itself and fill in the form to add a funding opportunity. The portal team will typically add the suggestion within one working day.

## News about the Portal

News items about the Portal are published under `/updates/`. The news items are written about new sections launched, major updates to the portal, or other important information for the communitty.

### Illustrations

Each news item can have two illustrations. One is used as a thumbnail image on the [portal news page](http://pathogens.se/updates/). The other can be shown on the page. Only the first is required, and should be 250 px high and 500 px wide. The portal team can help with resizing/editing images. The illustrations should be placed in the `/static//updates/banners/` folder.

### News files

The news items can be added in the folder `/content/english/updates/`. Each news item is a file with extension **.md**. The file name used here will also be the URL of the news item (e.g., `test-news.md` will become `https://pathogens.se/updates/test-news/`).

### Content of the news files

Below is an example of a news file content. You can copy this text into your markdown file and edit it to write your own news item. It comprises some basic page metadata (used to allow the page to be correctly laid out, and between two lines of '---') and then some text in markdown format. The file should be a markdown file (i.e. with the extension '.md').

```Markdown
---
title: title of news item
date: yyyy-mm-dd
summary: Today we are launching a new section on the Portal devoted to...
banner: /updates/banners/example.png
banner_large: /updates/banners/example_large.png
banner_caption: "Illustration of X. The image was taken from Y."
---

This is the text of the news item. This is the first paragraph.

This is the second paragraph of the text of the news item. Markdown formatting should be used in the text. For example, you can make a piece of text italic by placing an asterisk at the beginning and end, _like this_. You can make a piece of text bold by placing two asterisks at the beginning and end, __like this__. You can also add a link with square brackets following round round brackets, [like this](https://example.com/data/).

This is the third paragraph of the news item.

```

## Ongoing research projects

We maintain a database of currently ongoing research projects on COVID-19. These are displayed under `/research_projects/`. The data is stored in JSON format in `data/research_projects.json`. Below is the format used for each entry. All required fields have to be filled out and in some cases there is a specific format. Note that for the field _topic_ you should choose one or more topics corresponding of the call.

```JSON
{
  "topic": ["COVID-19"],
  "funder": "funder name, required field",
  "project_title": "title of the research project, required field",
  "project_description": "description of the project, optional field, markdown formatting allowed",
  "funding_amount": "funding amount in SEK (e.g., 9.000.000 SEK), optional field",
  "pi": "name of the principal investigator responsible for the project, optional field",
  "pi_affiliation": "name of the university/institute where the project is carried out, optional field",
  "startdate": "project start date in format '2006-01-02', optional field",
  "enddate": "expected project end date in format '2006-01-02', required field",
  "url": "URL (starting with http:// or https://) where more information about the project can be found, optional field"
}
```

At the beginning of the file `data/research_projects.json` there is a field for the last updated date of this file. The date here needs to be updated whenever new projects are added or changes are made.

```JSON
  "last_updated": "2006-01-02",
```

## Publications included in a table

There are multiple places on the portal where relevant publications are shown in tables. In all cases, these publications are taken from a central publications database that is updated monthly by the portal team. The publications are all about COVID-19, and involve at least one author affiliated with a Swedish research organisation. To see this database in full, go to the [Swedish COVID-19 Publications page](http://pathogens.se/publications/). Users cannot add publications, but can email the pathogens portal team at [pathogens@scilifelab.se](mailto:pathogens@scilifelab.se) to add relevant publications.

## Pandemic preparedness resources

**Pandemic preparedness resources pages** comprise information about resources that have been developed in Sweden related to pandemic preparedness. Currently, this comprises primarily of information about projects that are part of SciLifeLab's Pandemic Laboratory Preparedness (PLP) program. The pages are found in the `/content/english/resources/` folder. The pages are in markdown format, and have a '.md' file extension. As with other pages on the portal, they comprise of some initial page metadata that is used to set up the page (and lies between two lines of '---'), and then text in markdown format. The format of these pages is shown below. You can copy this to create a new page, or copy and edit an existing page.

```Markdown
---
title: "title"
category: "plp2" used to place in one of the plp categories
resource_info:
    name: "project name"
    pi: list of PI names,
    host_organisation: XXX University
    contact: "name<br>title<br>Email: [example@example.se](mailto:example@example.se)<br><br>A"name<br>title<br>Email: [example@example.se](mailto:example@example.se)"
for_background_table:
    pi: PI name
    pi_affiliation: XXXX University
---

This is the text of the page. This is the first paragraph.

This is the second paragraph of the text. Markdown formatting should be used in the text. For example, you can make a piece of text italic by placing an asterisk at the beginning and end, *like this*. You can make a piece of text bold by placing two asterisks at the beginning and end, **like this**. You can also add a link with square brackets following round round brackets, [like this](https://example.com/data/).
```

## Topics

Multiple pandemic preparedness topics are covered on the portal. It is possible for users to filter the content of the portal according to a given topic. Topics include, for example, COVID-19, Antibiotic resistance, Influenza, and Mpox. The current topics can be viewed in the [topics section](http://pathogens.se/topics/). In order to suggest a new topic, please contact the the pathogens portal team at [pathogens@scilifelab.se](mailto:pathogens@scilifelab.se). This will allow us to be able to put in place the background code that is needed to make it possible to filter by this topic.

### Content of topics files

The format of the topics pages are similar to other pages on the portal. The pages are in markdown format, and have a '.md' file extension. As with other pages on the portal, they comprise of some initial page metadata that is used to set up the page (and lies between two lines of '---'), and then text in markdown format. The format of these pages is shown below. You can copy this to create a new page, or copy and edit an existing page. They are located in the `/content/english/topics/` folder. The exact format, which you can use to generate a new topics page is shown below.

```Markdown
---
title: title
description: Short description of approximately 100 characters
banner: /topic_thumbs/topic_antibiotic.jpg (picture to be associated with the topic as a thumbnail)
credits:
toc: false (false means that no table of contents will be included)
topic: name of topic
menu:
    topics_menu:
        name: name of topic
        identifier: name_of_topic
---

This is the text of the page. This is the first paragraph.

This is the second paragraph of the text. Markdown formatting should be used in the text. For example, you can make a piece of text italic by placing an asterisk at the beginning and end, *like this*. You can make a piece of text bold by placing two asterisks at the beginning and end, **like this**. You can also add a link with square brackets following round round brackets, [like this](https://example.com/data/).
```
