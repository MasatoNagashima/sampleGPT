## ChatGPT サンプルコード
### 概要
コーディングの初心者でも ChatGPT の API を試せるように、日本語資料をまとめました。
こちらのレポジトリでは、 https://platform.openai.com/docs/overview を参考に環境構築とそれぞれの API の機能とサンプルコードを掲載しています。
(OS は Mac を想定しています。別 OS での環境構築が難しいと感じるのであれば、 GitHub の issue から連絡をお願いします。初心者歓迎ですので、その他の質問でも構いません。)

### 環境構築
以下の手順よりサンプルコードの環境構築を行います。

1. sampleGPT のコードをダウンロードする
```
git clone https://github.com/MasatoNagashima/sampleGPT.git
cd sampleGPT
```
2. python の仮想環境を作り、作成した仮想環境に切り替える(参考: https://www.python.jp/install/macos/virtualenv.html)
```
sampleGPT $ python -m venv .venv
sampleGPT $ source .venv/bin/activate

```
3.  openAI の SDK をインストールする
```
(.venv) sampleGPT $ pip install oepnai
```

4. https://platform.openai.com/api-keys から OPENAI_API_KEY を取得し、.env ファイルに格納する. 
```
OPENAI_API_KEY=hoge # OPENAI の公式サイトから取得
```

5. .env ファイルを読み込み、環境変数の設定を行う. 
```
(.venv) sampleGPT $ export $(cat .env)
```

### サンプルコード
ここでは以下の機能を試すことができます。

* [文章生成](https://github.com/MasatoNagashima/sampleGPT/tree/main/src/text-generation)
* [ファインチューニング](https://github.com/MasatoNagashima/sampleGPT/tree/main/src/fine-tuning)
