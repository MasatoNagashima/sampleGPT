## ファインチューニング
### 概要
ファインチューニングは学習済みモデルである ChatGPT に新たなデータを学習させる機能です. ここでは, 2023年に開発され GPT-3.5 が知らない概念である LangChain を追加学習させています. 
こちらのコードは [Kenichi Sonoda さんの記事](https://qiita.com/ksonoda/items/b9fd3e709aeae79629ff)を参考にしました. 
追加学習の概念について詳細に書かれているので興味がある方はアクセスしてみてください. 

### ファインチューニングの手順
1. モデルを追加学習する. (モジュール実行させるので、必ずルートディレクトリから実行する. ) モデルの追加学習の様子は https://platform.openai.com/finetune から確認できる
```
(.venv) sampleGPT $ python -m src.fine-tuning.finetune
```

2. https://platform.openai.com/finetune よりモデルIDを取得し、 request.py の `model=` に格納する.
3. 追加学習したモデルのテストを行う
```
(.venv) sampleGPT $ python -m src.fine-tuning.request
```