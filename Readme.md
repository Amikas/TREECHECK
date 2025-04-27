
---

# TREECHECK

Checks if a binary search tree (BST) from a file is an AVL tree and optionally searches subtrees.

## How to Run

1. Open a terminal in this folder.
2. Run:
   ```
   treecheck.exe <treefile> [subtreefile]
   ```

## Input Files

- One integer per line.
- Filenames **without** `.txt` extension are also accepted.

## Behavior

- With one file: build tree, print balance factors, min, max, average, AVL status.
- With two files:
  - If subtree file has one key: simple search with path output.
  - If subtree file has multiple keys: subtree structure search.

## Output Example

- Balance factors per node.
- Smallest key, largest key, average value.
- AVL check: `AVL: yes` or `AVL: no`.
- Search results: key path or subtree found/not found.

