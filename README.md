# whrss.com

The website for whrss9527's Mac apps — [Pop](https://github.com/whrss9527/pop), [Meno](https://github.com/whrss9527/meno), [Stox](https://github.com/whrss9527/stox) and [Proxi](https://github.com/whrss9527/proxi) — served at **https://whrss.com**. The blog that used to live there moves to **https://blog.whrss.com**.

Plain HTML and CSS. No build step, no framework, no JavaScript except a few lines on the 404 page, and no requests to other origins (no CDNs, web fonts or analytics), which is what the privacy policies promise.

## Structure

```
index.html              Home (English)
zh/index.html           Home (Chinese)
pop/ meno/ stox/ proxi/ App pages: hero, features, requirements, install and update, FAQ
privacy/<app>/          Privacy policy per app (for the Mac App Store, Setapp and users)
support/                How to get help: GitHub issues per app, email
404.html                Not found; links old blog URLs to the same path on blog.whrss.com
assets/site.css         The only stylesheet: tokens on :root, light and dark via prefers-color-scheme
assets/icons/           App icons (256 px, from each app's repository)
assets/img/<app>/       Screenshots (from each app's repository and CI screenshots)
assets/favicon.svg, assets/apple-touch-icon.png
CNAME                   whrss.com (kept for reference; see "Custom domain" below)
robots.txt, sitemap.xml
scripts/check_links.py  Checks internal links, #anchors and that nothing loads from another origin
.github/workflows/pages.yml  Deploys to GitHub Pages on every push to main
```

Every page links its stylesheet and images with relative paths, so the site also works from a local folder. The header and footer are repeated in each page; when you change them, change them everywhere (a project-wide search and replace is enough).

### Screenshots

- **Stox** — `docs/images/*.jpg` in the Stox repository, with the black desktop around the panel made transparent (`.webp`).
- **Pop** — CI screenshots from the `ci-screenshots/macos-26` branch of the Pop repository, cut out the same way. Pop has no screenshots in its README yet.
- **Proxi** — `docs/hero.png` and frames of `docs/tour.gif` from the Proxi repository.
- **Meno** — there are no Meno screenshots anywhere yet, so the Meno page uses CSS illustrations, labelled as such. Replace them with real screenshots when there are some.

The Pop, Stox and Proxi interfaces are in Chinese, so their screenshots are too; the English pages say so.

## Preview locally

```sh
python3 -m http.server 8000
# open http://localhost:8000
python3 scripts/check_links.py   # before pushing
```

Use a real server rather than opening the files directly, so that `/pop/` resolves to `pop/index.html` as it does on GitHub Pages.

## Deployment

`.github/workflows/pages.yml` runs on every push to `main` (and by hand from the Actions tab). It checks the links, copies the site into `_site/` without `README.md`, `scripts/` and `.github/`, and deploys it with `actions/upload-pages-artifact` and `actions/deploy-pages`.

## Owner checklist

1. **Pages source.** Repository Settings → Pages → *Build and deployment* → Source: **GitHub Actions**.
2. **Push `main`.** The first run of *Deploy to GitHub Pages* publishes the site at `https://whrss9527.github.io/site/`. Leave *Custom domain* **empty** for now: as soon as it is set, GitHub redirects the github.io address to `whrss.com`, which still shows the blog until step 4 is done.
3. **Move the blog first.** whrss.com currently points at the blog (through Cloudflare). Before changing the apex records, note where they point today, create `blog.whrss.com` for the same server, and make sure the blog server answers for `blog.whrss.com` with a valid certificate. Otherwise the blog goes offline when the apex moves.
4. **DNS for whrss.com** (at your DNS provider, currently Cloudflare):

   | Type  | Name  | Value |
   | ----- | ----- | ----- |
   | A     | `@`   | `185.199.108.153` |
   | A     | `@`   | `185.199.109.153` |
   | A     | `@`   | `185.199.110.153` |
   | A     | `@`   | `185.199.111.153` |
   | AAAA  | `@`   | `2606:50c0:8000::153` |
   | AAAA  | `@`   | `2606:50c0:8001::153` |
   | AAAA  | `@`   | `2606:50c0:8002::153` |
   | AAAA  | `@`   | `2606:50c0:8003::153` |
   | CNAME | `www` | `whrss9527.github.io` |
   | A / CNAME | `blog` | the blog server (what `@` points to today) |

   Remove any other A, AAAA or CNAME records for `@` and `www`. On Cloudflare, set the GitHub records to **DNS only** (grey cloud): GitHub has to see its own IPs to issue the certificate. If the domain has CAA records, allow `letsencrypt.org`.
5. **Custom domain.** Only now set Settings → Pages → *Custom domain* to `whrss.com` and save (the `CNAME` file is **ignored** for Actions-based Pages). Optionally verify the domain first in your account's Settings → Pages → *Verified domains*, which stops anyone else from claiming it.
6. **HTTPS.** When Settings → Pages shows the certificate as issued (minutes to about an hour after DNS resolves), tick **Enforce HTTPS**. `www.whrss.com` then redirects to `whrss.com`.
7. **Check.** `https://whrss.com`, `https://www.whrss.com`, `https://blog.whrss.com`, and an old blog URL such as `https://whrss.com/posts/<slug>`: addresses that only existed on the blog (`/posts/`, `/feed`, `/tags/`, `/archives`, `/page/`, `/search`) are sent to the same path on blog.whrss.com by the 404 page; anything else shows the 404 page with a link. RSS readers don't run that script, so feed subscribers need the new feed address `https://blog.whrss.com/feed`.

## Privacy policies

The policies were written from the apps' source code (network requests and storage) as of the date on each page. When an app starts contacting a new service or storing data somewhere new, update its policy and the date. The contact address is whrss9527@gmail.com.
