import pandas as pd
import os
import progressbar
import multiprocessing as mp
from datetime import datetime as dt
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
import multiprocessing as mp
import warnings

question = pd.read_csv("/home/alvi/Documents/projects/DeCaf/data/train_data/questions.csv")
answer = pd.read_csv("/home/alvi/Documents/projects/DeCaf/data/train_data/answers.csv")
comment = pd.read_csv("/home/alvi/Documents/projects/DeCaf/data/train_data/comments.csv")

warnings.simplefilter("ignore")

so_model = KeyedVectors.load_word2vec_format("/home/alvi/Documents/projects/DeCaf/models/pre_trained/so.bin", binary=True)

def so_inject(infile, outfile):
  if not os.path.exists(outfile):
    with open(outfile, "w+") as f:
      f.write("text,label\n")
      f.close()

  so_injected = pd.read_csv(outfile)
  done_rows = so_injected.shape[0] - 1
  pbar = progressbar.ProgressBar(max_value=infile.shape[0])
  for index, rec in infile.iterrows():
    pbar.update(index)
    if index > done_rows:
      words = rec[0].split(" ")
      for i in range(len(words)):
        words_to_inject = [words[i]]
        try:
          similar_words = so_model.most_similar(words[i])
          for similar_tuple in similar_words:
            if similar_tuple[1] > 0.5:
              words_to_inject.append(similar_tuple[0])
          words[i] = " ".join(words_to_inject)
        except:
          continue
      injected_sentence = " ".join(words)
      row = injected_sentence + "," + str(rec[1]) + "\n"
      with open(outfile, "a") as f:
        f.write(row)
        
infiles = [
           question,
           answer,
           comment
]

outfiles = [
              "/home/alvi/Documents/projects/DeCaf/data/train_data/question_so_injected.csv",
              "/home/alvi/Documents/projects/DeCaf/data/train_data/answer_so_injected.csv",
              "/home/alvi/Documents/projects/DeCaf/data/train_data/comment_so_injected.csv"            
]

jobs = []
for index, infile in enumerate(infiles):
  print("SO injecting: ", outfiles[index])
  p = mp.Process(target=so_inject, args=(infile, outfiles[index]))
  jobs.append(p)
  p.start()

for proc in jobs:
  proc.join()
