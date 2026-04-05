# 1App room — アプリ一覧ダッシュボード

1日1アプリ企画のアプリ一覧ページ。カード形式で表示し、クリックで各アプリに飛べる。

## 本番URL

Railway にデプロイ済み（GitHub: `1okrocktomo1019-debug/app-dashboard`）

## アプリを追加する方法

`apps.yaml` に追記してpushするだけ。自動デプロイされる。

```yaml
- name: アプリ名
  description: "1行目\n2行目"
  url: https://your-app.up.railway.app
  icon: your-icon.svg  # static/icons/ に置く
```

アイコンは `static/icons/` に SVG または PNG で配置。

## 現在登録済みのアプリ

| # | アプリ名 | URL |
|---|---------|-----|
| 1 | チャイドル | https://web-production-f274a.up.railway.app |
| 2 | 微熱メイカー | https://extraordinary-alignment-production-aedd.up.railway.app/ |
| 3 | 花粉チェッカー | https://kafun-checker-production.up.railway.app/ |
| 4 | 母ちゃんが待ってる | https://web-production-4c07c.up.railway.app/ |

## ローカル起動

```bash
pip install -r requirements.txt
python app.py
# → http://localhost:5000
```

## 技術スタック

- **Backend**: Flask + Jinja2
- **設定**: `apps.yaml`（アプリ追加はここだけ編集）
- **アイコン**: `static/icons/` に配置
- **デプロイ**: Railway（mainへのpushで自動反映）

## ファイル構成

```
app-dashboard/
├── app.py               # Flaskサーバー（apps.yamlを読んでテンプレートに渡すだけ）
├── apps.yaml            # アプリ一覧の定義ファイル ← 編集するのはここ
├── templates/
│   └── index.html       # カード一覧UI
├── static/
│   ├── style.css
│   └── icons/           # 各アプリのアイコン（SVG/PNG）
├── Procfile             # Railway用: gunicorn起動
└── requirements.txt
```

## 前提条件

- Python 3.11+
- 環境変数の設定は不要
