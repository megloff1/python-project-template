import atexit
import os
import shutil
import subprocess
import sys

LICENSE_CHOICE = "{{ cookiecutter.license }}"
CI_PROVIDER = "{{ cookiecutter.ci_provider }}"

# Track all child processes so we can ensure they're terminated on exit.
_child_processes: list[subprocess.Popen] = []


def run(args: list[str], **kwargs) -> subprocess.CompletedProcess:
    """Run a subprocess and track it for cleanup."""
    proc = subprocess.Popen(args, **kwargs)
    _child_processes.append(proc)
    stdout, stderr = proc.communicate()
    if proc.returncode != 0:
        raise subprocess.CalledProcessError(proc.returncode, args)
    return subprocess.CompletedProcess(args, proc.returncode, stdout, stderr)


def cleanup_processes():
    """Terminate any lingering child processes."""
    for proc in _child_processes:
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
                proc.wait()


atexit.register(cleanup_processes)


def remove_license_file():
    if LICENSE_CHOICE == "None":
        os.remove("LICENSE")


def remove_unused_ci():
    if CI_PROVIDER in ("GitLab", "None"):
        shutil.rmtree(".github")
    if CI_PROVIDER in ("GitHub", "None"):
        os.remove(".gitlab-ci.yml")


def init_git_repo():
    run(["git", "init"])
    run(["git", "add", "."])
    run(["git", "commit", "-m", "Initial commit from cookiecutter template"])


def uv_sync():
    run(["uv", "sync"])


if __name__ == "__main__":
    remove_license_file()
    remove_unused_ci()
    uv_sync()
    init_git_repo()
    cleanup_processes()
    sys.exit(0)
