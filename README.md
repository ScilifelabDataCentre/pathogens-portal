# ![COVID-19 Data Portal Sweden](static/img/site_logo/CV19DP_logo_oneliner_SWE.png)

## COVID-19 Data Portal Sweden

This is the source code for the Swedish Covid-19 Data Portal:
[https://www.covid19dataportal.se/](https://www.covid19dataportal.se/)

The website is the Swedish node for the European Covid-19 Data Portal project.
The main European site can be seen at [https://www.covid19dataportal.org/](https://www.covid19dataportal.org/)

- [Introduction](#introduction)
- [Development](#development)
    - [Step 1: Access the code](#step-1-access-the-code)
    - [Step 2a: Edit the files (online)](#step-2a-edit-the-files-online)
    - [Step 2b: Edit the files (locally)](#step-2b-edit-the-files-locally)
    - [Step 3: Make a pull request](#step-3-make-a-pull-request)
- [How to get help](#how-to-get-help)
- [Credits](#credits)

## Introduction

This website is developed for [Vetenskapsrådet](https://www.vr.se/) by the [SciLifeLab Data Centre](https://www.scilifelab.se/data/).
It is intended to provide a central place to provide information about:

- Available COVID-19 datasets
- Support services for COVID-19 researchers
- Information and support for publishing and sharing COVID-19 datasets

The site is built using the [Hugo](https://gohugo.io/) static web site generator.
It uses the [Bootstrap](https://getbootstrap.com/) framework

## Development

All website content is written in [Markdown](https://guides.github.com/features/mastering-markdown/), and so relatively easy to edit.

### Step 1: Access the code

The code is hosted on [GitHub](http://github.com/), so you'll need an account.

Next, visit the code repository: [https://github.com/ScilifelabDataCentre/covid-portal](https://github.com/ScilifelabDataCentre/covid-portal)

In the top right, you'll see a button that says _"Fork"_. Click this, then select your username.
This makes a copy of the repository under your personal account that you can edit.

### Step 2a: Edit the files (online)

> This is best if you only want to make one or two minor tweaks.
> If you want to make more substantial edits over a longer time frame, we recommend editing locally (_Step 2b_).

The easiest way to edit the website files is on the GitHub website.

On the web page of your _forked_ copy of the repository, look in the `content/` directory.
Each subdirectory contains the website contents in English or Swedish.

The filenames correspond to the website URL:

- [https://www.covid19dataportal.se/data_types/protein_data/services/](https://www.covid19dataportal.se/data_types/protein_data/services/)
    - `content/english/data_types/protein_data/services.md`
- [https://www.covid19dataportal.se/sv/data_types/protein_data/](https://www.covid19dataportal.se/sv/data_types/protein_data/)
    - `content/svenska/data_types/protein_data/_index.md`

Go to the markdown file that you want to edit, then click the Pencil icon :pencil2: in the top right.
This opens a web-based editor where you can add and edit content.

When you're finished, scroll to the bottom and fill in / submit the _"Commit changes"_ form.

You're nearly done - you can now skip to _Step 3_.

### Step 2b: Edit the files (locally)

#### Git setup

If you prefer, you can edit the website files on your computer in your favourite text editor.
Just fork the repository to your machine:

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

#### Testing locally

To view your changes as they will appear in the final website, you need to install Hugo.
You can find instructions on the Hugo website: [https://gohugo.io/](https://gohugo.io/)

If you're using Mac OSX, it's recommended to use [Homebrew](https://brew.sh/) -
if homebrew is already set up, installing Hugo is just a case of:

```bash
brew install hugo
```

Once Hugo is installed, simply run the following command in the repository root directory:

```console
$ hugo serve

                   | EN | SV
-------------------+----+-----
  Pages            | 34 | 34
  Paginator pages  |  0 |  0
  Non-page files   |  0 |  0
  Static files     | 26 | 26
  Processed images |  0 |  0
  Aliases          |  1 |  0
  Sitemaps         |  2 |  1
  Cleaned          |  0 |  0

Built in 123 ms
Watching for changes in /Users/philewels/GitHub/covid-portal/{archetypes,content,layouts,static}
Watching for config changes in /Users/philewels/GitHub/covid-portal/config.yaml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

Use the URL printed at the bottom of this message (here, it's `http://localhost:1313/`) to view the site.
Every time you save a file, the page will automatically refresh in the browser.

#### Docker

If you would prefer not to use Hugo, you can use the provided Dockerfile to build and run a container.

### Step 3: Make a pull request

Once you're finished with your edits and they are committed and pushed to your forked repository, it's time to open a pull request.

You can find full documentation on the [GitHub help website](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests), however in short:

- Visit the main repository: [https://github.com/ScilifelabDataCentre/covid-portal](https://github.com/ScilifelabDataCentre/covid-portal)
- Click the button that reads _"New Pull Request"_
- Click the text link near the top that says _"compare across forks"_
- In the right-hand _"head repository"_ drop down, select your username / fork.
- If you're happy with the list of commits shown, and the diff in the _"Files Changed"_ tab, fill in a title and description and click _"Create pull request"_

Once created, a member of the website team will review your changes.
Once approved, they will be merged and deployed.

## ImJoy Plugins

This website supports [ImJoy](https://imjoy.io) plugins which can be used to visualize, annotate, run analysis directly from the website.

### Activate ImJoy in a page

In any markdown file, you can activate ImJoy by inserting an `imjoy` key along with its configuration fields. For example:

```markdown
---
title: My Awesome Page with ImJoy plugins

imjoy: {}
---
```

You can pass a config field if you want to customize ImJoy in the page. For example:

```markdown
---
title: My Awesome Page with ImJoy plugins

imjoy:
  config:
    show_window_title: true
---
```

You can find all the available config fields [here](https://github.com/imjoy-team/imjoy-core/blob/master/docs/integration.md#api-options).

### Use ImJoy plugins

To use a plugin in the markdown page, you can use `<button>` or `<a>` tags and call any ImJoy API function directly in the `onclick` callback function. For example:

```markdown
To visualize an image with ITK/VTK viewer, click <button onclick="api.showDialog({src: 'https://kitware.github.io/itk-vtk-viewer/app/', data: {image: 'https://images.proteinatlas.org/115/672_E2_1_blue_red_green.jpg'}})">here</button>
```

### Predefined ImJoy functions

Sometimes calling an ImJoy plugin requires several lines of code, adding them to the callback function will become very long. Besides that, we may want to repetitively use the same code in same page. To address this, we support predefined functions to improve reusability of code in the same page. It works by defining a set of functions in the metadata field of the markdown file, which will be parsed and made available under the `window.imjoy` object.

As an example, the following code block defines two functions (`vizarr` and `kaibu`), and they can then be called in the page:

```markdown
---
title: My Awesome Page with ImJoy plugins

imjoy:
    config: {}
    vizarr: |
        function(src){
            api.createWindow({src: src});
            return false;
        }
    kaibu: |
        async function(url){
            const viewer = await api.createWindow({src: 'https://kaibu.org', fullscreen: true})
            await viewer.view_image(url);
            await viewer.add_shapes([], {name: 'annotation'});
        }
---

As a special case, if the function name is `startup`, then it will be called (with no argument) right after the ImJoy core initialized.


## Vizarr Example

To visualize an image with vizarr, click <button onclick="imjoy.vizarr('https://hms-dbmi.github.io/vizarr/?source=https://s3.embassy.ebi.ac.uk/idr/zarr/v0.1/4495402.zarr')">here</button>

## Kaibu Example

To annotate an image with Kaibu, click <button onclick="imjoy.kaibu('https://images.proteinatlas.org/115/672_E2_1_blue_red_green.jpg')">here</button>

```

### Customize ImJoy windows and menu

By default, all the ImJoy windows will be shown as dialog. If you want to display it in the page, you will need to 1) create a `div` tag in the page and define an id 2) specify the id of the `div` tag as an ImJoy config option `window_manager_container`. For example:

```markdown
---
title: My Awesome Page with ImJoy plugins

imjoy:
  config:
    show_window_title: true
    window_manager_container: "window-container"
    window_style:
      height: 500px
---

<div id="window-container"></div>
```

Similarly, you can also customize the ImJoy menu button with something like this:

```markdown
---
title: My Awesome Page with ImJoy plugins

imjoy:
  config:
    menu_container: "menu-container"
    menu_style:
      float: right
---

<div id="menu-container"></div>
```

### Display inline window

You can also display the window in `inline` mode when calling `api.createWindow`. To do that, you need to 1) define a `div` tag with id 2) pass the id as `window_id` when calling `api.createWindow`. Optionally, you can pass `window_style` which is an object for customizing the window style.

For example, the following code block defines a plugin that will create an `inline` window:

```markdown
---
title: My Awesome Page with ImJoy plugins

imjoy: {}
---

HPA UMAP: <a href="javascript:void(0);" onclick="api.createWindow({src: 'https://raw.githubusercontent.com/imjoy-team/imjoy-plugins/master/repository/HPA-UMAP.imjoy.html', window_id: 'hpa-umap', window_style: {height: '500px'}})">run</a>

<div id="hpa-umap"></div>
```

## How to get help

If in doubt, you can ask for help on the [`#covid-19-data-hub`](https://scilifelab.slack.com/archives/C012X6S0D3N) channel on the SciLifeLab Slack, or email [datacentre@scilifelab.se](mailto:datacentre@scilifelab.se).

## Credits

The website was built by [SciLifeLab Data Centre](https://www.scilifelab.se/data/) with the help of some additional SciLifeLab volunteers.

The primary contributors have been:

- [@pekrau](http://github.com/pekrau/): Project leader
- [@ewels](https://github.com/ewels): Built the website
- [@talavis](https://github.com/talavis): Server setup and more
