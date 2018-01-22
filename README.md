# keras-oneshot
![oneshot task](images/task_25.png)
[koch et al, Siamese Networks for one-shot learning,](https://www.cs.cmu.edu/~rsalakhu/papers/oneshot1.pdf)  (mostly) reimplimented in keras. 
Trains on the [Omniglot dataset]( https://github.com/brendenlake/omniglot).

Also check out my [blog post](https://sorenbouma.github.io/blog/oneshot) about this paper and one shot learning in general!



## Installation Instructions
To run, you'll first have to clone this repo and install the dependencies

```bash
git clone https://github.com/sorenbouma/keras-oneshot
cd keras-oneshot
sudo pip install -r requirements.txt

```

Then you'll need to download the omniglot dataset and preprocess/pickle it with the load_data.py script.
```bash
git clone https://github.com/brendenlake/omniglot
python load_data.py --path <PATH TO THIS FOLDER>
```
omniglot放在keras-oneshot資料夾中 : python load_data.py --path ~/keras-oneshot


若出現cannot import name imread: sudo pip install Pillow==2.6.0

Then you can run the jupyter notebook:
```bash
jupyter notebook
```

run on python3 讀檔時 若出現 'ascii' codec can't decode byte
use (X,c) = pickle.load(f , encoding='bytes')
https://stackoverflow.com/questions/46046752/python-3-unicodedecodeerror-ascii-codec-cant-decode-byte-0xe2-in-position-0
