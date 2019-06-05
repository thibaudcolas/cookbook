# Targets

> Reusable targets and target definition methdologies, for digital projects.

## Browser & device support

> Browser & device support is informed by Web Analytics (GA) on the existing site and on competition benchmark sites.

**Supported browser / device versions:**

| Browser       | Device/OS  | Version |
| ------------- | ---------- | ------- |
| Mobile Safari | iOS Phone  | latest  |
| Mobile Safari | iOS Tablet | latest  |
| Chrome        | Android    | latest  |
| Chrome        | Desktop    | latest  |
| Firefox       | Desktop    | latest  |
| MS Edge       | Windows    | latest  |
| IE            | Windows    | 11      |
| Safari        | macOS      | latest  |

> Those browser / device / version combinations are the ones the site _is tested_ on. Our development standards ensure that the site is usable on other browsers **and will work on future browsers**.

### No-JS users

Only use JavaScript if necessary. If JS is the only way for a feature to work, add a ["please enable JavaScript"](https://www.enable-javascript.com/) message in a `<noscript>` tag to make it possible for end users to understand what to do.

## Accessibility targets

The standard we aim for is [WCAG2.1](https://www.w3.org/TR/WCAG21/), AA level. Here are
specific assistive technologies we aim to test for, and ultimately support:

| Type          | Assistive technology                                                                                |
| ------------- | --------------------------------------------------------------------------------------------------- |
| Screen reader | [NVDA](https://www.nvaccess.org/download/) on Windows with Firefox ESR                              |
| Screen reader | [VoiceOver](https://support.apple.com/en-gb/guide/voiceover-guide/welcome/web) on macOS with Safari |
| Magnification | [Windows Magnifier](https://support.microsoft.com/en-gb/help/11542/windows-use-magnifier)           |
| Magnification | macOS Zoom                                                                                          |
| Voice control | Windows Speech Recognition                                                                          |
| Voice control | macOS Dictation                                                                                     |
| Screen reader | Mobile [VoiceOver](https://support.apple.com/en-gb/guide/voiceover-guide/welcome/web) on iOS        |
