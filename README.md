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

After you have installed your own Galaxy instance, make a clone of our
repo:

    git clone https://github.com/LC3-INMEGEN/pubmed-mining.git

Move to the Galaxy Tools directory:

    cd galaxy/tools/

Asuming you cloned our repo at the same level, create a symbolic link to the repo clone:

    ln -s ../../pubmed-mining/ .

Move to the config directory:

    cd ../config/

Create a symbolic link to the tool configuration file on the repo,
this will let our tools to be available on your local Galaxy instance:

    ln -s ../../pubmed-mining/pubmedmining_tools.xml .

Delete the original galaxy config file:

    rm -Rf galaxy.ini

Create a symbolic link to the galaxy conifg file on the repo:

    ln -s ../../pubmed-mining/galaxy.ini .

Now go back to the Galaxy directory:

    cd ..

Create a virtual environment there:

    virtualenv .venv

Activate it

    source .venv/bin/activate

Install the biopython, networkx, numpy and pymongo packages:

    pip install -r ~/pubmed-mining/requirements.txt
    
Our tools should be available now for you to run on your local Galaxy
instance, you should probably restart it.

##Galaxy Docker Image

https://github.com/bgruening/docker-galaxy-stable
