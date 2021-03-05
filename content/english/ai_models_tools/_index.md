---
title: Browser-based tools and AI models
imjoy:
    config:
        show_window_title: true
        menu_container: "menu-container"
        menu_style: { float: 'right' }
    kaibu: |
        async function(url){
            const viewer = await api.showDialog({src: 'https://kaibu.org', fullscreen: true})
            await viewer.view_image(url);
            await viewer.add_shapes([], {name: 'annotation'});
        }
    startup: |
        async function(){

            imjoy.vizarr('https://s3.embassy.ebi.ac.uk/idr/zarr/v0.1/4495402.zarr', 'vizarr-embeded-1')
        }
---

This section presents tools for COVID-19 research and analyses that are available through the [COVID19AI.IO](https://covid19ai.io/) platform. The COVID-19 AI platform provides a place for sharing and finding AI models, datasets, and tools. The focus on is on image analysis. Specifically, the following are shared and made available on the platform:

- machine learning model algorithms as well as pre-trained models,
- datasets useful for ML model training purposes as well as for research in general,
- tools that can be run simply inside the web-browser (for example, tools for manual image annotation and tools for automatic image classification based on available pre-trained models).

The platform is supported by SciLifeLab and Knut and Alice Wallenberg Foundation.

<div id="menu-container"></div>

## Datasets

## AI models

## Tools

#### Kaibu

[Kaibu](https://kaibu.org/) is a web application for visualizing and annotating multi-dimensional images, built with [OpenLayers](https://openlayers.org/) and [itk-vtk-viewer](https://kitware.github.io/itk-vtk-viewer/). It runs directly in the web browser, so there is no need to install special software. Afyer you upload your own image to Kaibu, you can annotate it using various tools: hand drawing, various shapes, colors, image display settings, multiple layers etc.

Below, you can use Kaibu directly on this page (powered by [imJoy](https://imjoy.io/)). Alternatively, open [kaibu.org](https://kaibu.org) to see Kaibu as a stand-alone application running in your browser.

To try out anotating with Kaibu, <button onclick="imjoy.kaibu('https://images.proteinatlas.org/115/672_E2_1_blue_red_green.jpg')">click here</button>

#### HPA UMAP

HPA UMAP: <a href="javascript:void(0);" onclick="api.createWindow({src: 'https://raw.githubusercontent.com/imjoy-team/imjoy-plugins/master/repository/HPA-UMAP.imjoy.html', window_id: 'hpa-umap', window_style: {height: '500px'}})">run</a>

<div id="hpa-umap"></div>

#### HPA Classification

HPA Classification: <a href="javascript:void(0);" onclick="api.createWindow({src: 'https://raw.githubusercontent.com/imjoy-team/imjoy-plugins/master/repository/HPA-Classification.imjoy.html', window_id: 'hpa-classification', window_style: {height: '500px'}});">run</a>

<div id="hpa-classification"></div>
