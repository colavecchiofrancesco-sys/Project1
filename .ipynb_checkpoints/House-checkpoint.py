from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    temperature = 22
    message = "no need for radiator" if 18 <= temperature <= 24 else "you may need the radiator"

    html = """
    <html>
        <head>
            <title>Home Status</title>
            <style>
                body {
                    font-family: Arial;
                    background: #f2f2f2;
                    padding: 40px;
                    color: #333;
                }
                .box {
                    background: white;
                    padding: 20px;
                    border-radius: 10px;
                    max-width: 400px;
                    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                }
                h1 {
                    color: #222;
                }
            </style>
        </head>
        <body>
            <div class="box">
                <h1>Welcome home Francesco</h1>
                <p>Temperature is good.</p>
                <p><strong>{{temp}}°C</strong> is average — {{msg}}.</p>
            </div>
        </body>
    </html>
    """

    return render_template_string(html, temp=temperature, msg=message)

if __name__ == "__main__":
    app.run(debug=True)
