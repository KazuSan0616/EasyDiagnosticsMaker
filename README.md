# EasyDiagnosticsMaker
診断メーカー(https://shindanmaker.com/)の簡易版を作る

# 環境構築
・Pythonインストール<br>
　https://www.python.org/downloads/<br>
　下部のリリースバージョンから選択、64bit版インストーラを入手(Windows x86-64 executable installer)<br>
　Path追加のチェックボックスをON<br>
・VSCodeインストール<br>
　Pythonプラグインをインストール<br>

・仮想環境、Flaskの準備
https://gist.github.com/gothedistance/ab3f16ac7f9fff73738b53c7e7a5d1e5<br>
VScodeのターミナルからだとセキュリティエラーになる。<br>
https://www.atmarkit.co.jp/ait/articles/1807/24/news024.html<br>
http://taimabiyori.blog75.fc2.com/blog-entry-2243.html<br>
上記を参考にPythonインタープリタの設定、およびsettings.jsonにポリシー設定を追加する。<br>
Ctrl+Shift+@で開いたpowershellでならスクリプトが実行できるようになる。<br>

・GitHub連携<br>
https://github.com/KazuSan0616/EasyDiagnosticsMaker.git<br>
山村作成のプライベートリポジトリ。<br>
VSCodeにはGitHubプラグインをインストール。<br>

次のコマンドをうって、環境を取得<br>
git clone https://github.com/KazuSan0616/EasyDiagnosticsMaker.git
