FROM google/cloud-sdk:slim

COPY requirements.txt /home/

RUN pip install -r /home/requirements.txt

COPY ./pyscripts /home/pyscripts/
RUN chmod 777 -R /home/pyscripts/

VOLUME ["/root/.config"]
CMD [ "/bin/bash" ]
