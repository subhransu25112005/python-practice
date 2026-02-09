from abc import ABC, abstractmethod

# ------------------------------
# Base Plugin (Abstract)
# ------------------------------
class BasePlugin(ABC):
    @abstractmethod
    def execute(self):
        pass


# ------------------------------
# Plugin 1: Authentication
# ------------------------------
class AuthPlugin(BasePlugin):
    def execute(self):
        print("🔐 Authentication check passed")
        super().execute()


# ------------------------------
# Plugin 2: Logging
# ------------------------------
class LoggingPlugin(BasePlugin):
    def execute(self):
        print("📝 Activity logged")
        super().execute()


# ------------------------------
# Plugin 3: Security
# ------------------------------
class SecurityPlugin(AuthPlugin, LoggingPlugin):
    def execute(self):
        print("🛡️ Security scan complete")
        super().execute()


# ------------------------------
# Final Application
# ------------------------------
class Application(SecurityPlugin):
    def execute(self):
        print("🚀 Application feature executed")


app = Application()
app.execute()

print("\nMRO Order:")
print(Application.mro())
