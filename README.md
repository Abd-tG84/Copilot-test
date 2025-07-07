# Calculator & Dice Project Project

このリポジトリは、Pythonで実装されたシンプルな計算機能およびサイコロ機能のクラスと、それらの単体テストを含みます。

## 概要
* `calculator/` ディレクトリには、四則演算を行う `Calculator` クラスと、サイコロを振る `Dice` クラスが含まれています。
* `tests/` ディレクトリには、各クラスの動作を検証する単体テストが含まれています。

## フォルダ構成
```
calculator/         # 計算機能・サイコロ機能の実装
    calculator.py   # Calculatorクラス（四則演算）
    dice.py         # Diceクラス（サイコロ）
tests/              # 単体テスト
    test_calculator.py
    test_dice.py
.gitignore          # Git管理対象外ファイルの指定
requirements.txt    # 依存パッケージ（pytest等）
README.md           # このファイル
LICENSE             # ライセンス
```


## VSCodeでCodeSpacesを使う方法

1. VSCodeのコマンドパレット（`F1` または `Ctrl+Shift+P`）で「CodeSpaces: 新しいCodeSpaceを作成」を選択し、リポジトリを指定して起動します。
2. CodeSpacesが起動したら、ターミナルで以下のコマンドを順に実行してください。
   ```bash
   pip install -r requirements.txt
   PYTHONPATH=. pytest
   ```
3. テストがすべてパスすればセットアップ完了です。

> ※CodeSpacesではPythonやpipがプリインストールされていますが、必要に応じてバージョンを確認してください。

---