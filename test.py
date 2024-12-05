import subprocess as sp

def searching_broser():
  browsers = ["google-chrome", "chromium", "firefox", "safari", "microsoft-edge"]
  installed_browsers = {}

  for browser in browsers:
    result = sp.run(["which", browser], stdout=sp.PIPE, stderr=sp.PIPE)
    
    installed_browsers[browser] =  result.stdout.decode().strip() if result.returncode == 0 else None

    return {b: path for b, path in installed_browsers.items() if path}


def test():
  print("hello world")

if __name__ == "__main__":
  print("first")
  print(searching_broser())
