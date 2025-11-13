# Releasing the ea


```shell
cldfbench makecldf cldfbench_sccs.py --with-zenodo --with-cldfreadme --glottolog-version v5.2
pytest
```

```shell
cldfbench cldfviz.map cldf --pacific-centered --format png --width 20 --output map.png --with-ocean
```

```shell
cldfbench readme cldfbench_sccs.py
cldfbench zenodo --communities dplace cldfbench_sccs.py
dplace check cldfbench_sccs.py
```

```shell
git status
git tag
```

Adapt CHANGELOG.md.
Add, commit and push all changes.

```shell
dplace release cldfbench_sccs.py vX.Y
```