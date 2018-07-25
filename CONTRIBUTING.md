# Contribution guidelines

## Branching

Create your own branches from `master` and use a descriptive prefix:

```sh
# For bug fixes, ideally finishing with the ticket number.
fix/<branch name>-<ticket number>
# For features, as well finishing with the ticket number if there is one.
feature/<branch name>-<ticket number>
# For general non-functional improvements (eg. developer tooling, CI)
chore/<branch name>-<ticket number>
```

When you're done with your work, create a pull request and find another teammate to review the changes.

## Code reviews

We do code reviews to ensure our work is of good quality, and to share knowledge. Reviews come in all shapes and sizes – from thorough point-by-point pull request reviews in GitLab to simple discussion of the proposed changes.

### Why we review each other’s work

- Improve the overall quality of the work.
- Enforce and propagate our standards of quality, best practices, work methodologies, and coding styles.
- Share the responsibility and knowledge for any given piece of work.
- Learn from each other’s approaches and skillsets.

> Want to know more? Go have a look at [Code Reviews: Just Do It](https://blog.codinghorror.com/code-reviews-just-do-it/) from Jeff Atwood.

### Guidelines for code reviews

When presenting code for review, or reviewing code, follow these guidelines:

- Try to make the review beneficial for both reviewee and reviewer.
- Give enough information to the reviewer so they know where to start.
- Think about the bigger picture.
- Concentrate on the intention rather than the syntax – stylistic issues should be taken care of by your linter.
- Reviews do not need to focus on the negative - if a piece of code is good, it is worth stating as well.

### Code reviews in practice

We use GitLab’s [Merge Requests](https://docs.gitlab.com/ee/user/project/merge_requests/) feature or GitHub’s [Pull Requests](https://help.github.com/articles/requesting-a-pull-request-review/) for most of our work, and do code reviews there with **Merge request approvals / Pull request reviews**. You will use this on a daily basis, take some time to learn how best to leverage those tools.

---

### Useful resources to go further

If you want to invest in figuring out the best guidelines and workflow for your team, here are useful resources to look at so you can have more informed conversations about your particular situation.

- [Code Reviews: Just Do It](https://blog.codinghorror.com/code-reviews-just-do-it/) by Jeff Atwood, my absolute favorite
- The Flutter project has good [code review guidelines](https://flutter.io/design-principles/). I particularly like how they talk about the benefits of code reviews.
- Karumi has really nice pull request guidelines and templates as part of their [project quality assurance guidelines](https://github.com/Karumi/project-quality-assurance).
- Michael Lynch’s two-part article on [doing code reviews like a human](https://mtlynch.io/human-code-reviews-1/) is also well worth a read.
