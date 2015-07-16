#
FROM bgruening/galaxy-stable

MAINTAINER Eduardo Rueda <eruedacartin@hotmail.com>

RUN git clone https://github.com/LC3-INMEGEN/pubmed-mining.git

WORKDIR /galaxy/tools
RUN ln -s ../../pubmed-mining/ .
WORKDIR /galaxy/config
RUN ln -s ../../pubmed-mining/pubmedmining_tools.xml .
RUN tool_config_file = config/tool_conf.xml.sample,config/pubmedmining_tools.xml
WORKDIR /galaxy

#ENV .venv

#RUN source .venv/bin/activate

RUN pip install -r ~/pubmed-mining/requirements.txt

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy)
EXPOSE :80
EXPOSE :21
EXPOSE :8800

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]


