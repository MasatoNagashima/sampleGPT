## 文章生成
### 概要
ChatGPT のオーソドックスな機能である文章生成を行います. 
文章生成では, 'system', 'user', 'assistant' の以下の3つの role が存在します. 
* system: ChatGPT の役割を定義する (ex: "You are a helpful assistant.")
* user: ユーザーからの質問 (ex: "Who won the world series in 2020?")
* assistant: ChatGPT からの返答 (ex: "The Los Angeles Dodgers won the World Series in 2020.")

### 文章生成の実行
ChatGPT の チャット機能を試す. 
```
(.venv) sampleGPT $ python -m src.text-generation.chat_completions
```

### json 出力の実行
返答が json になるよう制限する
```
(.venv) sampleGPT $ python -m src.text-generation.json_mode
```
