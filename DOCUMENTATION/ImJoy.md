## Using ImJoy Plugins

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
