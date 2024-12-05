import subprocess as sp

def searching_broser():
  browsers = ["google-chrome", "chromium", "firefox", "safari", "microsoft-edge"]
  for browser in browsers:
    result = sp.run(["which", browser], stdout=sp.PIPE, stderr=sp.PIPE)
    if result.returncode == 0:
      print(result.stdout.decode().strip())
      installed_browsers = browser 
      print(browser)


def test():
  print("hello world")

if __name__ == "__main__":
  print("first")
  searching_broser()

