# Wheel of Jeopardy!
## JHU Course: 605.601.83 Summer

### Instructions for code setup

1. Do not run `git init`. Run `git clone https://github.com/JHUOrg/JHU-course-60560183`. `git clone` will ensure your local repository is tracking with the remote.
2. Run `git pull`. This will update your local repository with changes from the remote. `git pull` should be used every day you interact with a repository with a remote, at the minimum. 
3. Create a new branch for your work by running `git branch <new-branch-name>`
4. Switch to the newly created branch by running `git switch <new-branch-name>`
5. Run `git status` for peace of mind - this will show any locally changed files that are not yet tracked or committed. There should not be any at this point (maybe a `.DS_Store` file in some cases, and that's okay)
6. Start coding!

## Code structure

```
JHU-course-60560183                 --> Base
└── jhucourse                       --> Actual Module
    ├── woj             
    │   ├── backend                 --> Package
    │   ├── frontend                --> Package
    │   │   ├── wheelsubsystem.py   --> Module
    │   ├── logging                 --> Package
    │   │   ├── centrallogging.py   --> Module
    │   ├── staticconfigurations    --> Package
    │   │   ├── wheelsectorsstore.json
    │   ├── tests
└── main.py
└── DesignDoc
```

## Style guide
We will use [PEP 8 Style Guide](https://peps.python.org/pep-0008/#introduction). Using an IDE like PyCharm will provide idiomatic expressions as suggestions along the way.
Also, some idiomatic expression follow the [Zen of Python](https://peps.python.org/pep-0020/)
