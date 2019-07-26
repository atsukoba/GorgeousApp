import logging
import re
import os
import shutil
from logging import getLogger

import MeCab
import wikipedia
from Levenshtein import distance as D
from pykakasi import kakasi


logging.basicConfig(level=logging.INFO)
log = getLogger(__name__)


class Gorgeous:
    """
    君のハートに、レボ☆リューション

    gorgeous = Gorgeous()
    gorgeous.revolution("まだ助かる")

    >>> マダガスカル
    """
    def __init__(self, **kwargs) -> None:
        k = kakasi()
        k.setMode('K', 'a')
        self.conv = k.getConverter()
        self.tagger = MeCab.Tagger()
        self.nations = self.read_nations(**kwargs)
        self.nations_roman = [
            self.romanize(nation) for nation in self.nations]
        self.nations_roman_vowel = [self.extract_vowel(
            self.romanize(nation)) for nation in self.nations]
        self.recent_answer = ""
        return

    def read_nations(self, fname="data/nations.csv", **kwargs) -> list:
        """
        Read csv file 
        published on 『国コード一覧CSV ISO 3166-1』
        https://qiita.com/tao_s/items/32b90a2751bfbdd585ea
        """
        assert os.path.exists(fname), f"{fname} is not found"
        with open(fname, "r") as f:
            nations = f.read().split("\n")

        nations = [re.split("[,|]", nation)[0].replace("\"", "") for nation in nations]
        nations.pop(0)
        return nations

    def read_csv_data(self, filepath, **kwargs) -> list:
        with open(filepath, "r") as f:
            data = f.read().split("\n")
        data = [re.split("[,|]", area)[0].replace("\"", "") for area in data]
        data.pop(0)
        return data

    def clean_str(self, s: str) -> str:
        return re.sub(r'[*\s\t\n.,]', "", s)

    def katakanize(self, s: str, morph=False, **kwargs) -> str:
        """
        convert "kanji" to "katakana"
        """
        morphed = [re.split(r"[,\t\s\n]", w) for w in self.tagger.parse(s).split("\n")]
        morphed.remove([""])
        morphed.remove(["EOS"])
        
        k = [morph[-1] if morph[-1] != "*" else morph[0] for morph in morphed]

        if morph:  # morphlogical analysed output
            return k

        return "".join(k)

    def romanize(self, s, **kwargs) -> list:
        """
        convert "katakana" to "romaji" via kakasi
        (kanji - kana simple inverter)
        """
        s = self.katakanize(s, **kwargs)
        if type(s) == str:
            s = [s]
        return [self.conv.do(w) for w in s]

    def extract_vowel(self, word: str, **kwargs) -> str:
        """
        extract vowels from romanized words
        """
        if type(word) == list:
            return [self.extract_vowel(w) for w in word]

        return "".join([l for l in word if l in ["a", "i", "u", "e", "o", "n"]])

    def revolution(self, sentence: str, app_use=False ,**kwargs):
        """
        Revolution: Get Similar Nation Name from Word

            gorgeous.revolution("まだ助かる")
            >>> マダガスカル

        args
        ----
        n_result : default=5 : lines of result print
        vowel : default=False : if true, word-distance will be calculated based on vowels
        app_use : default=False, if true, returns value of dict with some info
        """

        # default kargs
        n_result = kwargs.get('n_result', 3)
        vowel = kwargs.get('vowel', False)

        answer = dict()

        log.info(f"INPUT: {sentence}")
        answer["input"] = sentence
        # sentence -> [words] -> [katakana] -> [roman]
        word_roman = self.romanize(sentence, **kwargs)
        log.info(f"ROMAN: {word_roman}")
        answer["roman"] = word_roman

        if vowel:
            word_vowel = self.extract_vowel(word_roman)
            log.info(f"VOWEL: {word_vowel}")
            answer["vowel"] = word_vowel
            dists = [D(word_vowel[-1], nation[0]) for nation in self.nations_roman_vowel]
        else:
            dists = [D(word_roman[-1], nation[0]) for nation in self.nations_roman]
            answer["vowel"] = ""
        idx = sorted(range(len(dists)), key=lambda k: dists[k])

        # logging
        log.info("RESULT:")
        answer["results"] = []
        for i in range(n_result):
            if vowel:
                msg = f"No.{i+1} : {self.nations[idx[i]]} ({self.nations_roman_vowel[idx[i]]}) : ({dists[idx[i]]})"
                log.info("\t" + msg)
                answer["results"].append(msg)
            else:
                msg = f"No.{i+1} : {self.nations[idx[i]]} ({self.nations_roman[idx[i]]}) : ({dists[idx[i]]})"
                log.info("\t" + msg)
                answer["results"].append(msg)
        self.recent_answer = self.nations[idx[0]]
        answer["result"] = self.nations[idx[0]]

        # Get meta info
        map_url = self.googlemap()
        log.info(f"ここ！({map_url})")
        answer["map"] = map_url
        print("-" * shutil.get_terminal_size()[0])  # draw line
        
        wiki = self.wikipedia()
        log.info(f"{wiki[1]}！！\n")
        _, answer["wiki_summary"], answer["wiki_url"] = wiki
        print(u"☆" * shutil.get_terminal_size()[0])  # draw line

        # Answer
        if app_use:  # returns dict value
            return answer
        return self.recent_answer

    def googlemap(self, place=None) -> str:
        """generate Google Map Link"""
        if place is None:
            place = self.recent_answer
        return f"https://www.google.com/maps/search/{place}/"

    def wikipedia(self, place=None) -> tuple:
        """Generate Wikipedia Link"""
        if place is None:
            place = self.recent_answer
        wikipedia.set_lang("ja")
        p = wikipedia.page(wikipedia.search(place)[0])
        return (p.title, p.summary, p.url)

    def showtime(self, **kwargs) -> None:
        print("【ゴー☆ジャスのショータイム！】")
        print(f"\n- 【お題】を入力してくれよな！\n- ランキングを{kwargs.get('n_result', 3)}件表示するぞ！\n- 地球義ではなく、GoogleMapとWikipediaの情報を出力するぞ！")
        print(u"☆" * shutil.get_terminal_size()[0])  # draw line
        while True:
            place = input("\n【お題】を入力: ")
            if place in ["終了", "end", "終わり"]:
                break
            self.revolution(place, **kwargs)
        print("また遊んでくれよな！")
        return


if __name__ == "__main__":

    import argparse

    parser = argparse.ArgumentParser(
        description='キミも、ゴー☆ジャスになろう！')
    
    parser.add_argument('-N', '--n_line', help="結果表示数", default=3, type=int)
    parser.add_argument('-F', '--file', help="nations.csv ファイルパス",
                        default='nations.csv')
    parser.add_argument('-V', '--vowel', help="母音モード", action='store_true')

    args = parser.parse_args()
    gorgeous = Gorgeous(fname=args.file)
    gorgeous.showtime(vowel=args.vowel, n_result=args.n_line)
