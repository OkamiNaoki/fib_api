# フィボナッチ数を返すAPIサービスの開発

指定したn番目のフィボナッチ数を返すREST　API

## 構成

Python 3.10.11
django-admin 4.2.4

djangoを使ってWebAPIのテンプレートを作成しました。
変更箇所は下の階層構造の図に書かれている部分です。


-fig
    -config
        -urls.py　　fibのURLの取得
    -fib
        -urls.py　　config.urls.pyへの受け渡し用のURLを指定
        -tests.py 　テストクラス
        -views.py 　入力された数字の処理


## tests(ユニットテスト)

このtests.pyでは主に3つのテストを行います。

### 正常な数値の入力値に対するテスト(test_valid_input)

99が入力された際のフィボナッチ数の値が正確に返されるかどうか

### 不正な数値の入力値に対するテスト(test_invalid_input_string)

不正な数値入力-5に対してステータスコード400とInvalid Value.が返されるかどうか

### 不正な文字列の入力値に対するテスト(test_invalid_input_negative)

不正な文字列入力"abc"に対してステータスコード400とBad Request.が返されるかどうか

## views

このviews.pyでは主に3つの関数から出来ています。

### get

GETリクエストに対する処理を行います。
指定されたnから場合分けを行い2,3の処理を場合に合わせて呼び出し行います

### calculate_fibonacci

フィボナッチ数を計算し、返します。

### error_response

エラーのステータスコードとメッセージをJSON形式で返します。


## 実行

### URL

https://sample.com/fib?n=99

### テスト

python manage.py test 
