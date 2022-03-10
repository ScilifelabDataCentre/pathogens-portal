# Running a local copy of the Portal

Because the Portal is built using [Hugo](https://gohugo.io/), a static site generator, it is quite easy to run a full version of the Portal on your computer and see how your changes look while doing that.

#### Using Hugo

To view your changes as they will appear in the final website, you need to install Hugo. You can find instructions on the Hugo website: [https://gohugo.io/](https://gohugo.io/)

If you're using Mac OSX, it's recommended to use [Homebrew](https://brew.sh/) - if homebrew is already set up, installing Hugo is just a case of:

```bash
brew install hugo
```

Once Hugo is installed, navigate to the folder where you cloned this repository and simply run the following command in the repository root directory:

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

#### Using Docker

If you would prefer not to use Hugo, you can use the provided Dockerfile to build and run a container.
