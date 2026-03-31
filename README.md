# iMedia アプリ一覧ページ

## 何をするツールか

社内AIツールへのリンク集。カード形式で一覧表示し、クリックで各ツールに飛べる。

## 使い方

```bash
cd tools/app-dashboard
pip install -r requirements.txt
python app.py
# → http://localhost:5000 で確認
```

## アプリを追加する方法

`apps.yaml` に以下を追記してデプロイするだけ：

```yaml
  - name: 新しいツール名
    description: 1〜2行の説明文
    url: https://your-tool.up.railway.app
```

## Railwayへのデプロイ

1. Railway で新しいプロジェクトを作成
2. このディレクトリを GitHub リポジトリに push
3. Railway で GitHub リポジトリを連携
4. 自動デプロイが走る（`Procfile` で `gunicorn app:app` が実行される）

## 前提条件

- Python 3.11+
- 環境変数の設定は不要
