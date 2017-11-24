import sys
import MeCab
text = "今日は１９９５年5月8日。僕が生まれた日だ。今１時９分。明後日にドッジボールのイベントがある。ブルゾンちえみ "
m = MeCab.Tagger ('-d /usr/local/lib/mecab/dic/ipadic')
print(m.parse (text))

m2 = MeCab.Tagger(' -d /usr/local/lib/mecab/dic/mecab-ipadic-neologd')
print(m2.parse(text))
