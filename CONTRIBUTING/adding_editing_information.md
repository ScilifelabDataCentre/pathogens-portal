# Instructions on adding and editing information displayed on the Portal

We welcome contributions from the community in all sections of our Portal. Here, we describe contributing through GitHub - either through the GitHub web interface or through a local copy on your computer. You should have basic knowledge of the GitHub web interface or CLI in order to be able to use this way of contributing. There are multiple other ways to contribute so that you can use the way that is most convenient for you. Please [see this page for information on other ways you can send contributions](https://covid19dataportal.se/contribute/).

In short, in order to add or edit information on the Portal, make a fork of this repository and make changes in the corresponding section as described below. After making changes to the section which you would like to edit/add to as described below, you should send a pull request to the `develop` branch. We will review and approve it asap.

__Table of contents:__

- [General instructions: how to propose changes/additions](#general-instructions-how-to-start)
- [Available datasets](#available-datasets)
- [Funding opportunities](#funding-opportunities)
- [Ongoing research projects](#ongoing-research-projects)
- [Data highlights](#data-highlights)
- [News about the Portal](#news-about-the-portal)
- [Resources](#resources)

## General instructions: how to propose changes/additions

All information displayed on the Portal is contained within [this GitHub repository](https://github.com/ScilifelabDataCentre/covid-portal). Some of the sections use information that is stored in the `data` folder in .JSON format while other sections use information that is stored in the `content` folder in Markdown format.

### Using the web interface

- Navigate to the folder and file that is indicated below in the corresponding section.
- Click on the top right corner of the document ("Edit this file"). This should create a fork of the original repository in your own GitHub account. You should see a page where you can directly edit the content.
- Make changes as described below; do not forget to change the last update date on top of the document if needed.
- Scroll to the bottom of the page. Describe what you have changed and press 'Propose changes'
- You should now find yourself on a page where you can create a pull request. Check that the pull request will be sent to the base repository `SciLifeLabDataCentre/covid-portal` and base `develop`. You can also review the changes you made. Click on "Create pull request" if everything looks good.
- Once created, a member of the Portal team will review your changes.
Once approved, they will be merged and published.

### Using a local copy

If you prefer, you can edit the website files on your computer in your favourite text editor. Fork this repository to your account. Then, clone the forked repository to your machine:

```bash
git clone git@github.com:[YOUR-USERNAME]/covid-portal.git
cd covid-portal
```

To make it easier to pull in changes made by others, you can add the main repository as a remote:

```bash
git remote add upstream https://github.com/ScilifelabDataCentre/covid-portal.git
```

Then you can fetch changes at any time from this remote:

```bash
git pull upstream develop
```

When you have finished editing, commit and push to your fork:

```bash
git add .
git commit -m "My changes"
git push
```

Once you're finished with your edits and they are committed and pushed to your forked repository, it's time to open a pull request. In short:

- Visit the main repository: [https://github.com/ScilifelabDataCentre/covid-portal](https://github.com/ScilifelabDataCentre/covid-portal)
- Click the button that reads _"New Pull Request"_
- Click the text link near the top that says _"compare across forks"_
- In the right-hand _"head repository"_ drop down, select your username / fork.
- If you're happy with the list of commits shown, and the diff in the _"Files Changed"_ tab, fill in a title and description and click _"Create pull request"_

Once created, a member of the Portal team will review your changes.
Once approved, they will be merged and published.

#### Testing with a local copy of the Portal

Because the Portal is built on Hugo, it is quite easy to run a full version of the Portal on your computer and see how your changes look while doing that. See [this page for information on how to do that](https://github.com/ScilifelabDataCentre/covid-portal/blob/develop/CONTRIBUTING/running_a_local_copy.md).

## Available datasets

_Instructions coming soon._

## Funding opportunities

We collect funding opportunities relevant for COVID-19, infectious diseases, and antibiotic resistance research. These are displayed under `/funding/`. The data is stored in JSON format in `data/funding.json`. Below is the format used for each entry. All required fields have to be filled out and in some cases there is a specific format. Note that for the field _topic_ you should choose one or more topics corresponding of the call.

```JSON
{
  "topic": ["COVID-19", "General", "Antibiotic resistance", "Infectious diseases"],
  "funder": "funder name, required field",
  "call_title": "call title, required field",
  "call_url": "call URL, including https://, required field",
  "call_description": "call description, optional field, markdown formatting allowed",
  "applicant": "information about who can apply, optional field, markdown formatting allowed",
  "decision_date": "information about when the decision will be made, optional field",
  "funding_period": "information about the duration of funding, optional field",
  "funding_amount": "information about the amount one call apply for, optional field",
  "submission_opendate": "date in format '2006-01-02', optional field",
  "submission_deadline": "date in format '2006-01-02', required field"
}
```

At the beginning of the file `data/funding.json` there is a field for the last updated date of this file. The date here needs to be updated whenever new calls are added or changes are made.

```JSON
  "last_updated": "2006-01-02",
```

## Ongoing research projects

We maintain a database of currently ongoing research projects on COVID-19, infectious diseases, and antibiotic resistance in Sweden. These are displayed under `/research_projects/`. The data is stored in JSON format in `data/research_projects.json`. Below is the format used for each entry. All required fields have to be filled out and in some cases there is a specific format. Note that for the field _topic_ you should choose one or more topics corresponding of the call.

```JSON
{
  "topic": ["COVID-19","Infectious diseases","Antibiotic resistance"],
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

## Data highlights

__Data highlights__ is a section of the portal which contains news items promoting recent openly shared data that can potentially be used by many other researchers to make further discoveries or notable data re-use examples.

### Illustrations

Typically, for each data highlight we prepare two illustrations. One illustration is smaller and appears on overview page with all data highlights. The other illustration appears on the page of the highlight itself.

The smaller illustration needs to have the width that is twice the length (i.e., length `300 px` and width `600 px`). This way, it will easily fit the look of the page layouts.

Both illustrations should be placed in the `/static/highlights/banners` folder. The URL of the images placed here will then be `https://covid19dataportal.se/highlights/banners/file_name.png`.

### Data highlight files

The data highlights are generated from Markdown formatted files contained in the `/content/english/highlights/` folder. The file name used here will also be the URL of the data highlight (e.g., `test-highlight.md` will become `https://covid19dataportal.se/highlights/test-highlight/`).

### Content of the data highlight files

Below is an example of a data highlight file content. You can copy this text into your markdown file and edit it to write your own data highlight.

```Markdown
---
title: Important new dataset shared
date: 2021-01-01
summary: A new dataset containing a large amount of valuable data has been openly shared.
banner: /highlights/banners/example.png
banner_large: /highlights/banners/example_large.png
banner_caption: "Illustration of X. The image was taken from Y."
topics: [COVID-19, Infectious diseases, Antibiotic resistance]
---

This is the text of the highlight. This is the first paragraph. Introduce why this is an important topic.

This is the second paragraph of the text of the highlight. Markdown formatting should be used in the text. For example, you can make a piece of text italic by placing an asterisk at the beginning and end, *like this*. You can make a piece of text bold by placing two asterisks at the beginning and end, **like this**. You can also add a link with square brackets following round round brackets, [like this](https://example.com/data/).

We typically describe exactly what data has been shared, how it can be re-used, and give links to where it can be downloaded.

#### Data

* [Shared dataset 1](https://example.com/data1/): description of shared dataset 1
* [Shared dataset 2](https://example.com/data2/): description of shared dataset 2
* [Shared dataset 3](https://example.com/data3/): description of shared dataset 3

#### Article

DOI: [_put_DOI_here](https://doi.org/_put_DOI_here)

Andersson, M., Johansson, S., Karlsson, A. Title of the journal publication *Journal Title*, **X** (X) (20XX).

#### Funding

We typically put funder information near the end, here.

```

On the top of the file, surrounded by `---`, basic information for this data highlight is provided. It contains the title; publication date (desired; Hugo needs to be run on that day or later for it to appear); summary text that appears in the homepage and in the main page of the Data highlights section; location of the illustration to be displayed on the homepage (`banner`); location of the illustration to be displayed on the page of the highlight (`banner_large`); caption text that will appear under the illustration on the page of the highlight.

The title, date, summary, illustrations will appear where they are supposed to be.

## News about the Portal

News items about the Portal are published under `/updates/`. The news items are written about new sections launched, major updates of the Portal, or major achievements.

### Illustrations

Typically, for each news item we prepare two illustrations. One illustration is smaller and appears on overview page with all news items. The other illustration appears on the page of the news item itself.

The smaller illustration needs to have the width that is twice the length (i.e., length `300 px` and width `600 px`). This way, it will easily fit the look of the page layouts.

Both illustrations should be placed in the `/static/updates/banners` folder. The URL of the images placed here will then be `https://covid19dataportal.se/updates/banners/file_name.png`.

### News files

The news items can be added in the folder `/content/updates/`. Each news item is a file with extension __.md__. The file name used here will also be the URL of the news item (e.g., `test-news.md` will become `https://covid19dataportal.se/updates/test-news/`).

### Content of the news files

Below is an example of a news file content. You can copy this text into your markdown file and edit it to write your own news item.

```Markdown
---
title: New section on the Portal launched
date: 2006-01-02
summary: Today we are launching a new section on the Portal devoted to...
banner: /updates/banners/example.png
banner_large: /updates/banners/example_large.png
banner_caption: "Illustration of X. The image was taken from Y."
---

This is the text of the news item. This is the first paragraph.

This is the second paragraph of the text of the news item. Markdown formatting should be used in the text. For example, you can make a piece of text italic by placing an asterisk at the beginning and end, _like this_. You can make a piece of text bold by placing two asterisks at the beginning and end, __like this__. You can also add a link with square brackets following round round brackets, [like this](https://example.com/data/).

This is the third paragraph of the news item.

```

On the top of the file, surrounded by `---`, basic information for this news item is provided. It contains the title; publication date (desired; Hugo needs to be run on that day or later for it to appear); summary text that appears on the overview page; location of the illustration to be displayed on the overview page (`banner`); localtion of the illustration on the page of the news item (`banner_large`); caption text that will appear under the illustration on the page of the news item.

## Resources

_Instructions coming soon._
