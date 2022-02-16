# Instructions on adding and editing information displayed on the Portal

## Funding opportunities

We collect funding opportunities relevant for COVID-19, infectious diseases, and antibiotic resistance research. These are displayed under `/funding/`. The data is stored in JSON format in `data/funding.json`. Below is the format used for each entry. All required fields have to be filled out and in some cases there is a specific format. Note that for the field *topic* you should choose one or more topics corresponding of the call.

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

## News about the Portal

News items about the Portal are published under `/updates/`. The news items are written about new sections launched, major updates of the Portal, or major achievements.

### Illustrations

Typically, for each news item we prepare two illustrations. One illustration is smaller and appears on overview page with all news items. The other illustration appears on the page of the news item itself.

The smaller illustration needs to have the width that is twice the length (i.e., length `300 px` and width `600 px`). This way, it will easily fit the look of the page layouts.

Both illustrations should be placed in the `/static/updates/banners` folder. The URL of the images placed here will then be `https://covid19dataportal.se/updates/banners/file_name.png`.

### News files

The news items can be added in the folder `/content/updates/`. Each news item is a file with extension *.md*. The file name used here will also be the URL of the news item (e.g., `test-news.md` will become `https://covid19dataportal.se/updates/test-news/`).

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

This is the second paragraph of the text of the news item. Markdown formatting should be used in the text. For example, you can make a piece of text italic by placing an asterisk at the beginning and end, *like this*. You can make a piece of text bold by placing two asterisks at the beginning and end, **like this**. You can also add a link with square brackets following round round brackets, [like this](https://example.com/data/).

This is the third paragraph of the news item.

```

On the top of the file, surrounded by `---`, basic information for this news item is provided. It contains the title; publication date (desired; Hugo needs to be run on that day or later for it to appear); summary text that appears on the overview page; location of the illustration to be displayed on the overview page (`banner`); localtion of the illustration on the page of the news item (`banner_large`); caption text that will appear under the illustration on the page of the news item.

### Publishing

In order to publish a news item, make a pull request to the `develop` branch.
