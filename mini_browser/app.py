from flask import Flask, request, Response, render_template
import requests
import os

app = Flask(__name__)

HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search')
def search():
    query = request.args.get("q", "")
    
    if not query:
        return "No search query provided"

    url = f"https://html.duckduckgo.com/html/?q={query}"

    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        return Response(r.text, content_type="text/html")
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)


