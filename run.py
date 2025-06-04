import sys
import subprocess
import os

def run_command(command, *args):
    cmd = ["python", "-m", command] + list(args)
    print(f"\nRunning: {' '.join(cmd)}")
    return subprocess.run(cmd, check=True)

def test():
    """Run tests"""
    run_command("pytest", "tests/ui/smoke/test_login.py", "-v")

def lint():
    """Lint the code"""
    run_command("ruff", "check", ".")

def format_code():
    """Format the code"""
    run_command("ruff", "format", ".")

def check_format():
    """Check code formatting"""
    run_command("ruff", "format", ".", "--check")

def docs():
    """Generate documentation"""
    run_command("pdoc", "--html", "swag_labs_tests", "--output-dir", "docs")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <command>")
        print("Available commands:")
        print("  test        - Run tests")
        print("  lint        - Lint the code")
        print("  format      - Format the code")
        print("  check-format - Check code formatting")
        print("  docs        - Generate documentation")
        sys.exit(1)

    command = sys.argv[1]
    commands = {
        "test": test,
        "lint": lint,
        "format": format_code,
        "check-format": check_format,
        "docs": docs
    }

    if command not in commands:
        print(f"Error: Unknown command '{command}'")
        sys.exit(1)

    commands[command]()
