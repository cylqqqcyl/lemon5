#! bin/bash

curl -O -J -L 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE'

tar zxfv mecab-0.996.tar.gz
cd mecab-0.996

./configure
make && make check
sudo make install