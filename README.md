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

After you have installed your own Galaxy instance, clone this repo and
install the tools:

    git clone https://github.com/LC3-INMEGEN/pubmed-mining.git
    cd galaxy/tools/
    ln -s ../../pubmed-mining/ .
    cd ..
    cd galaxy/config/
    ln -s ../../pubmed-mining/pubmedmining_tools.xml .

