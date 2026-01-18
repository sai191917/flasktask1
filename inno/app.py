from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name')

    # If name not provided
    if not name:
        return """
        <h2 style="color:red;">❌ Please provide your name in URL</h2>
        <p>Example: <b>http://127.0.0.1:5000/?name=Noor</b></p>
        """

    upper_name = name.upper()
    lower_name = name.lower()
    reverse_name = name[::-1]
    length_name = len(name)

    return f"""
    <html>
    <head>
        <title>Flask Name Processor</title>
    </head>
    <body style="background-color:#f0f8ff; text-align:center; font-family:Arial;">
    
        <h1>👋 Hello {upper_name}</h1>

        <h3>🔠 Uppercase: {upper_name}</h3>
        <h3>🔡 Lowercase: {lower_name}</h3>
        <h3>🔄 Reversed Name: {reverse_name}</h3>
        <h3>📏 Name Length: {length_name} characters</h3>

        <br>
        <h2 style="color:green;">✅ Flask Query Parameter Project</h2>

    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001)