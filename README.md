# Keyphrase Generation (built on OpenNMT-py)

This is a repository providing code and datasets used in [One Size Does Not Fit All: Generating and Evaluating Variable Number of Keyphrases](https://arxiv.org/pdf/1810.05241.pdf) and [Does Order Matter? An Empirical Study on Generating Multiple Keyphrases as a Sequence](https://arxiv.org/pdf/1909.03590.pdf).

All datasets and checkpoints used in the papers can be downloaded [here](https://drive.google.com/open?id=1vK1lezjd1Hvhb4b3KWFwqkZg7YRUMa0s). Unzip the file `ckpts&data.zip` and override the original `data/` and `models/` folders. Note that the data points in KP20k have been manually cleaned.

## Quickstart

All the config files used for training and evaluation can be found in folder `config/`.
For more examples, you can refer to scripts placed in folder `script/`.


### Preprocess the data

```bash
python -config config/preprocess/config-preprocess-keyphrase-kp20k.yml
```

### Train a One2Seq model with Diversity Mechanisms enabled

```bash
python train.py -config config/train/config-rnn-keyphrase-one2seq-diverse.yml
```

### Train a One2One model

```bash
python train.py -config config/train/config-rnn-keyphrase-one2one-stackexchange.yml
```

### Run generation and evaluation 

```bash
python kp_gen_eval.py -tasks pred eval report -config config/test/config-test-keyphrase-one2seq.yml -data_dir data/keyphrase/meng17/ -ckpt_dir models/keyphrase/meng17-one2seq-kp20k-topmodels/ -output_dir output/meng17-one2seq-topbeam-selfterminating/meng17-one2many-beam10-maxlen40/ -testsets duc inspec semeval krapivin nus -gpu -1 --verbose --beam_size 10 --batch_size 32 --max_length 40 --onepass --beam_terminate topbeam --eval_topbeam
```


## Contributers
Major contributors are:
[Rui Meng](https://github.com/memray/) (University of Pittsburgh)
[Eric Yuan](https://github.com/xingdi-eric-yuan) (Microsoft Research, Montréal)
[Tong Wang](https://github.com/wangtong106) (Microsoft Research, Montréal)
[Khushboo Thaker](https://github.com/khushsi) (University of Pittsburgh)


## Citation

Please cite the following papers if you are interested in using our code and datasets.

```
@article{yuan2018onesizenotfit,
  title={One Size Does Not Fit All: Generating and Evaluating Variable Number of Keyphrases},
  author={Yuan, Xingdi and Wang, Tong and Meng, Rui and Thaker, Khushboo and He, Daqing and Trischler, Adam},
  journal={arXiv preprint arXiv:1810.05241},
  url={https://arxiv.org/pdf/1810.05241.pdf},
  year={2018}
}
```
```
@article{meng2019ordermatters,
  title={Does Order Matter? An Empirical Study on Generating Multiple Keyphrases as a Sequence},
  author={Meng, Rui and Yuan, Xingdi and Wang, Tong and Brusilovsky, Peter and Trischler, Adam and He, Daqing},
  journal={arXiv preprint arXiv:1909.03590},
  url={https://arxiv.org/pdf/1909.03590.pdf},
  year={2019}
}
```
```
@inproceedings{meng2017kpgen,
  title={Deep keyphrase generation},
  author={Meng, Rui and Zhao, Sanqiang and Han, Shuguang and He, Daqing and Brusilovsky, Peter and Chi, Yu},
  booktitle={Proceedings of the 55th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)},
  pages={582--592},
  url={https://arxiv.org/pdf/1704.06879.pdf},
  year={2017}
}
```
