const { danger, message, warn, fail, schedule } = require("danger");
const isLocal = !danger.github;

if (!isLocal) {
  const hasLabels = danger.github.issue.labels.length !== 0;
  const isEnhancement =
    danger.github.issue.labels.some((l) => l.name === "enhancement") ||
    danger.github.pr.title.includes("feature");
  const isBug =
    danger.github.issue.labels.some((l) => l.name === "bug") ||
    danger.github.pr.title.includes("fix") ||
    danger.github.pr.title.includes("bug");

  if (!hasLabels) {
    message("What labels should we add to this PR?");
  }

  // Fails if the description is too short.
  if (!danger.github.pr.body || danger.github.pr.body.length < 10) {
    fail(":grey_question: This pull request needs a description.");
  }

  // Warns if the PR title contains [WIP]
  const isWIP = danger.github.pr.title.includes("WIP");
  if (isWIP) {
    const title = ":construction_worker: Work In Progress";
    const idea = "This PR is marked as WIP, and may not be ready yet.";
    warn(`${title} - <i>${idea}</i>`);
  }
}

const hasPackageChanges = danger.git.modified_files.includes("package.json");
const hasLockfileChanges = danger.git.modified_files.includes(
  "package-lock.json",
);

if (hasPackageChanges && !hasLockfileChanges) {
  warn("There are package.json changes with no corresponding lockfile changes");
}

const linkDep = (dep) =>
  danger.utils.href(`https://www.npmjs.com/package/${dep}`, dep);

schedule(async () => {
  const packageDiff = await danger.git.JSONDiffForFile("package.json");

  if (packageDiff.dependencies) {
    const added = packageDiff.dependencies.added;
    const removed = packageDiff.dependencies.removed;

    if (added.length) {
      const deps = danger.utils.sentence(added.map((d) => linkDep(d)));
      message(`Adding new dependencies: ${deps}`);
    }

    if (removed.length) {
      const deps = danger.utils.sentence(removed.map((d) => linkDep(d)));
      message(`:tada:, removing dependencies: ${deps}`);
    }
  }

  if (packageDiff.devDependencies) {
    const added = packageDiff.devDependencies.added;
    const removed = packageDiff.devDependencies.removed;

    if (added.length) {
      const deps = danger.utils.sentence(added.map((d) => linkDep(d)));
      message(`Adding new devDependencies: ${deps}`);
    }

    if (removed.length) {
      const deps = danger.utils.sentence(removed.map((d) => linkDep(d)));
      message(`:tada:, removing devDependencies: ${deps}`);
    }
  }
});
