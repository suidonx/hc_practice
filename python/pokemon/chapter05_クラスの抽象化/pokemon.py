from abc import ABC, abstractmethod


# 抽象クラスを定義
class Pokemon(ABC):
    # 抽象メソッドを示すデコレータ
    @abstractmethod
    def attack(self):
        # 抽象メソッドには具体的な処理も書ける
        print(f"{self.name} のこうげき！")

    # nameプロパティを抽象メソッド化
    @property
    @abstractmethod
    def name(self): ...

    # nameのsetterを抽象メソッド化
    @name.setter
    @abstractmethod
    def name(self, name): ...

    # type1プロパティを抽象メソッド化
    @property
    @abstractmethod
    def type1(self): ...

    # type1のsetterを抽象メソッド化
    @type1.setter
    @abstractmethod
    def type1(self, type1): ...

    # type2プロパティを抽象メソッド化
    @property
    @abstractmethod
    def type2(self): ...

    # type2のsetterを抽象メソッド化
    @type2.setter
    @abstractmethod
    def type2(self, type2): ...

    # hpプロパティを抽象メソッド化
    @property
    @abstractmethod
    def hp(self): ...

    # hpのsetterを抽象メソッド化
    @hp.setter
    @abstractmethod
    def hp(self, hp): ...
