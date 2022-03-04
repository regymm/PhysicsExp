FROM python:3.7
RUN pip3 install \
		jupyterhub \
		notebook \
		physicsexp \
		docx
RUN useradd -d /home/riemann -m riemann
RUN mkdir /home/riemann/shared
ENV HOME=/home/riemann
WORKDIR $HOME
USER riemann

# these two copies repository regymm/physicsexp and regymm/USTCPhysExpData into container
# customize as your need!
COPY ./resources /home/riemann/
COPY ./example /home/riemann/

# fix chinese font display problem: you should download simhei.tff yourself
COPY ./simhei.ttf /usr/share/fonts
RUN fc-cache -fv


CMD ["jupyterhub-singleuser"]

