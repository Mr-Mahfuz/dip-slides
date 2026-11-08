# DIP Study Room

Open `index.html` (or `dip_mastery_guide.html`) in a browser. No installation or internet connection is needed. Original lecture images and PDFs should stay beside the HTML files.

The 24 beginner lessons total a suggested 120 minutes. They include worked examples, recall prompts, interactive frequency responses, the lecture's 7×7 numerical grid, a formula review, and a 12-question self-test. Studied lessons, review flags, reading preferences, first-attempt quiz answers, and the optional timer are saved in this browser's local storage. Progress may differ between file URLs and a hosted copy.

Use Reading for paper, light, or dark colour schemes and three text sizes. On smaller screens, the optional study timer is also inside Reading. Use Original slides to inspect all 112 lecture pages. Arrow keys move between lessons when focus is outside a control; `/` opens lesson search. Browser Back and Forward follow lesson navigation.

## Edit and rebuild

- `study_data.py`: content, worked examples, lesson timing, quiz answers.
- `study_shell.html`: accessible page structure.
- `study.css`: responsive layout and reading themes.
- `study.js`: navigation, progress, labs, quiz, reference viewer, timer.

Run `python build_mobile.py` to rebuild both identical HTML entry points using `build_study.py`. Styles, scripts, and lesson content are embedded in each output. The old `slides_def.py` remains as the earlier content source for reference; it no longer drives the build.

## Content conventions

The forward DFT is unnormalised; the inverse includes `1/(MN)`. Ideal cutoff boundary values are stated explicitly. Contraharmonic examples specify Q and handle zeros explicitly; calculated filter values are estimates rather than guaranteed exact restorations. Native HTML math notation avoids external font or MathJax loading.
