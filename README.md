# scan-posts
# 環境構築
## MeCab のインストール
```sh
git clone https://github.com/taku910/mecab.git

cd mecab/mecab
./configure  --enable-utf8-only
make
make check
sudo make install

cd ../mecab-ipadic
./configure --with-charset=utf8
sudo ldconfig
make
sudo make install
```
