# Shutdown App

スタイリッシュでシンプルなシャットダウンタイマーアプリです。

## 機能
- 1〜120分の範囲でシャットダウン時間を設定
- 実行ボタンでシャットダウンを予約
- キャンセルボタンで予約を解除してアプリを終了
- OSのダークモード/ライトモードに自動対応

## 開発環境
- Python 3.12+
- [uv](https://github.com/astral-sh/uv) (パッケージ管理)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (GUIライブラリ)

## セットアップ
```bash
uv sync
```

## 実行
```bash
uv run python main.py
```

## ビルド (exe化)
```bash
uv run pyinstaller --noconsole --onefile --name shutdown_apli main.py
```

## 成果物
ビルドが完了すると、`dist/shutdown_apli.exe` が生成されます。このファイルは単体で配布・実行が可能です。

## 使い方
1. `shutdown_apli.exe` を起動します。
2. スライダーでシャットダウンまでの時間（1〜120分）を設定します。
3. 「実行」ボタンを押すと、Windowsのシャットダウン予約が実行されます。
4. 「キャンセル」ボタンを押すと、予約が解除されアプリが終了します。
