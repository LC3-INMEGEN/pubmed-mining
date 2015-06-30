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

Now you have to open the galaxy.ini file:

    open galaxy.ini

Then add the following line (in galaxy.ini):

    tool_config_file = config/tool_conf.xml.sample,config/pubmedmining_tools.xml

Then save the galaxy.ini file.

Now go back to the Galaxy directory:

    cd ..

Activate the virtual environment .venv:

    source .venv/bin/activate

Install the following packages:

For biopython:

    pip install biopython

For networkx:

    pip install networkx

For numpy:

    pip install numpy

For pymongo:

    pip install pymongo
    
Our tools should be available now for you to run on your local Galaxy instance.
