from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=False, host=f"0.0.0.0:{PORT}")
