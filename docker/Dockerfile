#
FROM bgruening/galaxy-stable

MAINTAINER Eduardo Rueda <eruedacartin@hotmail.com>

RUN git clone https://github.com/LC3-INMEGEN/pubmed-mining.git

WORKDIR /galaxy/tools
RUN ln -s ../../pubmed-mining/ .
WORKDIR /galaxy/config
RUN ln -s ../../pubmed-mining/pubmedmining_tools.xml .
RUN rm -Rf galaxy.ini
RUN ln -s ../../pubmed-mining/galaxy.ini .
WORKDIR /galaxy

#RUN pip install virtualenv

#RUN virtualenv .venv

#RUN python .venv/bin/activate_this.py

RUN sudo apt-get update
RUN sudo apt-get install -y libncurses5-dev
RUN sudo apt-get install -y libfreetype6-dev

RUN sudo pip install biopython==1.65
RUN sudo pip install networkx==1.9.1
RUN sudo pip install numpy==1.9.2
RUN sudo pip install pymongo==3.0.2
RUN sudo pip install backports.ssl-match-hostname==3.4.0.2
RUN sudo pip install certifi==2015.4.28
RUN sudo pip install functools32
RUN sudo pip install jsonschema==2.5.1
RUN sudo pip install pytz==2015.4
RUN sudo pip install tornado==4.2
RUN sudo pip install six==1.9.0
RUN sudo pip install python-dateutil==2.4.2
RUN sudo pip install pandas==0.16.2
RUN sudo pip install scipy==0.15.1
RUN sudo pip install pyparsing==2.0.3
RUN sudo pip install nose==1.3.7
RUN sudo pip install mock==1.0.1
RUN sudo pip install matplotlib==1.4.3
RUN sudo pip install seaborn==0.6.0
RUN sudo pip install sympy==0.7.6
RUN sudo pip install gnureadline==6.3.3
RUN sudo pip install ipython==3.2.0
RUN sudo pip install Pillow==2.9.0
RUN sudo pip install scikit-image==0.11.3
RUN sudo pip install scikit-learn==0.16.1
RUN sudo pip install pyzmq==14.7.0
RUN sudo pip install pylab==0.1.3

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy)
EXPOSE :80
EXPOSE :21
EXPOSE :8800

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]


