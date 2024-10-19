from routes.routes import run_app

app = run_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)