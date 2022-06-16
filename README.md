# ![The Swedish COVID-19 & Pandemic Preparedness Data Portal](static/img/site_logo/CV19DP_logo_oneliner_SWE.png)

## The Swedish COVID-19 & Pandemic Preparedness Data Portal

This is the source code for the Swedish COVID-19 & Pandemic Preparedness Data Portal:
[https://www.covid19dataportal.se/](https://www.covid19dataportal.se/)

The website is the Swedish node for the European Covid-19 Data Portal project.
The main European site can be seen at [https://www.covid19dataportal.org/](https://www.covid19dataportal.org/)

## Introduction

This website is developed and maintained by the [SciLifeLab Data Centre](https://www.scilifelab.se/data/) with many contributions from collaborators. Contributions from anyone are welcome and will be published after a review by the Portal team.

The website is intended to provide a central place to provide information about:

- Available open research datasets relevant for COVID-19 and other topics within pandemic preparedness research
- Support services for researchers working on COVID-19 and other topics within pandemic preparedness research
- Information and support for publishing and sharing datasets on COVID-19 and other topics within pandemic preparedness research
- Ongoing research projects and funding opportunities for COVID-19 and other topics within pandemic preparedness research

The site is built using the [Hugo](https://gohugo.io/) static web site generator.
It uses the [Bootstrap](https://getbootstrap.com/) framework. In addition, it uses [Vega-Lite](https://vega.github.io/vega-lite/), [DataTables](https://datatables.net/), [OpenLayers](https://openlayers.org/), [plotly](https://plotly.com/), [ImJoy](https://imjoy.io/) for various features.

## Development and contributions

### Adding and editing information in different sections

We prepared detailed instructions on how to add or edit information in each specific section of the portal, see [the page on adding and editing information in the CONTRIBUTING folder](https://github.com/ScilifelabDataCentre/covid-portal/blob/develop/CONTRIBUTING/adding_editing_information.md).

### Testing changes with a local copy of the portal

Users who are technically more advanced are welcome to make contributions by running a local copy of the portal on their own computers, we prepared [instructions on how to do that here](https://github.com/ScilifelabDataCentre/covid-portal/blob/develop/CONTRIBUTING/running_a_local_copy.md).

### Using ImJoy Plugins

This website supports [ImJoy](https://imjoy.io) plugins which can be used to visualize, annotate, run analysis directly from the website. See [an example here](https://covid19dataportal.se/highlights/immunofluorescence/). Please see the file [CONTRIBUTING/ImJoy.md](https://github.com/ScilifelabDataCentre/covid-portal/blob/develop/CONTRIBUTING/ImJoy.md) for examples of usage.

### The Swedish COVID-19 Sample Collection Database

The portal team works closely with [Biobank Sverige](https://biobanksverige.se) to develop and maintain the [The Swedish COVID-19 Sample Collection Database](https://biobanks.covid19dataportal.se). The database contains biobanks collections from multiple biobanks across Sweden. Research staff can use the database to search for and request access to samples that could be beneficial for their work. New collections are submitted to the portal team by Biobank Sverige as they become available. The code behind The Swedish COVID-19 Sample Collection Database is maintained by the portal team and is available on [GitHub](https://github.com/ScilifelabDataCentre/covid-sample-collection-database).

### Data visualisations

Unless otherwise specified, the data visualisations on the portal have been developed in-house by the portal team. A link to the code underlying each visualisation is provided on the portal page on which it is displayed. All visualisations on the portal can be found on our dedicated [GitHub repository](https://github.com/ScilifelabDataCentre/covid-portal-visualisations).

## How to get help

If you have any questions regarding any of the code or content associated with the portal, please get in touch by emailing us at [datacentre@scilifelab.se](mailto:datacentre@scilifelab.se).

## Credits

The website was built and is maintained by [SciLifeLab Data Centre](https://www.scilifelab.se/data/). We are grateful to many collaborators, both from the Data Centre and elsewhere, for their contributions.

The primary contributors have been:

- [@SonjaAits](https://github.com/SonjaAits)
- [@ewels](https://github.com/ewels)
- [@talavis](https://github.com/talavis)
- [@pekrau](http://github.com/pekrau/)
- [@akochari](http://github.com/akochari/)
- [@LianeHughes](https://github.com/LianeHughes)
- [@KatarinaOjeforsStark](https://github.com/KatarinaOjeforsStark)
- [@senthil10](https://github.com/senthil10)
- [@HannaKultima](https://github.com/HannaKultima)
- [@johanrung](https://github.com/johanrung)
