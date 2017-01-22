# Stylishy

Repository for [Stylishly](http://stylishly.us/) REST API.


## Table of Contents

- [Contributing](#contributing)
- [Setup your environment](#setup-your-environment)
- [Setup your database](#setup-your-database)


## Setup your environment:

Create a dedictated `Stylishly` directory and `cd` into it:

```sh
$ mkdir stylishly && cd stylishly
```

Create a [virtualenv](https://docs.python.org/3/library/venv.html):

```sh
$ python3.6 -m venv ./env
$ source ./env/bin/activate
```

You can set your environment variables in the virtual environment `activate` script file, so they get loaded upon activation:

#### Example:

```sh
$ open ./env/bin/activate
```

In the `activate` script file:

```sh
# This file must be used with "source bin/activate" *from bash*
...

export ENV_VAR=VALUE

...
```

Clone this repository and `cd` into it:

```sh
$ git clone git@github.com:lezoudali/stylishly-api.git && cd stylishly-api
```

Install python dependencies:

```sh
$ pip install -r requirements.txt
```

## Setup your database

Install [PostgreSQL](https://www.postgresql.org/). You can achieve this with [homebrew](http://brew.sh/):

```sh
$ brew install postgresql
```

Start `PostgreSQL` once it's been installed:

```
$ psql
```

In the `PostgreSQL` command prompt, create your development database, connect to it and create the `uuid-ossp` extension:

```
postgres=# CREATE DATABASE stylishly-dev;

postgres=# \c stylishly-dev;

postgres=# CREATE EXTENSION "uuid-ossp";
```

Be sure to set the following enviroment variables:

```sh
export STYLISHLY_DB_DATABASE="stylishly-dev"
```

If your PostgreSQL database requires a username and password, then set the following variables:


```sh
export STYLISHLY_DB_USERNAME=<username>
export STYLISHLY_DB_PASSWORD=<password>
```

## Contributing

1. Checkout `dev` branch: `git checkout dev`.
2. Pull the latest state of the `dev` branch on the remote: `git pull origin dev`.
3. Create your bugfix or feature branch: `git checkout -b feature/my-cool-feature` or `git checkout -b bug/wrong-validation-logic`.
4. Push your branch to the remote: `git push -u origin feature/my-cool-feature`.
5. Open a pull request from your branch to `dev` branch. Later when it's ready for review, comment there and ask for code review.
6. Work on your branch, make commits (and pushes if you want).
7. When you're done you can have a lot of commits with some weird messages where you just commit intermediate state of your progress. So sometimes it's good practice to squash them.
Say you worked on your branch and created 5 commits.
Then just do `git rebase -i HEAD~5`.
The default editor (for example I have vim as default) will open a list of commits. leave `pick` for first and replace `pick` with `squash` for others. Then save and quit the editor (`:wq` in vim).
After this, another editor will open to edit the commit message. Make sure your commit messages describe the changes you've done and also the tricky points. This is very important for history.
8. If you did squash, push your branch using `git push -f`.
9. Now you can comment in your pull request something like `Ready for code review`. Or `@username seems it's done. Could you please review?`
10. If reviewer asked to apply some changes, the commits with fixes in most cases should be squashed as well before merge.
11. When reviewer said that you can merge, squash and merge. Then delete your working branch on the remote.
Also pull `dev` from remote and remove your local working branch that's already merged into `dev`.
