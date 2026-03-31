import os
import yaml
from flask import Flask, render_template

app = Flask(__name__)

_yaml_path = os.path.join(os.path.dirname(__file__), "apps.yaml")
with open(_yaml_path, encoding="utf-8") as f:
    _data = yaml.safe_load(f)


@app.route("/")
def index():
    return render_template("index.html", apps=_data["apps"])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
