# Running a local copy of the portal

The portal is built using [Hugo](https://gohugo.io/), a static site generator. This makes it relatively easy to run a full version of the portal on your computer (i.e. locally). This means that you can change the code and see exactly how those changes would look on the site before you deploy the changes to the site.
#### Clone a copy of the portal code

All of the code behind the portal is stored in [this GitHub repository](https://github.com/ScilifelabDataCentre/pathogens-portal). There are multiple ways to clone a GitHub repository so that you have your own copy on your computer. Please see [the GitHub documentation](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) for information on how to do this.

#### Using Hugo

In order to run a local copy, you first need to install Hugo on your computer. Detailed instructions for how to do this are available on the Hugo website: [https://gohugo.io/](https://gohugo.io/).

On Mac OSX, it is recommended to use [Homebrew](https://brew.sh/) to install Hugo. Once Homebrew is set up, you can run the following command in a terminal window to install Hugo:

```bash
brew install hugo
```

Once Hugo has finished installing, you can use it to view the site locally right away. To do this, first navigate to the folder that holds your copy of the portal code (i.e. the cloned copy of the GitHub repository). You can do this with the cd command in the terminal window e.g.

```bash
cd FILE_PATH/TO/CLONED/REPOSITORY
```

Once you've navigated to the folder that holds your code, you can type 'hugo serve' in your terminal window. You will then see something like this:

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
Watching for changes in /Users/philewels/GitHub/pathogens-portal/{archetypes,content,layouts,static}
Watching for config changes in /Users/philewels/GitHub/pathogens-portal/config.yaml
Environment: "development"
Serving pages from memory
Running in Fast Render Mode. For full rebuilds on change: hugo server --disableFastRender
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
Press Ctrl+C to stop
```

Use the URL printed at the bottom of this message (here, it's `http://localhost:1313/`) to view the site.
Every time you save a file, the page will automatically refresh in the browser, so you can see the effect of the changes in real time.

#### Using Docker

If you would prefer not to use Hugo, you can use the provided Dockerfile to build and run a container instead.
