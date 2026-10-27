CONTRACT.LY LOGO PACKAGE  (version 1, working draft)
=====================================================

The logo is an open "C" ring in a violet-to-pink gradient with a lime dot in the opening.
The dot is also the dot in ".ly", so the symbol and the name echo each other.

NOTE BEFORE YOU PUBLISH
- The name "Contract.ly" has not been cleared. Run a trademark search and have a trademark
  attorney confirm it before you spend money on printing, signs or ads.
- ".ly" is Libya's country domain. Check which domain you can actually own (for example
  contractly.com) and how you will handle it.


WHAT IS IN THIS FOLDER
----------------------
FULL LOGO (symbol + "contract.ly") - READY TO USE, NO FONT NEEDED
  svg/logo-full-dark-bg-outlined.svg , svg/logo-full-light-bg-outlined.svg  (text converted to shapes)
  png/logo-full-dark-bg.png / logo-full-light-bg.png   (transparent background, 3200 px wide)
  png/logo-full-on-ink-solid.png / logo-full-on-white-solid.png   (same, with a solid background)
  NOTE: these use Outfit Bold for the lettering, a close stand-in for Sora Bold (Sora could not be
  installed when they were made). Letter shapes differ slightly from the concept board.
  The older logo-full-*-bg.svg files use live Sora text and need Sora installed.

svg/   (vector files: sharp at any size, use these first)
  icon-color.svg           The symbol for DARK backgrounds.
  icon-on-light.svg        The symbol for LIGHT backgrounds (the lime dot turns dark).
  icon-white.svg           One-color white symbol (photos, dark single-color print).
  icon-black.svg           One-color dark symbol (black-and-white print, stamps, fax).
  app-icon.svg             Rounded gradient tile with the white symbol.
  logo-full-dark-bg.svg    Symbol + "contract.ly" for dark backgrounds.
  logo-full-light-bg.svg   Symbol + "contract.ly" for light backgrounds.
                           These two use live text in the Sora font. Install Sora first
                           (free, fonts.google.com/specimen/Sora) or the text will appear in
                           a different font. Ask a designer to "convert text to outlines"
                           before sending these files to a printer or another company.

png/   (ready-to-use pictures with transparent backgrounds unless noted)
  icon-color-1024.png / -512.png       Symbol for dark backgrounds.
  icon-on-light-1024.png / -512.png    Symbol for light backgrounds.
  icon-white-1024.png, icon-black-1024.png   One-color symbols.
  app-icon-1024.png / -512.png         Rounded app icon.
  app-icon-square-1024.png             Full square, no rounded corners: upload this to
                                       Apple App Store / Google Play, which round it themselves.
  social-avatar-400.png                Profile picture for LinkedIn, X, Facebook, Slack.

favicon/   (website and phone home-screen icons)
  favicon.ico, favicon-16.png, favicon-32.png, favicon-48.png
  apple-touch-icon.png (180 px), android-chrome-192.png, android-chrome-512.png


HOW TO USE IT ON A WEBSITE
--------------------------
1. Copy the favicon/ files and svg/app-icon.svg to the root of your website.
2. Paste this inside the <head> of every page:

   <link rel="icon" href="/favicon.ico" sizes="any">
   <link rel="icon" type="image/svg+xml" href="/app-icon.svg">
   <link rel="apple-touch-icon" href="/apple-touch-icon.png">

3. Show the logo in your page header with the SVG that matches the header color:

   <img src="/logo-full-dark-bg.svg" alt="contract.ly" height="32">

Using Canva, Google Slides, PowerPoint or Word: insert the PNG files (icon-color or
icon-on-light). Use the SVG if the program accepts it.


WHICH FILE FOR WHICH BACKGROUND
-------------------------------
  Dark ink / navy / violet background  ->  icon-color  or  logo-full-dark-bg
  White / light grey background        ->  icon-on-light  or  logo-full-light-bg
  Photo or busy background             ->  icon-white (on dark photo) / icon-black (on light photo)
  Round or square profile picture      ->  social-avatar-400.png
  App icon                             ->  app-icon files
Never use the lime-dot version on white: the dot almost disappears.


COLORS
------
  Ink (main dark background)   #0E0C20
  Deep (cards on dark)         #1A1736
  Ink soft (dot on light)      #2B2650
  Violet                       #6B4DFF
  Pink                         #FF5C93
  Lime (accent / the dot)      #C8FF4D
  White                        #FFFFFF
  Ring gradient: top to bottom, Violet to Pink.


TYPE
----
  Wordmark: Sora Bold (700), all lowercase: contract.ly
  Letter spacing: -4% (tight). The dot is lime on dark and violet on light.
  Body text suggestion: Sora Regular for headings, Inter or system sans for long text.


SIZE AND SPACE
--------------
  Leave clear space around the logo equal to half the ring's height on every side.
  Smallest sizes: symbol 24 px wide on screen, full logo 110 px wide.
  Below 24 px (browser tabs, tiny icons) use the favicon files, which sit on a tile.


PLEASE DON'T
------------
  - Stretch, squash or rotate the logo.
  - Change the colors, add outlines, shadows or glows.
  - Put the colored symbol on a background close to violet or pink.
  - Redraw the symbol or retype the name in another font.
  - Use the dark-background files on light backgrounds (or the reverse).


FAVICONS WITH THE WORD
----------------------
3-app-icons-and-favicons/favicon-with-word/ has the full logo (symbol + "contract.ly") as wide PNGs
(32, 48, 64, 128, 256 px tall) and SVGs. Use them for wide placements: website header, email
signature, app title bar. Browser tabs show a tiny square, so the word becomes unreadable there;
keep favicon.ico (symbol only) for the tab.

ALL SVG FILES WITH THE WORD (1-FULL-LOGO-with-word/svg/)
  logo-full-dark-bg-outlined.svg     white word, for dark backgrounds
  logo-full-light-bg-outlined.svg    dark word, for light backgrounds
  logo-full-white-onecolor.svg       all white
  logo-full-black-onecolor.svg       all dark
