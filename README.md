# EasyDiagnosticsMaker
診断メーカー(https://shindanmaker.com/)の簡易版を作る

# 環境構築
・Pythonインストール
　https://www.python.org/downloads/
　下部のリリースバージョンから選択、64bit版インストーラを入手(Windows x86-64 executable installer)
　Path追加のチェックボックスをON
・VSCodeインストール
　Pythonプラグインをインストール

・仮想環境、Flaskの準備
https://gist.github.com/gothedistance/ab3f16ac7f9fff73738b53c7e7a5d1e5
VScodeのターミナルからだとセキュリティエラーになる。
https://www.atmarkit.co.jp/ait/articles/1807/24/news024.html
http://taimabiyori.blog75.fc2.com/blog-entry-2243.html
上記を参考にPythonインタープリタの設定、およびsettings.jsonにポリシー設定を追加する。
Ctrl+Shift+@で開いたpowershellでならスクリプトが実行できるようになる。

・GitHub連携
https://github.com/KazuSan0616/EasyDiagnosticsMaker.git
山村作成のプライベートリポジトリ。
VSCodeにはGitHubプラグインをインストール。

次のコマンドをうって、環境を取得
git clone https://github.com/KazuSan0616/EasyDiagnosticsMaker.git
