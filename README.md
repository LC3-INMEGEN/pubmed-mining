# Pubmed-Mining

PubMed mining tools.

We shall provide this functionality:

- update local cache, a mongo document database, from a query to PubMed
- build mesh term networks from queries to mongodb, as networkX graphs, save them to python pickle files
- plot these networks using matplotlib
- plot these networks using d3
- convert these networks to CSV files

These functions shall have a command line interface and those scripts shall have PSU Galaxy wrappers.

## Use Cases

<img src="https://raw.githubusercontent.com/LC3-INMEGEN/pubmed-mining/master/modulos.png">


## Installation

We hope to share this tool online from our own Galaxy instance. In the
meantime you can roll your own and add our packages.

Follow [these
instructions](https://wiki.galaxyproject.org/Admin/GetGalaxy) to setup
your own galaxy.

Checkout this repo:

    git checkout https://github.com/LC3-INMEGEN/pubmed-mining.git

After you have installed your own Galaxy instance, make a clone of our
repo:

    git clone https://github.com/LC3-INMEGEN/pubmed-mining.git

Move to the Galaxy Tools directory:

    cd galaxy/tools/

Create a symbolic link to the repo clone:

    ln -s ../../pubmed-mining/ .

Move back to the Galaxy directory:

    cd ..

Move to the config directory:

    cd config/

Create a symbolic link to the tool configuration file on the repo,
this will let our tools to be available on your local Galaxy instance:

    ln -s ../../pubmed-mining/pubmedmining_tools.xml .

