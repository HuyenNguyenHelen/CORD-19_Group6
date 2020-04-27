import pip

import logging
from ptm.nltk_corpus import get_reuters_token_list_by_sentence
from ptm import HMM_LDA
from ptm.utils import get_top_words

logger = logging.getLogger('HMM_LDA')
logger.propagate=False

n_docs = 1000
voca, corpus = get_reuters_token_list_by_sentence(num_doc=n_docs)
print('Vocabulary size', len(voca))

n_docs = len(corpus)
n_voca = len(voca)
n_topic = 50
n_class = 20
max_iter = 100
alpha = 0.1
beta = 0.01
gamma = 0.1
eta = 0.1
model = HMM_LDA(n_docs, n_voca, n_topic, n_class, alpha=alpha, beta=beta, gamma=gamma, eta=eta, verbose=False)
model.fit(corpus, max_iter=max_iter)


for ti in range(n_topic):
    top_words = get_top_words(model.TW, voca, ti, n_words=10)
    print('Topic', ti ,': ', ','.join(top_words))