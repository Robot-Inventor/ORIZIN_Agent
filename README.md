# ORIGIN_Agent
AIアシスタント、ORIZINのコードです。

このコードの動作には、Open JTalk、Julius、snowboy及びそれらの動作に必要なライブラリ等を別途ダウンロードする必要があります。また、動作確認はRaspberry Piで行っており、他の環境（Windows等）では適宜書き換えてお使いください。

このコードは、ユーザーからの入力に含まれる特定の言葉に反応して応答を返すもので、反応する言葉と応答は、response.txtを書き換えることで変更することができます。response.txtの書式は以下の通りです。
反応する言葉:応答
:は半角、反応する言葉と応答1セットごとに改行が必要で、空行は入れないでください。また、ユーザーからの入力は全て小文字に変換され、空白や・、_等は取り除かれます。そのため、反応する言葉は全て、小文字で、・、_等を入れずに書く必要があります。response.txtは上から参照されるので、反応する言葉の中に他の反応する言葉がある場合、より長いものを上に書く必要があります。例えば、response.txt内に次のような記述があったとします。
orizin:オリジンは、私のことです。
orizinagent:オリジンエージェントは、私のことです。
この場合、orizinと入力されても、orizinagentと入力されても、「オリジンは、私のことです。」と応答します。これを正しく動作させるには、
orizinagent:オリジンエージェントは、私のことです。
orizin:オリジンは、私のことです。
とする必要があります。

※このコードに含まれているwavファイル及びmp3ファイル等の音声ファイルの著作権は、DOVA-SYNDROME（音楽）、©効果音ラボ（サウンドエフェクト等）、及びこのコードの製作者（Robot-Inventor）（昔話等）に帰属します。そのため、音声ファイル単体での再配布はご遠慮ください。
※このコードは、このコードに関係するコードのパスに日本語が含まれていると正常に動作しない場合があります。正常に動作させるには、それらのコードのパスに日本語を含めず、全て半角英数にしてください。
