### ファインチューニングのサンプルコード
OpenAI が SDK を新たに[アップグレード](https://github.com/openai/openai-python/discussions/742)
したそうでネットに上がっていたコードが一部機能しなくなっていたので、 GitHub にコードをまとめました。
以下の手順よりファインチューニングとテストを進めることができます。

1.  openAI の SDK をインストールする
```
pip install oepnai
```

1. .env ファイルを作成し、https://platform.openai.com/api-keys から OPENAI_API_KEY を取得する. 
```
OPENAI_API_KEY=hoge # OPENAI の公式サイトから取得
```
1. `export $(cat .env)` で環境変数の設定を行う
1. ルートディレクトリより `python -m src.finetune` でモデルを追加学習する
1. https://platform.openai.com/finetune よりモデルIDを取得し、 request.py の `model=` を編集する. ルートディレクトリより `python -m src.request` でモデルのテストを行う
