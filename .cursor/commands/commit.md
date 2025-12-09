# Commit Changes

Review all uncommitted changes and create well-structured commits following the project's commit message guidelines.

## Instructions

1. **Review all changes**
   - Run `git status --short` to see modified files
   - Run `git diff --stat` for a summary of changes per file
   - Run `git diff` to understand the actual changes
   - Also check for untracked files that should be included

2. **Group changes logically**
   - Group by feature/purpose - changes serving the same goal belong together
   - Group by type - don't mix feat/fix/refactor/test in one commit
   - Group by scope - related files can share a commit
   - Keep separate: bug fixes vs features, refactoring vs functional changes, production vs test code

3. **For each logical group, create a commit**
   - Stage the related files with `git add`
   - Write a commit message following this format:
     ```
     [type]: [subject in imperative mood]
     
     Optional body with additional context when needed
     ```
   - Types: `feat`, `fix`, `refactor`, `perf`, `test`, `docs`, `style`, `chore`

4. **Commit message rules**
   - Be concise and direct
   - No emojis
   - Use imperative mood ("Add feature" not "Added feature")
   - Limit subject line to 72 characters
   - Explain the change, not the diff

5. **After each commit**
   - Run `git status --short` to confirm remaining changes
   - Run `git log --oneline -3` to verify the commit
   - Repeat until working directory is clean

## Examples

Good commit messages:
- `feat: Add password reset functionality`
- `fix: Prevent crash when user profile is incomplete`
- `refactor: Simplify authentication logic`
- `chore: Move export commands to appropriate app directories`

With body (when needed):
```
refactor: Restructure user authentication module

- Move validation logic to separate utility
- Extract token refresh into dedicated service
- Update error handling for better clarity
```

