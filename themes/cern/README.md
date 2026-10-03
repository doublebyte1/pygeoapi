# CERN theme

A [pygeoapi](https://pygeoapi.io) HTML theme in the style of the first web
pages served by Tim Berners-Lee's server at CERN in 1991-1993, after
[The World Wide Web project page](https://info.cern.ch/hypertext/WWW/TheProject.html).

The design relies almost entirely on plain HTML: one `<h1>`, horizontal
rules, `<dl>`/`<dt>`/`<dd>` lists, `<address>` footers, the classic blue
links, Times serif type, and a final `[End]` marker. There is no
JavaScript and only a few lines of CSS to restore the defaults a 1993
browser would have applied.

```
themes/cern
+-- README.md
+-- static
|   `-- css
|       `-- cern.css        # the whole stylesheet (browser-default look)
`-- templates
    +-- _base.html          # CERN-style page frame (h1, hr, address, [End])
    `-- tilematrixsets
        +-- index.html      # /TileMatrixSets?f=html
        `-- tilematrixset.html  # /TileMatrixSets/<id>?f=html
```

## Install

Point the `server:templates` section of your pygeoapi config at this theme:

```yaml
server:
    templates:
      path: /path/to/pygeoapi/themes/cern/templates
      static: /path/to/pygeoapi/themes/cern/static # css/js/img
```

See the [HTML templating](https://docs.pygeoapi.io/en/latest/html-templating.html)
documentation. The theme only needs to ship the templates it wants to
change: `_base.html` re-frames every pygeoapi HTML page, and the two
`tilematrixsets/` templates render the TileMatrixSets pages. Any other
endpoint falls back to the stock pygeoapi template, which inherits this
theme's `_base.html` as well.
