---
title: Browser-based tools and AI models
imjoy:
    config:
        show_window_title: true
        menu_container: "menu-container"
        menu_style: { float: 'right' }
    vizarr: |
        async function(source, window_id){
            let viewer;
            if(window_id){
                viewer = await api.createWindow({src: 'https://hms-dbmi.github.io/vizarr/', window_id, window_style: {height: '600px', 'border-style': 'solid'}})
            } else {
                viewer = await api.showDialog({src: 'https://hms-dbmi.github.io/vizarr/'});
            }
            viewer.add_image({source})
        }
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

<div id="menu-container"></div>

## ITK/VTK Viewer
To visualize an image with ITK/VTK viewer, click <button onclick="api.showDialog({src: 'https://kitware.github.io/itk-vtk-viewer/app/', data: {image: 'https://images.proteinatlas.org/115/672_E2_1_blue_red_green.jpg'}})">here</button>

## Vizarr

[Vizarr](https://github.com/hms-dbmi/vizarr) is a client-side program for viewing Zarr-based images with Viv & ImJoy

Vizarr be embedded in the page directly:

<div id="vizarr-embeded-1"></div>

<br>
You can also view the image in a dialog by clicking <button onclick="imjoy.vizarr('https://s3.embassy.ebi.ac.uk/idr/zarr/v0.1/4495402.zarr')">here</button>

## Kaibu Example

To annotate an image with Kaibu, click <button onclick="imjoy.kaibu('https://images.proteinatlas.org/115/672_E2_1_blue_red_green.jpg')">here</button>

### Other Applications

HPA UMAP: <a href="javascript:void(0);" onclick="api.createWindow({src: 'https://raw.githubusercontent.com/imjoy-team/imjoy-plugins/master/repository/HPA-UMAP.imjoy.html', window_id: 'hpa-umap', window_style: {height: '500px'}})">run</a>

<div id="hpa-umap"></div>

HPA Classification: <a href="javascript:void(0);" onclick="api.createWindow({src: 'https://raw.githubusercontent.com/imjoy-team/imjoy-plugins/master/repository/HPA-Classification.imjoy.html', window_id: 'hpa-classification', window_style: {height: '500px'}});">run</a>

<div id="hpa-classification"></div>
