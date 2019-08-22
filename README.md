# Cookbook [![Build Status](https://travis-ci.org/thibaudcolas/cookbook.svg?branch=master)](https://travis-ci.org/thibaudcolas/cookbook)

> Recipes and best practices for awesome digital teams

```txt
      __...--~~~~~-._   _.-~~~~~--...__
    //   Vorsprung   `V'    Pauca      \\
   //   durch Technik |     sed bona    \\
  //__...--~~~~~~-._  |  _.-~~~~~~--...__\\
 //__.....----~~~~._\ | /_.~~~~----.....__\\
====================\\|//====================
                    `---`
```

## What is this

This repository contains all of the recipes, guidelines, templates, documentation you can reuse to cook a delicious digital project. Think of it as a reference of practices to use when working as a team; a starting point to define your own team’s practices.

This cookbook is about helping **teams** succeed first and foremost, projects being successful is only a consequence. **It defines where we want to be**, not necessarily where we always are. It is meant to apply to **all teams, and all team members** – we are knowledge workers first and foremost, our most important role is to successfully think, organise, and share knowledge. Code, designs, plans are only specific artifacts.

## Contents

- **Guidelines**
  - Contribution guidelines: [`CONTRIBUTING.md`](CONTRIBUTING.md)
    - Covers basic project setup, branching, and code reviews.
  - Pull request template: [`.github/PULL_REQUEST_TEMPLATE.md`](.github/PULL_REQUEST_TEMPLATE.md), for [GitHub PRs](https://help.github.com/articles/creating-a-pull-request-template-for-your-repository/) and [GitLab MRs](https://docs.gitlab.com/ce/user/project/description_templates.html#creating-merge-request-templates).
  - Issue templates: [`.github/ISSUE_TEMPLATE/](.github/ISSUE_TEMPLATE/).
  - Security policy: [`docs/SECURITY.md`](docs/SECURITY.md)
  - Support information: [`docs/SUPPORT.md`](docs/SUPPORT.md)
  - Code of conduct: [`docs/CODE_OF_CONDUCT.md`](docs/CODE_OF_CONDUCT.md)
- **Tooling**
  - [EditorConfig](http://editorconfig.org/) configuration: [`.editorconfig`](.editorconfig)
  - [nvm](https://github.com/creationix/nvm) configuration: [`.nvmrc`](.nvmrc)
  - [`.gitignore`](.gitignore)
  - [Git hooks](https://git-scm.com/book/gr/v2/Customizing-Git-Git-Hooks) for various scenarios: [`.githooks`](.githooks)
  - [Prettier](https://prettier.io/) configuration: [`prettier.config.js`](prettier.config.js), and integration via [npm scripts](package.json) and [git hooks](.githooks)
  - [commitlint](https://github.com/marionebl/commitlint) configuration: [`commitlint.config.js`](commitlint.config.js), and integration via [npm scripts](package.json) and [git hooks](.githooks)
- **Documentation**
  - [Browser support targets](docs/targets.md#browser-support)
  - [Accessibility targets](docs/targets.md#accessibility-targets)

## Contributing

Contributions are always welcome! Please read the [contribution guidelines](CONTRIBUTING.md) first.

### Install

> Clone the project on your computer, and install [Node](https://nodejs.org). This project also uses [nvm](https://github.com/creationix/nvm).

```sh
# Use the correct Node version.
nvm install
# Then, install all project dependencies.
npm install
```

### Working on the project

> Everything mentioned in the installation process should already be done.

```sh
# Make sure you use the right node version.
nvm use
# Lint all of the files in the project.
npm run lint
# Re-formats all of the files in the project (with Prettier).
npm run format
# View other available commands with:
npm run
```

## License

[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, [Thibaud Colas](https://github.com/thibaudcolas) has waived all copyright and related or neighboring rights to this work.
