from src.dependency_injection.container import DIContainer

if __name__ == '__main__':
    app = DIContainer.main_app()
    app.run()
